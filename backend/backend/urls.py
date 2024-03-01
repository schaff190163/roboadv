from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, StockDataViewSet, PortfolioViewSet, PortfolioStockViewSet
from .views import register, login_view, logout_view

router = DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'stockdata', StockDataViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'portfoliostocks', PortfolioStockViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]