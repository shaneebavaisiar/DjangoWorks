
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("works/",WorksGetPost.as_view()),
    path("works/<int:id>",WorkUpdateDelete.as_view())
]
