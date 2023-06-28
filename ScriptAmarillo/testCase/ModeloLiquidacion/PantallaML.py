from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
from selenium.webdriver import ActionChains
import time


class pantallaML:

    def pantallaML(self):
        self.wait = WebDriverWait(self.driver, 150)

        # Selecciona el menu

        Tablas = self.driver.find_element(By.XPATH, "//*[@id='_tablas']")
        Liquidaciones = self.driver.find_element(By.XPATH, "//*[@id='_tablas_liq']")
        ModelosLiquidacion = self.driver.find_element(By.XPATH, "//*[@id='modelosliquidacion']")

        try:
            action = ActionChains(self.driver)
            action \
                .click(Tablas) \
                .pause(4) \
                .move_to_element(Liquidaciones) \
                .pause(4) \
                .click(ModelosLiquidacion) \
                .release()
            action.perform()
            time.sleep(5)
            Log().info(" Abre la pantalla de Modelos Liquidación")

        except Exception as e:
            Log().error("No se pudo encontrar el menu indicado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            self.assertEqual("MODELOS DE LIQUIDACIÓN", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Modelos Liquidacion.")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise
