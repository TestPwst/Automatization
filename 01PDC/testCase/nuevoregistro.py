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
            self.assertEqual("PERFILES DE COMISIÓN : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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
            Porcentajeglobal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_porcentajeglobal))).text
            self.assertEqual("Porcentaje Global", Porcentajeglobal, "Campo visible")
            Log().info(" El campo 'Porcentaje Global' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Porcentaje Global' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Conimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_conimpuesto))).text
            self.assertEqual("Con impuesto", Conimpuesto, "Campo visible")
            Log().info(" El campo 'Con impuesto' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Con impuesto' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Comisionrepartidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_comisionrepartidor))).text
            self.assertEqual("Comisión Repartidor", Comisionrepartidor, "Campo visible")
            Log().info(" El campo 'Comisión Repartidor' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Comisión Repartidor' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cporcentajeglobal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_porcentajeglobal)))
            Cporcentajeglobal.send_keys(Configuracion.Iporcentajeglobal)
            Log().info(" Ingresa el Porcentaje Global del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Porcentaje Global, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cconimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_conimpuesto)))
            Cconimpuesto.click()
            Log().info(" Se hizó click en el Checkbox Con impuesto ")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Con impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccomisionrepar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_comisionrepartidor)))
            Ccomisionrepar.click()
            Log().info(" Se hizó click en el checkbox Comisión Repartidor ")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox Comisión Repartidor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y agregar nuevo

        try:
            Btopes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_topes)))
            Btopes.click()
            Log().info("Se hace el cambio a la pestaña Topes para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se dió click en el botón topes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevotopes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_topes)))
            Nuevotopes.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Topes.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida existencia de las etiquetas

        try:
            Moneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_moneda))).text
            self.assertEqual("Moneda", Moneda, "Campo visible")
            Log().info(" El campo 'Moneda' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Moneda' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tope = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tope))).text
            self.assertEqual("Tope", Tope, "Campo visible")
            Log().info(" El campo 'Tope' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tope' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Porcentajetopes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_porcentajetope))).text
            self.assertEqual("Porcentaje", Porcentajetopes, "Campo visible")
            Log().info(" El campo 'Porcentaje' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Porcentaje' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #ingreso de los valores en los campos

        try:
            Cmoneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_moneda)))
            Cmoneda.click()
            
            registro_moneda = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PESO MEXICANO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_moneda) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Moneda.")
            
        except Exception as e:
            Log().error("No se encontró el registro de moneda, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctope = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tope)))
            Ctope.send_keys(Configuracion.Itope)
            Log().info(" Ingresa el tope del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el tope, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cporcentajetope = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_porcentajetope)))
            Cporcentajetope.send_keys(Configuracion.Iporcentajetopes)
            Log().info(" Ingresa el Porcentaje del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Porcentaje, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardatopes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_topes)))
            Guardatopes.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Topes.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Cambio de pestaña y agregar nuevo

        try:
            Bctaarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ctaarticulo)))
            Bctaarticulo.click()
            Log().info("Se hace el cambio a la pestaña Cuenta Articulo para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se dió click en el botón Cuenta Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoctaarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_ctaarticulo)))
            Nuevoctaarticulo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Cuenta Articulo.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida existencia de las etiquetas

        try:
            Cuenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cuenta))).text
            self.assertEqual("Cuenta", Cuenta, "Campo visible")
            Log().info(" El campo 'Cuenta' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cuenta' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Articulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_articulo))).text
            self.assertEqual("Artículo", Articulo, "Campo visible")
            Log().info(" El campo 'Artículo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Artículo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Porcentajectaart = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_porcentajectaart))).text
            self.assertEqual("Porcentaje", Porcentajectaart, "Campo visible")
            Log().info(" El campo 'Porcentaje' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Porcentaje' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #ingreso Valores

        try:
            Ccuenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuenta)))
            Ccuenta.click()
            
            registro_cuenta = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100% ZACATECANA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuenta) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Cuenta.")
            
        except Exception as e:
            Log().error("No se encontró el registro de cuenta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_articulo)))
            Carticulo.click()

            registro_articulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='40041602']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_articulo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Articulo.")
            
        except Exception as e:
            Log().error("No se encontró el registro de articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cporcentajectaart = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_porcentajectaart)))
            Cporcentajectaart.send_keys(Configuracion.Iporcentajectaart)
            Log().info(" Ingresa el Porcentaje del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Porcentaje, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardactaarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_ctaarticulo)))
            Guardactaarticulo.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Cuenta Articulo.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Cuentas

        try:
            Bcuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cuentas)))
            Bcuentas.click()
            Log().info("Se hace el cambio a la pestaña Cuentas para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se dió click en el botón Cuentas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevocuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_cuentas)))
            Nuevocuentas.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Cuentas.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Validando Existencia de etiquetas

        try:
            Cuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cuentas))).text
            self.assertEqual("Cuenta", Cuentas, "Campo visible")
            Log().info(" El campo 'Cuenta' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cuenta' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Porcentajecuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_porcentajecuentas))).text
            self.assertEqual("Porcentaje", Porcentajecuentas, "Campo visible")
            Log().info(" El campo 'Porcentaje' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Porcentaje' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Ccuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuentas)))
            Ccuentas.click()
            
            registro_cuentas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100% ZACATECANA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuentas) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Cuenta.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Cuenta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cporcentajecuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_porcentajecuentas)))
            Cporcentajecuentas.send_keys(Configuracion.Iporcentajecuentas)
            Log().info(" Ingresa el Porcentaje del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Porcentaje, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardacuentas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_cuentas)))
            Guardacuentas.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Cuentas.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambia Pestaña Articulos

        try:
            Barticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_articulos)))
            Barticulos.click()
            Log().info("Se hace el cambio a la pestaña Articulos para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se dió click en el botón Articulos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_articulos)))
            Nuevoarticulo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Articulos.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Validando Existencia de Etiquetas

        try:
            Articulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_articulos))).text
            self.assertEqual("Artículo", Articulos, "Campo visible")
            Log().info(" El campo 'Artículo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Artículo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Porcentajearticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_porcentajearticulos))).text
            self.assertEqual("Porcentaje", Porcentajearticulos, "Campo visible")
            Log().info(" El campo 'Porcentaje' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Porcentaje' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresando Valores

        try:
            Carticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_articulos)))
            Carticulos.click()
            
            registro_articulos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='40041602']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_articulos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Articulo.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cporcentajearticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_porcentajearticulos)))
            Cporcentajearticulos.send_keys(Configuracion.Iporcentajearticulos)
            Log().info(" Ingresa el Porcentaje del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Porcentaje, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaarticulos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_articulos)))
            Guardaarticulos.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Articulos.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Btipodoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_tipodoc)))
            Btipodoc.click()
            Log().info("Se hace el cambio a la pestaña Tipos de Documento para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se dió click en el botón Tipo Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevotipodoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_tipodoc)))
            Nuevotipodoc.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Tipo Documento.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida la Existencia de las Etiquetas

        try:
            Tipodoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodoc))).text
            self.assertEqual("Tipo Documento", Tipodoc, "Campo visible")
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
            Origen = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_origen))).text
            self.assertEqual("Origen", Origen, "Campo visible")
            Log().info(" El campo 'Origen' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Origen' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Signo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_signo))).text
            self.assertEqual("Signo", Signo, "Campo visible")
            Log().info(" El campo 'Signo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Signo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cancelado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cancelado))).text
            self.assertEqual("Cancelado", Cancelado, "Campo visible")
            Log().info(" El campo 'Cancelado' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cancelado' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Ctipodoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodoc)))
            Ctipodoc.click()
            
            registro_tipodoc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM93']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodoc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Tipo Documento.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se encontró el registro de Tipo Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Corigen = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_origen)))
            Corigen.click()
            time.sleep(1)

            registro_origen = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='BackOffice']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_origen) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Backoffice.")
            
        except Exception as e:
            Log().error("No se dió click en la Opción Backoffice, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csigno = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_signo)))
            Csigno.click()
            
            registro_signo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Suma']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_signo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Suma.")
            
        except Exception as e:
            Log().error("No se dió click en la opción Suma, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccancelado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cancelado)))
            Ccancelado.click()
            Log().info(" Se dió click en el checkbox Cancelado.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Cancelado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardatipodoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_tipodoc)))
            Guardatipodoc.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Tipos Documento.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            time.sleep(1)
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False