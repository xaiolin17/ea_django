"""ea_pro_d URL Configuration

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
from django.contrib import admin
from django.urls import path
from app001.views import my_view, stock_list, add_random_data, stock_list_break

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a', my_view, name='静态页面'),
    path('data', stock_list, name='数据'),
    path('random/', add_random_data, name='插入的随机数据'),
    path('data_break/', stock_list_break, name='返回'),
]
