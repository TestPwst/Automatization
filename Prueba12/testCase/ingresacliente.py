from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/Versiones/automatizaciones/PosCu/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral
cerrarsesionP = SourceFileLoader("cerrarsesion", "C:/xampp/htdocs/versiones/automatizaciones/PosCu/cerrarsesion.py").load_module()
cerrarsesion = cerrarsesionP.cerrarsesion

class ingresacliente:

    def ingresacliente(self):
        """Ingresa Cliente"""
        self.wait = WebDriverWait(self.driver, 60)


        # Borra el cliente predeterminado
        try:
            ClienteBorrar = self.wait.until(conditions.visibility((By.ID, configgnral.id_cliente)))
            ClienteBorrar.click()
            Log().info(" Da click en clientes")
            time.sleep(1)
            ClienteBorrar.clear()
            Log().info(" Elimina los datos")

        except Exception as e:
            Log().error(
                "No se pudieron borrar los datos del cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        # Escribe el nuevo cliente
        try:
            ClienteNuevo = self.wait.until(conditions.visibility((By.ID, configgnral.id_cliente)))
            ClienteNuevo.send_keys(configgnral.nombre_cliente)
            Log().info("Escribe el nombre del cliente")
            time.sleep(1)


        except Exception as e:
            Log().error(
                "No se pudo escribir el nombre del cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise


        #Selecciona al cliente
        try:
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.DOWN) \
                .send_keys(Keys.ENTER) \
                .pause(1) \
                .release()
            action.perform()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Log().info("Selecciona al cliente")



        except Exception as e:
            Log().error(
                "No se pudo usar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise


