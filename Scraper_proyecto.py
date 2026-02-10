import requests
from bs4 import BeautifulSoup

# BLOQUE 1: Configuración de la conexión
url = "https://www.indura.cl/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# BLOQUE 2: Petición al servidor
print(f"Iniciando conexión con: {url}")
respuesta = requests.get(url, headers=headers, timeout=10)

# BLOQUE 3: Validación de estado (Retorno temprano)
if respuesta.status_code != 200:
    print(f"[ERROR] Código de estado: {respuesta.status_code}")
    exit()

# BLOQUE 4: Procesamiento de HTML
sopa = BeautifulSoup(respuesta.text, 'html.parser')

# BLOQUE 5: Extracción de Título
titulo_tag = sopa.find('title')
if not titulo_tag:
    print("[AVISO] No se encontró la etiqueta <title>")
    exit()

titulo_texto = titulo_tag.string.strip()
print(f"[TÍTULO ENCONTRADO]: {titulo_texto}")

# BLOQUE 6: Extracción de encabezado principal (H1)
encabezado = sopa.find('h1')
if not encabezado:
    print("[AVISO] No se encontró etiqueta H1 en esta página")
    exit()

print(f"[H1]: {encabezado.text.strip()}")