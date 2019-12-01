from django.shortcuts import render, redirect, get_object_or_404
from Apps.Producto.models import producto

from django.db import IntegrityError
from django.db.models import Sum
# Create your views here.
def listProducto(request):
    prod = producto.objects.all()
    context = {'prod':prod}
    template = 'Producto/listado.html'
    return render(request, template, context)

def updateOferta(request, idp):
    producto.objects.filter(id = idp).update(
        oferta = True
    )
    return redirect('listado')


