from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time
from config import Configuracion
from cerrarsesion import cerrarsesion

class cierraticket:

    def cierraticket(self):
        """Cierra ticket"""
        self.wait = WebDriverWait(self.driver, 60)

        # Cierra el ticket

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_desplazarabajo)))
            Moverpantalla.click()


            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(1) \
                .release()
            action.perform()
            cierraticket = self.wait.until(conditions.clickable((By.XPATH, Configuracion.boton_xpath_cerrarticket)))
            cierraticket.click()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Log().info(" Da click en el boton para cerrar el ticket")
            time.sleep(2)



        except Exception as e:
                Log().error(
                    "No se pudo cerrar la ventana del ticket, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return cerrarsesion.cerrarsesion()
                raise








