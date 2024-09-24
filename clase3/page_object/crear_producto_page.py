from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class CrearProductoPage:
    def __init__(self.driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    codigo_input = (By.ID, "id_codigo")
    nombre_input = (By.ID, "id_nombre")
    descriipcion_input = (By.ID, "id_descripcion")
    cantidad_minima_input = (By.ID, "id_cantidad_minnima")
    precio_input = (By.ID, "id_precio")
    guardar_producto_button = (By.ID, "btnSave")

    def abrir(self, url):
        self.driver.get(url)

    def ingresar_codigo(self, codigo):
        self.wait.until(EC.element_to_be_clickable(self.codigo_input)).send_keys(codigo)

    def ingresar_nombre(self, nombre):
        self.wait.until(EC.element_to_be_clickable(self.nombre_input)).send_keys(nombre)

    def ingresar_codigo(self, descripcion):
        self.wait.until(EC.element_to_be_clickable(self.descripcion_input)).send_keys(descripcion)

    def ingresar_cantidad_minima(self, cantidad_minima):
        cantidad_minima_campo = self.wait.until(EC.element_to_be_clickable(self.cantidad_minima_input))
        cantidad_minima_campo.clear()
        cantidad_minima_campo.send_keys(cantidad_minima)

    def ingresar_precio(self, precio):
        precio_campo = self.wait.until(EC.element_to_be_clickable(self.precio_input))
        precio_campo.clear()
        precio_capo.send_keys(precio)

    def guardar_producto(self):
        self.wait.until(EC.element_to_be_clickable(self.guardar_producto_button))click()