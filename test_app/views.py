from django.shortcuts import render


def greeting(request):
    return render(request, 'test_app/greeting.html', {})


def vk_api(request):
    return render(request, 'test_app/vk_api.html', {})