from django.http import HttpResponse
from datetime import datetime 
from django.template import Template, Context

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
    return HttpResponse('<br><br> Ya entendimos esto, es muy simple')

def dia_de_hoy(request):

        dia = datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)
    
def mi_nombre_es(self, nombre):

      documentoDeTexto = f"Mi nombre es: <br><br>  {nombre}"


      return HttpResponse(documentoDeTexto)
  
def probandoTemplate(self):

    miHtml = open("H:\Mi unidad\DATA Vverty\Coderhouse\Python\proyecto_python_coder\proyecto_felipe_lorenzo\proyecto_felipe_lorenzo\plantillas\index.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)