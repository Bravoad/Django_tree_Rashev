from django.urls import path
from .views import IndexView
from django.views.decorators.cache import cache_page
urlpatterns=[
    path('', cache_page(30 * 60)(IndexView.as_view()), name='main'),
]
