from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
            self.assertEqual("OBJETIVOS DIARIOS POR VENDEDOR : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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
            Vendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_vendedor))).text
            self.assertEqual("Vendedor", Vendedor, "Campo visible")
            Log().info(" El campo 'Vendedor' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Vendedor' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Fecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_fecha))).text
            self.assertEqual("Fecha", Fecha, "Campo visible")
            Log().info(" El campo 'Fecha' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo Fecha' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Efectividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_efectividad))).text
            self.assertEqual("Efectividad %", Efectividad, "Campo visible")
            Log().info(" El campo 'Efectividad %' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Efectividad %' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Se realiza el ingreso de datos en los campos.

        try:
            Cvendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_vendedor)))
            Cvendedor.click()

            registro_vendedor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ZI01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_vendedor) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Vendedor.")

        except Exception as e:
            Log().error("No se encontró el registro de Vendedor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # try:
        #     Cfecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fecha)))
        #     Cfecha.click()

        #     registro_fecha = self.wait.until(conditions.visibility((By.XPATH, "//button[text()='Hoy']")))

        #     action = ActionChains(self.driver)
        #     action \
        #         .click(registro_fecha) \
        #         .pause(0) \
        #         .release()
        #     action.perform()
        #     Log().info(" Se dió click en el botón hoy para seleccionar la fecha actual.")

        # except Exception as e:
        #     Log().error("No se dió click en el botón Hoy para seleccionar la fecha actual, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.driver.get_screenshot_as_file(img_name)
        #     return False

        try:
            Cefectividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_efectividad)))
            Cefectividad.send_keys(Configuracion.Iefectividad)
            Log().info(" Ingresa la efectividad del nuevo registro ")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la efectividad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y agregar nuevo

        try:
            Bgrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_grupos)))
            Bgrupos.click()
            Log().info("Se hace el cambio a la pestaña Grupos para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón grupos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevogrupo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_grupo)))
            Nuevogrupo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Grupos.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida existencia de las etiquetas

        try:
            Grupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_grupopolitica))).text
            self.assertEqual("Grupo Política", Grupopolitica, "Campo visible")
            Log().info(" El campo 'Grupo Política' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Grupo Política' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            TipoObjetivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipoobjetivo))).text
            self.assertEqual("Tipo Objetivo", TipoObjetivo, "Campo visible")
            Log().info(" El campo 'Tipo Objetivo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo Objetivo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Objetivodistribucion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_objetivodistribucion))).text
            self.assertEqual("Objetivo Distribución", Objetivodistribucion, "Campo visible")
            Log().info(" El campo 'Objetivo Distribución' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Objetivo Distribución' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #ingreso de los valores en los campos

        try:
            Cgrupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupopolitica)))
            Cgrupopolitica.click()

            registro_grupopolitica = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CPM01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupopolitica) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Grupo Politica.")

        except Exception as e:
            Log().error("No se encontró el registro de Grupo Politica, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoobjetivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipoobjetivo)))
            Ctipoobjetivo.click()

            registro_tipoobjetivo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Distribución Diaria']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoobjetivo) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se dió click en la opción Distribución Diaria.")

        except Exception as e:
            Log().error("No se dió click en la opción Distribución Diaria, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cobjetivodistribucion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_objetivodistribucion)))
            time.sleep(1)
            Cobjetivodistribucion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_objetivodistribucion)))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Cobjetivodistribucion) \
                .pause(0) \
                .release()
            action.perform()
            
            Cobjetivodistribucion.send_keys(Configuracion.Iobjetivodistribucion)
            
            Log().info(" Ingresa el Objetivo Distribucion  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el objetivo distribucion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardagrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_grupos)))
            Guardagrupos.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Grupos.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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