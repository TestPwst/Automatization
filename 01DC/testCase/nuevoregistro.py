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
            self.assertEqual("DESTINO CHEQUES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo ingresar el campo codigo, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se pudo ingresar el descripcion, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CMliquidacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mliquidacion)))
            CMliquidacion.click()

            registro_mliquidacion = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Debita']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_mliquidacion) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Modo Afectación, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cadeudado = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_adeudado)))
            Cadeudado.click()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Log().info(" Hizo click en el checkbox ")

        except Exception as e:
            Log().error("No se pudo ingresar el campo adeudado, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y agregar nuevo

        try:
            Bdestinos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_destinos)))
            Bdestinos.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se encontró el botón destinos, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevo2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_destinos)))
            Nuevo2.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dio click al botón Nuevo, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Cdestino = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_destinos)))
            Cdestino.click()

            registro_destino = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div[1]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_destino) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de Destino, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardarDestino = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_destinos)))
            GuardarDestino.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")

        except Exception as e:
            Log().error("No se dio click al botón Guardar, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            Log().error("No se dio click al botón Guardar, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
