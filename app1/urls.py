
from django.urls.conf import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home,name="home"),
    path('upload',views.upload,name="upload"),
    path('result',views.result,name="result"),
    path('hom',views.home,name="hom"),

]