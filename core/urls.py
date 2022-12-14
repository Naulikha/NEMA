from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
