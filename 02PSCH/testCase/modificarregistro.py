from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.log import Log
from common.globalparam import img_path
import os
import time

class modificarregistro:

    def modificarregistro(self, conditions, Configuracion):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 60)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(0) \
                .double_click(Registro) \
                .pause(0) \
                .release()
            action.perform()
            
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripción ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cqueryvariables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_queryvariables)))
            Cqueryvariables.clear()
            Cqueryvariables.send_keys(Configuracion.Mqueryvariables)
            Log().info(" Se modifica el contenido del campo Query Variables ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar los Query Variables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccomprimir = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_comprimir)))
            Ccomprimir.click()
            Log().info(" Se dió click en el checkbox Comprimir.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Comprimir, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cusuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_usuario)))
            Cusuario.click()

            registro_usuario = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='mabcecgut']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_usuario) \
                .double_click(registro_usuario) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de usuario.")

        except Exception as e:
            Log().error("No se encontró el registro de Usuario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpassword = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_password)))
            Cpassword.clear()
            Cpassword.send_keys(Configuracion.Mpassword)
            Log().info(" Se modifica el contenido del campo Password ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Password, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cactiva = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_activa)))
            Cactiva.click()
            Log().info(" Se dió click en el checkbox Activa.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Activa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
        
        try:
            Cejecutar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ejecutar)))
            Cejecutar.click()

            registro_ejecutar = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Interface']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_ejecutar) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Interface.")

        except Exception as e:
            Log().error("No se dió click en la opción Interface, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnombresalida = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nombresalida)))
            Cnombresalida.clear()
            Cnombresalida.send_keys(Configuracion.Mnombresalida)
            Log().info(" Se modifica el contenido del campo Nombre Salida ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Nombre Salida, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambia pestaña intrefaces

        try:
            Binterfaces = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_interfaces)))
            Binterfaces.click()
            Log().info(" Se cambia a la pestaña Interfaces para continuar con la modificación del registro.")

        except Exception as e:
            Log().error("No se dió click en el boton Interfaces, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Csistema = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_sistema)))
            Csistema.click()

            registro_sistema = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PMMC']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_sistema) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Sistema.")

        except Exception as e:
            Log().error("No se encontró el registro de Sistema, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cinterface = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_interface)))
            Cinterface.click()

            registro_interface = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='VOLDEL']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_interface) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Interface.")

        except Exception as e:
            Log().error("No se encontró el registro de Interface, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False