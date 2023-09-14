from django.urls import path

from converter.views import rate_view

urlpatterns = [
    path('rates/', rate_view)
]
