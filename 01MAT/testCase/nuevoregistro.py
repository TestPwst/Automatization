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
            self.assertEqual("MATRICES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error(
                "La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de las etiquetas
        try:
            Codigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo))).text
            self.assertEqual("Código", Codigo, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Codigo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigousuario))).text
            self.assertEqual("Código de Usuario", Codigousuario, "Campo visible")
            Log().info(" El campo 'Código de Usuario' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código de Usuario' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoalter))).text
            self.assertEqual("Código alternativo", Codigoalter, "Campo visible")
            Log().info(" El campo 'Código alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código alternativo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcion))).text
            self.assertEqual("Descripción", Descripcion, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")
            
        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Calle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_calle))).text
            self.assertEqual("Calle", Calle, "Campo visible")
            Log().info(" El campo 'Calle' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Calle' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Telefono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_telefono1))).text
            self.assertEqual("Teléfono 1", Telefono1, "Campo visible")
            Log().info(" El campo 'Teléfono 1' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Teléfono 1' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Telefono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_telefono2))).text
            self.assertEqual("Teléfono 2", Telefono2, "Campo visible")
            Log().info(" El campo 'Teléfono 2' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Teléfono 2' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Estado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_estado))).text
            self.assertEqual("Estado", Estado, "Campo visible")
            Log().info(" El campo 'Estado' por dif. tipo cambio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Estado' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tipomatriz = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipomatriz))).text
            self.assertEqual("Tipo de matriz", Tipomatriz, "Campo visible")
            Log().info(" El campo 'Tipo de matriz' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo de matriz' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Municipio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_municipio))).text
            self.assertEqual("Municipio", Municipio, "Campo visible")
            Log().info(" El campo 'Municipio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Municipio' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Localidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_localidad))).text
            self.assertEqual("Localidad", Localidad, "Campo visible")
            Log().info(" El campo 'Localidad' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Localidad' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Barrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_barrio))).text
            self.assertEqual("Barrio", Barrio, "Campo visible")
            Log().info(" El campo 'Barrio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Barrio' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigousuario)))
            Ccodigousuario.send_keys(Configuracion.Icodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo usuario, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calle)))
            Ccalle.send_keys(Configuracion.Icalle)
            Log().info(" Ingresa la calle del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1)))
            Ctelefono1.send_keys(Configuracion.Itelefono1)
            Log().info(" Ingresa el Telefono 1 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 1, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estado)))
            Cestado.click()
            
            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='15']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_estado) \
                .pause(1) \
                .double_click(registro_estado) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipomatriz = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipomatriz)))
            Ctipomatriz.click()
            
            registro_tipomatriz = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Mtriz Principal']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_tipomatriz) \
                .pause(1) \
                .double_click(registro_tipomatriz) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Tipo Matriz, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmunicipio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_municipio)))
            Cmunicipio.click()

            registro_municipio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_municipio) \
                .pause(1) \
                .double_click(registro_municipio) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidad)))
            Clocalidad.click()

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_localidad) \
                .pause(1) \
                .double_click(registro_localidad) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrio)))
            Cbarrio.click()

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_barrio) \
                .pause(1) \
                .double_click(registro_barrio) \
                .pause(1) \
                .release()
            action.perform()
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2)))
            Ctelefono2.send_keys(Configuracion.Itelefono2)
            Log().info(" Ingresa el Telefono 2 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 2, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña compañias

        try:
            Bcompanias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_companias)))
            Bcompanias.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error(
                "No se encontró el botón compañias, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevocompanias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_compania)))
            Nuevocompanias.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro igual al anterior.")

        except Exception as e:
            Log().error(
                "No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida existencia de las etiquetas

        try:
            Codigocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigocom))).text
            self.assertEqual("Código", Codigocom, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Codigo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoaltercom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoaltercom))).text
            self.assertEqual("Código alternativo", Codigoaltercom, "Campo visible")
            Log().info(" El campo 'Código alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código alternativo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcioncom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcioncom))).text
            self.assertEqual("Descripción", Descripcioncom, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")
            
        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Callecom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_callecom))).text
            self.assertEqual("Calle", Callecom, "Campo visible")
            Log().info(" El campo 'Calle' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Calle' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Telefono1com = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_telefono1com))).text
            self.assertEqual("Teléfono 1", Telefono1com, "Campo visible")
            Log().info(" El campo 'Teléfono 1' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Teléfono 1' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Estadocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_estadocom))).text
            self.assertEqual("Estado", Estadocom, "Campo visible")
            Log().info(" El campo 'Estado' por dif. tipo cambio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Estado' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tipocompania = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipocompania))).text
            self.assertEqual("Tipo de Compañia", Tipocompania, "Campo visible")
            Log().info(" El campo 'Tipo de Compañia' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo de Compañia' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Municipiocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_municipiocom))).text
            self.assertEqual("Municipio", Municipiocom, "Campo visible")
            Log().info(" El campo 'Municipio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Municipio' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Localidadcom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_localidadcom))).text
            self.assertEqual("Localidad", Localidadcom, "Campo visible")
            Log().info(" El campo 'Localidad' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Localidad' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Barriocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_barriocom))).text
            self.assertEqual("Barrio", Barriocom, "Campo visible")
            Log().info(" El campo 'Barrio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Barrio' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Ccodigocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigocom)))
            Ccodigocom.send_keys(Configuracion.Icodigocom)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoaltercom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoaltercom)))
            Ccodigoaltercom.send_keys(Configuracion.Icodigoaltercom)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcioncom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcioncom)))
            Cdescripcioncom.send_keys(Configuracion.Idescripcioncom)
            Log().info(" Ingresa la descripción del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccallecom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_callecom)))
            Ccallecom.send_keys(Configuracion.Icallecom)
            Log().info(" Ingresa la calle del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono1com = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1com)))
            Ctelefono1com.send_keys(Configuracion.Itelefono1com)
            Log().info(" Ingresa el Telefono 1 del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 1, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestadocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estadocom)))
            Cestadocom.click()
            
            registro_estadocom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='15']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_estadocom) \
                .pause(1) \
                .double_click(registro_estadocom) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipocompania = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipocompania)))
            Ctipocompania.click()

            registro_tipocompania = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_tipocompania) \
                .pause(1) \
                .double_click(registro_tipocompania) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Tipo Compania, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmunicipiocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_municipiocom)))
            Cmunicipiocom.click()

            registro_municipiocom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='9']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_municipiocom) \
                .pause(1) \
                .double_click(registro_municipiocom) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidadcom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidadcom)))
            Clocalidadcom.click()

            registro_localidadcom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_localidadcom) \
                .pause(1) \
                .double_click(registro_localidadcom) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarriocom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barriocom)))
            Cbarriocom.click()

            registro_barriocom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_barriocom) \
                .pause(1) \
                .double_click(registro_barriocom) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono2com = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2com)))
            Ctelefono2com.send_keys(Configuracion.Itelefono2com)
            Log().info(" Ingresa el Telefono 2 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 2, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Cambio Pestaña Regional

        try:
            Bregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_regional)))
            Bregional.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error(
                "No se encontró el botón regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_regional)))
            Nuevoregional.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro igual al anterior.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de etiquetas  gruposcc

        try:
            Codigoreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoreg))).text
            self.assertEqual("Código", Codigoreg, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Codigo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalterreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoalterreg))).text
            self.assertEqual("Código alternativo", Codigoalterreg, "Campo visible")
            Log().info(" El campo 'Código alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código alternativo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcionreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcionreg))).text
            self.assertEqual("Descripción", Descripcionreg, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Callereg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_callereg))).text
            self.assertEqual("Calle", Callereg, "Campo visible")
            Log().info(" El campo 'Calle' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Calle' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Telefono1reg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_telefono1reg))).text
            self.assertEqual("Teléfono 1", Telefono1reg, "Campo visible")
            Log().info(" El campo 'Teléfono 1' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Teléfono 1' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Telefono2reg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_telefono2reg))).text
            self.assertEqual("Teléfono 2", Telefono2reg, "Campo visible")
            Log().info(" El campo 'Teléfono 2' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Teléfono 2' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Estadoreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_estadoreg))).text
            self.assertEqual("Estado", Estadoreg, "Campo visible")
            Log().info(" El campo 'Estado' por dif. tipo cambio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Estado' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tiporegional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tiporegional))).text
            self.assertEqual("Tipo de Regional", Tiporegional, "Campo visible")
            Log().info(" El campo 'Tipo de Regional' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo de Regional' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Municipioreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_municipioreg))).text
            self.assertEqual("Municipio", Municipioreg, "Campo visible")
            Log().info(" El campo 'Municipio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Municipio' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Localidadreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_localidadreg))).text
            self.assertEqual("Localidad", Localidadreg, "Campo visible")
            Log().info(" El campo 'Localidad' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Localidad' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Barrioreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_barrioreg))).text
            self.assertEqual("Barrio", Barrioreg, "Campo visible")
            Log().info(" El campo 'Barrio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Barrio' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Ingresa los datos

        try:
            Ccodigoreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoreg)))
            Ccodigoreg.send_keys(Configuracion.Icodigoreg)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalterreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalterreg)))
            Ccodigoalterreg.send_keys(Configuracion.Icodigoalterreg)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionreg)))
            Cdescripcionreg.send_keys(Configuracion.Idescripcionreg)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccallereg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_callereg)))
            Ccallereg.send_keys(Configuracion.Icallereg)
            Log().info(" Ingresa la calle del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono1reg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1reg)))
            Ctelefono1reg.send_keys(Configuracion.Itelefono1reg)
            Log().info(" Ingresa el Telefono 1 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 1, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono2reg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2reg)))
            Ctelefono2reg.send_keys(Configuracion.Itelefono2reg)
            Log().info(" Ingresa el Telefono 2 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 2, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestadoreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estadoreg)))
            Cestadoreg.click()

            registro_estadoreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='15']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_estadoreg) \
                .pause(1) \
                .double_click(registro_estadoreg) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctiporegional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tiporegional)))
            Ctiporegional.click()

            registro_tiporegional = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PACIFICO']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_tiporegional) \
                .pause(1) \
                .double_click(registro_tiporegional) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Tipo Regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmunicipioreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_municipioreg)))
            Cmunicipioreg.click()

            registro_municipioreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_municipioreg) \
                .pause(1) \
                .double_click(registro_municipioreg) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidadreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidadreg)))
            Clocalidadreg.click()

            registro_localidadreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_localidadreg) \
                .pause(1) \
                .double_click(registro_localidadreg) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrioreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrioreg)))
            Cbarrioreg.click()

            registro_barrioreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_barrioreg) \
                .pause(1) \
                .double_click(registro_barrioreg) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_regional)))
            Guardaregional.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardacompania = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_companias)))
            Guardacompania.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            time.sleep(1)

        except Exception as e:
            Log().error(
                "No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False