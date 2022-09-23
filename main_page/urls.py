from django.urls import path
from main_page.views import MainPage

urlpatterns = [
    path('', MainPage.as_view(), name='main-page'),
]
