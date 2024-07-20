from django.contrib import admin
from django.urls import path
from .views import home, about, services
# Import the specific view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("about/", about), 
    path('home/', home, name='home'),
    path("services/", services),
    
    # Use the imported view function directly
]
