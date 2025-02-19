

<div align="center">
<div style="width: 100%; height: 200px; overflow: hidden; position: relative;"><img src="https://raw.githubusercontent.com/justog220/TIF-Geomatica/refs/heads/main/Informe/Images/ovitrampas.png" alt="Banner" style="position: absolute; top: -100px; left: 0; width: 100%;"></div>



<h1>mosqGIS</h1>
<img alt="PyPI - Version" src="https://img.shields.io/pypi/v/mosqGIS">
<img alt="Static Badge" src="https://img.shields.io/badge/OS-Linux-blue">
<img alt="Static Badge" src="https://img.shields.io/badge/contributions-welcome-orange">
<img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-red">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/justog220/mosqGIS/python-tests.yml?label=tests">

</div>

## Descripción

**mosqGIS** es un pipeline automatizado diseñado para la extracción y análisis de información de imágenes satelitales y datos de ovitrampas en el contexto de estudios de densidad de mosquitos. Este proyecto tiene como objetivo facilitar la obtención de matrices de clasificación de suelos, matrices de atracción y matrices de densidad de mosquitos inicial a partir de datos satelitales, utilizando tecnologías modernas de programación y herramientas de procesamiento de imágenes.

## Características

- **Extracción de datos**: Capacidad para descargar y procesar imágenes satelitales de Landsat 8.
- **Clasificación de suelos**: Generación de matrices de clasificación de suelos basadas en imágenes procesadas.
- **Predicción de densidad de mosquitos**: Análisis de datos de ovitrampas para determinar la densidad inicial de mosquitos.
- **Automatización**: Pipeline completamente automatizado para mejorar la eficiencia del flujo de trabajo.

## Requisitos

- Python 3.x
- gdal
- requirements.txt

## Instalación

Puedes instalar **mosqGIS** de las siguientes maneras:

### Opción 1: Instalación desde PyPI

Instala el paquete utilizando `pip`:

```bash
pip install mosqgis
```

### Opción 2: Instalación desde el código fuente

1. Clona el repositorio:

```bash
git clone https://github.com/justog220/mosqGIS.git
cd mosqGIS
```

2. Crear un entorno virtual e instalar las dependencias:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
pip install -r requirements.txt
```

## Uso

### Opción 1: Ejecutando desde PyPI
Si instalaste mosqGIS desde PyPI, puedes ejecutar el pipeline con el siguiente comando:

```bash
mosqGIS --carpeta_recortadas <ruta_a_imagenes_recortadas> --carpeta_no_recortadas <ruta_a_imagenes_no_recortadas> --ruta_poligono <ruta_del_poligono> --ruta_datos_ovitrampas <ruta_de_datos_ovitrampas>
```

### Opción 2: Ejecutando desde el repositorio
Si clonaste el repositorio, utiliza el siguiente comando:

```bash
python main.py --carpeta_recortadas <ruta_a_imagenes_recortadas> --carpeta_no_recortadas <ruta_a_imagenes_no_recortadas> --ruta_poligono <ruta_del_poligono> --ruta_datos_ovitrampas <ruta_de_datos_ovitrampas>
```

### Parámetros

- `--carpeta_recortadas`: Carpeta para imágenes recortadas.
- `--carpeta_no_recortadas`: Carpeta para imágenes no recortadas.
- `--ruta_poligono`: Ruta del archivo de polígono.
- `--ruta_datos_ovitrampas`: Ruta del archivo de datos de ovitrampas.

### Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar en este proyecto, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Agregando nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.