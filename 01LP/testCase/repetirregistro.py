from selenium.webdriver import ActionChains
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
            Log().error("No se dipo click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta

        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("LISTA DE PRECIOS : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
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
            CodigoAlter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo_alter))).text
            self.assertEqual("Código Alternativo", CodigoAlter, "Campo visible")
            Log().info(" El campo 'Codigo Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Codigo Alternativo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Descuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descuento))).text
            self.assertEqual("Descuento(%)", Descuento, "Campo visible")
            Log().info(" El campo 'Descuento' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Descuento' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Recargo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_recargo))).text
            self.assertEqual("Recargo(%)", Recargo, "Campo visible")
            Log().info(" El campo 'Recargo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Recargo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Moneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_moneda))).text
            self.assertEqual("Moneda", Moneda, "Campo visible")
            Log().info(" El campo 'Moneda' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Moneda' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            time.sleep(2)
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
            Cdescuento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descuento)))
            Cdescuento.send_keys(Configuracion.Idescuento)
            Log().info(" Ingresa el descuento del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descuento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Crecargo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_recargo)))
            Crecargo.send_keys(Configuracion.Irecargo)
            Log().info(" Ingresa el recargo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la recargo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

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
            Log().error("No se encontró el registro de Moneda, rvalidar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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