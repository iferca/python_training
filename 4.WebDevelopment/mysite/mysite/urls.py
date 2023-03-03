from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('greet/', include('greeter.urls')),
    path('admin/', admin.site.urls),
]
