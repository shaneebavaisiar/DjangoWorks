
from django.contrib import admin
from django.urls import path
from .views import book_list,book_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',book_list),
    path('books/<int:id>',book_detail)
]
