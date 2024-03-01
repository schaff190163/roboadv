from rest_framework import viewsets, permissions
from .models import Stock, StockData, Portfolio, PortfolioStock
from .serializers import StockSerializer, StockDataSerializer, PortfolioSerializer, PortfolioStockSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDataViewSet(viewsets.ModelViewSet):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

class PortfolioStockViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioStockSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return PortfolioStock.objects.filter(portfolio__user=self.request.user)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username, password=password)
            return HttpResponse('User registered successfully')
        else:
            return HttpResponse('Username is already taken')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('User logged in successfully')
        else:
            return HttpResponse('Invalid username or password')

def logout_view(request):
    logout(request)
    return HttpResponse('User logged out successfully')