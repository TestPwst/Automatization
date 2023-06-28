from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class modificarML:

    def modificarML(self):
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

        Registro = self.driver.find_element(By.XPATH, "//span[contains(text(), '( 3)')]")

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
            time.sleep(5)

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
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionML)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.MdescripcionML)
            Log().info(" Se modifica el contenido del campo Descripción ")
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
            Ccantidaddias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidaddiasML)))
            Ccantidaddias.clear()
            Ccantidaddias.send_keys(Configuracion.McantidaddiasML)
            Log().info(" Se modifica el contenido del campo Cantidad de Días ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad de días, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccantidadmaxima = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadmaximaML)))
            Ccantidadmaxima.clear()
            Ccantidadmaxima.send_keys(Configuracion.McantidadmaximaML)
            Log().info(" Se modifica el contenido del campo Cantidad Maxima ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad maxima, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Clistaprecio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_listaprecioML)))
            Clistaprecio.click()
            time.sleep(5)

            registro_listaprecio = self.driver.find_element(By.XPATH, "//span[text()='Lista de Precios SCRP2.0 INTERIOR (16% IVA)']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_listaprecio) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Lista Precio.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Listaprecio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccodigomodelo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_codigomodelo)))
            Ccodigomodelo.click()
            time.sleep(5)

            registro_codigomodelo = self.driver.find_element(By.XPATH, "//span[text()='Modelo Cobranza Prueba 2']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_codigomodelo) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Codigo Modelo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Codigo Modelo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            MoverPantalla = self.wait.until(conditions.visibility((By.XPATH, "//div[contains(@id, 'General_tabpage')]")))
            MoverPantalla.click()
            time.sleep(5)

            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se movió la pantalla hacia abajo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo mover la pantalla hacia abajo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cmostraradver = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mostraradver)))
            Cmostraradver.click()
            Log().info(" Se dió click en el checkbox Mostrar Advertencias.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Mostrar Advertencias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccierreliqcargadef = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierreliqcargadefinitiva)))
            Ccierreliqcargadef.click()
            Log().info(" Se dió click en el checkbox Cierre Liquidacion Carga Definitiva.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Cierre Liquidacion Carga Definitiva, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cquitardocs = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_quitardocsliqcerrada)))
            Cquitardocs.click()
            Log().info(" Se dió click en el checkbox Quitar Documentos.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Quitar Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cinhibiroperaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_inhibiroperaciones)))
            Cinhibiroperaciones.click()
            Log().info(" Se dió click en el checkbox Inhibir Operaciones.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Inhibir Operaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccerrarliqvacias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierreliqvacias)))
            Ccerrarliqvacias.click()
            Log().info(" Se dió click en el checkbox Cerrar Liquidaciones Vacias.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Cerrar Liquidaciones Vacias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cinhibircarga = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_inhibircarga)))
            Cinhibircarga.click()
            Log().info(" Se dió click en el checkbox Inhibir Carga.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Inhibir Carga, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cignorarerrores = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ignorarerrores)))
            Cignorarerrores.click()
            Log().info(" Se dió click en el checkbox Ignorar Errores.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Ignorar Errores, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccargapreciospoliticas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargaprecios)))
            Ccargapreciospoliticas.click()
            time.sleep(5)

            registro_cargaprecios = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[5]/ui-combobox/div/ul/li[2]")

            action = ActionChains(self.driver)
            action \
                .click(registro_cargaprecios) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Carga precios y politcas.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción de Carga precios y politicas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Chasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hasta)))
            Chasta.click()
            time.sleep(5)

            registro_hasta = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[6]/ui-combobox/div/ul/li[2]")

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_hasta) \
                .pause(4) \
                .click(registro_hasta) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Hasta.")
            time.sleep(3)

            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en la opción de hasta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
