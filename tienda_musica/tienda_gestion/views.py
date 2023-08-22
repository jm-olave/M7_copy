from django.shortcuts import render, redirect
from .models import *
from django.db import connection
import csv
from django.http import HttpResponse

from .forms import FileUploadForm

#mail
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
# Create your views here.
def send_email(request):  
   if request.method == "GET": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = "texto prueba"  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = ["joshuamht@outlook.com", ]  
           message = "mensaje de prueba"
           print("lelga hasta aca?")
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
 
   return HttpResponse('<h1> email enviado</h1>')

def crear_artista(request):
    artista = Artista.objects.create(nombre = 'marcianeke', bio="Cantante de musica trap" )
    artista.save()
    album = Album.objects.create(titulo = 'Esto es trap', fecha_salida = '2023-08-11', artista = artista)
    album.save()

def exportar_artistas(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM tienda_gestion_artista;")
        with open('archivo.csv', 'w') as archivocsv:
            csvwriter = csv.writer(archivocsv)
            csvwriter.writerow(['id','nombre','bio'])
            for fila in cursor.fetchall():
                csvwriter.writerow(fila)
    return HttpResponse('<h1> Termino la lectura del archivo</h1>')


def consultar_artistas_album(request):
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT artista.nombre , COUNT(album.id) as numero_albums
        FROM tienda_gestion_artista artista
        INNER JOIN tienda_gestion_album album ON artista.id = album.artista_id
        GROUP BY artista.id, artista.nombre
        ORDER BY numero_albums DESC;
        """)
        resultado = cursor.fetchall()
    return HttpResponse(f'<p> Artistas X Album <br> {resultado} </p>')



def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the uploaded file to the database
            return redirect('consulta')  # Redirect to a success page
    else:
        form = FileUploadForm()
    return render(request, 'tienda_gestion/upload_file.html', {'form': form})


