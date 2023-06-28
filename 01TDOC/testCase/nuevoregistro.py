from selenium.webdriver import ActionChains, Keys
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
            self.assertEqual("TIPOS DE DOCUMENTOS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cgrupo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupo)))
            Cgrupo.click()

            registro_grupo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='P001']")))

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
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionimp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionimp)))
            Cdescripcionimp.send_keys(Configuracion.Idescripcionimp)
            Log().info(" Ingresa la descripción de impresión del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripción de impresión, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipovalorizacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipovalorizacion)))
            Ctipovalorizacion.click()

            registro_tipoval = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Por artículos']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoval) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Por Articulos.")

        except Exception as e:
            Log().error("No se dió click en la opción por articulos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuesto)))
            Cimpuesto.click()

            registro_impuesto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='106']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuesto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Impuesto.")

        except Exception as e:
            Log().error("No se encontró el registro de Impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclavecorr = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clavecorr)))
            Cclavecorr.send_keys(Configuracion.Iclavecorr)
            Log().info(" Ingresa la clave correlativa del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la clave correlativa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info(" Se dió doble click en el registro de Tipo Documento.")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo de Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloimp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimp)))
            Cmodeloimp.click()

            registro_modeloimp = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 37209284']")))

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

            registro_modeloimpmovil = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 37209284']")))

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
            Log().info(" Se dió click en la tecla espacio para mover la pantalla hacia abajo.")
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
            Cemitircuando = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_emitircuando)))
            Cemitircuando.click()

            registro_emitircuando = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Siempre']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_emitircuando) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Siempre.")

        except Exception as e:
            Log().error("No se dipo click en la opción siempre, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cguardarcomo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_guardarcomo)))
            Cguardarcomo.click()

            registro_guardarcomo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Emitir Siempre']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_guardarcomo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Emitir Siempre.")

        except Exception as e:
            Log().error("No se dió click en la opción Emitir Siempre, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click en el chekcbox Con Articulos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Caceptaformaspago = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aceptarformaspago)))
            Caceptaformaspago.click()
            Log().info(" Se dió click en la opción Acepta Formas de Pago.")

        except Exception as e:
            Log().error("No se dió clcik en el checkbox Acepta Formas de Pago, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Canularhh = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_anularhh)))
            Canularhh.click()
            Log().info(" Se dió click en la opción Anular HH.")

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
            Log().info("Se hace el cambio a la pestaña Comportamiento para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón comportamiento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

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
            Log().info(" Se dió click en la opción Acredita.")

        except Exception as e:
            Log().error("No se dió click en la opción Acredita, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Crubro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_rubro)))
            Crubro.click()

            registro_rubro = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div[3]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_rubro) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Rubro.")

        except Exception as e:
            Log().error("No se encontró el registro de Rubro, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodogeneracionlote = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modogeneracionlotes)))
            Cmodogeneracionlote.click()

            registro_generacionlotes = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Especificar Lote (Manual)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_generacionlotes) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Especificar Lote (Manual).")

        except Exception as e:
            Log().error("No se dió click en la opción Especificar Lote (Manual), validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccontrolstockenlinea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_controlstockenlinea)))
            Ccontrolstockenlinea.click()
            Log().info(" Se dió click en el checkbox Control Stock en Linea.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Control de Stock en Linea, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodostockenlinea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modostockenlinea)))
            Cmodostockenlinea.click()

            registro_modostockenlinea = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Controlar desde depósito (Por lotes)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modostockenlinea) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Controlar desde depósito (Por lotes).")

        except Exception as e:
            Log().error("No se dió click en la opción Controlar desde depósito (Por lotes), validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se agrega el tipo de Rubro permitido

        try:
            Tiposrubropermitidos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tiposrubropermitidos))).text
            self.assertEqual("Tipos de rubro permitidos", Tiposrubropermitidos, "Campo visible")
            Log().info(" El campo 'Tipos de rubro permitidos' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipos de rubro permitidos' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevotiposrubroperm = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_tiposrubro)))
            Nuevotiposrubroperm.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de tipos Rubro permitidos.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Datos

        try:
            Ctiposrubro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tiposrubro)))
            Ctiposrubro.click()

            registro_tiposrubro = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div[2]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tiposrubro) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Tipo Documento.")

        except Exception as e:
            Log().error("No se encontró el registro de Tipos Rubro, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardartiposrubro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_tiposrubro)))
            Guardartiposrubro.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro de Tipos Rubro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Ventas

        try:
            Bventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ventas)))
            Bventas.click()
            Log().info("Se hace el cambio a la pestaña Ventas para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

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
            Log().info(" Se dió click en la opción de Modo Afectacion Ventas.")

        except Exception as e:
            Log().error("No se dió clikc en la opción de Modo Afectación Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cafectarimportes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_afectarimportes)))
            Cafectarimportes.click()
            Log().info(" Se dió click en el checkbox Afectar Importes.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Afectar Importes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cafectarunidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_afectarunidades)))
            Cafectarunidades.click()
            Log().info(" Se dió click en el checkbox Afectar Unidades.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Afectar Unidades, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalculodescrecar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calculodescrecar)))
            Ccalculodescrecar.click()

            registro_descrecar = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Aplicar porcentaje en cascada']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_descrecar) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Aplicar Porcentaje en Cascada.")

        except Exception as e:
            Log().error("No se dió click en la opción Apicar Porcentaje en Cascada, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodoaplipoliticas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoaplipoliticas)))
            Cmodoaplipoliticas.click()

            registro_aplipoliticas = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Aplicar todas']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_aplipoliticas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Aplicar Todas.")

        except Exception as e:
            Log().error("No se dió click en la opción Aplicar Todas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña liquidaciones

        try:
            Bliquidaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_liquidaciones)))
            Bliquidaciones.click()
            Log().info("Se hace el cambio a la pestaña Liquidaciones para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Liquidaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los Valores

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

        try:
            Cmodoafectacionliq = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoafectacionliq)))
            Cmodoafectacionliq.click()

            registro_modoafectacionliq = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[3]/span[2]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoafectacionliq) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Modo Afectación Liquidaciones.")

        except Exception as e:
            Log().error("No se click en la opción de Modo Afectacion Liquidciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvisibleagregarnuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_visibleagregarnuevo)))
            Cvisibleagregarnuevo.click()
            Log().info(" Se dió click en el checkbox Ignorar Ajuste.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Agregar Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cafectaentrega = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_afectaentrega)))
            Cafectaentrega.click()
            Log().info(" Se dió click en el checkbox Afecta Entrega.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Afecta Entrega, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Reg. Visita

        try:
            Bregvisita = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_regvisita)))
            Bregvisita.click()
            Log().info("Se hace el cambio a la pestaña Reg. Visita para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Reg. Visita, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresar los datos

        try:
            Cgenerarvisita = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_genregistrovisita)))
            Cgenerarvisita.click()
            Log().info("Se hace click en el checkbox Generar Registro de Visita")

        except Exception as e:
            Log().error("No se dió click en el checkbox Generar Registro de Visita, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Crubrovisita = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_rubroregvisita)))
            Crubrovisita.click()

            registro_rubrovisita = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Visita con venta']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_rubrovisita) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro Rubro Visita.")

        except Exception as e:
            Log().error("No se encontró el registro de Rubro Visita, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Cheques

        try:
            Bcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cheques)))
            Bcheques.click()
            Log().info("Se hace el cambio a la pestaña Cheques para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Cheques, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevotiposcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_tipocheque)))
            Nuevotiposcheques.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Tipos Cheques.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Ctipocheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipocheque)))
            Ctipocheque.click()

            registro_tipocheque = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Cheque al dia']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipocheque) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da dobleclick en el registro Tipos Cheques")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo de Cheque, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardatipocheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_tipocheque)))
            Guardatipocheque.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Tipos Cheques.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Caceptacheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aceptacheque)))
            Caceptacheque.click()
            Log().info("Se hace click en el checkbox Acepta Cheque")

        except Exception as e:
            Log().error("No se dió click en el checkbox Acepta Cheque, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Caceptaefectivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aceptaefectivo)))
            Caceptaefectivo.click()
            Log().info("Se hace click en el checkbox Acepta Efectivo")

        except Exception as e:
            Log().error("No se dió click en el checkbox Acepta Efectivo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdestinocheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_destinocheque)))
            Cdestinocheque.click()

            registro_destinocheque = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Cartera']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_destinocheque) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Destino Cheque.")

        except Exception as e:
            Log().error("No se encontró el registro de Destino Cheque, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Reparto HH

        try:
            Brepartohh = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_repartohh)))
            Brepartohh.click()
            Log().info("Se hace el cambio a la pestaña Reparto HH para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Reparto HH, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Datos

        try:
            Ceditableliq = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_editableliq)))
            Ceditableliq.click()
            Log().info("Se hace click en el checkbox Editable en liquidación de reparto")

        except Exception as e:
            Log().error("No se dió click en el checkbox Editable en liquidación de reparto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Restricciones

        try:
            Brestricciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_restricciones)))
            Brestricciones.click()
            Log().info("Se hace el cambio a la pestaña Restricciones para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Restricciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Nuevo

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegpermitida)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Linea de Negocio.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valor

        try:
            Ccodigolinea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_codigolinea)))
            Ccodigolinea.click()

            registro_codigolinea = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CIGARROS']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_codigolinea) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Codigo Linea.")

        except Exception as e:
            Log().error("No se encontró el registro de Codigo Linea, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardalinea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegpermitida)))
            Guardalinea.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Linea de Negocio.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info("Se hace el cambio a la pestaña Generar Desde para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Generar Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresar Datos

        try:
            Ccancelarccd = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cancelarccd)))
            Ccancelarccd.click()
            Log().info("Se hace click en el checkbox Cancelar CCD al generar")

        except Exception as e:
            Log().error("No se dió click en el checkbox Cancelar CCD al generar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresar Nuevo

        try:
            Nuevogenerardesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_incluiritem)))
            Nuevogenerardesde.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Generar Desde.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Datos

        try:
            Ctipodocumentogd = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocitem)))
            Ctipodocumentogd.send_keys(Configuracion.Itipodocumentogd)
            time.sleep(2)
            Log().info(" Ingresa el tipo documento del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el tipo documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardagenerardesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_incluiritem)))
            Guardagenerardesde.click()
            time.sleep(2)
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Generar Desde.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

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
            return False
