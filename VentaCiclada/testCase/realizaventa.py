from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class ventaciclada:

    def ventaciclada(self):
        """Ingresa al documento para realizar la venta"""
        self.wait = WebDriverWait(self.driver, 150)

        #Ingresa a Venta de Contado

        try:

            Documentos = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_documentos']")))

            action = ActionChains(self.driver)
            action \
                .click(Documentos) \
                .pause(0) \
                .release()
            action.perform()

            Clientes = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_doc_cli']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Clientes) \
                .pause(0) \
                .release()
            action.perform()

            MasDocs = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='doc_clientes_more']")))

            action = ActionChains(self.driver)
            action \
                .click(MasDocs) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Abre el menú para visualizar mas documentos")

        except Exception as e:
            Log().error("No se pudo ingresar al menu indicado, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            raise

        Registro = self.wait.until(conditions.visibility((By.XPATH, "//*[text()='Venta Contado    (PM03)']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(0) \
                .double_click(Registro) \
                .pause(0) \
                .release()
            action.perform()
            Log().info("Se abre el documento de venta de contado a realizar")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el el registro deseado, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        #Ingresa el cliente y los artículos a comprar.
        for i in range(30):

            try:
                Ccliente = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cliente)))
                Ccliente.send_keys(Configuracion.Icuenta)
                time.sleep(5)
                Ccampo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ob)))
                Ccampo.click()
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo cuenta, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Bagregar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_add_art)))
                Bagregar.click()
                time.sleep(5)

            except Exception as e:
                Log().error("No se pudo click al botón agregar artículos, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            # Se agregan los artículos a la venta
            try:
                Cart1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_art)))
                Cart1.send_keys(Configuracion.Iarticulo1)
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo artículo 1, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Cnumserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_numserie)))
                Cnumserie.click()
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo numero de serie, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Ccant = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cant)))
                Ccant.send_keys(Configuracion.Icantidad)
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo cantidad, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Aceptar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar_art)))
                Aceptar.click()
                time.sleep(5)

            except Exception as e:
                Log().error("No se pudo dar click al botón de aceptar, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Cart2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_art)))
                Cart2.send_keys(Configuracion.Iarticulo2)
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo artículo 2, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Cnumserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_numserie)))
                Cnumserie.click()
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo numero de serie, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Ccant = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cant)))
                Ccant.send_keys(Configuracion.Icantidad)
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo cantidad, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Aceptar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar_art)))
                Aceptar.click()
                Log().info("Se agrega el artículo facturado por packing a la venta")
                time.sleep(5)

            except Exception as e:
                Log().error("No se pudo dar click al botón de aceptar, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Cart3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_art)))
                Cart3.send_keys(Configuracion.Iarticulo3)
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo artículo 3, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Cnumserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_numserie)))
                Cnumserie.click()
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo numero de serie, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Ccant = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cant)))
                Ccant.send_keys(Configuracion.Icantidad)
                time.sleep(3)

            except Exception as e:
                Log().error("No se pudo ingresar el campo cantidad, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                Aceptar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptar_art)))
                Aceptar.click()
                time.sleep(5)

            except Exception as e:
                Log().error("No se pudo dar click al botón de aceptar, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            #Cierra el agregado de artículos
            try:
                Cancelar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_art)))
                Cancelar.click()
                time.sleep(5)

            except Exception as e:
                Log().error("No se pudo dar click al botón de Cancelar, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise

            try:
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
                Guarda.click()
                Log().info("Se guarda la venta realizaada")
                time.sleep(8)

            except Exception as e:
                Log().error("No se dar click al botón Guardar, validar que la acción anterior haya finalizado,"
                            "que el xpath sea el correcto o que la página no presente lentitud")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(2)
                self.driver.close()
                raise
