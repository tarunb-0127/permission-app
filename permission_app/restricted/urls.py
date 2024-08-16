# restricted/urls.py
# restricted/urls.py
from django.urls import path
from .views import CustomLoginView, check_permission, restricted_page

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('check_permission/', check_permission, name='check_permission'),
    path('restricted_page/', restricted_page, name='restricted_page'),
]
