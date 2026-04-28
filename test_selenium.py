from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def get_chrome_options():
    """Configura las opciones de Chrome para evitar detección."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    return options

def run_test():
    options = get_chrome_options()
    driver = webdriver.Chrome(options=options)
    
    # Inyección de script para ocultar rastros de automatización
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    print("🚀 Iniciando navegación hacia Indura...")
    driver.get("https://www.indura.cl/Categoria/Soldadura/3")
    time.sleep(10)  # Espera para carga de JS y validación de WAF

    # --- BLOQUE DE VALIDACIÓN DE TÍTULO (Early Return) ---
    titulo = driver.title
    print(f"📄 Título obtenido: {titulo}")

    if "ERROR" in titulo.upper() or "ACCESS DENIED" in titulo.upper():
        print("❌ BLOQUEO PERSISTENTE: CloudFront rechazó la conexión.")
        driver.quit()
        return

    if "INDURA" not in titulo.upper():
        print("⚠️ Título inesperado. Posible redirección o carga incompleta.")
        driver.quit()
        return

    print("✅ ¡ÉXITO! Acceso validado.")

    # --- BLOQUE DE EXTRACCIÓN DE CONTENIDO ---
    try:
        body_text = driver.find_element(By.TAG_NAME, "body").text
        if "$" in body_text:
            print("💰 Confirmado: Se visualizan precios en el DOM.")
        if "$" not in body_text:
            print("⚠️ Acceso concedido, pero los precios no cargaron (revisar selectores).")
    except Exception as e:
        print(f"💥 Error al leer el body: {e}")

    # --- FINALIZACIÓN ---
    driver.quit()
    print("🔌 Sesión cerrada correctamente.")

if __name__ == "__main__":
    run_test()
