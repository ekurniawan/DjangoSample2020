from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h2>Hello World</h2>")


