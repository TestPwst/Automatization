from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class ModificarPM:

    def ModificarPM(self):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 20)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registro = self.driver.find_element(By.XPATH, "//span[text()='20']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(2) \
                .double_click(Registro) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        #Modifica los valores

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionPM)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.MdescripcionPM)
            Log().info(" Se modifica el contenido del campo Observaciones 1 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ccargarrutas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargarrutas)))
            Ccargarrutas.click()
            time.sleep(5)

            registro_cargarrutas = self.driver.find_element(By.XPATH, "//li[text()='Una ruta']")

            action = ActionChains(self.driver)
            action \
                .click(registro_cargarrutas) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono la opción Una Ruta ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de Cargar Rutas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio pestaña Permisos

        try:
            Bpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_permisosPM)))
            Bpermisos.click()
            Log().info("Se hace el cambio de pestaña Permisos para continuar con la modificación del registro")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Modifica Valores Lista Precios

        try:
            Nuevopermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_permisoPM)))
            Nuevopermiso.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_permisosPM)))
            Cpermisos.click()
            time.sleep(5)

            registro_permisos = self.driver.find_element(By.XPATH, "//li[text()='Anular documentos']")

            action = ActionChains(self.driver)
            action \
                .click(registro_permisos) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Anular Documentos ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Anular Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardarpermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_permisoPM)))
            Guardarpermiso.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Permiso', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña linea negocio

        try:
            Blineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_lineasnegocioPM)))
            Blineanegocio.click()
            Log().info("Se hace el cambio a la pestaña Lineas de Negocio para continuar con la modificación del registro")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Lineas de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio de pestaña Impulso Ventas

        try:
            Bimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impulsoventas)))
            Bimpulsoventas.click()
            Log().info("Se hace el cambio de pestaña Impulso Ventas para continuar con la modificación del registro")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Modificando Valores

        Registroimpulsoventas = self.driver.find_element(By.XPATH, "//span[text()='MARLBORO LS BOX 20 (FA01001)']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(2) \
                .click(Registroimpulsoventas) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el primer registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Se repite el proceso

        Registroimpulsoventas = self.driver.find_element(By.XPATH, "//span[text()='MARLBORO GOLD KS BOX 20 (FA01002)']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(2) \
                .click(Registroimpulsoventas) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, revise si el xpath sigue siendo el mismo y si durante la acción de cambio de pestaña tardo mucho tiempo en realizarse")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el segundo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Repite proceso

        Registroimpulsoventas = self.driver.find_element(By.XPATH, "//span[text()='MARLBORO LS BOX 14 (FA01003)']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(2) \
                .click(Registroimpulsoventas) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el tercer registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Repite Proceso

        Registroimpulsoventas = self.driver.find_element(By.XPATH, "//span[text()='MARLBORO GOLD KS SOF 20 (FA01004)']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(2) \
                .click(Registroimpulsoventas) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el cuarto registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Repite proceso

        Registroimpulsoventas = self.driver.find_element(By.XPATH, "//span[text()='MARLBORO GOLD KS BOX 14 (FA01005)']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpulsoventas) \
                .pause(2) \
                .click(Registroimpulsoventas) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impulsoventa)))
            Eliminaimpulsoventas.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar de Impulso Ventas', para eliminar el quinto registro.")

        except Exception as e:
            Log().error("No se click en el botón Eliminar de Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise
