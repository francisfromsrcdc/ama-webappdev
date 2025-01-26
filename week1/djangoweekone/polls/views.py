from django.http import JsonResponse
from django.shortcuts import render
import random
#/polls
def index(request):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    selected_joke = random.choice(jokes)
    return JsonResponse({'funnyjoke': selected_joke})