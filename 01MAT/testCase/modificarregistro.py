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
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
            time.sleep(2)
            
        except Exception as e:
            Log().error(
                "No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))

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
            Log().error(
                "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigousuario)))
            Ccodigousuario.clear()
            Ccodigousuario.send_keys(Configuracion.Mcodigousuario)
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
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
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
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
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
            Ccalle.clear()
            Ccalle.send_keys(Configuracion.Mcalle)
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
            Ctelefono1.clear()
            Ctelefono1.send_keys(Configuracion.Mtelefono1)
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

            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUANAJUATO']")))

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

            registro_municipio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CELAYA']")))

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

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CELAYA']")))

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

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CELAYA']")))

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
            Ctelefono2.clear()
            Ctelefono2.send_keys(Configuracion.Mtelefono2)
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
            Registrocompanias = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigocom+"']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrocompanias) \
                .pause(1) \
                .double_click(Registrocompanias) \
                .pause(1) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Ccodigoaltercom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoaltercom)))
            Ccodigoaltercom.clear()
            Ccodigoaltercom.send_keys(Configuracion.Mcodigoaltercom)
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
            Cdescripcioncom.clear()
            Cdescripcioncom.send_keys(Configuracion.Mdescripcioncom)
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
            Ccallecom.clear()
            Ccallecom.send_keys(Configuracion.Mcallecom)
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
            Ctelefono1com.clear()
            Ctelefono1com.send_keys(Configuracion.Mtelefono1com)
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
            
            registro_estadocom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUANAJUATO']")))

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

            registro_municipiocom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ALLENDE']")))

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

            registro_localidadcom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SANTA CRUZ']")))

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

            registro_barriocom = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SANTA CRUZ']")))

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
            Ctelefono2com.clear()
            Ctelefono2com.send_keys(Configuracion.Mtelefono2com)
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
            Registroregional = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigoreg+"']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroregional) \
                .pause(1) \
                .double_click(Registroregional) \
                .pause(1) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # modifica Valores

        try:
            Ccodigoalterreg = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalterreg)))
            Ccodigoalterreg.clear()
            Ccodigoalterreg.send_keys(Configuracion.Mcodigoalterreg)
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
            Cdescripcionreg.clear()
            Cdescripcionreg.send_keys(Configuracion.Mdescripcionreg)
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
            Ccallereg.clear()
            Ccallereg.send_keys(Configuracion.Mcallereg)
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
            Ctelefono1reg.clear()
            Ctelefono1reg.send_keys(Configuracion.Mtelefono1reg)
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
            Ctelefono2reg.clear()
            Ctelefono2reg.send_keys(Configuracion.Mtelefono2reg)
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
            
            registro_estadoreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUANAJUATO']")))

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

            registro_tiporegional = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='NORTE']")))

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

            registro_municipioreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CELAYA']")))

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

            registro_localidadreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CELAYA']")))

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

            registro_barrioreg = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CELAYA']")))

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
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            
        except Exception as e:
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False