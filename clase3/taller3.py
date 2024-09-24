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

class CrearProductoTest(unittest.TestCase):

    def setUp(self):
        driver_options = Options()
        #driver_options.add_argument("--headless")
        driver_options.add_argument("start-maximized")
        #driver_options.add_argument("window-size=800x600")
        self.driver = webdriver.Chrome(options = driver_options)
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
        codigo_input = driver.find_element(By.XPATH,'//*[@id="id_codigo"]')
        codigo_input.send_keys(codigo_producto)
        nombre_input = wait.until(EC.presence_of_element_located((By.ID,"id_nombre")))
        nombre_input.send_keys(nombre_producto)
        descripcion_input = wait.until(EC.visibility_of_element_located((By.ID,"id_descripcion")))
        descripcion_input.send_keys(descripcion_producto)
        cantidad_minima_input = wait.until(EC.element_to_be_clickable((By.ID,"id_cantidad_minima")))
        cantidad_minima_input.clear()
        cantidad_minima_input.send_keys(cantidad_producto)
        precio_input = wait.until(EC.element_to_be_clickable((By.ID,"id_precio")))
        precio_input.clear()
        precio_input.send_keys(precio_producto)
        guardar_producto_button = wait.until(EC.element_to_be_clickable((By.ID,"btnSave")))
        driver.save_screenshot("1. crear_producto.png")
        guardar_producto_button.click()
        self.assertIn("/productos/", driver.current_url)
        titulo_pagina = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/section/nav/ul/li[2]/a/strong')
        titulo_text = "Lista de Productos"
        self.assertEqual(titulo_pagina.text, titulo_text, f"El texto esta {titulo_pagina.text}, pero se esperaba {titulo_text}")

    def test_editar_producto(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://127.0.0.1:9000/productos/")
        fila = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="datatable"]/tbody/tr[2]')))
        fila.click()
        editar_button = driver.find_element(By.ID,"edit_record")
        editar_button.click()
        codigo_producto = "00000200"
        nombre_producto = "Honor 200 Pro"
        cantidad_producto = 10
        precio_producto = 490
        descripcion_producto = "Nuevo Android 14"
        codigo_input = driver.find_element(By.ID,"id_codigo")
        codigo_input.clear()
        codigo_input.send_keys(codigo_producto)
        nombre_input = wait.until(EC.presence_of_element_located((By.NAME,"nombre")))
        nombre_input.clear()
        nombre_input.send_keys(nombre_producto)
        cantidad_minima_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#id_cantidad_minima")))
        cantidad_minima_input.clear()
        cantidad_minima_input.send_keys(cantidad_producto)
        precio_input = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_precio"]')))
        precio_input.clear()
        precio_input.send_keys(precio_producto)
        descripcion_input = driver.find_element(By.ID,"id_descripcion")
        descripcion_input.clear()
        descripcion_input.send_keys(descripcion_producto)
        editar_producto_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/section[2]/div/div/div/div/form/div[2]/button")))
        driver.save_screenshot("2. producto_editado.png")
        editar_producto_button.click()
        self.assertIn("/productos/", driver.current_url)

    def test_ver_productos(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://127.0.0.1:9000/productos/")
        fila3 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="datatable"]/tbody/tr[3]')))
        fila3.click()
        ver_button = driver.find_element(By.ID,"view_record")
        ver_button.click()
        driver.save_screenshot("3. vista_producto_creado.png")
        regresar_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/a")))
        regresar_button.click()
        fila2 = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="datatable"]/tbody/tr[2]')))
        fila2.click()
        ver_button = driver.find_element(By.ID,"view_record")
        ver_button.click()
        driver.save_screenshot("4. vista_producto_editado.png")
        regresar_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/section[2]/div/div/div/div/div[3]/a")))
        regresar_button.click()
        self.assertIn("/productos/", driver.current_url)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

class EliminarProductoTest(unittest.TestCase):

    def setUp(self):
        driver_options = Options()
        #driver_options.add_argument("--headless")
        driver_options.add_argument("start-maximized")
        #driver_options.add_argument("window-size=800x600")
        self.driver = webdriver.Chrome(options = driver_options)
        self.driver.implicitly_wait(3)
        self.wait = WebDriverWait(self.driver, 2)
    
    def test_eliminar_producto(self):
        driver = self.driver
        wait = self.wait
        driver.get("http://127.0.0.1:9000/productos/")
        fila = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="datatable"]/tbody/tr[2]')))
        fila.click()
        eliminar_button = driver.find_element(By.ID,"delete_record")
        eliminar_button.click()
        confirmar_button = driver.find_element(By.ID,"confirm_delete_record")
        confirmar_button.click()
        driver.save_screenshot("5. producto_editado_eliminado.png")
        self.assertIn("/productos/", driver.current_url)
    
    def tearDown(self):
        if self.driver:
            self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(CrearProductoTest))
    suite.addTest(loader.loadTestsFromTestCase(EliminarProductoTest))
    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(
        output = "reportes",
        report_name = "Crear producto",
        report_title = "Crear, editar, visualizar y eliminar producto utilizando Selenium",
        combine_reports = True,
        add_timestamp = True
    )
    runner.run(suite())