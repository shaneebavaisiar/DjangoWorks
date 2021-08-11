"""bookProUsingTemplateView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import BookList,BookCreate,BookUpdate,BookView,BookDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list',BookList.as_view(),name='list'),
    path('create',BookCreate.as_view(),name='create'),
    path('update/<int:id>',BookUpdate.as_view(),name='update'),
    path('detail/<int:id>',BookView.as_view(),name='detail'),
    path('delete/<int:pk>',BookDelete.as_view(),name='delete')
]
