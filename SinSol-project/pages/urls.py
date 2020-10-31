from django.urls import path
from . import views
from .views import CategoryView

urlpatterns = [
    path('', views.index ,name='index'),
    path('about', views.about ,name='about'),
    path('<category_name>', CategoryView.as_view()),
]
