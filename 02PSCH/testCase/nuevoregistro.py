from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time



class nuevoregistro:

    def nuevoregistro(self, conditions, Configuracion):
        """Abre la ventana para crear un nuevo registro"""
        self.wait = WebDriverWait(self.driver, 60)

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta
        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("PROGRAMAS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de las etiquetas
        try:
            Codigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo))).text
            self.assertEqual("Código", Codigo, "Campo visible")
            Log().info(" El campo 'Código' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Código' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcion))).text
            self.assertEqual("Descripción", Descripcion, "Campo visible")
            Log().info(" El campo 'Descripción' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo Descripción' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Queryvariables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_queryvariables))).text
            self.assertEqual("Query Variables", Queryvariables, "Campo visible")
            Log().info(" El campo 'Query Variables' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Query Variables' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Comprimir = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_comprimir))).text
            self.assertEqual("Comprimir", Comprimir, "Campo visible")
            Log().info(" El campo 'Comprimir' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Comprimir' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Usuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_usuario))).text
            self.assertEqual("Usuario", Usuario, "Campo visible")
            Log().info(" El campo 'Usuario' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Usuario' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Password = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_password))).text
            self.assertEqual("Password", Password, "Campo visible")
            Log().info(" El campo 'Password' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Password' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Activa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_activa))).text
            self.assertEqual("Activa", Activa, "Campo visible")
            Log().info(" El campo 'Activa' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Activa' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ejecutar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_ejecutar))).text
            self.assertEqual("Ejecutar", Ejecutar, "Campo visible")
            Log().info(" El campo 'Ejecutar' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Ejecutar' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el Codigo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la Descripcion del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cqueryvariables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_queryvariables)))
            Cqueryvariables.send_keys(Configuracion.Iqueryvariables)
            Log().info(" Ingresa los Query Variables del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar los Query Variables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cusuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_usuario)))
            Cusuario.click()

            registro_usuario = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='mabvvv002']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_usuario) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Usuario.")

        except Exception as e:
            Log().error("No se encontró el registro de Usuario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpassword = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_password)))
            Cpassword.send_keys(Configuracion.Ipassword)
            Log().info(" Ingresa el Password del nuevo registro ")

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
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

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

        # Continuar con el Ingreso de los Valores

        try:
            Cnombresalida = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nombresalida)))
            Cnombresalida.send_keys(Configuracion.Inombresalida)
            Log().info(" Ingresa el Nombre Salida del nuevo registro ")

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
            Log().info(" Se cambia a la Pestaña Interfaces para continuar con el nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el boton Interfaces, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida Existencia de Etiquetas

        try:
            Sistema = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_sistema))).text
            self.assertEqual("Sistema", Sistema, "Campo visible")
            Log().info(" El campo 'Sistema' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Sistema' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Interface = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_interface))).text
            self.assertEqual("Interface", Interface, "Campo visible")
            Log().info(" El campo 'Interface' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo Interface' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Csistema = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_sistema)))
            Csistema.click()

            registro_sistema = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CFD']")))

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
            registro_interface = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CFD']")))

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
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
