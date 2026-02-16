# Datavergencia: Pipeline de Inteligencia de Mercado (Scraping Indura)

## 🎯 Propósito del Proyecto
Este repositorio es una demostración técnica de soluciones de ingeniería de datos aplicadas al sector industrial. Debido a acuerdos de confidencialidad (NDA) en experiencias laborales previas, este proyecto sirve como **evidencia de capacidad técnica**, replicando arquitecturas de extracción, procesamiento y automatización de datos en un entorno controlado y público.

El objetivo central es capturar, procesar y visualizar la fluctuación de precios de insumos en el catálogo de **Indura**, transformando datos web no estructurados en una herramienta operativa para la toma de decisiones.

## 🏗️ Arquitectura del Pipeline ETL
El sistema opera bajo un flujo de ingeniería de datos moderno y portable:

1. **Extracción (Web Scraping)**: Motor desarrollado en Python que automatiza la obtención de precios, descripciones y disponibilidad desde Indura.
2. **Almacenamiento Cloud**: Integración con **Amazon S3** (`datavergencia-industrial-datos`) para la persistencia de datos crudos (Data Lake).
3. **Procesamiento**: Uso de **Pandas** en Fedora Linux para la limpieza, normalización y transformación de los archivos CSV extraídos.
4. **Visualización y Reporte**: Carga automatizada en **Google Sheets API**, permitiendo el acceso a dashboards actualizados sin intervención manual.



## 🛠️ Stack Tecnológico
* **Lenguajes**: Python 3.x
* **Cloud**: AWS (S3), Google Cloud (Sheets/Drive API)
* **Contenedores**: **Docker** (para asegurar la portabilidad y despliegue del entorno)
* **Librerías Clave**: Pandas, Boto3, Gspread, Selenium
* **Entorno de Desarrollo**: Fedora Linux

## 🐳 Portabilidad con Docker
Para garantizar que el pipeline sea ejecutable en cualquier infraestructura sin conflictos de dependencias, el proyecto está completamente contenedorizado.

**Para construir y ejecutar el contenedor:**
1. Construir la imagen: `docker build -t datavergencia-etl .`
2. Ejecutar el proceso: `docker run --env-file .env datavergencia-etl`

## 🚀 Instalación (Entorno Local)
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv .venv && source .venv/bin/activate`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Configurar credenciales: Asegurar la presencia de `Himitsu.json` para Google Cloud y las llaves de AWS en el entorno.
5. Ejecutar integrador: `python integrador_reporte.py`.

---
**Datavergencia** | *Proyecto desarrollado por Daniel Troncoso para validar competencias en Ingeniería de Datos y automatización industrial.*
