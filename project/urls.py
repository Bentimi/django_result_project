from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('form', views.form, name='form'),
    path('register', views.register, name='register'),
    # path('my_login', views.my_login, name='my_login'),
    path('portal', views.portal, name='portal'),
    path('', views.my_login, name='my_login'),
    # path('result', views.result, name='result'),
    path('user-logout', views.user_logout, name='user-logout'),

# CRUD
    path('dashboard', views.Dashboard, name='dashboard'),
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('record/<int:pk>', views.Singular_record, name='record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),

# FILE
path('file', views.file, name='file'),
path('nav', views.nav, name='nav'),
# path('import', views.ImportView.as_view(), name='import' )

]