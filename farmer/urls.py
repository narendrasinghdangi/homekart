from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='FarmerHome'),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path("success/",views.success,name="success"),
    path("products/<int:id>",views.productView, name="ProductView"),
]