from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class AgregarEMP:

    def AgregarEMP(self):
        """Abre la ventana para crear un nuevo registro"""
        self.wait = WebDriverWait(self.driver, 20)

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta
        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("EMPRESAS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoEMP)))
            Ccodigo.send_keys(Configuracion.IcodigoEMP)
            Log().info(" Ingresa el codigo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionEMP)))
            Cdescripcion.send_keys(Configuracion.IdescripcionEMP)
            Log().info(" Ingresa la descripción del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccodigoalter.send_keys(Configuracion.IcodigoalterEMP)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccodigogln.send_keys(Configuracion.IcodigoglnEMP)
            Log().info(" Ingresa el codigo GLN del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo GLN, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Crazonsocial.send_keys(Configuracion.IrazonsocialEMP)
            Log().info(" Ingresa la Razón Social del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Razón Social, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccalle.send_keys(Configuracion.IcalleEMP)
            Log().info(" Ingresa la calle del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la calle, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cesquina1.send_keys(Configuracion.Iesquina1EMP)
            Log().info(" Ingresa la esquina 1 del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cesquina2.send_keys(Configuracion.Iesquina2EMP)
            Log().info(" Ingresa la esquina 2 del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctelefono1.send_keys(Configuracion.Itelefono1EMP)
            Log().info(" Ingresa el Telefono 1 del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el telefono 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctelefono2.send_keys(Configuracion.Itelefono2EMP)
            Log().info(" Ingresa el Telefono 2 del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el telfono2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cruc.send_keys(Configuracion.IrucEMP)
            Log().info(" Ingresa el ruc del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el RUC, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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

            registro_estado = self.driver.find_element(By.XPATH, "//span[text()='DISTRITO FEDERAL']")

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

            registro_deptoprovi = self.driver.find_element(By.XPATH, "//span[text()='IZTACALCO']")

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

            registro_localidad = self.driver.find_element(By.XPATH, "//span[text()='IZTACALCO']")

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

            registro_barrio = self.driver.find_element(By.XPATH, "//span[text()='IZTACALCO']")

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
            Cobservaciones.send_keys(Configuracion.IobservacionesEMP)
            Log().info(" Ingresa las Observaciones del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las observaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cnumpuerta.send_keys(Configuracion.InropuertaEMP)
            Log().info(" Ingresa el Num de la puerta del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Num de la puerta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info("Se hace el cambio a la pestaña Series para continuar con el registro nuevo")
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

        try:
            Nuevoserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_serie)))
            Nuevoserie.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Series.")
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

        # Ingresa los datos

        try:
            Ccodigoserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoserie)))
            Ccodigoserie.send_keys(Configuracion.Icodigoserie)
            Log().info(" Ingresa el Codigo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdescripcionserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionserie)))
            Cdescripcionserie.send_keys(Configuracion.Idescripcionserie)
            Log().info(" Ingresa la Descripcion del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccodigoalterserie.send_keys(Configuracion.Icodigoalterserie)
            Log().info(" Ingresa el Codigo alternativo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Codigo Alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info("Se hace el cambio a la pestaña Configuración Vias para continuar con el registro nuevo")
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

        try:
            Nuevovias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_via)))
            Nuevovias.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Configuración Vias.")
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

            # ingresar los valores

        try:
            Ctipodocvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocvias)))
            Ctipodocvias.send_keys(Configuracion.Itipodocvias)
            Log().info(" Ingresa el Tipo Documento del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Tipo Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cviasbackkoffice.send_keys(Configuracion.Iviasback)
            Log().info(" Ingresa las Vias Backoffice del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las Vías Backoffice, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cviasmobile.send_keys(Configuracion.Iviasmobile)
            Log().info(" Ingresa las Vias Mobile del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las Vías Mobile, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdescripcionvias.send_keys(Configuracion.Idescripcionvias)
            Log().info(" Ingresa la Descripción Vias del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripción Vias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro de Configuracion Vias .")
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
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro de Serie.")
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

        # Cambio Pestaña Calendario

        try:
            Bcalendario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_calendario)))
            Bcalendario.click()
            Log().info("Se hace el cambio a la pestaña Calendario para continuar con el registro nuevo")
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

        # Ingresar Valores

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
            Cmartes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_martes)))
            Cmartes.click()
            Log().info(" Se dió click en el checkbox Martes.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Martes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cjueves = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_jueves)))
            Cjueves.click()
            Log().info(" Se dió click en el checkbox Jueves.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Jueves, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cviernes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viernes)))
            Cviernes.click()
            Log().info(" Se dió click en el checkbox Viernes.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Viernes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click en el checkbox Sabado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Contabilidad

        try:
            Bcontabilidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_contabilidad)))
            Bcontabilidad.click()
            Log().info("Se hace el cambio a la pestaña Contabilidad para continuar con el registro nuevo")
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

        # Ingresa Valores

        try:
            Cdesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_fechadesdeEMP)))
            Cdesde.clear()
            Cdesde.send_keys(Configuracion.IfechadesdeEMP)
            Log().info(" Ingresa la fecha Desde del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Fecha desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Chasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_fechahastaEMP)))
            Chasta.clear()
            Chasta.send_keys(Configuracion.IfechahastaEMP)
            Log().info(" Ingresa la fecha Hasta del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Fecha Hasta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
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
