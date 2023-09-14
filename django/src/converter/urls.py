from django.urls import path

from converter.views import rate_view, rate_path_view

urlpatterns = [
    path('rates/<str:from_>/<str:to>/<int:value>', rate_path_view),
    path('rates/', rate_view),
]
