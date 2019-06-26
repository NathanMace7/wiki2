from django.urls import path, include
from . import views

#Here is a group of URls the website contains
app_name = 'wiki'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('errors/401', views.test_401_error , name='test_401_error'), # Used to ensure the 401 warning doesnt appear in the log.
    path('errors/500', views.test_500_error , name='test_500_error'), # Used to ensure the 407 error appears in the log.
    path('errors/404', views.test_404_error , name='test_404_error'), # Used to ensure the 404 warning appears in the log.
    path('errors/502', views.test_502_error , name='test_502_error'), # Used to ensure the 502 warning appears in the log.
    path('upload/', views.upload_file, name='upload_page' ), 
    path('<str:pk>/edit', views.edit_page, name='edit_page'),
    path('<str:pk>/save', views.save_page, name='save_page'),
    path('<str:pk>/', views.view_page, name='detail'),
       
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
