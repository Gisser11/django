from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    get_usertext =  request.GET['usertext']
    reversed_text =get_usertext[::-1]
    print(get_usertext)
    return render(request, 'reversed.html', {'usertext':reversed_text})