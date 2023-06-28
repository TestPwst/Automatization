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
            self.assertEqual("MODELOS DE COBRANZA : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error(
                "La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
            Log().error(
                "El campo 'Codigo' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
            Log().error(
                "El campo 'Descripción' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tipodocgenerar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodocgenerar))).text
            self.assertEqual("Tipo Documento", tipodocgenerar, "Campo visible")
            Log().info(" El campo 'Tipo Documento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo Documento' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            accioncobranza = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_accioncobranza))).text
            self.assertEqual("Acción", accioncobranza, "Campo visible")
            Log().info(" El campo 'Acción cobranza' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Acción cobranza' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            modocobranza = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modogenerar))).text
            self.assertEqual("Modo generar", modocobranza, "Campo visible")
            Log().info(" El campo 'Modo generar cobranza' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Modo generar cobranza' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tipodocdescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodocdescuento))).text
            self.assertEqual("Tipo Documento", tipodocdescuento, "Campo visible")
            Log().info(" El campo 'Tipo Documento descuento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo Documento descuento' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            acciondescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_acciondescuent))).text
            self.assertEqual("Acción", acciondescuento, "Campo visible")
            Log().info(" El campo 'Acción descuento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Acción descuento' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            mododescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_mododescuento))).text
            self.assertEqual("Modo generar", mododescuento, "Campo visible")
            Log().info(" El campo 'Modo generar descuento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Modo generar descuento' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tipodocretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodocretencion))).text
            self.assertEqual("Tipo Documento", tipodocretencion, "Campo visible")
            Log().info(" El campo 'Tipo Documento retencion' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo Documento retencion' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            accionretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_accionretencion))).text
            self.assertEqual("Acción", accionretencion, "Campo visible")
            Log().info(" El campo 'Acción retencion' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Acción retencion' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            modoretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modoretencion))).text
            self.assertEqual("Modo generar", modoretencion, "Campo visible")
            Log().info(" El campo 'Modo generar retencion' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Modo generar retencion' no se muestra visible, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tipodoccobranza = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocgenerar)))
            tipodoccobranza.click()

            registro_cobranza = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM93']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cobranza) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de generar cobranza, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Caccioncobranza = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_accioncobranza)))
            Caccioncobranza.click()
            
            registro_accion = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Editar']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_accion) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro accion cobranza, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodocobranza = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modogenerar)))
            Cmodocobranza.click()
            
            registro_modo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='un documento por cliente']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modo) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro modo generar cobranza, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccreckgenerar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_Generarcobranza)))
            Ccreckgenerar.click()
            
        except Exception as e:
            Log().error(
                "No se encontró el registro de Habilitar generar documento, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tipodocdescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocdescuento)))

            action = ActionChains(self.driver)
            action \
                .move_to_element(tipodocdescuento) \
                .pause(1) \
                .release()
            action.perform()

            time.sleep(1)
            tipodocdescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocdescuento)))
            tipodocdescuento.click()
            
            registro_descuento = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM93']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_descuento) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de generar descuento, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cacciondescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_acciondescuent)))
            Cacciondescuento.click()
            
            registro_acciondescuento = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-container/ui-row[3]/ui-combobox/div/ul/li[3]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_acciondescuento) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro accion descuento, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmododescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mododescuento)))
            Cmododescuento.click()
            
            registro_mododescuento = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-container/ui-row[4]/ui-combobox/div/ul/li[3]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_mododescuento) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro modo descuento, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Checkdescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_Generardescuento)))
            Checkdescuento.click()
            
        except Exception as e:
            Log().error(
                "No se encontró el registro del check generar descuento, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tipodocretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocretencion)))
            time.sleep(1)
            tipodocretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocretencion)))
            tipodocretencion.click()
            
            registro_retencion = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM93']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_retencion) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de generar retencion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Caccionretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_accionretencion)))
            Caccionretencion.click()
            
            registro_retencion = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-container/ui-row[3]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_retencion) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro accion retencion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodoretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoretencion)))
            Cmodoretencion.click()
            
            registro_modoretencion = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-container/ui-row[4]/ui-combobox/div/ul/li[2]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoretencion) \
                .pause(1) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro modo retencion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Checkretencion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_Generarretencion)))
            Checkretencion.click()
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "No se encontró el registro de generar retencion, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
            Log().error(
                "No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto,el tiempo de la accion o si exise un registro igual ya creado")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False