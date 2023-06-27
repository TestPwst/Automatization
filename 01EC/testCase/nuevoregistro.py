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
            self.assertEqual("EVENTOS CONTABLES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            Ccodigocontabilizador = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigocontabilizador)))
            Ccodigocontabilizador.send_keys(Configuracion.Icodigoconta)
            Log().info(" Ingresa el codigo contabilizador del nuevo registro ")

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
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigenimporte = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origenimporte)))
            Corigenimporte.send_keys(Configuracion.Iorigenimporte)
            Log().info(" Ingresa el Origen de Importe del nuevo registro ")

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
            Corigendescripcion.send_keys(Configuracion.Iorigendescrip)
            Log().info(" Ingresa el Origen de Importe del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen de Importe, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click en el checkbox Generar Asiento Unico, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click en el checkbox Forzar Cierre, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccuentacierre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuentacierre)))
            Ccuentacierre.click()

            registro_cuentacierre = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

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
            Log().info("Se hace el cambio a la pestaña Parametros para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón parametros, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoparametros = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_parametros)))
            Nuevoparametros.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Parametros.")

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
            Corden = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_orden)))
            Corden.send_keys(Configuracion.Iorden)
            Log().info(" Ingresa la orden del nuevo registro ")

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
            Cnomnegocio.send_keys(Configuracion.Inomnegocio)
            Log().info(" Ingresa el Nombre del Negocio del nuevo registro ")

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
            Corigenvalor.send_keys(Configuracion.Iorigenvalor)
            Log().info(" Ingresa el Origen Valor del nuevo registro ")

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
            Clargo.send_keys(Configuracion.Ilargo)
            Log().info(" Ingresa el largo del nuevo registro ")

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
            Cdecimales.send_keys(Configuracion.Idecimales)
            Log().info(" Ingresa los decimales del nuevo registro ")

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
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Parametros.")
            time.sleep(2)

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
            Log().info("Se hace el cambio a la pestaña Items para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón items, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoitems = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_item)))
            Nuevoitems.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Items.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

        try:
            Cordenitem = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ordeni)))
            Cordenitem.send_keys(Configuracion.Iordenitem)
            Log().info(" Ingresa la orden del nuevo registro ")

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
            Cdescripcionitem.send_keys(Configuracion.Idescripitem)
            Log().info(" Ingresa la descripcion del nuevo registro ")

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
            Corigenimporteitem.send_keys(Configuracion.Iorigenimportei)
            Log().info(" Ingresa el Origen de Importe del nuevo registro ")

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
            Corigenctacontable.send_keys(Configuracion.Iorigencuencon)
            Log().info(" Ingresa el Origen Cuena Contable del nuevo registro ")

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
            Corigenctrocosto1.send_keys(Configuracion.Iorigencencost1)
            Log().info(" Ingresa el Origen Centro Costo 1 del nuevo registro ")

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
            Corigenctrocosto2.send_keys(Configuracion.Iorigencencost2)
            Log().info(" Ingresa el Origen Centro Costo 2 del nuevo registro ")

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
            Corigenctrocosto3.send_keys(Configuracion.Iorigencencost3)
            Log().info(" Ingresa el Origen Centro Costo 3 del nuevo registro ")

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
            Corigencotizacion.send_keys(Configuracion.Iorigencotizacion)
            Log().info(" Ingresa el Origen Cotizacion del nuevo registro ")

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
            Corigendescripcionitem.send_keys(Configuracion.Iorigendescripi)
            Log().info(" Ingresa el Origen Cotizacion del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Origen Cotizacion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modo)))
            Cmodo.click()

            registro_tipomoneda = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Debe']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipomoneda) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Debe.")

        except Exception as e:
            Log().error("No se dió click en la opción Debe, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaitems = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_items)))
            Guardaitems.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Items.")

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

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
