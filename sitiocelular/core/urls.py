from django.urls import path
from.views import home,galeria,listado_celulares,nuevo_celular,modificar_celular,eliminar_celular,registro_usuario

urlpatterns = [
    
   path('', home, name='home'),
   path('galeria/', galeria, name='galeria'),
   path('listado-celulares/',listado_celulares, name='listado_celulares'),
   path('nuevo-celular/', nuevo_celular, name='nuevo_celular'),
   path('modificar-celular/<id>/', modificar_celular, name="modificar_celular"),
   path('eliminar-celular/<id>/', eliminar_celular, name="eliminar_celular" ),    
   path('registro/', registro_usuario, name="registro_usuario"),
]