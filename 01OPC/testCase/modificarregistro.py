from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from common.log import Log
from common.globalparam import img_path
import os
import time


class modificarregistro:

    def modificarregistro(self, conditions, Configuracion):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 100)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dipo click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PRU20']")))

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
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica los valores

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripción ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Propiedades por defecto

        try:
            Bpropiedades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_propiedadesxdefecto)))
            Bpropiedades.click()
            Log().info("Se hace el cambio a la pestaña Propiedades Por Defecto para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Propiedades Por Defecto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modificar Datos

        try:
            Cgrupocliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupocliente)))
            Cgrupocliente.click()

            registro_grupocliente = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GRUPOSORIANA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupocliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Grupo Cliente ")

        except Exception as e:
            Log().error("No se encontró el registro de Grupo Cliente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csubgrupocliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_subgrupocliente)))
            Csubgrupocliente.click()

            registro_subgrupocliente = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CENTROS COMERCIALES']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_subgrupocliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Subgrupo Cliente ")

        except Exception as e:
            Log().error("No se encontró el registro de Subgrupo Cliente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estado)))
            Cestado.click()

            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='BAJA CALIFORNIA SUR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estado) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Estado ")

        except Exception as e:
            Log().error("No se encontró el registro de Estado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdeptoprovi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deptoprovi)))
            Cdeptoprovi.click()

            registro_deptoprovi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='4']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deptoprovi) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Depto/Provi ")

        except Exception as e:
            Log().error("No se encontró el registro de Depto/Provi, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidad)))
            Clocalidad.click()

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CABO SAN LUCAS']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidad) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Localidad ")

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrio)))
            Cbarrio.click()

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CABO SAN LUCAS']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Barrio ")

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipocliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipocliente)))
            Ctipocliente.click()

            registro_tipocliente = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='TIENDA DE CONVENIENCIA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipocliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tipo Cliente ")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo CLiente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoexclusividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipoexclusividad)))
            Ctipoexclusividad.click()

            registro_tipoexclusividad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='G1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipoexclusividad) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tipo Exclusividad ")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Exclusividad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cprimernivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_primernivel)))
            Cprimernivel.click()

            registro_primernivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM5']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_primernivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Primer Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Primer Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csegundonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_segundonivel)))
            Csegundonivel.click()

            registro_segundonivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='51']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_segundonivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Segundo Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Segundo Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctercernivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tercernivel)))
            Ctercernivel.click()

            registro_tercernivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='28491']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tercernivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tercer Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Tercer Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccuartonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuartonivel)))
            Ccuartonivel.click()

            registro_cuartonivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='0001']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuartonivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Cuarto Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Cuarto Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(15)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False