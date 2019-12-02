"""Mark2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

""" 
Importaciones para manejos de archivos media y estaticos
"""
from django.conf import settings
#from django.conf.urls.static import static
""" 
Importaciones para Login y Logout
"""
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required


from Apps.Producto.views import listProducto, updateOferta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.Principal.urls', namespace="Principal")),
    path('producto', listProducto, name="listado"),
    path('update/<int:idp>', updateOferta, name="update"),
    #path('accounts/login/', login, name="login"),
    #path('accounts/logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),    
    #path('registro', registration, name="registro"),

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

