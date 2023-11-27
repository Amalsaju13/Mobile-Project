"""
URL configuration for mobile project.

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
from django.urls import path,include
from owner import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/mobile/add',views.AddMobile.as_view(),name="addmobile"),
    path('owner/mobile/all',views.MobileList.as_view(),name="allmobiles"),
    path('owner/mobile<int:id>',views.MobileDetailView.as_view(),name="mobiledetail"),
    path('owner/mobile/remove<int:id>',views.MobileDeleteView.as_view(),name="mobiledelete"),
    path('owner/mobile/change<int:id>',views.ChangeMobile.as_view(),name="changemobile"),
    path('owner/dashboard',views.DashBoardView.as_view(),name="dashboard"),
    path('owner/order/<int:id>',views.OrderDetailView.as_view(),name='orderdetail'),
    path('owner/order/edit/<int:id>',views.OrderChangeView.as_view(),name='orderedit'),
    path('customers/',include("customer.urls")),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
