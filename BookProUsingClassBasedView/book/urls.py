
from django.contrib import admin
from django.urls import path
from .views import BookList,BookCreate,BookUpdate,BookDetail,Bookdelete

urlpatterns = [
    path('booklist',BookList.as_view(),name='booklist'),
    path('bookcreate',BookCreate.as_view(),name='bookcreate'),
    path('bookupdate/<int:pk>',BookUpdate.as_view(),name='bookupdate'),
    path('bookdetail/<int:pk>',BookDetail.as_view(),name='bookdetail'),
    path('bookdelete/<int:pk>',Bookdelete.as_view(),name='bookdelete')
]
