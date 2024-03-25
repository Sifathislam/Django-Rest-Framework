from django.urls import path, include
from .views import UserViewSet, ProductViewSet,CategoryViewSet, ProductFilterList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'UserViewSet', UserViewSet)
router.register(r'ProductViewSet', ProductViewSet)
router.register(r'CategoryViewSet', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filterProducts/', ProductFilterList.as_view(), name='Product_list'), 

]
