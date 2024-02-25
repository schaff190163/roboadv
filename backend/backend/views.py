from django.http import JsonResponse

def get_hardcoded_value(request):
    data = {"value": "Hello from Django!"}
    return JsonResponse(data)