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
            Log().error("No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro = self.driver.find_element(By.XPATH, "//span[text()='1']")

        try:
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
            Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
            Log().info(" Se modifica el contenido del campo Codigo Alternativo")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el codigo alternativo revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_usuario)))
            Ccodigousuario.clear()
            Ccodigousuario.send_keys(Configuracion.Mcodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo usuario, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripcion")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
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
            Log().error("No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1)))
            Ctelofono1.clear()
            Ctelofono1.send_keys(Configuracion.Mtelefono1)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2)))
            Ctelofono2.clear()
            Ctelofono2.send_keys(Configuracion.Mtelefono2)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estado)))
            Cestado.click()

            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='11']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estado) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmunicipio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_municipio)))
            Cmunicipio.click()

            registro_municipio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='11']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_municipio) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidad)))
            Clocalidad.click()

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidad) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrio)))
            Cbarrio.click()

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrio) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
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
            time.sleep(2)
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
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_regional)))
            Cregional.click()

            registro_regional = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SUBDIRECCION PACIFICO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_regional) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunidadnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_unidadnegocio)))
            Cunidadnegocio.click()

            registro_unidadnegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM02']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_unidadnegocio) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Unidad de Negocio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodistribuidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodistribuidor)))
            Ctipodistribuidor.click()

            registro_tipodistribuidor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Prueba Tipo Distribuidor 2']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodistribuidor) \
                .pause(0) \
                .release()
            action.perform()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Distribuidor, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña para modificar

        try:
            Bagencias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_agencias)))
            Bagencias.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se encontró el botón agencias, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registroagencias = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Prueba automatizada del campo descripción Agencias']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroagencias) \
                .pause(0) \
                .double_click(Registroagencias) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modificar Valores

        try:
            Ccodigoalterage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alterage)))
            Ccodigoalterage.clear()
            Ccodigoalterage.send_keys(Configuracion.Mcodigoalterage)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionage)))
            Cdescripcionage.clear()
            Cdescripcionage.send_keys(Configuracion.Mdescripcionage)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalleage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calleage)))
            Ccalleage.clear()
            Ccalleage.send_keys(Configuracion.Mcalleage)
            Log().info(" Ingresa la calle del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono1age = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1age)))
            Ctelofono1age.clear()
            Ctelofono1age.send_keys(Configuracion.Mtelefono1age)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono2age = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2age)))
            Ctelofono2age.clear()
            Ctelofono2age.send_keys(Configuracion.Mtelefono2age)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestadoage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estadoage)))
            Cestadoage.click()

            registro_estadoage = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUANAJUATO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estadoage) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdeptoprovi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deptoprovi)))
            Cdeptoprovi.click()

            registro_deptoprovi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deptoprovi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidadage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidadage)))
            Clocalidadage.click()

            registro_localidadage = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidadage) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrioage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrioage)))
            Cbarrioage.click()

            registro_barrioage = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrioage) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmatrizage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_matrizage)))
            Cmatrizage.click()

            registro_matrizage = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_matrizage) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Matriz, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccompaniaage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_companiaage)))
            Ccompaniaage.click()

            registro_companiaage = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_companiaage) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Compañia, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cregionalage = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_regionalage)))
            Cregionalage.click()

            registro_regionalage = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SUBDIRECCION PACIFICO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_regionalage) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoagencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipoagencia)))
            Ctipoagencia.click()

            registro_tipoagencia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='LO F1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipoagencia) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Distribuidor, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y modificar

        try:
            Boficinas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_oficinas)))
            Boficinas.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se encontró el botón oficinas, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registrooficinas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Prueba automatizada del campo descripción Oficina']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrooficinas) \
                .pause(0) \
                .double_click(Registrooficinas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Ccodigoalterofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alterofi)))
            Ccodigoalterofi.clear()
            Ccodigoalterofi.send_keys(Configuracion.Mcodigoalterofi)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionofi)))
            Cdescripcionofi.clear()
            Cdescripcionofi.send_keys(Configuracion.Mdescripcionofi)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalleofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calleofi)))
            Ccalleofi.clear()
            Ccalleofi.send_keys(Configuracion.Mcalleofi)
            Log().info(" Ingresa la calle del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la calle, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono1ofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1ofi)))
            Ctelofono1ofi.clear()
            Ctelofono1ofi.send_keys(Configuracion.Mtelefono1ofi)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelofono2ofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2ofi)))
            Ctelofono2ofi.clear()
            Ctelofono2ofi.send_keys(Configuracion.Mtelefono2ofi)
            Log().info(" Ingresa el primer número del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el primer número, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestadoofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estadoofi)))
            Cestadoofi.click()

            registro_estadoofi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GUANAJUATO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estadoofi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de estado, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdeptoproviofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deptoprovioofi)))
            Cdeptoproviofi.click()

            registro_deptoprovi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deptoprovi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de municipio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidadofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidadofi)))
            Clocalidadofi.click()

            registro_localidadofi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidadofi) \
                .pause(2) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrioofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrioofi)))
            Cbarrioofi.click()

            registro_barrioofi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CORTAZAR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrioofi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmatrizofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_matrizofi)))
            Cmatrizofi.click()

            registro_matrizofi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_matrizofi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Matriz, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccompaniaofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_companiaofi)))
            Ccompaniaofi.click()

            registro_companiaofi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS CIGATAM']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_companiaofi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Compañia, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cregionalofi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_regionalofi)))
            Cregionalofi.click()
            time.sleep(5)

            registro_regionalofi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SUBDIRECCION SUR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_regionalofi) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipooficina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipooficina)))
            Ctipooficina.click()

            registro_tipoaoficina = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='sin clasificar']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipoaoficina) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Distribuidor, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaoficinas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_oficina)))
            Guardaoficinas.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

         # Cambio de pestaña y modificar

        try:
            Bcuentascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_CuentasCont)))
            Bcuentascontables.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se encontró el botón cuentas contables, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registrocuentas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrocuentas) \
                .pause(0) \
                .double_click(Registrocuentas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

         # Modifica Valores Cuentas contables

        try:
            CTipoDoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodoc)))
            CTipoDoc.click()

            registro_tipodoc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM17']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_tipodoc) \
                .pause(0) \
                .double_click(registro_tipodoc) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de tipo de documento, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CCtaCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_ctacont)))
            CCtaCont.click()

            registro_ctacont = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba cambio']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctacont) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de cuenta contable, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CCentroCosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_centrocosto)))
            CCentroCosto.click()

            registro_ctrcosto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba cambio']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctrcosto) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de centro costo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardarCtasCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_acepta_ctacont)))
            GuardarCtasCont.click()
            Log().info(" Se presiona el boton 'Aceptar', para guardar el registro.")

        except Exception as e:
            Log().error("No se encontró el botón Aceptar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaagencias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_agencias)))
            Guardaagencias.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            time.sleep(2)
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
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False