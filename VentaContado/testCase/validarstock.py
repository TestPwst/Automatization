from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class validarstock:

    def validarstock(self):
        """Se abre el reporte de stock para validar la dismunición de mercancía"""
        self.wait = WebDriverWait(self.driver, 70)

        try:
            VerReporte = self.wait.until(conditions.visibility((By.XPATH, Configuracion.refrescar_report)))
            VerReporte.click()
            time.sleep(10)
            Log().info("Se actualiza el stock del vendedor")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(2)

        except Exception as e:
            Log().error("No se dar click al botón refrescar reporte, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.quit()
            raise
