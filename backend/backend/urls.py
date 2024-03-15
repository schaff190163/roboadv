from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (StockViewSet, StockDataViewSet, PortfolioViewSet, 
                     PortfolioStockViewSet)
from .views import register, login_view, logout_view

from django.urls import path
from .views import StockList, StockDetail, StockDataList, StockDataDetail, PortfolioList, PortfolioDetail, PortfolioStockList, PortfolioStockDetail

urlpatterns = [
    path('stocks/', StockList.as_view(), name='stock-list'),
    path('stocks/<int:pk>/', StockDetail.as_view(), name='stock-detail'),
    path('stockdata/', StockDataList.as_view(), name='stockdata-list'),
    path('stockdata/<int:pk>/', StockDataDetail.as_view(), name='stockdata-detail'),
    path('portfolios/', PortfolioList.as_view(), name='portfolio-list'),
    path('portfolios/<int:pk>/', PortfolioDetail.as_view(), name='portfolio-detail'),
    path('portfoliostocks/', PortfolioStockList.as_view(), name='portfoliostock-list'),
    path('portfoliostocks/<int:pk>/', PortfolioStockDetail.as_view(), name='portfoliostock-detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]