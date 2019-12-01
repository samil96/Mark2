from django.shortcuts import render, redirect
from Apps.Producto.models import producto
# Create your views here.
def listProducto(request):
    prod = producto.objects.all()
    prod2 = producto.objects.filter(oferta = True)
    context = {'prod':prod, 'prod2':prod2}
    template = 'Producto/listado.html'
    return render(request, template, context)

def updateOferta(request, idp):
    producto.objects.filter(id = idp).update(
        oferta = True
    )
    return redirect('listado')


