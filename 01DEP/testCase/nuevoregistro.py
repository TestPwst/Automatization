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
            self.assertEqual("DEPÓSITOS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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
            Ccodigogln = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_gln)))
            Ccodigogln.send_keys(Configuracion.Icodigogln)
            Log().info(" Ingresa el codigo GLN del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo GLN, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ccalle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calle)))
            Ccalle.send_keys(Configuracion.Icalle)
            Log().info(" Ingresa la calle del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la calle, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnumpuerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nropuerta)))
            Cnumpuerta.send_keys(Configuracion.Inropuerta)
            Log().info(" Ingresa el Num de la puerta del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Num de la puerta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.send_keys(Configuracion.Iesquina1)
            Log().info(" Ingresa la esquina 1 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2)))
            Cesquina2.send_keys(Configuracion.Iesquina2)
            Log().info(" Ingresa la esquina 2 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccapacidadm3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_capacidad)))
            Ccapacidadm3.send_keys(Configuracion.Icapacidad)
            Log().info(" Ingresa la Capacidad M3 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Capacidad M3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cobservacion1D = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observacion1d)))
            Cobservacion1D.send_keys(Configuracion.Iobservacion1d)
            Log().info(" Ingresa la observacion 1D del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Observacion 1D, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cobservacion2D = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observacion2d)))
            Cobservacion2D.send_keys(Configuracion.Iobservacion2d)
            Log().info(" Ingresa la Observacion 2D del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Observacion 2D, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclasificacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_clasificacion)))
            Cclasificacion.click()

            registro_clasificacion = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Producto en buen estado                                                                             ']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_clasificacion) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Clasifiación.")

        except Exception as e:
            Log().error("No se encontró el registro de Clasifiación, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info(" Se dió doble click en el registro de Distribuidor.")

        except Exception as e:
            Log().error("No se encontró el registro de Distribuidor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdepositoprincipal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_depositoprincipal)))
            Cdepositoprincipal.click()

            registro_depprincipal = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div[9]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_depprincipal) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Deposito Principal.")

        except Exception as e:
            Log().error("No se encontró el registro de Deposito Principal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cagencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_agencia)))
            Cagencia.click()

            registro_agencia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_agencia) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Agencia.")

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

            registro_oficina = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_oficina) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Oficina.")

        except Exception as e:
            Log().error("No se encontró el registro de Oficina, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdepositocentral = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_depositocentral)))
            Cdepositocentral.click()
            Log().info(" Se dió click en el checkbox Deposito Central.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox Deposito Central, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Stock de Mercaderías

        try:
            Bstockmercaderias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_stockmercaderia)))
            Bstockmercaderias.click()
            Log().info("Se hace el cambio a la pestaña Stock de Mercaderias para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón stock mercaderias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevostock = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_stockmercaderia)))
            Nuevostock.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Stock Mercaderias.")

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
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cstockmin = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_stockmin)))
            Cstockmin.send_keys(Configuracion.Istockmin)
            Log().info(" Ingresa el Stock Minimo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Stock Minimo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cstockdes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_stockdes)))
            Cstockdes.send_keys(Configuracion.Istockdes)
            Log().info(" Ingresa el Stock Deseado del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Stock Deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardarStockMerca = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_stockmercaderia)))
            GuardarStockMerca.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro Stock Mercaderias.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
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
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevocuentascont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_CuentasCont)))
            Nuevocuentascont.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Cuentas Contables.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
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
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CCtaCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_ctacont)))
            CCtaCont.click()

            registro_ctacont = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctacont) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Cuentas Contables.")

        except Exception as e:
            Log().error("No se encontró el registro de cuenta contable, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CCentroCosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_centrocosto)))
            CCentroCosto.click()

            registro_ctrcosto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctrcosto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Centro Costo.")

        except Exception as e:
            Log().error("No se encontró el registro de centro costo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
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
            Log().error("No se dipo click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
