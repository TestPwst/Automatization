from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class realizaventa:

    def realizarventa(self):
        """Ingresa al documento para realizar la venta"""
        self.wait = WebDriverWait(self.driver, 70)

        #Ingresa a Venta de Contado

        Documentos = self.driver.find_element(By.XPATH, "//*[@id='_documentos']")
        Clientes = self.driver.find_element(By.XPATH, "//*[@id='_doc_cli']")
        MasDocs = self.driver.find_element(By.XPATH, "//*[@id='doc_clientes_more']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Documentos) \
                .pause(4) \
                .move_to_element(Clientes) \
                .pause(4) \
                .click(MasDocs) \
                .release()
            action.perform()

            time.sleep(10)

        except Exception as e:
            Log().error("No se pudo ingresar al menu indicado, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            raise

        Registro = self.driver.find_element(By.XPATH, "//*[text()='Venta Contado    (PM03)']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(2) \
                .double_click(Registro) \
                .pause(2) \
                .release()
            action.perform()

            Log().info("Se abre el documento de venta a realizar")
            time.sleep(13)

        except Exception as e:
            Log().error("No se encontró el el registro deseado, validar que la acción anterior haya finalizado,"
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

        #Ingresa el cliente y los artículos a comprar.

        try:
            Ccliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cliente)))
            Ccliente.send_keys(Configuracion.Icuenta)
            Ccampo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ob)))
            Ccampo.click()
            time.sleep(15)

        except Exception as e:
            Log().error("No se pudo ingreso el campo cuenta, validar que la acción anterior haya finalizado,"
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
            Bagregar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_add_art)))
            Bagregar.click()
            time.sleep(7)

        except Exception as e:
            Log().error("No se pudo dar click al botón agregar artículos, validar que la acción anterior haya finalizado,"
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
            Cart1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_art)))
            Cart1.send_keys(Configuracion.Iarticulo1)
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo ingresar el campo artículo, validar que la acción anterior haya finalizado,"
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
            Cnumserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_numserie)))
            Cnumserie.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se pudo ingresar el campo numero de serie, validar que la acción anterior haya finalizado,"
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
            Ccant1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cant)))
            Ccant1.send_keys(Configuracion.Icantidad1)
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo ingresar el campo para ingresar la cantidad, validar que la acción anterior haya finalizado,"
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
            Aceptar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar_art)))
            Aceptar.click()
            Log().info("Se agrega el artículo facturado por unidades a la venta")
            time.sleep(10)

        except Exception as e:
            Log().error("No se pudo dar click al botón de aceptar, validar que la acción anterior haya finalizado,"
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
            Cart2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_art)))
            Cart2.send_keys(Configuracion.Iarticulo2)
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo ingresar el campo artículo, validar que la acción anterior haya finalizado,"
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
            Cnumserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_numserie)))
            Cnumserie.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se pudo ingresar el campo numero de serie, validar que la acción anterior haya finalizado,"
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
            Ccant2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cant)))
            Ccant2.send_keys(Configuracion.Icantidad2)
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo ingresar el campo cantidad, validar que la acción anterior haya finalizado,"
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
            Aceptar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar_art)))
            Aceptar.click()
            Log().info("Se agrega el artículo facturado por packing a la venta")
            time.sleep(10)

        except Exception as e:
            Log().error("No se pudo dar click al botón de aceptar, validar que la acción anterior haya finalizado,"
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
            Cancelar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_art)))
            Cancelar.click()
            time.sleep(5)

        except Exception as e:
            Log().error("No se pudo dar clikc al botón de Cancelar, validar que la acción anterior haya finalizado,"
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
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info("Se guarda la venta realizaada")
            time.sleep(15)

        except Exception as e:
            Log().error("No se dar click al botón Guardar, validar que la acción anterior haya finalizado,"
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
