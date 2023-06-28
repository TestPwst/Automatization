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
            self.assertEqual("PERFILES MÓVILES (PERFIL VENDEDOR) : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la Descripcion del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccargarrutas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargarrutas)))
            Ccargarrutas.click()

            registro_cargarrutas = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Todas las rutas']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_cargarrutas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono la opción Todas las Rutas ")

        except Exception as e:
            Log().error("No se dió click en la opción Todas las Rutas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodocdefault1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocdefault1)))
            Ctipodocdefault1.send_keys(Configuracion.Itipodocdefault)
            Log().info(" Ingresa el Tipo documento default del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Tipo documento default, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodocdefault2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocdefault2)))
            Ctipodocdefault2.click()

            registro_tipodocdef = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Normal']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipodocdef) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono la opción Normal ")

        except Exception as e:
            Log().error("No se dió click en la opción Normal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodocargaliq = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modocargaliq)))
            Cmodocargaliq.click()

            registro_modocargaliq = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Utilizar liquidación activa o crear nueva']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_modocargaliq) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Modo carga liquidación ")

        except Exception as e:
            Log().error("No se encontró el registro de Modo carga liquidación, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmododescargahh = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mododescargahh)))
            Cmododescargahh.click()

            registro_mododescargahh = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Documento (carga directa)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_mododescargahh) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono  la opción Documento (carga directa) ")

        except Exception as e:
            Log().error("No se dió click en la opción Documento (carga directa), validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodopdv = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modopdv)))
            Cmodopdv.click()
            Log().info(" Se dió click en el checkbox Modo PDV ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Modo PDV, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cregcoordenadasgps = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_regcoordenadasgps)))
            Cregcoordenadasgps.click()
            Log().info(" Se dió click en el checkbox Registrar coordenadas GPS ")

        except Exception as e:
            Log().error("No se dió click en el chekcbox Registrar coordenadas GPS, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfinautomatico = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_finautovisita)))
            Cfinautomatico.click()

            registro_finautomatico = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='No lo toma']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_finautomatico) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción No lo toma ")

        except Exception as e:
            Log().error("No se dió click en la opción No lo toma, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cintervalolectura = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_intervalolectura)))
            Cintervalolectura.send_keys(Configuracion.Iintervalolectura)
            Log().info(" Ingresa el Intervalo lectura coordenadas GPS(min) del nuevo registro ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Intervalo lectura coordenadas GPS(min), validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(1)
            Bvarios.click()
            time.sleep(1)
            Log().info("Se hace el cambio de pestaña Varios para continuar con el registro nuevo")

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
            Ccargarresumenctasu = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargaresumenctasu)))
            Ccargarresumenctasu.click()
            Log().info(" Se dió click en el checkbox Cargar resumen de cuentas únicamente del vendedor de la ruta ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Cargar resumen de cuentas únicamente del vendedor de la ruta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cverificarlimcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_verificarlimcredito)))
            Cverificarlimcredito.click()
            Log().info(" Se dió click en el checkbox Verificar límite de crédito ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Verificar límite de crédito, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cverificaropcguardar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_verificaropcguardar)))
            Cverificaropcguardar.click()
            Log().info(" Se dió click en el checkbox Verificar opción 'guardar como' del tipo de documento ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Verificar opción 'guardar como' del tipo de documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpermitirpagos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_permitirpagos)))
            Cpermitirpagos.click()
            Log().info(" Se dió click en el checkbox Permitir Pagos ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Permitir Pagos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_discodedatos)))
            Moverpantalla.click()

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
            Cdiscodedatos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_discodedatos)))
            Cdiscodedatos.click()

            registro_discodedatos = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='M']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_discodedatos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Disco de Datos ")

        except Exception as e:
            Log().error("No se encontró el registro de Disco de Datos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipovendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipovendedor)))
            Ctipovendedor.click()

            registro_tipovendedor = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Autoventa']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipovendedor) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Autoventa ")

        except Exception as e:
            Log().error("No se dió click en la opción Autoventa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cenviardocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_enviardocumentos)))
            Cenviardocumentos.click()
            Log().info(" Se dió click en el checkbox Enviar documentos de inmediato al servidor. ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Enviar documentos de inmediato al servidor., validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Permisos

        try:
            Bpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_permisos)))
            Bpermisos.click()
            Log().info("Se hace el cambio a la pestaña Permisos para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevopermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_permiso)))
            Nuevopermiso.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Cpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_permisos)))
            Cpermisos.click()

            registro_permisos = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Inhibir Georeferenciación']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_permisos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Inihibir Georeferenciación ")

        except Exception as e:
            Log().error("No se dió click en la opción Inihibir Georeerenciación, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarpermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_permiso)))
            Guardarpermiso.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Permiso', para guardar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevopermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_permiso)))
            Nuevopermiso.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_permisos)))
            Cpermisos.click()

            registro_permisos = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Anular documentos']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_permisos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Anular Documentos ")

        except Exception as e:
            Log().error("No se dió click en la opción Anular Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarpermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_permiso)))
            Guardarpermiso.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Permiso', para guardar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Lineas de Negocio

        try:
            Blineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_lineasnegocio)))
            Blineanegocio.click()
            Log().info("Se hace el cambio a la pestaña Lineas de Negocio para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Lineas de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegocio)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingreso de los datos

        try:
            Clineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lineanegocio)))
            Clineanegocio.click()

            registro_lineanegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CIGARROS']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lineanegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Linea de negocio ")

        except Exception as e:
            Log().error("No se encontró el registro de Linea de negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarlineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegocio)))
            Guardarlineanegocio.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Linea de Negocio', para guardar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se repite el proceso

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegocio)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lineanegocio)))
            Clineanegocio.click()

            registro_lineanegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='EORDERING']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lineanegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Linea de negocio ")

        except Exception as e:
            Log().error("No se encontró el registro de Linea de negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarlineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegocio)))
            Guardarlineanegocio.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Linea de Negocio', para guardar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repetir Registro

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegocio)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lineanegocio)))
            Clineanegocio.click()

            registro_lineanegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SERVICIOS']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lineanegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Linea de negocio ")

        except Exception as e:
            Log().error("No se encontró el registro de Linea de negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarlineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegocio)))
            Guardarlineanegocio.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Linea de Negocio', para guardar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Impulso Ventas

        try:
            Bimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impulsoventas)))
            Bimpulsoventas.click()
            Log().info("Se hace el cambio a la pestaña Impulso Ventas para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articulo)))
            Carticulo.send_keys(Configuracion.Iarticulo1)
            Log().info(" Ingresa el Articulo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(2)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se repite paso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articulo)))
            Carticulo.send_keys(Configuracion.Iarticulo2)
            Log().info(" Ingresa el Articulo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(2)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repetir Proceso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articulo)))
            Carticulo.send_keys(Configuracion.Iarticulo3)
            Log().info(" Ingresa el Articulo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(2)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se repite proceso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articulo)))
            Carticulo.send_keys(Configuracion.Iarticulo4)
            Log().info(" Ingresa el Articulo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(2)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Repetir proceso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articulo)))
            Carticulo.send_keys(Configuracion.Iarticulo5)
            Log().info(" Ingresa el Articulo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(2)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambiar Pestaña Mantenimiento Clientes

        try:
            Bmanclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_mantenclientes)))
            Bmanclientes.click()
            Log().info("Se hace el cambio a la pestaña Mantenimiento Clientes para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Mantenimiento Clientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresar Valores

        try:
            Cagregarclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_agregarclientes)))
            Cagregarclientes.click()
            Log().info(" Se dió click en el checkbox Permiso agregar nuevos clientes ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Permiso agregar nuevos clientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodificarclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modificarclientes)))
            Cmodificarclientes.click()
            Log().info(" Se dió click en el checkbox Permiso modificar clientes existentes ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Permiso modificar clientes existentes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Crutareferencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_rutareferencia)))
            Crutareferencia.click()

            registro_rutareferencia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='8. ÚNICA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_rutareferencia) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Ruta Referencia ")

        except Exception as e:
            Log().error("No se encontró el registro de Ruta Referencia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasif1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif1)))
            Cclasif1.click()
            Log().info(" Se dió click en el checkbox Clasificación 1 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasif2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif2)))
            Cclasif2.click()
            Log().info(" Se dió click en el checkbox Clasificación 2 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasif3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif3)))
            Cclasif3.click()
            Log().info(" Se dió click en el checkbox Clasificación 3 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccolonia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_colonia)))
            Ccolonia.click()
            Log().info(" Se dió click en el checkbox Colonia ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Colonia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigopostal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigopostal)))
            Ccodigopostal.click()
            Log().info(" Se dió click en el checkbox Codigo Postal ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Codigo Postal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdireccion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_direccion)))
            Cdireccion.click()
            Log().info(" Se dió click en el checkbox Direccion ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Direccion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Centornopdv = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_entornopdv)))
            Centornopdv.click()
            Log().info(" Se dió click en el checkbox Entorno PDV ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Entorno PDV, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.click()
            Log().info(" Se dió click en el checkbox Esquina 1 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2)))
            Cesquina2.click()
            Log().info(" Se dió click en el checkbox Esquina 2 ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpaises = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_paises)))
            Cpaises.click()
            Log().info(" Se dió click en el checkbox Paises ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Paises, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdepartamento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_departamento)))
            Cdepartamento.click()
            Log().info(" Se dió click en el checkbox Departamento ")

        except Exception as e:
            Log().error("No se dió click en el chekcbox Departamento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_localidad)))
            Clocalidad.click()
            Log().info(" Se dió click en el checkbox Localidad ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
