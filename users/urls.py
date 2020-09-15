from django.urls import path
from .views import follow_toggle, mypage

app_name='users'
urlpatterns=[
    path('<int:id>/follow_toggle', follow_toggle, name="follow_toggle"),
    path('<int:id>/mypage', mypage, name="mypage"),
]