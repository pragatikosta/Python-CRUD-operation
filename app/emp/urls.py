from django.urls import path
from .views import emp_home, add_emp, delete_emp, update_emp

urlpatterns = [
    path('home/', emp_home, name='emp_home'),
    path('add-emp/', add_emp, name='add_emp'),
    path('delete-emp/<int:emp_id>/', delete_emp, name='delete_emp'),
    path('update-emp/<int:emp_id>/', update_emp, name='update_emp'),
]
