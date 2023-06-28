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
        self.wait = WebDriverWait(self.driver, 100)

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta
        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("CONFIGURACIONES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la Descripcion del nuevo registro ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Documentos

        try:
            Bdocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_documentos)))
            Bdocumentos.click()
            Log().info("Se hace el cambio a la pestaña Documentos para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingreso los datos

        try:
            Cempresaemision = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_empresaemision)))
            Cempresaemision.click()

            registro_empresaemision = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='58']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_empresaemision) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Empresa Emisión Documentos ")

        except Exception as e:
            Log().error("No se encontró el registro de Empresa Emisión Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cserieemision = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_serieemision)))
            Cserieemision.click()

            registro_serieemision = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_serieemision) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Serie emisión documentos ")

        except Exception as e:
            Log().error("No se encontró el registro de Serie emisión documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmonedabase = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_monedabase)))
            Cmonedabase.click()

            registro_monedabase = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PESO MEXICANO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_monedabase) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Moneda Base ")

        except Exception as e:
            Log().error("No se encontró el registro de Moneda Base, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvendedoremision = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_vendedoremision)))
            Cvendedoremision.click()

            registro_vendedoremision = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='VENDEDOR  MOSTRADOR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_vendedoremision) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Vendedor emisión documentos ")

        except Exception as e:
            Log().error("No se encontró el registro de Vendedor emisión documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdepositoemision = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_depositoemision)))
            Cdepositoemision.click()

            registro_depositoemision = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='4200']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_depositoemision) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Depósito emisión documentos ")

        except Exception as e:
            Log().error("No se encontró el registro de Depósito emisión documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodoemision = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modoemision)))
            Cmodoemision.click()

            registro_modoemision = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Normal']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modoemision) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Normal.")

        except Exception as e:
            Log().error("No se dió click en la opción Normal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodofechastock = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modofechastock)))
            Cmodofechastock.click()

            registro_modofechastock = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Fecha del documento']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modofechastock) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Fecha del Documento.")

        except Exception as e:
            Log().error("No se dió click en la opción Fecha del Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodolimcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modolimcredito)))
            Cmodolimcredito.click()

            registro_modolimcredito = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Crédito abierto']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modolimcredito) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Credito Abierto.")

        except Exception as e:
            Log().error("No se dió click en la opción Credito Abierto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Varios

        try:
            Bvarios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_varios)))
            Bvarios.click()
            Log().info("Se hace el cambio a la pestaña Varios para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Varios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

        try:
            Clenguajexdefecto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lenguajexdefecto)))
            Clenguajexdefecto.click()

            registro_lenguajexdefecto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ESPAÑOL (MEXICO)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lenguajexdefecto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Lenguaje por Defecto ")

        except Exception as e:
            Log().error("No se encontró el registro de Lenguaje por Defecto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clenguajetraduccion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lenguajetraduccion)))
            Clenguajetraduccion.click()

            registro_lenguajetraduc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ESPAÑOL (MEXICO)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lenguajetraduc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Lenguaje para Traducción ")

        except Exception as e:
            Log().error("No se encontró el registro de Lenguaje para Traducción, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccierrecalendario1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierrecalendario)))
            Ccierrecalendario1.click()

            registro_cierrecalendario1 = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Días previos a la fecha actual']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cierrecalendario1) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Días previos a la fecha actual.")

        except Exception as e:
            Log().error("No se dió click en la opción Días previos a la fecha actual, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccierrecalendario2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierrecalendario2)))
            Ccierrecalendario2.send_keys(Configuracion.Icalendariocierre)
            Log().info(" Ingresa el Cierre Caledario del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Cierre Calendario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnopermitirfactura = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nopermitirfactura)))
            Cnopermitirfactura.send_keys(Configuracion.Inopermitirfact)
            Log().info(" Ingresa los días de no permitir factura del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar los días de no permitir factura, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantdecimalespre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantdecimalespre)))
            Ccantdecimalespre.send_keys(Configuracion.Icantdecimalespre)
            Log().info(" Ingresa la cantidad de decimales en el precio del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad de dceimales en el precio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantdecimalesdoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantdecimalesdoc)))
            Ccantdecimalesdoc.send_keys(Configuracion.Icantdecimalesdoc)
            Log().info(" Ingresa la cantidad de decimales en el documento del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad de dceimales en el documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdiferenciahoraria = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_diferenciahoraria)))
            Cdiferenciahoraria.send_keys(Configuracion.Idiferenciahoraria)
            Log().info(" Ingresa la Diferencia horaria  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Diferencia horaria, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cgenerarentrega = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_generarentrega)))
            Cgenerarentrega.click()
            Log().info(" Se dió click en el checkbox Generar entrega dinero de cheques ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Generar entrega dinero de cheques, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmantenerdocs = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mantenerdocs)))
            Cmantenerdocs.click()
            Log().info(" Se dió click en el checkbox Mantener documentos en liquidación al emitir ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Mantener documentos en liquidación al emitir, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvalidarnur = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_validarnur)))
            Cvalidarnur.click()
            Log().info(" Se dió click en el checkbox Validar NUR al asignar clientes a la ruta ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Validar NUR al asignar clientes a la ruta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Rangos Codigo

        try:
            Brangoscodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_rangoscodigo)))
            Brangoscodigo.click()
            Log().info("Se hace el cambio a la pestaña Rangos Codigo para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Rango Codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa al dato para modificar

        Registrorango = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Arquitectura de cliente']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrorango) \
                .pause(0) \
                .double_click(Registrorango) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Arquitrctura Cliente, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Arquitectura Cliente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

        try:
            Cdesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_desde)))
            Cdesde.clear()
            Cdesde.send_keys(Configuracion.Irangosdesde)
            Log().info(" Ingresa el Rango Desde  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar El Rango Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitude")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hasta)))
            Chasta.clear()
            Chasta.send_keys(Configuracion.Irangoshasta)
            Log().info(" Ingresa el Rango Hasta  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar El Rango Hasta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarango = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar)))
            Guardarango.click()
            Log().info(" Se da clic en el boton Aceptar; se debe modificar la informacion del registro de Arquitectura de Cliente.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se repite el proceso

        Registrorango2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Bancos' and @class = 'tabulator-cell-value']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrorango2) \
                .pause(0) \
                .double_click(Registrorango2) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Bancos, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Bancos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Datos

        try:
            Cdesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_desde)))
            Cdesde.clear()
            Cdesde.send_keys(Configuracion.Irangosdesde)
            Log().info(" Ingresa el Rango Desde  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar El Rango Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hasta)))
            Chasta.clear()
            Chasta.send_keys(Configuracion.Irangoshasta)
            Log().info(" Ingresa el Rango Hasta  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar El Rango Hasta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarango = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar)))
            Guardarango.click()
            Log().info(" Se da clic en el boton Aceptar; se debe modificar la informacion del registro de Bancos.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió clcik en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se repite proceso

        Registrorango3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Cajas' and @class = 'tabulator-cell-value']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrorango3) \
                .pause(0) \
                .double_click(Registrorango3) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Cajas, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Cajas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Datos

        try:
            Cdesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_desde)))
            Cdesde.clear()
            Cdesde.send_keys(Configuracion.Irangosdesde)
            Log().info(" Ingresa el Rango Desde  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar El Rango Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hasta)))
            Chasta.clear()
            Chasta.send_keys(Configuracion.Irangoshasta)
            Log().info(" Ingresa el Rango Hasta  del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar El Rango Hasta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarango = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar)))
            Guardarango.click()
            Log().info(" Se da clic en el boton Aceptar; se debe modificar la informacion del registro de Cajas.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Propiedades por defecto

        try:
            Bpropiedades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_propiedadesxdefecto)))
            Bpropiedades.click()
            Log().info("Se hace el cambio a la pestaña Propiedades Por Defecto para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Propiedades Por Defecto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Clistaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_listaprecios)))
            Clistaprecios.click()

            registro_listaprecios = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='8251']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_listaprecios) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Lista precios ")

        except Exception as e:
            Log().error("No se encontró el registro de Lista Precios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cgrupocliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupocliente)))
            Cgrupocliente.click()

            registro_grupocliente = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GRUPODETALLE']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupocliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Grupo Cliente ")

        except Exception as e:
            Log().error("No se encontró el registro de Grupo Cliente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csubgrupocliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_subgrupocliente)))
            Csubgrupocliente.click()

            registro_subgrupocliente = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GRUPO DETALLE']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_subgrupocliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Subgrupo Cliente ")

        except Exception as e:
            Log().error("No se encontró el registro de Subgrupo Cliente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccanal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_canal)))
            Ccanal.click()

            registro_canal = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='RETAIL']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_canal) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Canal ")

        except Exception as e:
            Log().error("No se encontró el registro de Canal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csubcanal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_subcanal)))
            Csubcanal.click()

            registro_subcanal = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='GT']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_subcanal) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Subcanal ")

        except Exception as e:
            Log().error("No se encontró el registro de Subcanal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estado)))
            Cestado.click()

            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MEXICO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estado) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Estado ")

        except Exception as e:
            Log().error("No se encontró el registro de Estado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdeptoprovi = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deptoprovi)))
            Cdeptoprovi.click()

            registro_deptoprovi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='COACALCO DE BERRIOZABAL']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deptoprovi) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Depto/Provi ")

        except Exception as e:
            Log().error("No se encontró el registro de Depto/Provi, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidad)))
            Clocalidad.click()

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SAN FRANCISCO COACALCO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidad) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Localidad ")

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarrio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrio)))
            Cbarrio.click()

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SAN FRANCISCO COACALCO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Barrio ")

        except Exception as e:
            Log().error("No se encontró el registro de Barrio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Czonageografica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_zonageo)))
            Czonageografica.click()

            registro_zonageo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='VISITABLE']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_zonageo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Zona Geografica")

        except Exception as e:
            Log().error("No se encontró el registro de Zona Geografica, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Czonareparto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_zonareparto)))
            Czonareparto.click()

            registro_zonareparto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='REPARTO 01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_zonareparto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Zona Reparto ")

        except Exception as e:
            Log().error("No se encontró el registro de Zona Reparto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Czonaventa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_zonaventa)))
            Czonaventa.click()

            registro_zonaventa = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ZONA DE VENTA A01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_zonaventa) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Zona de Venta ")

        except Exception as e:
            Log().error("No se encontró el registro de Zona de Venta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdistribuidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_distribuidor)))
            Cdistribuidor.click()

            registro_distribuidor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='58']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_distribuidor) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Distribuidor ")

        except Exception as e:
            Log().error("No se encontró el registro de Distribuidor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cagencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_agencia)))
            Cagencia.click()

            registro_agencia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Distribuidora Mabezihua (GUERRERO 76-522722-0001)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_agencia) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Agencia ")

        except Exception as e:
            Log().error("No se encontró el registro de Agencia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Coficina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_oficina)))
            Coficina.click()

            registro_oficina = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='76-522722D001']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_oficina) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Oficina ")

        except Exception as e:
            Log().error("No se encontró el registro de Oficina, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cperfilcuenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_perfilcuenta)))
            Cperfilcuenta.click()

            registro_perfilcuenta = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Contado']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_perfilcuenta) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Perfil de Cuenta ")

        except Exception as e:
            Log().error("No se encontró el registro de Perfil Cuenta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cempresa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_empresa)))
            Cempresa.click()

            registro_empresa = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='58']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_empresa) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Empresa ")

        except Exception as e:
            Log().error("No se encontró el registro de Empresa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipocliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipocliente)))
            Ctipocliente.click()

            registro_tipocliente = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ABARROTES/MISCELANEA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipocliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tipo Cliente ")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Cliente, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoexclusividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipoexclusividad)))
            Ctipoexclusividad.click()

            registro_tipoexclusividad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Sin Calcular']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipoexclusividad) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tipo Exclusividad ")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Exclusividad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cprimernivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_primernivel)))
            Cprimernivel.click()

            registro_primernivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM8']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_primernivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Primer Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Primer Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csegundonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_segundonivel)))
            Csegundonivel.click()

            registro_segundonivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='82']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_segundonivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Segundo Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Segundo Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctercernivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tercernivel)))
            Ctercernivel.click()

            registro_tercernivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='01269']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tercernivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tercer Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Tercer Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccuartonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuartonivel)))
            Ccuartonivel.click()

            registro_cuartonivel = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='0002']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuartonivel) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Cuarto Nivel ")

        except Exception as e:
            Log().error("No se encontró el registro de Cuarto Nivel, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Dispositivos

        try:
            Bdispositivos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_dispositivos)))
            Bdispositivos.click()
            Log().info("Se hace el cambio a la pestaña Dispositivos para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Dispositivos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingreso de los datos

        try:
            Cnombreusuarios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nombreusuarios)))
            Cnombreusuarios.send_keys(Configuracion.Inombreusuarios)
            Log().info(" Ingresa el Nombre usuarios del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Nombre usuarios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccontrasena = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_contrasena)))
            Ccontrasena.send_keys(Configuracion.Icontrasena)
            Log().info(" Ingresa la Contraseña del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Contraseña, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Opciones Personalizadas

        try:
            Bopcpersonalizadas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_opcpersonalizadas)))
            Bopcpersonalizadas.click()
            Log().info("Se hace el cambio a ola pestaña Opciones Personalizadas para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Opciones Personalizadas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoopciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_opcpersonalizadas)))
            Nuevoopciones.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Opciones Personalizadas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo de la pestaña Opciones Personalizadas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Cclave = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clave)))
            Cclave.send_keys(Configuracion.Iclave)
            Log().info(" Ingresa la Clave del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Clave, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvalor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_valor)))
            Cvalor.send_keys(Configuracion.Ivalor)
            Log().info(" Ingresa el valor del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Valor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaropcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptaropc)))
            Guardaropcion.click()
            Log().info(" Se presiona el boton 'Aceptar de la pestaña Opciones Personalizadas', para guardar el registro.")

        except Exception as e:
            Log().error("No se encontró el botón Aceptar de la pestaña Opciones Personalizadas, rvalidar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoopciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_opcpersonalizadas)))
            Nuevoopciones.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Opciones Personalizadas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo de la pestaña Opciones Personalizadas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclave = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clave)))
            Cclave.send_keys(Configuracion.Iclave2)
            Log().info(" Ingresa la Clave del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Clave, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvalor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_valor)))
            Cvalor.send_keys(Configuracion.Ivalor2)
            Log().info(" Ingresa el valor del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Valor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaropcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptaropc)))
            Guardaropcion.click()
            Log().info(" Se presiona el boton 'Aceptar de la pestaña Opciones Personalizadas', para guardar el registro.")

        except Exception as e:
            Log().error("No se encontró el botón Aceptar de la pestaña Opciones Personalizadas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoopciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_opcpersonalizadas)))
            Nuevoopciones.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Opciones Personalizadas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo de la pestaña Opciones Personalizadas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclave = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clave)))
            Cclave.send_keys(Configuracion.Iclave3)
            Log().info(" Ingresa la Clave del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Clave, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvalor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_valor)))
            Cvalor.send_keys(Configuracion.Ivalor3)
            Log().info(" Ingresa el valor del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Valor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaropcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptaropc)))
            Guardaropcion.click()
            Log().info(" Se presiona el boton 'Aceptar de la pestaña Opciones Personalizadas', para guardar el registro.")

        except Exception as e:
            Log().error("No se encontró el botón Aceptar de la pestaña Opciones Personalizadas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambiar Pestaña Mantenimiento Clientes

        try:
            Bcontabilidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_contabilidad)))
            Bcontabilidad.click()
            Log().info("Se hace el cambio a la pestaña Contabilidad para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió clck en el botón Contabilidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresar Valores

        try:
            Cagruparitems = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_agruparitems)))
            Cagruparitems.click()
            Log().info(" Se dió click en el checkbox Agrupar Items ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Agrupar Items, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(15)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
