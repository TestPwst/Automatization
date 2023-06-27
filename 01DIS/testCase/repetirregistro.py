from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.log import Log
from common.globalparam import img_path
import os
import time


class repetirregistro:

    def repetirregistro(self, conditions, Configuracion):
        """Se refresca la pantalla para crear un nuevo registro"""

        self.wait = WebDriverWait(self.driver, 60)

        # Da clic en refrescar
        try:
            Refresca = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca.click()
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto,el tiempo de la accion o si ya existe un registro ya creado igual")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Da clic en nuevo

        try:
            Nuevo2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo)))
            Nuevo2.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro igual al anterior.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_usuario)))
            Ccodigousuario.send_keys(Configuracion.Icodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo usuario, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
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
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
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
            Log().error("No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1)))
            Ctelofono1.send_keys(Configuracion.Itelefono1)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2)))
            Ctelofono2.send_keys(Configuracion.Itelefono2)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estado)))
            Cestado.click()

            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='9']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estado) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmunicipio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_municipio)))
            Cmunicipio.click()

            registro_municipio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='5']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_municipio) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidad)))
            Clocalidad.click()

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUSTAVO A. MADERO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidad) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrio)))
            Cbarrio.click()

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUSTAVO A. MADERO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrio) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmatriz = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_matriz)))
            Cmatriz.click()

            registro_matriz = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_matriz) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Matriz, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccompania = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_compania)))
            Ccompania.click()

            registro_compania = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_compania) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Compañia, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_regional)))
            Cregional.click()

            registro_regional = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SUBDIRECCION DF']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_regional) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunidadnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_unidadnegocio)))
            Cunidadnegocio.click()

            registro_unidadnegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_unidadnegocio) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Unidad de Negocio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodistribuidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodistribuidor)))
            Ctipodistribuidor.click()

            registro_tipodistribuidor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Distribuidor MDZ']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodistribuidor) \
                .pause(0) \
                .release()
            action.perform()
            time.sleep(1)

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Distribuidor, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
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
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            AbrirError = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_error)))
            AbrirError.click()
            Log().info(" Se da clic en el boton del mensaje de registro duplicado")

        except Exception as e:
            Log().error(
                "No se dio click al botón del mensaje de registro duplicado, validar que la acción anterior haya finalizado,"
                "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            Cierra_mensaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar)))
            Cierra_mensaje.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar el mensaje de duplicidad de llave primaria")

        except Exception as e:
            Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_ventana)))
            Cierra_ventana.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana")

        except Exception as e:
            Log().error("No se encontró el botón Cerrar de la ventana., revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False