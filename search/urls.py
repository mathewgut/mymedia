from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search_form, name="search_form"),
    path("search/results", views.search_results, name="search_results"),
    path("results/item/", views.search_item_details,name="result_item")
]