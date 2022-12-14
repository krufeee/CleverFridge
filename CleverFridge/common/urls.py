from django.urls import path

from CleverFridge.common.views import IndexView, HomepageView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('homepage/', HomepageView.as_view(), name='homepage'),
)