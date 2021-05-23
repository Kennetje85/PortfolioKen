from django.shortcuts import render

# Create your views here.
# Define function
def hello_world(request):  # HttpRequestObject
    return render(request, 'hello_world.html', {})