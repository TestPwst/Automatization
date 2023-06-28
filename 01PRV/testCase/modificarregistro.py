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
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2021103']")))

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
            Crazonsocial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_razonsocial)))
            Crazonsocial.clear()
            Crazonsocial.send_keys(Configuracion.Mrazonsocial)
            Log().info(" Se modifica el contenido del campo Razon Social ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Razón Social, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para ingresar el Nom negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calle)))
            Ccalle.clear()
            Ccalle.send_keys(Configuracion.Mcalle)
            Log().info(" Se modifica el contenido del campo Calle ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la calle, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.clear()
            Cesquina1.send_keys(Configuracion.Mesquina1)
            Log().info(" Se modifica el contenido del campo Esquina 1 ")

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
            Cesquina2.clear()
            Cesquina2.send_keys(Configuracion.Mesquina2)
            Log().info(" Se modifica el contenido del campo Esquina 2 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnumpuerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nropuerta)))
            Cnumpuerta.clear()
            Cnumpuerta.send_keys(Configuracion.Mnropuerta)
            Log().info(" Se modifica el contenido del campo Num Puesrta ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Num de la puerta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1)))
            Ctelefono1.clear()
            Ctelefono1.send_keys(Configuracion.Mtelefono1)
            Log().info(" Se modifica el contenido del campo Telefono 1 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el telefono 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2)))
            Ctelefono2.clear()
            Ctelefono2.send_keys(Configuracion.Mtelefono2)
            Log().info(" Se modifica el contenido del campo Telefono 2 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el telefono 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigopostal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigopostal)))
            Ccodigopostal.clear()
            Ccodigopostal.send_keys(Configuracion.Mcodigopostal)
            Log().info(" Se modifica el contenido del campo Codigo Postal ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Codigo Postal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccorreoelec = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_correoelectronico)))
            Ccorreoelec.clear()
            Ccorreoelec.send_keys(Configuracion.Mcorreoelec)
            Log().info(" Se modifica el contenido del campo Correo Electronico ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Correo Electrónico, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clistaprecio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_listaprecio)))
            Clistaprecio.click()

            registro_listaprecio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Lista de Precios SCRP2.0 INTERIOR (16% IVA)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_listaprecio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Lista Precio ")

        except Exception as e:
            Log().error("No se encontró el registro de Lista Precio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cestado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estado)))
            Cestado.click()

            registro_estado = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='15']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estado) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de estado ")

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

            registro_deptoprovi = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ACOLMAN']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deptoprovi) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de depto/provi ")

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

            registro_localidad = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SAN BARTOLO ACOLMAN']")))

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
            Cbarrios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barrio)))
            Cbarrios.click()

            registro_barrio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SAN BARTOLO ACOLMAN']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_barrio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Barrios ")

        except Exception as e:
            Log().error("No se encontró el registro de Barrios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuesto)))
            Cimpuesto.click()

            registro_impuesto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IVA 16%']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuesto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Impuesto ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de Impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Sucursales

        try:
            Bsucursales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_sucursales)))
            Bsucursales.click()
            Log().info("Se hace el cambio a la pestaña sucursales para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón sucursales, revise si el xpath sigue siendo el mismovalidar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registrosucursales = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrosucursales) \
                .pause(0) \
                .double_click(Registrosucursales) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Sucursales creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se dió click en el registro de Sucursales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cerrar Pestaña Sucursales

        try:
            Bcerrarpestana = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrarsucursal)))
            Bcerrarpestana.click()
            Log().info("Se cerró la pestaña Sucursales para continuar con la modificación")

        except Exception as e:
            Log().error("No se encontró el botón para cerrar la pestaña de sucursales, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Cuentas Contables

        try:
            Bctascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cuentascontables)))
            Bctascontables.click()
            time.sleep(1)
            Bctascontables.click()
            Log().info("Se hace el cambio de pestaña Cuentas Contables para continuar con la modificación del registro")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Cuentas Contables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registroctascontables = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroctascontables) \
                .pause(0) \
                .double_click(Registroctascontables) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Cuentas Contables creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Cuentas Contables, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modificar Registros

        try:
            Ctipodoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocumento)))
            Ctipodoc.click()

            registro_tipodoc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM17']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodoc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Tipo de Documento ")

        except Exception as e:
            Log().error("No se encontró el registro de Tipo de Documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cctacontable = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_ctacontable)))
            Cctacontable.click()

            registro_ctacont = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba cambio']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctacont) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Cuenta Contable ")

        except Exception as e:
            Log().error("No se encontró el registro de Cuenta Contable, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccentroscosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_centrocosto)))
            Ccentroscosto.click()

            registro_centrocosto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba cambio']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_centrocosto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Centro Costo ")

        except Exception as e:
            Log().error("No se encontró el registro de Centro Costo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardactascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_ctascontables)))
            Guardactascontables.click()
            Log().info(" Se da clic en el boton Aceptar; se debe modificar el registro de Cuentas Contables.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitude")
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
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False