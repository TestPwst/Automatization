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
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))

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
            Ccodigocontabilizador = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigocontabilizador)))
            Ccodigocontabilizador.clear()
            Ccodigocontabilizador.send_keys(Configuracion.Mcodigoconta)
            Log().info(" Se modifica el contenido del campo Codigo Contabilizador ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo contabilizador, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenimporte = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenimporte)))
            Corigenimporte.clear()
            Corigenimporte.send_keys(Configuracion.Morigenimporte)
            Log().info(" Se modifica el contenido del campo Origen Importe ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen de Importe, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigendescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origendescripcion)))
            Corigendescripcion.clear()
            Corigendescripcion.send_keys(Configuracion.Morigendescrip)
            Log().info(" Se modifica el contenido del campo Origen Descripción ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Descripción, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cgenerarasiento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_generarasiento)))
            Cgenerarasiento.click()
            Log().info(" Se dió click en el checkbox Generar Asiento Unico.")

        except Exception as e:
            Log().error("No se encontró el campo de Generar Asiento Unico, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cforzarcierre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_forzarcierre)))
            Cforzarcierre.click()
            Log().info(" Se dió click en el checkbox Forzar Cierre.")

        except Exception as e:
            Log().error("No se encontró el campo Forzar Cierre, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccuentacierre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuentacierre)))
            Ccuentacierre.click()

            registro_cuentacierre = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuentacierre) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Cuenta Cierre.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de Cuenta Cierre, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña parametros

        try:
            Bparametros = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_parametros)))
            Bparametros.click()
            Log().info("Se hace el cambio a la pestaña Parametros para continuar con la Modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón parametros, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registroparametros = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroparametros) \
                .pause(0) \
                .double_click(Registroparametros) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Parmetros, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Parametros, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Corden = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_orden)))
            Corden.clear()
            Corden.send_keys(Configuracion.Morden)
            Log().info(" Se modifica el contenido del campo Orden ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la orden, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnomnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nomnegocio)))
            Cnomnegocio.clear()
            Cnomnegocio.send_keys(Configuracion.Mnomnegocio)
            Log().info(" Se modifica el contenido del campo Nom Negocio ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Nombre del Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenvalor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenvalor)))
            Corigenvalor.clear()
            Corigenvalor.send_keys(Configuracion.Morigenvalor)
            Log().info(" Se modifica el contenido del campo Origen Valor ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Valor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clargo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_largo)))
            Clargo.clear()
            Clargo.send_keys(Configuracion.Mlargo)
            Log().info(" Se modifica el contenido del campo Largo ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el largo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdecimales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_decimales)))
            Cdecimales.clear()
            Cdecimales.send_keys(Configuracion.Mdecimales)
            Log().info(" Se modifica el contenido del campo Decimales ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar los decimales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaparametros = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_parametros)))
            Guardaparametros.click()
            time.sleep(2)
            Guardaparametros.click()
            time.sleep(2)
            Log().info(" Se da clic en el boton Guardar; se guardar la modificaciones del registro parametros.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Items

        try:
            Bitems = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_items)))
            Bitems.click()
            Log().info("Se hace el cambio a la pestaña Items para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón items, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registroitems = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='10']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroitems) \
                .pause(0) \
                .double_click(Registroitems) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Items, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Items, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # modifica Valores

        try:
            Cordenitem = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ordeni)))
            Cordenitem.clear()
            Cordenitem.send_keys(Configuracion.Mordenitem)
            Log().info(" Se modifica el contenido del campo Orden ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la orden, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionitem = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcioni)))
            Cdescripcionitem.clear()
            Cdescripcionitem.send_keys(Configuracion.Mdescripitem)
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
            Corigenimporteitem = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenimportei)))
            Corigenimporteitem.clear()
            Corigenimporteitem.send_keys(Configuracion.Morigenimportei)
            Log().info(" Se modifica el contenido del campo Origen Importe ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen de Importe, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenctacontable = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenctacont)))
            Corigenctacontable.clear()
            Corigenctacontable.send_keys(Configuracion.Morigencuencon)
            Log().info(" Se modifica el contenido del campo Origen Cuenta Contable ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Cuenta Contable, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenctrocosto1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenctrocosto1)))
            Corigenctrocosto1.clear()
            Corigenctrocosto1.send_keys(Configuracion.Morigencencost1)
            Log().info(" Se modifica el contenido del campo Origen Centro Costo 1 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Centro Costo 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenctrocosto2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenctrocosto2)))
            Corigenctrocosto2.clear()
            Corigenctrocosto2.send_keys(Configuracion.Morigencencost2)
            Log().info(" Se modifica el contenido del campo Origen Centro Costo 2 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Centro Costo 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenctrocosto3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenctrocosto3)))
            Corigenctrocosto3.clear()
            Corigenctrocosto3.send_keys(Configuracion.Morigencencost3)
            Log().info(" Se modifica el contenido del campo Origen Centro Costo 3 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Centro Costo 3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigencotizacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origencotizacion)))
            Corigencotizacion.clear()
            Corigencotizacion.send_keys(Configuracion.Morigencotizacion)
            Log().info(" Se modifica el contenido del campo Origen Cotización ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Cotizacion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigendescripcionitem = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origendescripcioni)))
            Corigendescripcionitem.clear()
            Corigendescripcionitem.send_keys(Configuracion.Morigendescripi)
            Log().info(" Se modifica el contenido del campo Origen Descripcion ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modo)))
            Cmodo.click()

            registro_tipomoneda = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Haber']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipomoneda) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Haber.")

        except Exception as e:
            Log().error("No se dió click en la registro Opción Haber, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaitems = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_items)))
            Guardaitems.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar el registro de Items.")
            time.sleep(1)

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
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False