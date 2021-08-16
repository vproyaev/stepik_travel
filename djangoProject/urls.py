"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from stepik_tours import views as stepik_tours_view


urlpatterns = [
    path('', stepik_tours_view.main_view, name='main'),
    path('departure/<str:departure>/', stepik_tours_view.departure_view, name='departure'),
    path('tour/<int:tour>/', stepik_tours_view.tour_view, name='tour')
]

handler404 = stepik_tours_view.custom404
handler500 = stepik_tours_view.custom500
