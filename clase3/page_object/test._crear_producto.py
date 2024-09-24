import unittest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import HtmlTestRunner
from crear_producto_page import CrearProductoPage

class CrearProductoTest(unittest.TestCase):

    def setUp(self):
        driver_options = Options()
        #headless es para que no se muestre la ejecución
        #driver_options.add_argument("--headless")
        #driver_options.add_argument("start-maximized")
        driver_options.add_argument("window-size=800x600")
        driver_path = r"D:\JB Enterprise\Automatización de Pruebas Python con Selenium\semana-03\clase\clase3\browser\chrome\chromedriver-win64\129.0.6668.58\chromedriver.exe"
        binary_path = r"D:\JB Enterprise\Automatización de Pruebas Python con Selenium\semana-03\clase\clase3\browser\chrome\chrome-win64\129.0.6668.58\chrome.exe"
        service = Service(driver_path)
        driver_options.binary_location = binary_path
        self.driver = webdriver.Chrome(service = service, options = driver_options)
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 2)

    def test_crear_producto(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://127.0.0.1:9000/productos/crear/")
        codigo_producto = "00000101"
        nombre_producto = "Iphone16"
        cantidad_producto = 5
        precio_producto = 99
        descripcion_producto = "Celular alta gama"
        paginaCrearProducto = CrearProductoPage(driver)
        paginaCrearProducto.abrir("http://127.0.0.1:9000/productos/crear/")
        paginaCrearProducto.ingresar_codigo(codigo_producto)
        paginaCrearProducto.ingresar_nombre(nombre_producto)
        paginaCrearProducto.ingresar_descripcion(descripcion_producto)
        paginaCrearProducto.ingresar_cantidad_minima(cantidad_minima_producto)
        paginaCrearProducto.ingresar_precio(precio_producto)
        paginaCrearProducto.guardar_producto()

    def tearDown(self):
        if self.driver:
            self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(CrearProductoTest))
    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(
        output = "reportes",
        report_name = "Crear producto",
        report_title = "Crear nuevo producto utilizando Selenium",
        combine_reports = True,
        add_timestamp = True
    )
    runner.run(suite())