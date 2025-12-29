from django.urls import path
from .views import main, get_info
urlpatterns = [
    path('', main, name='main'),
    path('persons/', get_info,name='info_page')
]