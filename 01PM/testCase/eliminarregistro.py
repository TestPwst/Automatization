from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

        Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='20']")))

        try:
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
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Permisos

        try:
            Bpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_permisos)))
            Bpermisos.click()
            Log().info("Se hace el cambio de pestaña Permisos para continuar con la eliminación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Elimina Datos

        Registropermisos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Inhibir Georeferenciación']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registropermisos) \
                .pause(0) \
                .click(Registropermisos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el primer registro de Permisos, para proceder a eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el primer registro de la pestaña permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminapermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_permiso)))
            Eliminapermiso.click()
            Log().info(" Se presiona el boton 'Eliminar de Permiso', para eliminar el segundo registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repetir Registro

        Registropermisos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Anular documentos']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registropermisos) \
                .pause(0) \
                .click(Registropermisos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el segundo registro de Permisos, para proceder a Eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el segundo registro de la pestaña permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminapermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_permiso)))
            Eliminapermiso.click()
            Log().info(" Se presiona el boton 'Eliminar de Permiso', para eliminar el segundo registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña linea de negocio

        try:
            Blineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_lineasnegocio)))
            Blineanegocio.click()
            Log().info("Se hace el cambio a la pestaña Lineas de Negocio para continuar con la eliminación del registro")

        except Exception as e:
            Log().error("No se dipo click en el botón Lineas de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Elimina Datos

        Registrolineanegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CIGARROS']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrolineanegocio) \
                .pause(0) \
                .click(Registrolineanegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el primer registro de Linea de Negocio, para proceder a Eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el primer registro de Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminalineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_lineanegocio)))
            Eliminalineanegocio.click()
            Log().info(" Se presiona el boton 'Eliminar de Linea de Negocio', para eliminar el primer registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repetir Proceso

        Registrolineanegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='EORDERING']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrolineanegocio) \
                .pause(0) \
                .click(Registrolineanegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el segundo registro Linea de negocio, para proceder a Eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el segundo registro de Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminalineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_lineanegocio)))
            Eliminalineanegocio.click()
            Log().info(" Se presiona el boton 'Eliminar de Linea de Negocio', para eliminar el segundo registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Elimina Linea negocio

        Registrolineanegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SERVICIOS']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrolineanegocio) \
                .pause(0) \
                .click(Registrolineanegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el tercer registro Lineas de Negocio, para proceder a Eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el tercer registro de la pestaña permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminalineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_lineanegocio)))
            Eliminalineanegocio.click()
            Log().info(" Se presiona el boton 'Eliminar de Linea de Negocio', para eliminar el tercer registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Impulso Ventas

        try:
            Bimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impulsoventas)))
            Bimpulsoventas.click()
            Log().info("Se hace el cambio de pestaña Impulso Ventas para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modificando Valores

        Registroimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO LS BOX 20 (FA01001)']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(0) \
                .click(Registroimpulsoventas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el primer registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se repite el proceso

        Registroimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO GOLD KS BOX 20 (FA01002)']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(0) \
                .click(Registroimpulsoventas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, revise si el xpath sigue siendo el mismo y si durante la acción de cambio de pestaña tardo mucho tiempo en realizarse")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el segundo registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repite proceso

        Registroimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO LS BOX 14 (FA01003)']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(0) \
                .click(Registroimpulsoventas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaimpulsoventas = self.wait.until( conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el tercer registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repite Proceso

        Registroimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO GOLD KS SOF 20 (FA01004)']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(0) \
                .click(Registroimpulsoventas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el cuarto registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repite proceso

        Registroimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO GOLD KS BOX 14 (FA01005)']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(0) \
                .click(Registroimpulsoventas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el quinto registro.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se cambia a la pestaña Mantenimiento clientes

        try:
            Bmanclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_mantenclientes)))
            Bmanclientes.click()
            Log().info("Se hace el cambio a la pestaña Mantenimiento Clientes para continuar con la eliminación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Mantenimiento Clientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasif1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif1)))
            Cclasif1.click()
            Log().info(" Se dió click en el checkbox Clasificación 1 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasif2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif2)))
            Cclasif2.click()
            Log().info(" Se dió click en el checkbox Clasificación 2 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasif3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif3)))
            Cclasif3.click()
            Log().info(" Se dió click en el checkbox Clasificación 3 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccolonia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_colonia)))
            Ccolonia.click()
            Log().info(" Se dió click en el checkbox Colonia ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Colonia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigopostal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigopostal)))
            Ccodigopostal.click()
            Log().info(" Se dió click en el checkbox Codigo Postal ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Codigo Postal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdireccion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_direccion)))
            Cdireccion.click()
            Log().info(" Se dió click en el checkbox Direccion ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Direccion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Centornopdv = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_entornopdv)))
            Centornopdv.click()
            Log().info(" Se dió click en el checkbox Entorno PDV ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Entorno PDV, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.click()
            Log().info(" Se dió click en el checkbox Esquina 1 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2)))
            Cesquina2.click()
            Log().info(" Se dió click en el checkbox Esquina 2 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpaises = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_paises)))
            Cpaises.click()
            Log().info(" Se dió click en el checkbox Paises ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Paises, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdepartamento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_departamento)))
            Cdepartamento.click()
            Log().info(" Se dió click en el checkbox Departamento ")

        except Exception as e:
            Log().error("No se dió click en el chekcbox Departamento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_localidad)))
            Clocalidad.click()
            Log().info(" Se dió click en el checkbox Localidad ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='20']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro4) \
                .pause(0) \
                .click(Registro3) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
            time.sleep(3)
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
            time.sleep(3)
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
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Refresca4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca4.click()
            Log().info(" Se presiona el boton 'Refrescar', para verificar si el registro ha sido eliminado.")
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
            Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_pantalla)))
            Cierra_todo.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla de Perfiles Moviles.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Cerrar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False