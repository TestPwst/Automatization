from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from common.log import Log
from common.globalparam import img_path
import os
import time

class eliminarregistro:

    def eliminarregistro(self, conditions, Configuracion):

        self.wait = WebDriverWait(self.driver, 60)
        """Se selecciona el registro y se elimina."""
            # Da clic en refrescar
        try:
            Refresca3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca3.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a eliminar el registro.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))
            time.sleep(1)
            Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro3) \
                .pause(0) \
                .double_click(Registro3) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            VentanaTope = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_topes)))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(VentanaTope) \
                .pause(0) \
                .click(VentanaTope) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la ventana de tope, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 5)
            Tope = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='7.0000%']")))
            self.wait = WebDriverWait(self.driver, 60)
            action = ActionChains(self.driver)
            action \
                .move_to_element(Tope) \
                .pause(0) \
                .click(Tope) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el tope creado, para proceder a eliminarlo.")

        except (NoSuchElementException, TimeoutException):
            pass
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_topes)))
            Elimina.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            VentantaCuentaArticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ctaarticulo)))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(VentantaCuentaArticulo) \
                .pause(0) \
                .click(VentantaCuentaArticulo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la ventana cuenta/articulo, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 5)
            CuentaArticulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100% ZACATECANA (Código: 679945 - Código interno: 0010447891)']")))
            self.wait = WebDriverWait(self.driver, 60)
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(CuentaArticulo) \
                .pause(0) \
                .click(CuentaArticulo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la cuenta/articulo creado, para proceder a eliminarlo.")

        except (NoSuchElementException, TimeoutException):
            pass
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_ctaarticulo)))
            Elimina.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            VentantaCuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cuentas)))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(VentantaCuentas) \
                .pause(0) \
                .click(VentantaCuentas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la ventana cuentas, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 5)
            Cuenta = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100% ZACATECANA (Código: 679945 - Código interno: 0010447891)']")))
            self.wait = WebDriverWait(self.driver, 60)
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Cuenta) \
                .pause(0) \
                .click(Cuenta) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la cuenta creado, para proceder a eliminarlo.")

        except (NoSuchElementException, TimeoutException):
            pass
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_cuentas)))
            Elimina.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            VentantaArticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_articulos)))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(VentantaArticulos) \
                .pause(0) \
                .click(VentantaArticulos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la cuenta/articulo creado, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 5)
            Articulos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='FLEX SHAVE G MAX II (40041602)']")))
            self.wait = WebDriverWait(self.driver, 60)

            action = ActionChains(self.driver)
            action \
                .move_to_element(Articulos) \
                .pause(0) \
                .click(Articulos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el articulo creado, para proceder a eliminarlo.")
        
        except (NoSuchElementException, TimeoutException):
            pass
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_articulos)))
            Elimina.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            VentantaTipoDoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_tipodoc)))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(VentantaTipoDoc) \
                .pause(0) \
                .click(VentantaTipoDoc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en la ventana tipo documento, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 5)
            TipoDoc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1 Click - 1 Pedido Contado para Factura (PM93)']")))
            self.wait = WebDriverWait(self.driver, 60)
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(TipoDoc) \
                .pause(0) \
                .click(TipoDoc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el tipo de documento creado, para proceder a eliminarlo.")

        except (NoSuchElementException, TimeoutException) as e:
            pass
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_tipodoc)))
            Elimina.click()
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro3) \
                .pause(0) \
                .click(Registro3) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina)))
            Elimina.click()
            Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Confirma_Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_acepta_eliminar)))
            Confirma_Elimina.click()
            Log().info(" Se confirma el eliminado del registro")
            
        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Refresca4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca4.click()
            Log().info(" Se presiona el boton 'Refrescar', para verificar que el registro se ha eliminado.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_pantalla)))
            Cierra_todo.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla de Perfiles de Comisión.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Cerrar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False