from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse


def home_view(request: HttpRequest):
    return render(request, 'main/index.html')

def vision_view(request):
    return render(request, 'main/vision.html')

def digital_view(request):
    return render(request, 'main/digital.html')

def stats_view(request):
    return render(request, 'main/stats.html')

def ai_view(request):
    return render(request, 'main/ai.html')

def future_view(request):
    return render(request, 'main/future.html')

def about_view(request):
    return render(request, 'main/about.html')

def set_theme_view(request):
    # نقرأ الخيار من الرابط، مثلاً /set-theme/?theme=light
    theme = request.GET.get('theme', 'dark')
    if theme not in ('light', 'dark'):
        theme = 'dark'

    # نرجع المستخدم لنفس الصفحة اللي كان فيها
    next_url = request.META.get('HTTP_REFERER') or reverse('main:home_view')

    # نجهز الرد مع الكوكي
    response = HttpResponseRedirect(next_url)
    response.set_cookie('theme', theme, max_age=60*60*24*365)  # سنة كاملة
    return response


