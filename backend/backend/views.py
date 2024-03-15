from rest_framework import viewsets, permissions
from .models import Stock, StockData, Portfolio, PortfolioStock
from rest_framework import viewsets
from .serializers import StockSerializer, StockDataSerializer, PortfolioSerializer, PortfolioStockSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed
import json

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, obj):
        return obj.user == request.user

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDataViewSet(viewsets.ModelViewSet):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioStockViewSet(viewsets.ModelViewSet):
    queryset = PortfolioStock.objects.all()
    serializer_class = PortfolioStockSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return PortfolioStock.objects.filter(portfolio__user=self.user)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username, password=password)
            return JsonResponse({'message': 'User registered successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Username is already taken'}, status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'User logged in successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'User logged out successfully'}, status=200)