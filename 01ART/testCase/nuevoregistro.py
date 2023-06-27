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
            self.assertEqual("ARTÍCULOS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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
            Ccodigointerno = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigointerno)))
            Ccodigointerno.send_keys(Configuracion.Icodigointerno)
            Log().info(" Ingresa el codigo interno del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo interno, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_usuario)))
            Ccodigousuario.send_keys(Configuracion.Icodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo usuario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cdescripcioncolector = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcioncolector)))
            Cdescripcioncolector.send_keys(Configuracion.Idescripcioncolector)
            Log().info(" Ingresa la Descripcion Colector del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion Colector, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cliquidarcomo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_liquidarcomo)))
            Cliquidarcomo.send_keys(Configuracion.Iliquidarcomo)
            Log().info(" Ingresa el liquidar como del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el liquidar como, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfamilia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_familia)))
            Cfamilia.click()

            registro_familia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_familia) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Familia ")

        except Exception as e:
            Log().error("No se encontró el registro de Familia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

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
            Log().info(" Se selecciono el registro de Linea Negocio ")

        except Exception as e:
            Log().error("No se encontró el registro de Linea Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigobarras = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigobarras)))
            Ccodigobarras.send_keys(Configuracion.Icodigobarras)
            Log().info(" Ingresa el Codigo de Barras del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Codigo de Barras, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunidadnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_unidadnegocio)))
            Cunidadnegocio.click()

            registro_unidadnegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PHILIP MORRIS MEXICO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_unidadnegocio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Unidad Negocio ")

        except Exception as e:
            Log().error("No se encontró el registro de Unidad Negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_packing)))
            Cpacking.click()

            registro_packing = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='HINGE LID BOX']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_packing) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Packing ")

        except Exception as e:
            Log().error("No se encontró el registro de Packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunidadventa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_unidadventa)))
            Cunidadventa.click()

            registro_unidadventa = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CAJETILLA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_unidadventa) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Unidad Venta ")

        except Exception as e:
            Log().error("No se encontró el registro de Unidad Venta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdiasvalidez = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_diasvalidez)))
            Cdiasvalidez.send_keys(Configuracion.Idiasvalidez)
            Log().info(" Ingresa los días de validez del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar los días de validez, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunidadesxpacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unidadesxpacking)))
            Cunidadesxpacking.clear()
            Cunidadesxpacking.send_keys(Configuracion.Iunidadesxpacking)
            Log().info(" Ingresa las unidades por packing del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las unidades por packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdecimalespacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_decimalespacking)))
            Cdecimalespacking.clear()
            Cdecimalespacking.send_keys(Configuracion.Idecimalespacking)
            Log().info(" Ingresa los decimales por packing del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar los decimales de cada packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cuhf1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unidadeshomofact1)))
            Cuhf1.send_keys(Configuracion.Iuhf1)
            Log().info(" Ingresa las Unidades Homogéneas Factor 1 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las Unidades Homogéneas Factor 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cuhf2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unidadeshomofact2)))
            Cuhf2.send_keys(Configuracion.Iuhf2)
            Log().info(" Ingresa las Unidades Homogéneas Factor 2 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las Unidades Homogéneas Factor 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cuhf3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unidadeshomofact3)))
            Cuhf3.send_keys(Configuracion.Iuhf3)
            Log().info(" Ingresa las Unidades Homogéneas Factor 3 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las Unidades Homogéneas Factor 3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cuhf4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unidadeshomofact4)))
            Cuhf4.send_keys(Configuracion.Iuhf4)
            Log().info(" Ingresa las Unidades Homogéneas Factor 4 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las Unidades Homogéneas Factor 4, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cactivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_activo)))
            Cactivo.click()
            Log().info(" Se dió click en el checkbox activo ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Activo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfacturaxpacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_facturaxpacking)))
            Cfacturaxpacking.click()
            Log().info(" Se dió click en el checkbox Factura por Packing ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox Factura por packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Lista Precios

        try:
            Blistaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_listaprecios)))
            Blistaprecios.click()
            Log().info("Se hace el cambio a la pestaña Lista de Precios para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Lista de Precios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

        try:
            Cdescripcionlp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionlp)))
            Cdescripcionlp.send_keys(Configuracion.Idescripcionlp)
            Log().info(" Ingresa la Descripcion LP del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Descripcion LP, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cobservacionlp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observacionlp)))
            Cobservacionlp.send_keys(Configuracion.Iobservacionlp)
            Log().info(" Ingresa la Observacion LP del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Observacion LP, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Impuestos

        try:
            Bimpuestos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impuestos)))
            Bimpuestos.click()
            Log().info("Se hace el cambio a la pestaña impuestos para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón impuestos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa datos

        try:
            Cformulacpu = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_formulapu)))
            Cformulacpu.clear()
            Cformulacpu.send_keys(Configuracion.Iimpuesto)
            Log().info(" Ingresa la Fórmula cálculo precio unitario del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Fórmula cálculo precio unitario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impuesto)))
            Nuevoimpuesto.click()
            Log().info(" Se presiona el boton 'Nuevo de la pestaña Impuesto' , para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo de la pestaña Impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Cimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuesto)))
            Cimpuesto.click()

            registro_impuesto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IMPUESTO CIGARRO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuesto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Impuesto ")

        except Exception as e:
            Log().error("No se encontró el registro de Impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impuesto)))
            Guardarimpuesto.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña impuesto', para guardar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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

        # Ingreso de los datos

        try:
            Cclasifart1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_clasifart1)))
            Cclasifart1.click()

            registro_clasifart1 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='FULL FLAVOR']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_clasifart1) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Clasificación de Articulo 1 ")

        except Exception as e:
            Log().error("No se encontró el registro de Clasificación de Articulo 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csabor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_sabor)))
            Csabor.click()

            registro_sabor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Regular']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_sabor) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Sabor ")

        except Exception as e:
            Log().error("No se encontró el registro de Sabor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitudr")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipoarticulo)))
            Ctipoarticulo.click()

            registro_tipoarticulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CON FILTRO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipoarticulo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tipo de Articulo ")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo de Articulo, verificar si el xpath sigue siendo el mismo, si al abrir la ayuda tardo mas de lo esperado, si la ayuda abre de manera correcta o si fallo la selección del registro del campo anterior")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Custom Properties

        try:
            Bcustom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_customproperties)))
            Bcustom.click()
            Log().info("Se hace el cambio a la pestaña Custom Properties para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón Custom Properties, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Caguascalientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aguascalientes)))
            Caguascalientes.click()
            Log().info(" Se dió click en el checkbox Aguascalientes")

        except Exception as e:
            Log().error("No se dió click en el checkbox Aguascalientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbajacalifornia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_bajacalifornia)))
            Cbajacalifornia.click()
            Log().info(" Se dió click en el checkbox de Baja California ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Baja California, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbajacaliforniasur = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_bajacaliforniasur)))
            Cbajacaliforniasur.click()
            Log().info(" Se dió click en el checkbox Baja California Sur ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Baja California Sur, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccampeche = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_campeche)))
            Ccampeche.click()
            Log().info(" Se dió click en el checkbox Campeche ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Campeche, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccoahuila = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_coahuila)))
            Ccoahuila.click()
            Log().info(" Se dió click en el checkbox Coahuila ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Coahuila, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccolima = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_colima)))
            Ccolima.click()
            Log().info(" Se dió click en el checkbox Colima ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Colima, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cchiapas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_chiapas)))
            Cchiapas.click()
            Log().info(" Se dió click en el checkbox Chiapas ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Chiapas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cchihuahua = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_chihuahua)))
            Cchihuahua.click()
            Log().info(" Se dió click en el checkbox Chihuahua ")

        except Exception as e:
            Log().error("No se dio click en el checkbox Chihuahua, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdf = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_df)))
            Cdf.click()
            Log().info(" Se dió click en el checkbox Distrito Federal ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Distrito Federal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdurango = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_durango)))
            Cdurango.click()
            Log().info(" Se dió click en el checkbox Durango ")

        except Exception as e:
            Log().error("No se dió click en el checkbpx Durango, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cguanajuato = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_guanajuato)))
            Cguanajuato.click()
            Log().info(" Se dió click en el checkbox Guanajuato ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Guanajuato, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cguerrero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_guerrero)))
            Cguerrero.click()
            Log().info(" Se dió click en el checkbox Guerrero ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Guerrero, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chidalgo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hidalgo)))
            Chidalgo.click()
            Log().info(" Se dió click en el checkbox Hidalgo ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Hidalgo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cjalisco = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_jalisco)))
            Cjalisco.click()
            Log().info(" Se dió click en el checkbox Jalisco")

        except Exception as e:
            Log().error("No se dió click en el checkbox Jalisco, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmexico = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mexico)))
            Cmexico.click()
            Log().info(" Se dió click en el checkbox México")

        except Exception as e:
            Log().error("No se dió click en el checkbox México, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmichoacan = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_michoacan)))
            Cmichoacan.click()
            Log().info(" Se dió click en el checkbox Michoacan")

        except Exception as e:
            Log().error("No se dió click en el checkbox Michoacan, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmorelos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_morelos)))
            Cmorelos.click()
            Log().info(" Se dió click en el checkbox Morelos")

        except Exception as e:
            Log().error("No se dió click en el checkbox Morelos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnayarit = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nayarit)))
            Cnayarit.click()
            Log().info(" Se dió click en el checkbox Nayarit")

        except Exception as e:
            Log().error("No se dió click en el checkbox Nayarit, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnuevoleon = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nuevoleon)))
            Cnuevoleon.click()
            Log().info(" Se dió click en el checkbox Nuevo León")

        except Exception as e:
            Log().error("No se dió click en el checkbox Nuevo León, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Coaxaca = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_oaxaca)))
            Coaxaca.click()
            Log().info(" Se dió click en el checkbox Oaxaca")

        except Exception as e:
            Log().error("No se dió click en el checkbox Oaxaca,validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpuebla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_puebla)))
            Cpuebla.click()
            Log().info(" Se dió click en el checkbox Puebla")

        except Exception as e:
            Log().error("No se dió click en el checkbox Puebla, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cqueretaro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_queretaro)))
            Cqueretaro.click()
            Log().info(" Se dió click en el checkbox Queretaro")

        except Exception as e:
            Log().error("No se dió click en el checkbox Queretaro, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cquintanaroo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_quintanaroo)))
            Cquintanaroo.click()
            Log().info(" Se dió click en el checkbox Quintana Roo")

        except Exception as e:
            Log().error("No se dió click en el checkbox Quintana Roo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csanluis = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sanluis)))
            Csanluis.click()
            Log().info(" Se dió click en el checkbox San Luis Potosi")

        except Exception as e:
            Log().error("No se dió click en el checkbox San Luis Potosi, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csinaloa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sinaloa)))
            Csinaloa.click()
            Log().info(" Se dió click en el checkbox Sinaloa")

        except Exception as e:
            Log().error("No se dió click en el checkbox Sinaloa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csonora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sonora)))
            Csonora.click()
            Log().info(" Se dió click en el checkbox Sonora")

        except Exception as e:
            Log().error("No se dió click en el checkbox Sonora, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctabasco = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tabasco)))
            Ctabasco.click()
            Log().info(" Se dió click en el checkbox Tabasco")

        except Exception as e:
            Log().error("No se dió click en el checkbox Tabasco, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctamaulipas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tamaulipas)))
            Ctamaulipas.click()
            Log().info(" Se dió click en el checkbox Tamaulipas")

        except Exception as e:
            Log().error("No se dió click en el checkbox Tamaulipas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctlaxcala = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tlaxcala)))
            Ctlaxcala.click()
            Log().info(" Se dió click en el checkbox Tlaxcala")

        except Exception as e:
            Log().error("No se dió click en el checkbox Tlaxcala, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cveracruz = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_veracruz)))
            Cveracruz.click()
            Log().info(" Se dió click en el checkbox Veracruz")

        except Exception as e:
            Log().error("No se dió click en el checkbox Veracruz, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cyucatan = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_yucatan)))
            Cyucatan.click()
            Log().info(" Se dió click en el checkbox Yucatan")

        except Exception as e:
            Log().error("No se dió click en el checkbox Yucatan, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Czacatecas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_zacatecas)))
            Czacatecas.click()
            Log().info(" Se dió click en el checkbox Zacatecas")

        except Exception as e:
            Log().error("No se dió click en el checkbox Zacatecas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
