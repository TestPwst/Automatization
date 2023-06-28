from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class AgregarOBD:

    def AgregarOBD(self):
        """Abre la ventana para crear un nuevo registro"""
        self.wait = WebDriverWait(self.driver, 20)

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta
        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("OBJETIVOS DIARIOS POR VENDEDOR : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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

        #Se realiza el ingreso de datos en los campos.

        try:
            Cvendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_vendedorOBD)))
            Cvendedor.click()
            time.sleep(5)

            registro_vendedor = self.driver.find_element(By.XPATH, "//span[text()='ZI01']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_vendedor) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el regitro de Vendedor.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Vendedor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cfecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechaOBD)))
            Cfecha.click()
            time.sleep(5)

            registro_fecha = self.driver.find_element(By.XPATH, "//button[text()='Hoy']")

            action = ActionChains(self.driver)
            action \
                .click(registro_fecha) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en el Botón hoy para seleccionar la fecha actual.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Hoy para seleccionar la actual, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cefectividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_efectividad)))
            Cefectividad.send_keys(Configuracion.Iefectividad)
            Log().info(" Ingresa la efectividad del nuevo registro ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la efectividad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio de pestaña y agregar nuevo

        try:
            Bgrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_gruposOBD)))
            Bgrupos.click()
            Log().info("Se hace el cambio a la pestaña Grupos para continuar con el registro nuevo")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón grupos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Nuevogrupo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_grupoOBD)))
            Nuevogrupo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Grupos.")
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

        #ingreso de los valores en los campos

        try:
            Cgrupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupopoliticaOBD)))
            Cgrupopolitica.click()
            time.sleep(5)

            registro_grupopolitica = self.driver.find_element(By.XPATH, "//span[text()='CPM01']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupopolitica) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el regitro de Grupos Politica.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Grupo Politica, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctipoobjetivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipoobjetivo)))
            Ctipoobjetivo.click()
            time.sleep(3)

            registro_tipoobjetivo = self.driver.find_element(By.XPATH, "//li[text()='Volumen Mensual']")

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoobjetivo) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Volumen Mensual.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Volumen Mensaual, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctipounidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipounidad)))
            Ctipounidad.click()
            time.sleep(3)

            registro_tipounidad = self.driver.find_element(By.XPATH, "//li[text()='Unidad']")

            action = ActionChains(self.driver)
            action \
                .click(registro_tipounidad) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Unidad.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción unidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cobjetivocantidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_objetivocantidad)))
            Cobjetivocantidad.send_keys(Configuracion.Iobjetivocantidad)
            Log().info(" Ingresa el Objetivo Cantidad del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Objetivo Cantidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Guardagrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_grupos)))
            Guardagrupos.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Grupos.")
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
