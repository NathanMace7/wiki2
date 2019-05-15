from django.urls import path, include


from . import views

app_name = 'wiki'
urlpatterns = [
    #path('accounts/login/' LoginView.as_view(), name='login')
    #path('accounts/logout/' LogoutView.as_view(), name='logout')
    path('', views.IndexView.as_view(), name='index'),
    path('<str:pk>/edit', views.edit_page, name='edit_page'),
    path('<str:pk>/save', views.save_page, name='save_page'),
    path('<str:pk>/', views.view_page, name='detail'),
    path('<str:pk>/upload/', views.upload_file, name='upload_page' ),    
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
