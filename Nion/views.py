from django.http import HttpResponse

def home(request):
    return HttpResponse("<title>N ION</title>")
def account(request):
    return HttpResponse("<title>N ION- account</title>")
def username(request):
    return HttpResponse("<title>N ION - username</title>")
def settings(request):
    return HttpResponse("<title>N ION - settings</title>")
