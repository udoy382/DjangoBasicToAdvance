"""mySite URL Configuration

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
from mySite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homePage),
    # path('about-us/', views.aboutUs),
    # path('Course/', views.Course),
    # path('Course/<str:courseid>', views.courseDetails),
    # path('Course/<int:courseid>', views.courseDetails),
    # path('Course/<slug:courseid>', views.courseDetails),
    # path('Course/<courseid>', views.courseDetails),


    # ------------ New Page Urls ------------

    path('', views.homePage, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('submitform/', views.submitform, name='submitform'),
    path('calculator/', views.calculator, name='calculator'),
    path('evenodd/', views.evenodd, name='evenodd'),
    path('marksheet/', views.marksheet, name='marksheet'),
    # path('newsdeatils/<newsid>', views.newsDeatils, name='newsDeatils'),
    path('newsdeatils/<slug>', views.newsDeatils, name='newsDeatils'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)