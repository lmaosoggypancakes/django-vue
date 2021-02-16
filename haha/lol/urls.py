from django.urls import path
from . import views
urlpatterns = [
    path('api/all', views.get_all),
    path('api/login', views.login_view),
    path('api/logout', views.logout_view),
    path('api/post/<int:id>', views.grab_post),
    path('api/check', views.check_view),
    path('api/register', views.register)
]