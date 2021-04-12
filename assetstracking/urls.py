from django.urls    import path
from .              import views


urlpatterns = [
    path('', views.home, name="assets"),
    path('assets', views.home, name="assets"),
    path('createAsset/', views.createAsset, name="createAsset"),
    path('createBorrowing/', views.createBorrowing, name="createBorrowing"),
    path('updateBorrowing/<str:borrowing_test>/', views.updateBorrowing, name="updateBorrowing"),
    path('deleteBorrowing/<str:pk>/', views.deleteBorrowing, name="deleteBorrowing"),
    path('rfid/', views.rfid, name="rfid"),
    path('tags/', views.tags, name="tags"),
    path('employee/<str:employee_test>/', views.employee, name="employee"),
    path('subscriber/<str:subscriber_test>/', views.subscriber, name="subscriber"),
    path('welcome', views.index),
    path('login', views.login, name="login"),

]