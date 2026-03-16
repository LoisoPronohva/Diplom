from django.urls import path
from .views import UserListView, UserDetailView, ErrorTestView

urlpatterns = [

    path("", UserListView.as_view()),
    path("<int:pk>/", UserDetailView.as_view()),

    path("error-test/", ErrorTestView.as_view()),
]