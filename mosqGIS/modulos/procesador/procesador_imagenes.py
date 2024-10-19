"""
Módulo: procesador_imagenes

Este módulo contiene la clase `RecortadorImagenes`, que se utiliza para recortar imágenes basadas
en un polígono dado y funciones para recortar archivos TIF utilizando shapefiles de
línea de corte con la herramienta gdalwarp de GDAL.

Clases:
-------
    - RecortadorImagenes: Recorta imágenes en una carpeta especificada basándose en un polígono
                            dado.

Funciones:
----------
- crop_tif(input_tif,
            output_tif,
            cutline_shapefile): Recorta un archivo TIF utilizando un shapefile
                                de línea de corte usando gdalwarp.

    Args:
        input_tif (str): Ruta al archivo TIF de entrada que se recortará.
        output_tif (str): Ruta donde se guardará el archivo TIF recortado.
        cutline_shapefile (str): Ruta al shapefile que define la línea de corte para el recorte.

    Descripción:
    ------------
    Esta función utiliza la herramienta gdalwarp de GDAL para recortar un archivo TIF
    utilizando un shapefile de línea de corte. El proceso consiste en construir un
    comando gdalwarp con los parámetros adecuados, que incluyen el shapefile como línea de corte
    y la opción para recortar según esta línea. Si el comando se ejecuta correctamente, se
    guarda el archivo TIF recortado en la ubicación especificada por `output_tif`.
"""
import os
import subprocess

class RecortadorImagenes:
    """
    Clase para recortar imágenes basadas en un polígono dado.

    Atributos:
        carpeta_recortadas (str): Ruta a la carpeta de imágenes recortadas.
        carpeta_no_recortadas (str): Ruta a la carpeta de imágenes no recortadas.
        ruta_poligono (str): Ruta al archivo del polígono utilizado para recortar.
    """

    def __init__(self, carpeta_recortadas, carpeta_no_recortadas, ruta_poligono):
        """
        Inicializa la clase RecortadorImagenes.

        Args:
            carpeta_recortadas (str): Ruta a la carpeta de imágenes recortadas.
            carpeta_no_recortadas (str): Ruta a la carpeta de imágenes no recortadas.
            ruta_poligono (str): Ruta al archivo del polígono utilizado para recortar.
        """
        self.carpeta_recortadas = carpeta_recortadas
        self.carpeta_no_recortadas = carpeta_no_recortadas
        self.ruta_poligono = ruta_poligono

    def recortar_imagenes(self):
        """
        Recorta imágenes en la carpeta especificada y guarda los resultados en otra carpeta.

        Verifica si la carpeta de imágenes recortadas existe, y si no, la crea. Luego, itera
        sobre las imágenes no recortadas, las recorta utilizando el polígono especificado y guarda
        los resultados en la carpeta de imágenes recortadas.

        Returns:
            None
        """
        if os.path.exists(self.carpeta_recortadas):
            print(f"La carpeta '{self.carpeta_recortadas}' existe.")
            os.system(f"rm -rf {self.carpeta_recortadas}/*")
        else:
            print(f"La carpeta '{self.carpeta_recortadas}' no existe. Se creará ahora.")
            try:
                os.makedirs(self.carpeta_recortadas)
                print(f"Se ha creado la carpeta '{self.carpeta_recortadas}/'.")
            except OSError as error:
                print(f"No se pudo crear la carpeta '{self.carpeta_recortadas}': {error}")

        for nombre_archivo in os.listdir(self.carpeta_no_recortadas):
            if nombre_archivo.endswith(".TIF") or nombre_archivo.endswith(".tif"):
                ruta_completa = os.path.join(self.carpeta_no_recortadas, nombre_archivo)
                crop_tif(ruta_completa,
                         f"{self.carpeta_recortadas}/{nombre_archivo}",
                         self.ruta_poligono)

def crop_tif(input_tif, output_tif, cutline_shapefile):
    """
    Recorta un archivo TIF utilizando un shapefile de línea de corte usando gdalwarp.

    Args:
        input_TIF (str): Ruta al archivo TIF de entrada que se recortará.
        output_TIF (str): Ruta donde se guardará el archivo TIF recortado.
        cutline_shapefile (str): Ruta al shapefile que define la línea de corte para el recorte.

    Descripción:
    ------------
    Esta función utiliza la herramienta gdalwarp de GDAL para recortar un archivo TIF
    utilizando un shapefile de línea de corte. El proceso consiste en construir un
    comando gdalwarp con los parámetros adecuados, que incluyen el shapefile como línea de corte
    y la opción para recortar según esta línea. Si el comando se ejecuta correctamente, se
    guarda el archivo TIF recortado en la
    ubicación especificada por `output_TIF`.
    """
    # Construir el comando gdalwarp
    comando_gdalwarp = [
        "gdalwarp",
        "-cutline", cutline_shapefile,
        "-crop_to_cutline",
        input_tif,
        output_tif
    ]

    # Ejecutar el comando gdalwarp
    try:
        subprocess.run(comando_gdalwarp, check=True)
        print("El comando gdalwarp se ejecutó correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar gdalwarp: {e}")
