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
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro = self.driver.find_element(By.XPATH, "//span[text()='PM55']")

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
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
            Log().info(" Se modifica el contenido del campo Codigo Alternativo ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cgrupo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupo)))
            Cgrupo.click()

            registro_grupo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='P009']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Grupo.")

        except Exception as e:
            Log().error("No se encontró el registro de grupo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripción ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionimp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionimp)))
            Cdescripcionimp.clear()
            Cdescripcionimp.send_keys(Configuracion.Idescripcionimp)
            Log().info(" Se modifica el contenido del campo Descripción de Impresión ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripción de impresión, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodocumento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocumento)))
            Ctipodocumento.click()

            registro_tipodoc = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Documento de Venta']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipodoc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Documento de Venta.")

        except Exception as e:
            Log().error("No se dió click en la opción Documento de Venta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloimp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimp)))
            Cmodeloimp.click()

            registro_modeloimp = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 32149749']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloimp) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Modelo Impresión.")

        except Exception as e:
            Log().error("No se encontró el registro de Modelo Impresión, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloimpmovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimpmovil)))
            Cmodeloimpmovil.click()

            registro_modeloimpmovil = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 32149749']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloimpmovil) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Modelo Impresión Movil.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de Modelo Impresión Movil, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modeloimpmovil)))
            Moverpantalla.click()
            time.sleep(2)

            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(1) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón espacio para mover la pantalla hacía abajo ")
            time.sleep(1)

        except Exception as e:
            Log().error("No se Movio la pantalla hacia abajo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cguardarcomo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_guardarcomo)))
            Cguardarcomo.click()

            registro_guardarcomo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Seleción del Usuario']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_guardarcomo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Selección del Usuario.")

        except Exception as e:
            Log().error("No se dió click en la opción Selección del Usuario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cconarticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_conarticulos)))
            Cconarticulos.click()
            Log().info(" Se dió click en el checkbox Con Articulos.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Con Articulos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Caceptaformaspago = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aceptarformaspago)))
            Caceptaformaspago.click()
            Log().info(" Se dió click en el checkbox Acepta Formas de Pago.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Acepta Formas de Pago, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccambiarfechaemision = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cambiofechaemision)))
            Ccambiarfechaemision.click()
            Log().info(" Se dió click en el checkbox Permitir Cambiar Fecha Emisión.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Permitir Cambiar Fecha Emisión, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Canularhh = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_anularhh)))
            Canularhh.click()
            Log().info(" Se dió click en el checkbox Anular HH.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Anular HH, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Comportamiento

        try:
            Bcomportamiento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_comportamiento)))
            Bcomportamiento.click()
            Log().info("Se hace el cambio a la pestaña Comportamiento para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón comportamiento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica datos

        try:
            Cmodoafectacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoafectacion)))
            Cmodoafectacion.click()

            registro_modoafectacion = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Acredita']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoafectacion) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción No afecta stock.")

        except Exception as e:
            Log().error("No se dió click en la opción No afecta stock, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Ventas

        try:
            Bventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ventas)))
            Bventas.click()
            Log().info("Se hace el cambio a la pestaña Ventas para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodoafectacionventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoafectacionventas)))
            Cmodoafectacionventas.click()

            registro_modoafectacionventas = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[4]/ui-container/ui-row[2]/span[2]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoafectacionventas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Debita.")

        except Exception as e:
            Log().error("No se dió click en la opción Debita, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambia Pestaña CCD

        try:
            Bccd = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ccd)))
            Bccd.click()
            Log().info("Se hace el cambio a la pestaña CCD para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón CCD, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Datos

        try:
            Cmodoafectacionccd = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoafectacionccd)))
            Cmodoafectacionccd.click()

            registro_modoafectacionccd = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[5]/ui-container/ui-row[2]/span[2]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoafectacionccd) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Modo Afectación CCD.")

        except Exception as e:
            Log().error("No se dió click en la opción de Modo Afectacion CCD, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionccd = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionccd)))
            Cdescripcionccd.send_keys(Configuracion.Idescripcionccd)
            Log().info(" Ingresa la descripción del registro que esta siendo modificado ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cverificalimites = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_verificalim)))
            Cverificalimites.click()
            Log().info(" Se dió click en el checkbox Verifica Limites.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Verifica limites de Credito, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccampoaux = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aux)))
            Ccampoaux.click()

            registro_modoafectacionccd = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Reducir Crédito Disponible']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoafectacionccd) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Ampliar Crédito Disponible.")

        except Exception as e:
            Log().error("No se dió click en la opción Ampliar Crédito Disponible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Liquidaciones

        try:
            Bliquidaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_liquidaciones)))
            Bliquidaciones.click()
            Log().info("Se hace el cambio a la pestaña Liquidaciones para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Liquidaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Cafectaliquidacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_afectaliquidacion)))
            Cafectaliquidacion.click()
            Log().info(" Se dió click en el checkbox Afecta Liquidación.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Afecta Liquidacion de dinero, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Reg. Visita

        try:
            Bregvisita = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_regvisita)))
            Bregvisita.click()
            Log().info("Se hace el cambio a la pestaña Reg. Vidita para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Reg. Visita, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Cheques

        try:
            Bcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cheques)))
            Bcheques.click()
            Log().info("Se hace el cambio a la pestaña Cheques para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Cheques, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Generar Desde

        try:
            Bgenerardesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_generardesde)))
            Bgenerardesde.click()
            Log().info("Se hace el cambio a la pestaña Generar Desde para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Generar Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False