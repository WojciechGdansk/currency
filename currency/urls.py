"""
URL configuration for currency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from exchange import views
from average_value import views as average_view
from buy_sell_difference import views as difference_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exchange/<str:currency>/<str:date>/', views.Exchange.as_view(), name='exchange'),
    path('min_and_max_value/<str:currency>/<str:quotation_number>',
         average_view.MaxAndMinAverageValue.as_view(), name='min_and_max_value'),
    path('difference/<str:currency>/<str:quotation_number>',
         difference_view.MajorDifferenceBetweenButAndSellRate.as_view(), name="difference")
]
