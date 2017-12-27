from django.conf.urls import url
from management import views

urlpatterns = [
    url(r'^booklist/', views.BookList.as_view()),
]
