from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from common.log import Log
from common.globalparam import img_path
import os
import time

class repetirregistro:

    def repetirregistro(self, conditions, Configuracion):
        """Se refresca la pantalla para crear un nuevo registro"""

        self.wait = WebDriverWait(self.driver, 60)

        # Da clic en refrescar
        try:
            Refresca = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca.click()
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
            time.sleep(2)
            
        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Da clic en nuevo

        try:
            Nuevo2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo)))
            Nuevo2.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro igual al anterior.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta

        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("MODELOS DE LIQUIDACIÓN : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            time.sleep(2)
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
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cantidaddias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cantidaddias))).text
            self.assertEqual("Cantidad de días para generación de nueva liquidación", Cantidaddias, "Campo visible")
            Log().info(" El campo 'Cantidad de días para generación de nueva liquidación' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cantidad de días para generación de nueva liquidación' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cantidadmaxima = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cantidadmaxima))).text
            self.assertEqual("Cantidad máxima de liquidaciones activas por vendedor", Cantidadmaxima, "Campo visible")
            Log().info(" El campo 'Cantidad máxima de liquidaciones activas por vendedor' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cantidad máxima de liquidaciones activas por vendedor' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Listaprecio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_listaprecio))).text
            self.assertEqual("Lista Precio valorización diferencias:", Listaprecio, "Campo visible")
            Log().info(" El campo 'Lista Precio valorización diferencias' por dif. tipo cambio' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Lista Precio valorización diferencias', validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigomodelo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigomodelo))).text
            self.assertEqual("Código del modelo de cobranza", Codigomodelo, "Campo visible")
            Log().info(" El campo 'Código del modelo de cobranza' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Código del modelo de cobranza' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Mostraradvertencias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_mostraradver))).text
            self.assertEqual("Mostrar advertencias", Mostraradvertencias, "Campo visible")
            Log().info(" El campo 'Mostrar advertencias' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Mostrar advertencias' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Requerircierre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cierreliqcargadefinitiva))).text
            self.assertEqual("Requerir cierre de liquidación en carga definitiva", Requerircierre, "Campo visible")
            Log().info(" El campo 'Requerir cierre de liquidación en carga definitiva' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Requerir cierre de liquidación en carga definitiva' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Quitardocs = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_quitardocsliqcerrada))).text
            self.assertEqual("Permitir quitar documentos de liquidación cerrada", Quitardocs, "Campo visible")
            Log().info(" El campo 'Permitir quitar documentos de liquidación cerrada' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Permitir quitar documentos de liquidación cerrada' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Inhibiroperaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_inhibiroperaciones))).text
            self.assertEqual("Inhibir operaciones sobre liquidación cerrada", Inhibiroperaciones, "Campo visible")
            Log().info(" El campo 'Inhibir operaciones sobre liquidación cerrada' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Inhibir operaciones sobre liquidación cerrada' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Pliquidacionesvacias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cierreliqvacias))).text
            self.assertEqual("Permitir cerrar liquidaciones vacias", Pliquidacionesvacias, "Campo visible")
            Log().info(" El campo 'Permitir cerrar liquidaciones vacias' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Permitir cerrar liquidaciones vacias' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Inhibircarga = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_inhibircarga))).text
            self.assertEqual("Inhibir carga si hay liquidaciones activas", Inhibircarga, "Campo visible")
            Log().info(" El campo 'Inhibir carga si hay liquidaciones activas' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Inhibir carga si hay liquidaciones activas' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Solicitarfechacierre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_solicitarfechacierre))).text
            self.assertEqual("Solicitar fecha de cierre", Solicitarfechacierre, "Campo visible")
            Log().info(" El campo 'Solicitar fecha de cierre' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Solicitar fecha de cierre' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ignorarerrores = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_ignorarerrores))).text
            self.assertEqual("Ignorar errores al descargar cheques", Ignorarerrores, "Campo visible")
            Log().info(" El campo 'Ignorar errores al descargar cheques' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Ignorar errores al descargar cheques' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Desdefecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_desdefecha))).text
            self.assertEqual("Desde Fecha", Desdefecha, "Campo visible")
            Log().info(" El campo 'Desde Fecha' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Desde Fecha' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hastafecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hastafecha))).text
            self.assertEqual("Hasta Fecha", Hastafecha, "Campo visible")
            Log().info(" El campo 'Hasta Fecha' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Hasta Fecha' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Fechavigenciaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_fechavigencia))).text
            self.assertEqual("Fecha vigencia precios", Fechavigenciaprecios, "Campo visible")
            Log().info(" El campo 'Fecha vigencia precios' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Fecha vigencia precios' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cargaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cargaprecios))).text
            self.assertEqual("Carga precios y políticas", Cargaprecios, "Campo visible")
            Log().info(" El campo 'Carga precios y políticas' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Carga precios y políticas' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hasta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hasta))).text
            self.assertEqual("hasta", Hasta, "Campo visible")
            Log().info(" El campo 'hasta' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'hasta' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            time.sleep(2)
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
            Ccantidaddias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidaddias)))
            Ccantidaddias.send_keys(Configuracion.Icantidaddias)
            Log().info(" Ingresa la cantidad de días del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad de días, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantidadmaxima = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadmaxima)))
            Ccantidadmaxima.send_keys(Configuracion.Icantidadmaxima)
            Log().info(" Ingresa la cantidad maxima del nuevo registro ")
            
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la cantidad maxima, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clistaprecio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_listaprecio)))
            Clistaprecio.click()
            
            registro_listaprecio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Lista de Precios sugeridos INTERIOR (16% IVA)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_listaprecio) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Lista Precio.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Lista Precio, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigomodelo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_codigomodelo)))
            Ccodigomodelo.click()
            
            registro_codigomodelo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Modelo Cobranza Prueba 1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_codigomodelo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Codigo Modelo.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Codigo Modelo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            MoverPantalla = self.wait.until(conditions.visibility((By.XPATH, "//div[contains(@id, 'General_tabpage')]")))
            MoverPantalla.click()
        
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se movió la pagina hacía abajo.")
            
        except Exception as e:
            Log().error("No se pudo mover la pantalla hacía abajo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmostraradver = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mostraradver)))
            time.sleep(1)
            Cmostraradver = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mostraradver)))
            Cmostraradver.click()
            Log().info(" Se dió click en el checkbox Mostrar Advertencias.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Mostrar Advertencias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccierreliqcargadef = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierreliqcargadefinitiva)))
            Ccierreliqcargadef.click()
            Log().info(" Se dió click en el checkbox Cierre Liquidacion Carga Definitiva.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Cierre Liquidacion Carga Definitiva, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cquitardocs = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_quitardocsliqcerrada)))
            Cquitardocs.click()
            Log().info(" Se dió click en el checkbox Quitar Documentos.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Quitar Documentos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cinhibiroperaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_inhibiroperaciones)))
            Cinhibiroperaciones.click()
            Log().info(" Se dió click en el checkbox Inhibir Operaciones.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Inhibir Operaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccerrarliqvacias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cierreliqvacias)))
            Ccerrarliqvacias.click()
            Log().info(" Se dió click en el checkbox Cerrar Liquidaciones Vacias.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Cerrar Liquidaciones Vacias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cinhibircarga = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_inhibircarga)))
            Cinhibircarga.click()
            Log().info(" Se dió click en el checkbox Inhibir Carga.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Inhibir Carga, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfechacierre = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_solicitarfechacierre)))
            Cfechacierre.click()
            Log().info(" Se dió click en el checkbox Solicitar Fecha Cierre.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Solicitar Fecha Cierre, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cignorarerrores = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ignorarerrores)))
            Cignorarerrores.click()
            Log().info(" Se dió click en el checkbox Ignorar Errores.")
            
        except Exception as e:
            Log().error("No se dió click en el checkbox Ignorar Errores, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdesdefecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechadesde)))
            Cdesdefecha.click()
            
            registro_desdefecha = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/div/span[18]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_desdefecha) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón Hoy para seleccionar la fecha Actual.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Desde Fecha, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chastafecha = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechahasta)))
            Chastafecha.click()
            
            registro_hastafecha = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[7]/div[2]/div/div[2]/div/span[19]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_hastafecha) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón Hoy para seleccionar la fecha Actual.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se encontró el registro de Hasta Fecha, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvigenciaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fechavigencia)))
            Cvigenciaprecios.click()
            
            registro_vigenciaprecios = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[8]/div[2]/div/div[2]/div/span[19]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_vigenciaprecios) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en el botón Hoy para seleccionar la fecha Actual.")
            
        except Exception as e:
            Log().error("No se encontró el registro de Fecha Vigencia Precios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccargapreciospoliticas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cargaprecios)))
            Ccargapreciospoliticas.click()
            
            registro_cargaprecios = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[5]/ui-combobox/div/ul/li[1]")))

            action = ActionChains(self.driver)
            action \
                .click(registro_cargaprecios) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción de Carga Precios y Politicas.")
            
        except Exception as e:
            Log().error("No se dió click en la opción de Carga precios y politicas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; No se debe crear un nuevo registro.")
            
        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.wait = WebDriverWait(self.driver, 5)
            Cierra_mensaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar)))
            self.wait = WebDriverWait(self.driver, 60)
            Cierra_mensaje.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar el mensaje de duplicidad de llave primaria")

        except (NoSuchElementException, TimeoutException) as e:
            try:
                Abrir_error = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_error)))
                Abrir_error.click()
                Log().info(" Se presiona el boton 'Cerrar', para cerrar el mensaje de duplicidad de llave primaria")

            except Exception as e:
                Log().error("v Cerrar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return False

            try:
                time.sleep(1)
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                Cierra_mensaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar)))
                Cierra_mensaje.click()
                Log().info(" Se presiona el boton 'Cerrar', para cerrar el mensaje de duplicidad de llave primaria")

            except Exception as e:
                Log().error("v Cerrar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return False

        except Exception as e:
            Log().error("v Cerrar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_ventana)))
            Cierra_ventana.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana")
            
        except Exception as e:
            Log().error("No se dió click en el botón Cerrar de la ventana., validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False