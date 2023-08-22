from django.shortcuts import render
from .models import *
from django.db import connection
import csv
from django.http import HttpResponse
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
# Create your views here.

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




# enviar correo
def enviar_correo(request):
    if request.method == 'GET':
        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls = settings.EMAIL_USE_TLS
        ) as conexion:
            encabezado = "Esto es otro test desde el views"
            cuerpo = "este es el cuerpo de mi correo test"
            remitente = settings.EMAIL_HOST_USER
            recipiente = ["joshuamht@outlook.com",] 
            EmailMessage(encabezado, cuerpo, remitente, recipiente, connection=conexion).send()
    return HttpResponse('<h1> Correo enviado!!!</h1>')