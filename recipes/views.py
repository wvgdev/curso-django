from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        
        'Name': 'Weslley Garcia'
        
        }) #status=566, vc consegue adicionar status nessa pagina.

def sobre(request):
    return render(request, 'teste.html')

def contato(request):
    return HttpResponse('CONTATO')