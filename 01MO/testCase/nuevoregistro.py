from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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
            self.assertEqual("MONEDAS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
            Log().error("El campo 'Codigo' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
            Log().error("El campo 'Descripción' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Simbolo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_simbolo))).text
            self.assertEqual("Símbolo", Simbolo, "Campo visible")
            Log().info(" El campo 'Símbolo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Símbolo' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            SimboloISO = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_simiso))).text
            self.assertEqual("Símbolo ISO", SimboloISO, "Campo visible")
            Log().info(" El campo 'Simbolo ISO' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Símbolo ISO' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
            Log().error("No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CSimbolo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_simbolo)))
            CSimbolo.send_keys(Configuracion.Isimbolo)
            Log().info(" Ingresa el símbolo del nuevo registro ")
        
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el símbolo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CSimboloISO = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_simiso)))
            CSimboloISO.send_keys(Configuracion.IsimboloISO)
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Log().info(" Ingresa el símbolo ISO del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el símbolo ISO, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Cambia de pestaña y continua la creación del registro

        try:
            Cotizacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cotizacion)))
            Cotizacion.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se encontró el botón Cotizaciones, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_nuevocot)))
            Nuevo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Valida la existencia de las etiquetas

        try:
            Fecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_fecha))).text
            self.assertEqual("Fecha", Fecha, "Campo visible")
            Log().info(" El campo 'Fecha' si se encuentra visible en la pestaña sub canal.")

        except Exception as e:
            Log().error("El campo 'Fecha' no se muestra visible en la pestaña sub canal, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cambio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cambio))).text
            self.assertEqual("Cambio", Cambio, "Campo visible")
            Log().info(" El campo 'Cambio' si se encuentra visible en la pestaña sub canal.")

        except Exception as e:
            Log().error("El campo 'Cambio' no se muestra visible en la pestaña sub canal, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Venta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_venta))).text
            self.assertEqual("Venta", Venta, "Campo visible")
            Log().info(" El campo 'Venta' si se encuentra visible en la pestaña sub canal.")

        except Exception as e:
            Log().error("El campo 'Venta' no se muestra visible en la pestaña sub canal, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Compra = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_compra))).text
            self.assertEqual("Compra", Compra, "Campo visible")
            Log().info(" El campo 'Compra' si se encuentra visible en la pestaña sub canal.")

        except Exception as e:
            Log().error("El campo 'Compra' no se muestra visible en la pestaña sub canal, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Fiscal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_fiscal))).text
            self.assertEqual("Fiscal", Fiscal, "Campo visible")
            Log().info(" El campo 'Fiscal' si se encuentra visible en la pestaña sub canal.")

        except Exception as e:
            Log().error("El campo 'Fiscal' no se muestra visible en la pestaña sub canal, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Agrega los datos a los campos correspondientes

        try:
            Ccambio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cambio)))
            Ccambio.send_keys(Configuracion.Icambio)
            Log().info(" Ingresa el cambio del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el cambio, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cventa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_venta)))
            Cventa.send_keys(Configuracion.Iventa)
            Log().info(" Ingresa la venta del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la venta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccompra = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_compra)))
            Ccompra.send_keys(Configuracion.Icompra)
            Log().info(" Ingresa la compra del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la compra, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfiscal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_fiscal)))
            Cfiscal.send_keys(Configuracion.Ifiscal)
            Log().info(" Ingresa fiscal del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el fiscal, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda2)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
        
        except Exception as e:
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Cambia de pestaña y continua la creación del registro

        try:
            Bcuentascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ctacont)))
            Bcuentascontables.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error("No se encontró el botón cuentas contables, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_nuevoctacont)))
            Nuevo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Valida la existencia de las etiquetas

        try:
            TipoDoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodoc))).text
            self.assertEqual("Tipo Documento", TipoDoc, "Campo visible")
            Log().info(" El campo 'Tipo Documento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tipo Documento' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CuentaCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cuentacont))).text
            self.assertEqual("Cuenta Contable", CuentaCont, "Campo visible")
            Log().info(" El campo 'Cuenta Contable' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cuenta Contable' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CentroCosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_centrocosto))).text
            self.assertEqual("Centro Costo", CentroCosto, "Campo visible")
            Log().info(" El campo 'Centro Costo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Centro Costo' no se muestra visible, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #ingresar los valores

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

        except Exception as e:
            Log().error("No se encontró el registro de tipo de documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CCtaCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_ctacont)))
            CCtaCont.click()

            registro_ctacont = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctacont) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de cuenta contable, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CCentroCosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_centrocosto)))
            CCentroCosto.click()
            
            registro_centrocosto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='prueba']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_centrocosto) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de centro costo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardarCtasCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptactacont)))
            GuardarCtasCont.click()
            Log().info(" Se presiona el boton 'Aceptar', para guardar el registro.")

        except Exception as e:
            Log().error("No se encontró el botón Aceptar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False