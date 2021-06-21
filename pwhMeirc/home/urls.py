from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    # path('admin/',admin.site.urls),
    path('', views.home,name='home'),
    # path('', include('home.urls'))
]
# 127.0.0.1:8000/home