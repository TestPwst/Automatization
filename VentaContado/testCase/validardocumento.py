from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class validardocumento:

    def validardocumento(self):
        """Se ingresa a documentos pendientes para ver el documento creado"""

        self.wait = WebDriverWait(self.driver, 70)

        # Ingresa a la pantalla documentos emitidos

        Documentos = self.driver.find_element(By.XPATH, "//*[@id='_documentos']")
        Emitidos = self.driver.find_element(By.XPATH, "//*[@id='verdocumentos|false']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Documentos) \
                .pause(3) \
                .click(Documentos) \
                .pause(2) \
                .click(Emitidos) \
                .release()
            action.perform()

            time.sleep(5)

        except Exception as e:
            Log().error("No se pudo ingresar el menu documentos emitidos, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            raise

        FiltroDoc = self.driver.find_element(By.XPATH, "//div[text()= 'Documentos Emitidos']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(FiltroDoc) \
                .pause(3) \
                .double_click(FiltroDoc) \
                .pause(3) \
                .release()
            action.perform()

            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click al filto documentos emitidos, validar que la acción anterior haya finalizado,"
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

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, "//div[text()= '# Sucursal de documento']")))
            Moverpantalla.click()
            time.sleep(3)

            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .send_keys(Keys.SPACE) \
                .send_keys(Keys.SPACE) \
                .pause(5) \
                .release()
            action.perform()
            time.sleep(3)

        except Exception as e:
            Log().error("No se logró mover la pantalla, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.quit()
            raise

        FiltroHoy = self.driver.find_element(By.XPATH, "//div[text()= 'Hoy']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(FiltroHoy) \
                .pause(5) \
                .double_click(FiltroHoy) \
                .pause(5) \
                .release()
            action.perform()

            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click al filto hoy, revise validar que la acción anterior haya finalizado,"
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

        try:
            Refrescar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refrescar.click()
            Log().info("Se visualiza la venta realizada")
            time.sleep(10)

        except Exception as e:
            Log().error("No se dió click el botón Refrescar, validar que la acción anterior haya finalizado,"
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
