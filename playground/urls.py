from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('task/', views.notify_customers),
    path('logger/', views.Logger.as_view()),
    path('cach/', views.function_cach)
]
