Pipeline ETL — Monitoreo de Precios Industriales
Pipeline end-to-end de ingeniería de datos para captura, almacenamiento y visualización de precios de insumos industriales. Automatiza la extracción desde proveedores web, persiste datos en AWS S3 y genera reportes actualizados en Google Sheets sin intervención manual.
Arquitectura
Web Scraping (Selenium) → AWS S3 (Data Lake) → Procesamiento (Pandas) → Google Sheets API
1. Extracción
Motor de scraping con Selenium y anti-detección (CDP injection) para captura automatizada de catálogos de proveedores industriales.
2. Almacenamiento Cloud
Datos crudos almacenados en bucket S3 (datavergencia-industrial-datos) usando boto3 para persistencia escalable.
3. Procesamiento
Transformación y limpieza de datos con Pandas — normalización de precios, detección de cambios, validación de esquemas.
4. Visualización
Carga automatizada a Google Sheets via API (gspread) para acceso en tiempo real sin intervención manual.
Stack Técnico

Lenguaje: Python 3.x
Cloud: AWS S3 (boto3), Google Cloud (Sheets/Drive API)
Scraping: Selenium, BeautifulSoup
Data Processing: Pandas
Containerización: Docker
Entorno: Fedora Linux
