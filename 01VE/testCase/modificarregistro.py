from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
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
            Log().error(
                "No se dió click al botón Refrescar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ZI20']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ZI20']")))

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
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalter)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigousuario)))
            Ccodigousuario.clear()
            Ccodigousuario.send_keys(Configuracion.Mcodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo usuario, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnomnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nomnegocio)))
            Cnomnegocio.clear()
            Cnomnegocio.send_keys(Configuracion.Mnomnegocio)
            Log().info(" Ingresa el Nom Negocio del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Nom Negocio, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdocidentidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_docidentidad)))
            Cdocidentidad.clear()
            Cdocidentidad.send_keys(Configuracion.Mdocidentidad)
            Log().info(" Ingresa el Documento de Identidad del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Documento de Identidad, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calle)))
            Ccalle.clear()
            Ccalle.send_keys(Configuracion.Mcalle)
            Log().info(" Ingresa la calle del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la calle, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnropuerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nropuerta)))
            Cnropuerta.clear()
            Cnropuerta.send_keys(Configuracion.Mnropuerta)
            Log().info(" Ingresa el nro puerta del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el nro puerta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.clear()
            Cesquina1.send_keys(Configuracion.Mesquina1)
            Log().info(" Ingresa la Esquina 1 del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la Esquina 1, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2)))
            Cesquina2.clear()
            Cesquina2.send_keys(Configuracion.Mesquina2)
            Log().info(" Ingresa la Esquina 2 del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la Esquina 2, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1)))
            Ctelefono1.clear()
            Ctelefono1.send_keys(Configuracion.Mtelefono1)
            Log().info(" Ingresa el Telefono 1 del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 1, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2)))
            Ctelefono2.clear()
            Ctelefono2.send_keys(Configuracion.Mtelefono2)
            Log().info(" Ingresa el Telefono 2 del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 2, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cempresabase = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_empresabase)))
            Cempresabase.click()
            
            registro_empresabase = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='59']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_empresabase) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Empresa Base, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Ccuenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuenta)))
            Ccuenta.click()

            registro_cuenta = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='0010409091']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuenta) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Cuenta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdistribuidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_distribuidor)))
            Cdistribuidor.click()

            registro_distribuidor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Codigo1234']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_distribuidor) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Distribuidor, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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

        except Exception as e:
            Log().error(
                "No se encontró o no existe el registro deseado de Agencia, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Coficina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_oficina)))
            Coficina.click()

            registro_oficina = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_oficina) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Oficina, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Cdeposito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deposito)))
            Cdeposito.click()

            registro_deposito = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='4198']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deposito) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Deposito, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloliq = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloliq)))
            Cmodeloliq.click()

            registro_modeloliq = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloliq) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Modelo Liquidación, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cperfilmovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_perfilmovil)))
            Cperfilmovil.click()

            registro_perfilmovil = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_perfilmovil) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Perfil Movil, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipovendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipovendedor)))
            Ctipovendedor.click()

            registro_tipovendedor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM03']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipovendedor) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Tipo Vendedor, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cusuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_usuario)))
            Cusuario.click()

            registro_usuario = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='mabvvv003']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_usuario) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Usuario, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Cplatmovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_platmovil)))
            Cplatmovil.click()

            registro_platmovil = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ANDROID']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_platmovil) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Plataforma Movil, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_platmovil)))
            Moverpantalla.click()

            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se pudo mover la pantalla, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cformulapedido = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_formulapedido)))
            time.sleep(1)
            Cformulapedido = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_formulapedido)))
            Cformulapedido.click()

            registro_formulapedido = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='No Aplicar']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_formulapedido) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Formula Pedido, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chabilitarencuestas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_habilitarencuestas)))
            Chabilitarencuestas.click()
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Habilitar Encuestas, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Series

        try:
            Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
            Bseries.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
        
        except Exception as e:
            Log().error(
                "No se dió click al botón Series, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registroseries = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroseries) \
                .pause(0) \
                .click(Registroseries) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_series)))
            Eliminaseries.click()
            Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

        except Exception as e:
            Log().error("No se dió click al botón Eliminar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_series)))
            Nuevoserie.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Cserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_serie)))
            Cserie.click()

            registro_serie = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Mabezihua RUTA 02 (02)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_serie) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Serie, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoimpresora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipoimpresora)))
            Ctipoimpresora.click()

            registro_tipoimpresora = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Serial']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoimpresora) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Tipo Impresora, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpuertoimpresora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_puertoimpresora)))
            Cpuertoimpresora.click()

            registro_puertoimpresora = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='B']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_puertoimpresora) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Puerto Impresora, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpreslenguaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_impreslenguaje)))
            Cimpreslenguaje.click()

            registro_impreslenguaje = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Sewoo CPCL LK-P41']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_impreslenguaje) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Impresora Lenguaje, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclavecorr = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clavecorr)))
            Cclavecorr.clear()
            Cclavecorr.send_keys(Configuracion.Mclavecorr)
            Log().info(" Ingresa la Clave Correlativo del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la Clave Correlativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdesdenumero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_desdenumero)))
            Cdesdenumero.clear()
            Cdesdenumero.send_keys(Configuracion.Mdesdenumero)
            Log().info(" Ingresa Desde Numero del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar Desde Numero, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chastanumero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hastanumero)))
            Chastanumero.clear()
            Chastanumero.send_keys(Configuracion.Mhastanumero)
            Log().info(" Ingresa Hasta Numero del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar Hasta Numero, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_serie)))
            Guardarserie.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Documentos

        try:
            Bdocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_documentos)))
            Bdocumentos.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error(
                "No se dió click al botón Documentos, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registrodocumentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Ticket Intermec para Factura']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrodocumentos) \
                .pause(0) \
                .double_click(Registrodocumentos) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica Valores

        try:
            Cmodeloimpresion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimpresion)))
            Cmodeloimpresion.click()

            registro_modeloimpresion = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 1885622']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloimpresion) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Modelo de Impresión, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardardocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_documento)))
            Guardardocumentos.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña documentos reparto

        try:
            Bdocreparto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_documentoreparto)))
            Bdocreparto.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Documentos Reparto, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registrodocreparto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Ticket Intermec para Factura']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrodocreparto) \
                .pause(0) \
                .double_click(Registrodocreparto) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloimpresion2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimpresion2)))
            Cmodeloimpresion2.click()

            registro_modeloimpresion2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 1885622']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloimpresion2) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Modelo de Impresión, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Guardartipodocumento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_documentoreparto)))
            time.sleep(1)
            Guardartipodocumento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_documentoreparto)))
            Guardartipodocumento2.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            time.sleep(1)
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            
        except Exception as e:
            Log().error("No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False