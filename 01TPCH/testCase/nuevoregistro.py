from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
            self.assertEqual("TIPOS DE CHEQUES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de las etiquetas
        try:
            Codigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo))).text
            self.assertEqual("Código", Codigo, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Codigo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcion))).text
            self.assertEqual("Descripción", Descripcion, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Descripción' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Modocontrolven = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modocontrolven))).text
            self.assertEqual("Modo control vencimiento", Modocontrolven, "Campo visible")
            Log().info(" El campo 'Modo control vencimiento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Modo control vencimiento' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Modocontrolcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modocontrolcheques))).text
            self.assertEqual("Modo control cheques adeudados", Modocontrolcheques, "Campo visible")
            Log().info(" El campo 'Modo control cheques adeudados' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Modo control cheques adeudados' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Unicomediopago = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_unicomediopago))).text
            self.assertEqual("Único medio de pago en el documento", Unicomediopago, "Campo visible")
            Log().info(" El campo 'Único medio de pago en el documento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Único medio de pago en el documento' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Generadoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_generadoc))).text
            self.assertEqual("Genera documento", Generadoc, "Campo visible")
            Log().info(" El campo 'Genera documento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Genera documento' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tipodoccheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodoccheque))).text
            self.assertEqual("Tipo documento cheque", Tipodoccheque, "Campo visible")
            Log().info(" El campo 'Tipo documento cheque' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo documento cheque' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Vencimientolimite = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_vencimientolimite))).text
            self.assertEqual("Verificar vencimiento por límite de crédito", Vencimientolimite, "Campo visible")
            Log().info(" El campo 'Verificar vencimiento por límite de crédito' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Verificar vencimiento por límite de crédito' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Liberarcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_liberarcredito))).text
            self.assertEqual("Liberar crédito", Liberarcredito, "Campo visible")
            Log().info(" El campo 'Liberar crédito' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Liberar crédito' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodocontrolven = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modocontrolven)))
            Cmodocontrolven.click()
            
            registro_modocontrolven = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Vencimiento al día']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modocontrolven) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Vencimiento del día.")
            
        except Exception as e:
            Log().error("No se dió click en la opción Vencimiento del día, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodocontrolcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modocontrolcheques)))
            Cmodocontrolcheques.click()
            
            registro_modocontrolcheques = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Todos los cheques']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modocontrolcheques) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Todos los Cheques.")
            
        except Exception as e:
            Log().error("No se dió click en la opción Todos los Cheques, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click en el checkbox Unico Medio Pago, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            
            registro_tipodoccheque = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM33']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_tipodoccheque) \
                .pause(0) \
                .double_click(registro_tipodoccheque) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Tipo de Documento Cheque.")
            
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
            
            registro_vencimientolimte = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Verificar según fecha del documento']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_vencimientolimte) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Verificar según fecha del documento.")
            
        except Exception as e:
            Log().error("No se dió click en la opción Verificar según fecha del documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cliberarcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_liberarcredito)))
            Cliberarcredito.click()
            Log().info(" Se dió click en el checkbox Liberar Credito.")
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

            # Cambio de pestaña y agregar nuevo

        try:
            Bcuentascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_CuentasCont)))
            Bcuentascontables.click()
            Log().info("Se hace el cambio a la pestaña Cuentas Contables para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se dió click en el botón cuentas contables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevo2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_CuentasCont)))
            Nuevo2.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Cuentas Contables.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida la existencia de las etiquetas

        try:
            TipoDoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodoc))).text
            self.assertEqual("Tipo Documento", TipoDoc, "Campo visible")
            Log().info(" El campo 'Tipo Documento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo Documento' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CuentaCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cuentacont))).text
            self.assertEqual("Cuenta Contable", CuentaCont, "Campo visible")
            Log().info(" El campo 'Cuenta Contable' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cuenta Contable' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CentroCosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_centrocosto))).text
            self.assertEqual("Centro Costo", CentroCosto, "Campo visible")
            Log().info(" El campo 'Centro Costo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Centro Costo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # ingresar los valores

        try:
            CTipoDoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodoc)))
            CTipoDoc.click()
            
            registro_tipodoc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM93']")))

            action = ActionChains(self.driver)
            action \
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
            
            registro_ctacont = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))

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
            
            registro_ctrcosto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))

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
            Log().info(" Se presiona el boton 'Aceptar', para guardar el registro de Cuentas Contables.")
            
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
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False