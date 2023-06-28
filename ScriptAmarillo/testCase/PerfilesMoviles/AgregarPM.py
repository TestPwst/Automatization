from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class AgregarPM:

    def AgregarPM(self):
        """Abre la ventana para crear un nuevo registro"""
        self.wait = WebDriverWait(self.driver, 20)

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
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoPM)))
            Ccodigo.send_keys(Configuracion.IcodigoPM)
            Log().info(" Ingresa el codigo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionPM)))
            Cdescripcion.send_keys(Configuracion.IdescripcionPM)
            Log().info(" Ingresa la Descripcion del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ccargarrutas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargarrutas)))
            Ccargarrutas.click()
            time.sleep(5)

            registro_cargarrutas = self.driver.find_element(By.XPATH, "//li[text()='Todas las rutas']")

            action = ActionChains(self.driver)
            action \
                .click(registro_cargarrutas) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono la opción Todas las Rutas ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Todas las Rutas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ctipodocdefault1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocdefault1)))
            Ctipodocdefault1.send_keys(Configuracion.Itipodocdefault)
            Log().info(" Ingresa el Tipo documento default del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Tipo documento default, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ctipodocdefault2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocdefault2)))
            Ctipodocdefault2.click()
            time.sleep(3)
            Ctipodocdefault2.click()
            time.sleep(5)

            registro_tipodocdef = self.driver.find_element(By.XPATH, "//li[text()='Normal']")

            action = ActionChains(self.driver)
            action \
                .click(registro_tipodocdef) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono la opción Normal ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Normal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cmodocargaliq = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modocargaliq)))
            Cmodocargaliq.click()
            time.sleep(5)

            registro_modocargaliq = self.driver.find_element(By.XPATH, "//li[text()='Utilizar liquidación activa o crear nueva']")

            action = ActionChains(self.driver)
            action \
                .click(registro_modocargaliq) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Modo carga liquidación ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Modo carga liquidación, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cmododescargahh = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mododescargahh)))
            Cmododescargahh.click()
            time.sleep(5)

            registro_mododescargahh = self.driver.find_element(By.XPATH, "//li[text()='Documento (carga directa)']")

            action = ActionChains(self.driver)
            action \
                .click(registro_mododescargahh) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono  la opción Documento (carga directa) ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Documento (carga directa), validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cmodopdv = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modopdv)))
            Cmodopdv.click()
            Log().info(" Se dió click en el checkbox Modo PDV ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Modo PDV, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cregcoordenadasgps = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_regcoordenadasgps)))
            Cregcoordenadasgps.click()
            Log().info(" Se dió click en el checkbox Registrar coordenadas GPS ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el chekcbox Registrar coordenadas GPS, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cfinautomatico = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_finautovisita)))
            Cfinautomatico.click()
            time.sleep(5)

            registro_finautomatico = self.driver.find_element(By.XPATH, "//li[text()='No lo toma']")

            action = ActionChains(self.driver)
            action \
                .click(registro_finautomatico) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción No lo toma ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción No lo toma, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cintervalolectura = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_intervalolectura)))
            Cintervalolectura.send_keys(Configuracion.Iintervalolectura)
            Log().info(" Ingresa el Intervalo lectura coordenadas GPS(min) del nuevo registro ")
            time.sleep(3)
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
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Varios

        try:
            Bvarios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_variosPM)))
            Bvarios.click()
            time.sleep(3)
            Bvarios.click()
            Log().info("Se hace el cambio de pestaña Varios para continuar con el registro nuevo")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Varios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise


        # Ingresa los datos

        try:
            Ccargarresumenctasu = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargaresumenctasu)))
            Ccargarresumenctasu.click()
            Log().info(" Se dió click en el checkbox Cargar resumen de cuentas únicamente del vendedor de la ruta ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Cargar resumen de cuentas únicamente del vendedor de la ruta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cverificarlimcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_verificarlimcredito)))
            Cverificarlimcredito.click()
            Log().info(" Se dió click en el checkbox Verificar límite de crédito ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Verificar límite de crédito, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cverificaropcguardar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_verificaropcguardar)))
            Cverificaropcguardar.click()
            Log().info(" Se dió click en el checkbox Verificar opción 'guardar como' del tipo de documento ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Verificar opción 'guardar como' del tipo de documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cpermitirpagos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_permitirpagos)))
            Cpermitirpagos.click()
            Log().info(" Se dió click en el checkbox Permitir Pagos ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Permitir Pagos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise



        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_discodedatos)))
            Moverpantalla.click()
            time.sleep(5)

            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón espacio para mover la pantalla hacía abajo ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se Movio la pantalla hacia abajo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cdiscodedatos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_discodedatos)))
            Cdiscodedatos.click()
            time.sleep(5)

            registro_discodedatos = self.driver.find_element(By.XPATH, "//li[text()='M']")

            action = ActionChains(self.driver)
            action \
                .click(registro_discodedatos) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Disco de Datos ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Disco de Datos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ctipovendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipovendedorPM)))
            Ctipovendedor.click()
            time.sleep(5)

            registro_tipovendedor = self.driver.find_element(By.XPATH, "//li[text()='Autoventa']")

            action = ActionChains(self.driver)
            action \
                .click(registro_tipovendedor) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Autoventa ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Autoventa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cenviardocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_enviardocumentos)))
            Cenviardocumentos.click()
            Log().info(" Se dió click en el checkbox Enviar documentos de inmediato al servidor. ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Enviar documentos de inmediato al servidor., validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio de pestaña Permisos

        try:
            Bpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_permisosPM)))
            Bpermisos.click()
            Log().info("Se hace el cambio a la pestaña Permisos para continuar con el registro nuevo")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Permisos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Nuevopermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_permisoPM)))
            Nuevopermiso.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # ingresar los valores

        try:
            Cpermisos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_permisosPM)))
            Cpermisos.click()
            time.sleep(5)

            registro_permisos = self.driver.find_element(By.XPATH, "//li[text()='Inhibir Georeferenciación']")

            action = ActionChains(self.driver)
            action \
                .click(registro_permisos) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Inihibir Georeferenciación ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en la opción Inihibir Georeerenciación, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardarpermiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_permisoPM)))
            Guardarpermiso.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Permiso', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Lineas de Negocio

        try:
            Blineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_lineasnegocioPM)))
            Blineanegocio.click()
            Log().info("Se hace el cambio a la pestaña Lineas de Negocio para continuar con el registro nuevo")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Lineas de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegocioPM)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Ingreso de los datos

        try:
            Clineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lineanegocioPM)))
            Clineanegocio.click()
            time.sleep(5)

            registro_lineanegocio = self.driver.find_element(By.XPATH, "//span[text()='CIGARROS']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lineanegocio) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Linea de negocio ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Linea de negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardarlineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegocioPM)))
            Guardarlineanegocio.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Linea de Negocio', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Se repite el proceso

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegocioPM)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Clineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lineanegocioPM)))
            Clineanegocio.click()
            time.sleep(5)

            registro_lineanegocio = self.driver.find_element(By.XPATH, "//span[text()='EORDERING']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lineanegocio) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Linea de negocio ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Linea de negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardarlineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegocioPM)))
            Guardarlineanegocio.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Linea de Negocio', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Repetir Registro

        try:
            Nuevolineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_lineanegocioPM)))
            Nuevolineanegocio.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Permiso' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Permiso, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Clineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_lineanegocioPM)))
            Clineanegocio.click()
            time.sleep(5)

            registro_lineanegocio = self.driver.find_element(By.XPATH, "//span[text()='SERVICIOS']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_lineanegocio) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Linea de negocio ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Linea de negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardarlineanegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_lineanegocioPM)))
            Guardarlineanegocio.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Linea de Negocio', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Linea de Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Impulso Ventas

        try:
            Bimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impulsoventas)))
            Bimpulsoventas.click()
            Log().info("Se hace el cambio a la pestaña Impulso Ventas para continuar con el registro nuevo")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Impulso Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Ingresa Valores

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articuloPM)))
            Carticulo.send_keys(Configuracion.Iarticulo1)
            Log().info(" Ingresa el Articulo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(3)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Se repite paso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articuloPM)))
            Carticulo.send_keys(Configuracion.Iarticulo2)
            Log().info(" Ingresa el Articulo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(3)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Repetir Proceso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articuloPM)))
            Carticulo.send_keys(Configuracion.Iarticulo3)
            Log().info(" Ingresa el Articulo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(3)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Se repite proceso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articuloPM)))
            Carticulo.send_keys(Configuracion.Iarticulo4)
            Log().info(" Ingresa el Articulo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(3)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Repetir proceso

        try:
            Nuevoimpulsoventas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impulsoventa)))
            Nuevoimpulsoventas.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impulso de Ventas' , para crear un nuevo registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articuloPM)))
            Carticulo.send_keys(Configuracion.Iarticulo5)
            Log().info(" Ingresa el Articulo del nuevo registro ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardararticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impulsoventas)))
            Guardararticulo.click()
            time.sleep(3)
            Guardararticulo.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña Impulso de Ventas', para guardar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña Impulso de Ventas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambiar Pestaña Mantenimiento Clientes

        try:
            Bmanclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_mantenclientes)))
            Bmanclientes.click()
            Log().info("Se hace el cambio a la pestaña Mantenimiento Clientes para continuar con el registro nuevo")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Mantenimiento Clientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Ingresar Valores

        try:
            Cagregarclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_agregarclientes)))
            Cagregarclientes.click()
            Log().info(" Se dió click en el checkbox Permiso agregar nuevos clientes ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Permiso agregar nuevos clientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cmodificarclientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_modificarclientes)))
            Cmodificarclientes.click()
            Log().info(" Se dió click en el checkbox Permiso modificar clientes existentes ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Permiso modificar clientes existentes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Crutareferencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_rutareferencia)))
            Crutareferencia.click()
            time.sleep(5)

            registro_rutareferencia = self.driver.find_element(By.XPATH, "//span[text()='8. ÚNICA']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_rutareferencia) \
                .pause(3) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Ruta Referencia ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Ruta Referencia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cclasif1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif1)))
            Cclasif1.click()
            Log().info(" Se dió click en el checkbox Clasificación 1 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cclasif2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif2)))
            Cclasif2.click()
            Log().info(" Se dió click en el checkbox Clasificación 2 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cclasif3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clasif3)))
            Cclasif3.click()
            Log().info(" Se dió click en el checkbox Clasificación 3 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Clasificación 3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ccolonia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_colonia)))
            Ccolonia.click()
            Log().info(" Se dió click en el checkbox Colonia ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Colonia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Ccodigopostal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigopostal)))
            Ccodigopostal.click()
            Log().info(" Se dió click en el checkbox Codigo Postal ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Codigo Postal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cdireccion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_direccion)))
            Cdireccion.click()
            Log().info(" Se dió click en el checkbox Direccion ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Direccion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Centornopdv = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_entornopdv)))
            Centornopdv.click()
            Log().info(" Se dió click en el checkbox Entorno PDV ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Entorno PDV, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.click()
            Log().info(" Se dió click en el checkbox Esquina 1 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2)))
            Cesquina2.click()
            Log().info(" Se dió click en el checkbox Esquina 2 ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cpaises = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_paises)))
            Cpaises.click()
            Log().info(" Se dió click en el checkbox Paises ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Paises, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cdepartamento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_departamento)))
            Cdepartamento.click()
            Log().info(" Se dió click en el checkbox Departamento ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el chekcbox Departamento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Clocalidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_localidad)))
            Clocalidad.click()
            Log().info(" Se dió click en el checkbox Localidad ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el checkbox Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

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
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise
