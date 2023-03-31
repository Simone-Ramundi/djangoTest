from django.urls import path
from . import views

urlpatterns = [
    path('ciao/', views.members),
    path('test/', views.test, name='test'),
    path('index/', views.index, name='index'),
    path('modulo/', views.modulo, name='modulo'),
    # path('', views.template_view),
    path('form/', views.form),
        # "backend" - path('', views.post),
    path('library_searching/', views.library_searching),
    path('library_searching/library_online/', views.library_online),
    path('delete/<int:id>', views.delete, name='delete'),

    # front-end
    path('', views.main, name='main'),
    path('members/', views.vista, name='vista'),
    path('members/details/<int:id>', views.details, name='details'),
]