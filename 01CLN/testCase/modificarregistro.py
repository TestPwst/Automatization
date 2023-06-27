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

        # Ingresa datos filtro

        try:
            Ccodclientefiltro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codcliente)))
            Ccodclientefiltro.clear()
            Ccodclientefiltro.send_keys(Configuracion.Ifiltro)
            Log().info(" Ingresa el codigo cliente en el filtro del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo cliente en el filtro, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            time.sleep(2)
            Refresca2.click()
            time.sleep(2)
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")

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
            Log().error("No se pudo encontrar el campo para modificar la Razón Social, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para modificar la calle, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para modificar la esquina 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para modificar la esquina 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info(" Se modifica el contenido del campo Num Puerta ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el Num de la puerta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para modificar la Codigo Postal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info(" Se modifica el contenido del campo telefono 1 ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el telefono 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para modificar el telefono 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo encontrar el campo para Modificar el Nom negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cperfilcredito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_perfilcredito)))
            Cperfilcredito.click()

            registro_perfilcredito = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='4151']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_perfilcredito) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de perfil credito ")

        except Exception as e:
            Log().error("No se encontró el registro de Perfil Credito, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se encontró el registro de Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
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
            Ccolonia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_colonia)))
            Ccolonia.clear()
            Ccolonia.send_keys(Configuracion.Mcolonia)
            Log().info(" Se modifica el contenido del campo Colonia ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la colonia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccoordenadasx = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_coordenadasx)))
            Ccoordenadasx.clear()
            Ccoordenadasx.send_keys(Configuracion.Mcoordenadasx)
            Log().info(" Se modifica el contenido del campo Coordenadas X ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las coordenadas x, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccoordenadasy = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_coordenadasy)))
            Ccoordenadasy.clear()
            Ccoordenadasy.send_keys(Configuracion.Mcoordenadasy)
            Log().info(" Se modifica el contenido del campo Coordenadas Y ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar las coordenadas y, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().info("Se hace el cambio de pestaña sucursales para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón sucursales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registrosucursales = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[4]/ui-container/ui-row/span/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrosucursales) \
                .pause(0) \
                .double_click(Registrosucursales) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de sucursales, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña sucursales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores Sucursales

        try:
            Cnomnegociosuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nomnegociosuc)))
            Cnomnegociosuc.send_keys(Configuracion.Inomnegociosuc)
            Log().info(" Se modifica el contenido del campo Nom Negocio ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el Nom negocio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Crazonsocialsuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_razonsocialsuc)))
            Crazonsocialsuc.send_keys(Configuracion.Irazonsocialsuc)
            Log().info(" Se modifica el contenido del campo Razon Social ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Razón Social, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccallesuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_callesuc)))
            Ccallesuc.send_keys(Configuracion.Icallesuc)
            Log().info(" Se modifica el contenido del campo Calle ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la calle, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clistapreciosuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_listapreciosuc)))
            Clistapreciosuc.click()

            registro_listapreciosuc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Lista de Precios SCRP2.0 INTERIOR (16% IVA)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_listapreciosuc) \
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
            Cestadosuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_estadosuc)))
            Cestadosuc.click()

            registro_estadosuc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='15']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_estadosuc) \
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
            Cmunicipiosuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_municipiosuc)))
            Cmunicipiosuc.click()

            registro_municipiosuc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='9']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_municipiosuc) \
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
            Clocalidadsuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_localidadsuc)))
            Clocalidadsuc.click()

            registro_localidadsuc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidadsuc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Localidad ")

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbarriossuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_barriosuc)))
            Cbarriossuc.click()

            registro_localidadsuc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='AMECAMECA DE JUAREZ']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_localidadsuc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Localidad ")

        except Exception as e:
            Log().error("No se encontró el registro de Localidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccoloniasuc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_coloniasuc)))
            Ccoloniasuc.clear()
            Ccoloniasuc.send_keys(Configuracion.Mcoloniasuc)
            Log().info(" Se modifica el contenido del campo colonia ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la colonia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarsucursales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_sucursal)))
            Guardarsucursales.click()
            time.sleep(1)
            Log().info(" Se presiona el boton 'Aceptar', para guardar la modificación del registro de sucursales.")

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
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False