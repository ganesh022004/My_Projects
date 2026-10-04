from django.urls import path
from . import views

urlpatterns = [

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # Employee CRUD
    path('employee_list/', views.employee_list, name='employee_list'),

    path('employee_create/', views.employee_create, name='employee_create'),

    path(
        'employee_update/<int:id>/',
        views.employee_update,
        name='employee_update'
    ),

    path(
        'delete_emp/<int:id>/',
        views.delete_emp,
        name='delete_emp'
    ),

    path(
            'about_page/',
            views.about_page,
            name='about_page'
        ),
        path(
            'home/',
                    views.home,
                    name='home'
                ),
]