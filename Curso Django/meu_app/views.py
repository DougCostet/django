from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos</h1>')


def soma(request, numero_a, numero_b):
    total = numero_a + numero_b
    return HttpResponse(f'A soma é: {total}')
