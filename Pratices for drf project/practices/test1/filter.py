import django_filters
from . models import Product

class ProductFilter(django_filters.FilterSet):
    product_category__id = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['product_category__id']

    search_fields = ['id','title','price']
