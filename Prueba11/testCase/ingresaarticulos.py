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
from cerrarsesion import cerrarsesion
from config import Configuracion


class ingresaarticulos:

    def ingresaarticulos(self):
        """Ingresa Articulos"""
        self.wait = WebDriverWait(self.driver, 60)
        time.sleep(2)
# Cierra mensaje de alerta
        try:
            alerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_buton_cerrarmensaje)))
            alerta.click()
            Log().info("Cierra mensaje de alerta")
            time.sleep(1)


        except Exception as e:
            Log().error(
                "No se pudo cerrar el mensaje de alerta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise
        
        # Ingresa primer articulo
        try:
            Articulo1 = self.wait.until(conditions.visibility((By.ID, Configuracion.id_articulos)))
            Articulo1.send_keys(Configuracion.articulo1)
            Log().info(" Escribe el primer articulo")
            time.sleep(1)


        except Exception as e:
            Log().error(
                "No se pudo escribir el codigo del articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise




        #Selecciona el articulo
        try:
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.DOWN) \
                .send_keys(Keys.ENTER) \
                .pause(1) \
                .release()
            action.perform()
            Log().info("Selecciona el articulo")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)



        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise


