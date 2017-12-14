from django.conf.urls import url

from User.views import LoginView

urlpatterns = [
    url(r'login/', LoginView.as_view()),
]