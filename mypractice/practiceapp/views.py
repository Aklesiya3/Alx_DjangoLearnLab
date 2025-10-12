from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the home page!")
def about_view(request):
    return render(request, 'practiceapp/about.html')
def book_list_view(request):
    books=[
        {'title': 'moana', 'author': 'disney'},
        {'title': 'one piece', 'author': 'adventure'},
        {'title': 'naruto', 'author': 'hidden leaf'},
    ]
    context={'books': books}
    return render(request, 'practiceapp/book_list.html',context)