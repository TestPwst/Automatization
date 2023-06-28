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

        self.wait = WebDriverWait(self.driver, 20)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='840011']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='840011']")))
    
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
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
            Log().info(" Se modifica el contenido del campo Codigo Alternativo")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripcion")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipodocumento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipodocumento)))
            Ctipodocumento.clear()
            Ctipodocumento.send_keys(Configuracion.Mtipodoc)
            Log().info(" Se modifica el contenido del campo Tipo Documento ")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el tipo de documento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Capliglobal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_apliglobal)))
            Capliglobal.click()
            Log().info(" Se dió click en el checkbox Aplicación Global.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Aplicación Global, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y modificar

        try:
            Bporarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_porarticulo)))
            Bporarticulo.click()
            Log().info("Se hace el cambio a la pestaña Por Articulo para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Por Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registroporarticulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MARLBORO LS BOX 20 (FA01001)']")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroporarticulo) \
                .pause(0) \
                .double_click(Registroporarticulo) \
                .pause(0) \
                .release()
            action.perform()
            
            Log().info(" Se da clic en el registro de Por Articulo, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Por Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica Valores

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articulo)))
            Carticulo.clear()
            Carticulo.send_keys(Configuracion.Iarticulo)
            Log().info(" Se modifica el contenido del campo Articulo ")

        except Exception as e:
            Log().error("No se encontró el campo para modificar el Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticuloabonificar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_articuloabonificar)))
            Carticuloabonificar.clear()
            Carticuloabonificar.send_keys(Configuracion.Marticuloabonif)
            Log().info(" Se modifica el contenido del campo Articulo a Bonificar ")

        except Exception as e:
            Log().error("No se encontró el campo para modificar el Articulo a Bonificar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantidadabonif = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadabonificar)))
            Ccantidadabonif.clear()
            Ccantidadabonif.send_keys(Configuracion.Mcantidadabonificar)
            Log().info(" Se modifica el contenido del campo Cantidad a Bonificar ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Cantidad a Bonificar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccantidadenbonificacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadenbonificacion)))
            Ccantidadenbonificacion.clear()
            Ccantidadenbonificacion.send_keys(Configuracion.Mcantidadenbonificacion)
            Log().info(" Se modifica el contenido del campo Cantidad en Bonificación ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Cantidad en Bonificacion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarporarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_porarticulo)))
            Guardarporarticulo.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar la modificación del registro de Por Articulo.")
            time.sleep(1)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False