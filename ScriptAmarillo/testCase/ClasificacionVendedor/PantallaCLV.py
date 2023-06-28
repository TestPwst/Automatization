from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
from selenium.webdriver import ActionChains
import time


class PantallaCLV:

    def PantallaCLV(self):
        self.wait = WebDriverWait(self.driver, 150)
        # Abre la pantalla

        # Selecciona el menu

        Tablas = self.driver.find_element(By.XPATH, "//*[@id='_tablas']")
        Vendedores = self.driver.find_element(By.XPATH, "//*[@id='_tablas_vend']")
        Clasificaciones = self.driver.find_element(By.XPATH, "//*[@id='clasificacionesvendedor']")

        try:
            action = ActionChains(self.driver)
            action \
                .click(Tablas) \
                .pause(4) \
                .move_to_element(Vendedores) \
                .pause(4) \
                .click(Clasificaciones) \
                .release()
            action.perform()
            time.sleep(3)
            Log().info(" Abre la pantalla de Clasificación Vendedor")

        except Exception as e:
            Log().error("No se pudo encontrar el menu indicado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        """Abre pantalla de listado de registros."""
        self.wait = WebDriverWait(self.driver, 10)

        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("CLASIFICACIONES VENDEDOR", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Clasificación Vendedor.")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

            # Da clic en nuevo
        try:
            Nuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo)))
            Nuevo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise
