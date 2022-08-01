from django.shortcuts import render

def main_view(request):
    return render(request, 'index.html')

# Create your views here.
