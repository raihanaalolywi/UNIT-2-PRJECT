from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("vision/", views.vision_view, name="vision_view"),
    path("digital/", views.digital_view, name="digital_view"),
    path("stats/", views.stats_view, name="stats_view"),
    path("ai/", views.ai_view, name="ai_view"),
    path("future/", views.future_view, name="future_view"),
    path("about/", views.about_view, name="about_view"),
    path('set-theme/', views.set_theme_view, name='set_theme'),

]
