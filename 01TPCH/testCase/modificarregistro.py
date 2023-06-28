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
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test']")))
            
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
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodocontrolven = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modocontrolven)))
            Cmodocontrolven.click()
            
            registro_modocontrolven = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Vencimiento del documento']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modocontrolven) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Vencimiento del documento.")
            
        except Exception as e:
            Log().error("No se dió click en la opción Vencimiento del documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodocontrolcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modocontrolcheques)))
            Cmodocontrolcheques.click()
            
            registro_modocontrolcheques = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Cheques vencidos']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modocontrolcheques) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Cheques Vencidos.")
            
        except Exception as e:
            Log().error("No se dió click en la opción Cheques vencidos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunicomediopago = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unicomediopago)))
            Cunicomediopago.click()
            Log().info(" Se dió click en el checkbox Unico Medio Pago.")
            
        except Exception as e:
            Log().error("No dió click en el checkbox Unico Medio Pago, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitude")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cgeneradoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_generadoc)))
            Cgeneradoc.click()
            Log().info(" Se dió click en el checkbox Genera Documento.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Genera Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodoccheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodoccheque)))
            Ctipodoccheque.click()
            
            registro_tipodoccheque = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM31']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_tipodoccheque) \
                .pause(0) \
                .double_click(registro_tipodoccheque) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Tipo Documento Cheque.")
            
        except Exception as e:
            Log().error("No se encontró el registro de tipo de documento cheque, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvencimientolimite = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_vencimientolimite)))
            Cvencimientolimite.click()
            
            registro_vencimientolimte = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-combobox/div/ul/li[1]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_vencimientolimte) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Vencimiento Limite.")
            
        except Exception as e:
            Log().error("No se dió click en la opción de Vencimiento Limite, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cliberarcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_liberarcredito)))
            Cliberarcredito.click()
            Log().info(" Se dió click en el checkbox liberar credito.")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox liberar credito, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y modificar

        try:
            Bcuentascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_CuentasCont)))
            Bcuentascontables.click()
            Log().info("Se hace el cambio de pestaña para continuar con la modifcación del regisro")
            
        except Exception as e:
            Log().error("No se dió click en el botón cuentas contables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro2) \
                .pause(0) \
                .double_click(Registro2) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Cuentas Contables, para proceder a modificarlo.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Cuentas Contables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica Valores Cuentas contables

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
            Log().info(" Se dió doble click en el registro de Tipo Documento.")
            
        except Exception as e:
            Log().error("No se encontró el registro de tipo de documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
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
            Log().info(" Se dió doble click en el registro de Cuentas Contables.")
            
        except Exception as e:
            Log().error("No se encontró el registro de cuenta contable, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
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
            Log().info(" Se dió doble click en el registro de Centro Costo.")
            
        except Exception as e:
            Log().error("No se encontró el registro de centro costo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardarCtasCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_acepta_ctacont)))
            GuardarCtasCont.click()
            Log().info(" Se presiona el boton 'Aceptar', para guardar la modificación del registro de Cuentas Contables.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
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
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False