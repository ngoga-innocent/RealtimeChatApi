
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Auth/',include('Auth.urls')),
    path('', include('chat.urls')),  # new
]
