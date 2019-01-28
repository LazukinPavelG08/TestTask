import requests
from django.conf import settings
from django.http import  HttpResponseRedirect, JsonResponse
from .serializers import ProfileModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Profile


def get_code(request):
    if request.method == 'GET':
        app_id = settings.VK_APP_ID
        redirect_uri = 'http://127.0.0.1:8000/get_token/'
        vk_url = f"https://oauth.vk.com/authorize?client_id={app_id}&display=page&scope=offline&redirect_uri={redirect_uri}&v=5.92"
    return HttpResponseRedirect(vk_url)

def get_token(request):
    if request.method == 'GET':
        code = request.GET.get("code")
        error = request.GET.get("error")

        redirect_url = 'http://127.0.0.1:8000/get_token/'

        if not code or error:
            return JsonResponse({"status": "error", "messgae": error})

        auth_url = f'https://oauth.vk.com/access_token?client_id={settings.VK_APP_ID}&client_secret={settings.VK_SECRET_KEY}&redirect_uri={redirect_url}&code={code}&scope=offline&v=5.92'
        auth_response = requests.get(url=auth_url).json()

        if error or 'error' in auth_response:
            return JsonResponse({"status": "error", "message": auth_response["error"]})

        access_token = auth_response['access_token']
        user_info = requests.get(f'https://api.vk.com/method/users.get?access_token={access_token}&v=5.92').json()


        profile, created = Profile.objects.get_or_create(
            vk_id=auth_response["user_id"],
            defaults=dict(
                first_name=user_info['response'][0]['first_name'],
                last_name=user_info['response'][0]['last_name'],
                access_token=access_token
            )
        )

        return JsonResponse({"status": "success", "message": "profile created!"})

@api_view(['GET'])
def get_profiles(request):
    qs = Profile.objects.all()
    serializer = ProfileModelSerializer(qs, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_profile(request, pk):
    try:
        qs = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response({})
    serializer = ProfileModelSerializer(qs)

    return Response(serializer.data)