from django.shortcuts import render

def mis_notas(request):
    lista_de_notas = [2,3,4,5,6,7,8,9]
    contexto = {"notas" : lista_de_notas}
    return render(request,"templates/index.html" , contexto)