from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import get_chatbot_response

def index(request):
    return render(request, 'index.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = get_chatbot_response(user_input)
        return JsonResponse({'response': response})
