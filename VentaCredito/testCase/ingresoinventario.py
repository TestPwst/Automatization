from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
from selenium.webdriver import ActionChains
import time


class ingresoinventario:

    def ingresosinventario(self):
        self.wait = WebDriverWait(self.driver, 150)

        # Selecciona el menu

        try:
            CMenu = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_menu)))
            CMenu.click()
            CMenu.send_keys(Configuracion.Imenu)
            time.sleep(2)

        except Exception as e:
            Log().error("No se ingresó al campo buscar, validar que la acción anterior haya finalizado,"
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
            Explorador = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_explorador)))
            Explorador.click()
            Log().info("Se ingresa al explorador de reportes")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click al botón buscar, validar que la acción anterior haya finalizado,"
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

        """Abre pantalla Explorador de Reportes"""
        self.wait = WebDriverWait(self.driver, 10)

        # Busca el reporte para visualizar el inventario del vendedor
        try:
            CBuscar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_buscar)))
            CBuscar.send_keys(Configuracion.Ibuscar)
            time.sleep(2)

        except Exception as e:
            Log().error("No se ingresó el campo buscar, validar que la acción anterior haya finalizado,"
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
            Buscar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_buscar)))
            Buscar.click()
            time.sleep(4)

        except Exception as e:
            Log().error("No se dió click al botón buscar, validar que la acción anterior haya finalizado,"
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

        Registro = self.driver.find_element(By.XPATH, "//span[text()='jmdadmin']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(2) \
                .double_click(Registro) \
                .pause(2) \
                .release()
            action.perform()

            Log().info("Se ingresa al reporte de toma de stock del vendedor")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el el reporte deseado, validar que la acción anterior haya finalizado,"
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

        #Ingresa los valores para abrir el reporte
        try:
            CDesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_desde)))
            CDesde.send_keys(Configuracion.Idesde)
            time.sleep(2)

        except Exception as e:
            Log().error("No se ingresó el campo Desde Linea, validar que la acción anterior haya finalizado,"
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
            CHasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hasta)))
            CHasta.send_keys(Configuracion.Ihasta)
            time.sleep(2)

        except Exception as e:
            Log().error("No se ingresó el campo hasta línea, validar que la acción anterior haya finalizado,"
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
            CAlmacen = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_almancen)))
            CAlmacen.send_keys(Configuracion.Ialmacen)
            time.sleep(2)

        except Exception as e:
            Log().error("No se ingresó el campo buscar, validar que la acción anterior haya finalizado,"
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
            VerReporte = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ver)))
            VerReporte.click()
            time.sleep(1)
            VerReporte.click()
            Log().info("Se ingresan los datos para ver el reporte del vendedor deseado")
            time.sleep(7)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click al botón buscar, validar que la acción anterior haya finalizado,"
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