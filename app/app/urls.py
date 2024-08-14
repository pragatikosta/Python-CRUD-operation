from django.contrib import admin
from django.urls import path,include
from .views import home, about, services
# Import the specific view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("about/", about), 
    path('home/', home, name='home'),
    path("services/", services),
    path("emp/",include('emp.urls'))
    
    # Use the imported view function directly
]
