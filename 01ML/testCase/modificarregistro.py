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

        self.wait = WebDriverWait(self.driver, 60)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[contains(text(), '( 3)')]")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[contains(text(), '( 3)')]")))
            
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

        #Modifica los valores

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripción ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantidaddias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidaddias)))
            Ccantidaddias.clear()
            Ccantidaddias.send_keys(Configuracion.Mcantidaddias)
            Log().info(" Se modifica el contenido del campo Cantidad de Días ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad de días, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantidadmaxima = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadmaxima)))
            Ccantidadmaxima.clear()
            Ccantidadmaxima.send_keys(Configuracion.Mcantidadmaxima)
            Log().info(" Se modifica el contenido del campo Cantidad Maxima ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad maxima, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clistaprecio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_listaprecio)))
            Clistaprecio.click()
            
            registro_listaprecio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Lista de Precios SCRP2.0 INTERIOR (16% IVA)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_listaprecio) \
                .pause(0) \
                .double_click(registro_listaprecio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Lista Precio.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Listaprecio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigomodelo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_codigomodelo)))
            Ccodigomodelo.click()

        except Exception as e:
            Log().error("No se encontró la ayuda de Codigo Modelo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
        
        try:
            registro_codigomodelo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Modelo Cobranza Prueba 2']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_codigomodelo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Codigo Modelo.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Codigo Modelo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            MoverPantalla = self.wait.until(conditions.visibility((By.XPATH, "//div[contains(@id, 'General_tabpage')]")))
            MoverPantalla.click()
            
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se movió la pantalla hacia abajo.")
            
        except Exception as e:
            Log().error("No se pudo mover la pantalla hacia abajo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmostraradver = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mostraradver)))
            Cmostraradver.click()
            Log().info(" Se dió click en el checkbox Mostrar Advertencias.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Mostrar Advertencias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccierreliqcargadef = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierreliqcargadefinitiva)))
            Ccierreliqcargadef.click()
            Log().info(" Se dió click en el checkbox Cierre Liquidacion Carga Definitiva.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Cierre Liquidacion Carga Definitiva, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cquitardocs = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_quitardocsliqcerrada)))
            Cquitardocs.click()
            Log().info(" Se dió click en el checkbox Quitar Documentos.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Quitar Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cinhibiroperaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_inhibiroperaciones)))
            Cinhibiroperaciones.click()
            Log().info(" Se dió click en el checkbox Inhibir Operaciones.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Inhibir Operaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccerrarliqvacias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierreliqvacias)))
            Ccerrarliqvacias.click()
            Log().info(" Se dió click en el checkbox Cerrar Liquidaciones Vacias.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Cerrar Liquidaciones Vacias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cinhibircarga = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_inhibircarga)))
            Cinhibircarga.click()
            Log().info(" Se dió click en el checkbox Inhibir Carga.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Inhibir Carga, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cignorarerrores = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ignorarerrores)))
            Cignorarerrores.click()
            Log().info(" Se dió click en el checkbox Ignorar Errores.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Ignorar Errores, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdesdefecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechadesde)))
            Cdesdefecha.click()
            
            registro_desdefecha = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/span[19]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_desdefecha) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón Hoy para seleccionar la fecha Actual.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Desde Fecha, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chastafecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechahasta)))
            Chastafecha.click()
            
            registro_hastafecha = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[7]/div[2]/div/div[2]/div/span[20]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_hastafecha) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón Hoy para seleccionar la fecha Actual.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Hasta Fecha, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvigenciaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechavigencia)))
            Cvigenciaprecios.click()
            
            registro_vigenciaprecios = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[8]/div[2]/div/div[2]/div/span[20]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_vigenciaprecios) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón Hoy para seleccionar la fecha Actual.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Fecha Vigencia Precios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccargapreciospoliticas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargaprecios)))
            Ccargapreciospoliticas.click()
            
            registro_cargaprecios = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[5]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_cargaprecios) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Carga precios y politcas.")
            
        except Exception as e:
            Log().error("No se dió click en la opción de Carga precios y politicas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hasta)))
            Chasta.click()
            
            registro_hasta = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[6]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_hasta) \
                .pause(0) \
                .click(registro_hasta) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Hasta.")
            
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en la opción de hasta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False