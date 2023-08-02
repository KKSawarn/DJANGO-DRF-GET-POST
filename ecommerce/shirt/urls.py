from django.contrib import admin
from django.urls import path

from shirt.views import CreateCategoryView, CreateShirtView

urlpatterns = [
    path("createShirt/",CreateShirtView.as_view(),name="create_shirt_view"),
    path("createCategory/",CreateCategoryView.as_view(),name="create_category_view")
]
