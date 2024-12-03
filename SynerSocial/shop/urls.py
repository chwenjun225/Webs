from django.utils.translation import gettext_lazy as _
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
	path(_('<slug:category_slug>/'), views.product_list, name='product_list_by_category'),
	path(_('<int:id>/<slug:slug>/'), views.product_detail, name='product_detail'),
    path(_(''), views.product_list, name='product_list'),
]