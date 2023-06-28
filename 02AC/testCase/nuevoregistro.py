from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
            self.assertEqual("AUTORIZACIONES DE CRÉDITO : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de las etiquetas
        try:
            Empresa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_empresa))).text
            self.assertEqual("Empresa", Empresa, "Campo visible")
            Log().info(" El campo 'Empresa' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Empresa' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Moneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_moneda))).text
            self.assertEqual("Moneda", Moneda, "Campo visible")
            Log().info(" El campo 'Moneda' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Moneda' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Modo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modo))).text
            self.assertEqual("Modo", Modo, "Campo visible")
            Log().info(" El campo 'Modo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Modo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cantidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cantidad))).text
            self.assertEqual("Cantidad", Cantidad, "Campo visible")
            Log().info(" El campo 'Cantidad' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cantidad' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Contrasena = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_contrasena))).text
            self.assertEqual("Contraseña", Contrasena, "Campo visible")
            Log().info(" El campo 'Contraseña' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Contraseña' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")

            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Se realiza el ingreso de datos en los campos.

        try:
            CEmpresa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_empresa)))
            CEmpresa.click()

            registro_empresa = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='58']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_empresa) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el regitro de Empresa.")

        except Exception as e:
            Log().error("No se encontró el registro de Empresa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CMoneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_moneda)))
            CMoneda.click()

            registro_moneda = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_moneda) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el regitro de Moneda.")

        except Exception as e:
            Log().error("No se encontró el registro de Moneda, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CModo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modo)))
            CModo.click()

            registro_modo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Limite personalizado (evento Documento_OnValidarAutorizacionCreditoGeneral)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Limite personalizado (evento Documento_OnValidarAutorizacionCreditoGeneral).")

        except Exception as e:
            Log().error("No se encontró la opción de Limite personalizado (evento Documento_OnValidarAutorizacionCreditoGeneral), validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CUsuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_usuario)))
            CUsuario.click()

            registro_usuario = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='mabcecgut']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_usuario) \
                .double_click(registro_usuario) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el regitro de Usuario.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de Usuario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CAutoriza = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidad)))
            CAutoriza.send_keys(Configuracion.Icantidad)
            Log().info(" Ingresa de autorización del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la autorización, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CContrasena = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_contrasena)))
            CContrasena.send_keys(Configuracion.Icontrasena)
            Log().info(" Ingresa la contraseña del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la contrasena, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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