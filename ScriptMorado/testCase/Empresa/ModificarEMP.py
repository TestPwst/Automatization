from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class ModificarEMP:

    def ModificarEMP(self):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 20)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            time.sleep(5)

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

        Registro = self.driver.find_element(By.XPATH, "//span[text()='2021']")

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
            time.sleep(3)

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
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionEMP)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.MdescripcionEMP)
            Log().info(" Se modifica el contenido del campo Descripción ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alterEMP)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.McodigoalterEMP)
            Log().info(" Se modifica el contenido del campo Codigo Alternativo ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccodigogln = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_glnEMP)))
            Ccodigogln.clear()
            Ccodigogln.send_keys(Configuracion.McodigoglnEMP)
            Log().info(" Se modifica el contenido del campo Codigo GLN ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el codigo GLN, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Crazonsocial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_razonsocialEMP)))
            Crazonsocial.clear()
            Crazonsocial.send_keys(Configuracion.MrazonsocialEMP)
            Log().info(" Se modifica el contenido del campo Razón Social ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Razón Social, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccalle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calleEMP)))
            Ccalle.clear()
            Ccalle.send_keys(Configuracion.McalleEMP)
            Log().info(" Se modifica el contenido del campo Calle ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la calle, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1EMP)))
            Cesquina1.clear()
            Cesquina1.send_keys(Configuracion.Mesquina1EMP)
            Log().info(" Se modifica el contenido del campo Esquina 1 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2EMP)))
            Cesquina2.clear()
            Cesquina2.send_keys(Configuracion.Mesquina2EMP)
            Log().info(" Se modifica el contenido del campo Esquina 2 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctelefono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1EMP)))
            Ctelefono1.clear()
            Ctelefono1.send_keys(Configuracion.Mtelefono1EMP)
            Log().info(" Se modifica el contenido del campo telefono 1 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el telefono 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctelefono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2EMP)))
            Ctelefono2.clear()
            Ctelefono2.send_keys(Configuracion.Mtelefono2EMP)
            Log().info(" Se modifica el contenido del campo telefono 2 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el telfono2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cruc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_rucEMP)))
            Cruc.clear()
            Cruc.send_keys(Configuracion.MrucEMP)
            Log().info(" Se modifica el contenido del campo RUC ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el RUC, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estadoEMP)))
            Cestado.click()
            time.sleep(5)

            registro_estado = self.driver.find_element(By.XPATH, "//span[text()='BAJA CALIFORNIA']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estado) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Estado.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Estado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdeptoprovi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deptoproviEMP)))
            Cdeptoprovi.click()
            time.sleep(5)

            registro_deptoprovi = self.driver.find_element(By.XPATH, "//span[text()='PLAYAS DE ROSARITO']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deptoprovi) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Depto/Provincia.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Depto/Provincia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidadEMP)))
            Clocalidad.click()
            time.sleep(5)

            registro_localidad = self.driver.find_element(By.XPATH, "//span[text()='PRIMO TAPIA']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidad) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Localidad.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cbarrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrioEMP)))
            Cbarrio.click()
            time.sleep(5)

            registro_barrio = self.driver.find_element(By.XPATH, "//span[text()='PRIMO TAPIA']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrio) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Barrio.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cobservaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observacionesEMP)))
            Cobservaciones.clear()
            Cobservaciones.send_keys(Configuracion.MobservacionesEMP)
            Log().info(" Se modifica el contenido del campo Observaciones ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar las observaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_resolfiscales)))
            Cresolfiscales.click()
            Log().info(" Se dió click en el checkbox Resoluciones Fiscales.")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox Resoluciones Fiscales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cnumpuerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nropuertaEMP)))
            Cnumpuerta.clear()
            Cnumpuerta.send_keys(Configuracion.MnropuertaEMP)
            Log().info(" Se modifica el contenido del campo Num de Puerta")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el Num de la puerta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Series

        try:
            Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
            Bseries.click()
            Log().info("Se hace el cambio a la pestaña Series para continuar con la modificación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registroseries = self.driver.find_element(By.XPATH, "//span[text()='20']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroseries) \
                .pause(2) \
                .double_click(Registroseries) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Series, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Modifica Valores Cuentas contables

        try:
            Cdescripcionserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionserie)))
            Cdescripcionserie.clear()
            Cdescripcionserie.send_keys(Configuracion.Mdescripcionserie)
            Log().info(" Se modifica el contenido del campo Descripción ")
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
            Ccodigoalterserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalterserie)))
            Ccodigoalterserie.clear()
            Ccodigoalterserie.send_keys(Configuracion.Mcodigoalterserie)
            Log().info(" Se modifica el contenido del campo Codigo Alternativo ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el Codigo Alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio de pestaña Configuración Vias

        try:
            Bconfigvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_configvias)))
            Bconfigvias.click()
            Log().info("Se hace el cambio a la pestaña Configuración de Vías para continuar con la modificación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Configuracion de Vias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registrovias = self.driver.find_element(By.XPATH, "//span[text()='PM03']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrovias) \
                .pause(2) \
                .double_click(Registrovias) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Configuración Vías, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el registro de Configuración Vías, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Modificar Valores

        try:
            Ctipodocvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocvias)))
            Ctipodocvias.clear()
            Ctipodocvias.send_keys(Configuracion.Mtipodocvias)
            Log().info(" Se modifica el contenido del campo Tipo Documento ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el Tipo Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cviasbackkoffice = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viasbackoffice)))
            Cviasbackkoffice.clear()
            Cviasbackkoffice.send_keys(Configuracion.Mviasback)
            Log().info(" Se modifica el contenido del campo Vías Backoffice ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar las Vías Backoffice, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cviasmobile = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viasmobile)))
            Cviasmobile.clear()
            Cviasmobile.send_keys(Configuracion.Mviasmobile)
            Log().info(" Se modifica el contenido del campo Vías Mobile ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar las Vías Mobile, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdescripcionvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionvias)))
            Cdescripcionvias.clear()
            Cdescripcionvias.send_keys(Configuracion.Mdescripcionvias)
            Log().info(" Se modifica el contenido del campo Descripción ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Descripción Vias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Guardarvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_vias)))
            Guardarvias.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar la modificación del registro de Configuración Vías.")
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

        try:
            Guardarserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_series)))
            Guardarserie.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar la modificación del registro Series.")
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

        # Cambio de pestaña y modificar

        try:
            Bcalendario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_calendario)))
            Bcalendario.click()
            Log().info("Se hace el cambio a la pestaña Calendario para continuar con la modificación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Calendario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Modifica Valores Cuentas contables

        try:
            Clunes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_lunes)))
            Clunes.click()
            Log().info(" Se dió click en el checkbox Lunes.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Lunes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cmiercoles = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_miercoles)))
            Cmiercoles.click()
            Log().info(" Se dió click en el checkbox Miercoles.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Miercoles, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Csabado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sabado)))
            Csabado.click()
            Log().info(" Se dió click en el checkbox Sabado.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió clikc en checkbox Sabado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña para Modificar

        try:
            Bresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_resolfiscales)))
            Bresolfiscales.click()
            Log().info("Se hace el cambio a la pestaña Resoluciones Fiscales para continuar con la modificación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Resolución Fiscales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Nuevoresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_resolfiscales)))
            Nuevoresolfiscales.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Resoluciones Fiscales.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Ingreso Datos

        try:
            Cserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_serie)))
            Cserie.click()
            time.sleep(5)

            registro_serie = self.driver.find_element(By.XPATH, "//span[text()='20']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_serie) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Serie.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Serie, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cnumresol = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nroresolucion)))
            Cnumresol.send_keys(Configuracion.Inroresolfiscal)
            Log().info(" Ingresa el Num de la puerta del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Num de Resolución, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Crangoinicio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_rangoinicio)))
            Crangoinicio.send_keys(Configuracion.Irangoinicio)
            Log().info(" Ingresa el Rango Inicio del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Rango Inicio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Crangofin = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_rangofin)))
            Crangofin.send_keys(Configuracion.Irangofin)
            Log().info(" Ingresa el Rango Fin del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Rango Fin, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Guardaresolfiscal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_resolfiscales)))
            Guardaresolfiscal.click()
            Log().info(" Se da clic en el boton Guardar; se debe guardar el registro de Resolución Fiscal.")
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