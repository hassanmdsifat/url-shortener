from django.urls import path
from url_shortener_app.views.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
]
