from django.shortcuts import render


def greeting(request):
    return render(request, 'test_app/greeting.html', {})
