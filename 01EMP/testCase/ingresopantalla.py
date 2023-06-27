from importlib.machinery import SourceFileLoader
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.log import Log
from common.globalparam import img_path
import os
from selenium.webdriver import ActionChains
import time

buscador = SourceFileLoader("buscador", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/buscador.py").load_module()
Buscador = buscador.buscador


class ingresopantalla:

    def ingresopantalla(self, conditions, Configuracion):
        self.wait = WebDriverWait(self.driver, 60)

        # Selecciona el menu
        try:
            Tablas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas']")))

            action = ActionChains(self.driver)
            action \
                .click(Tablas) \
                .pause(0) \
                .release()
            action.perform()

            Empresas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas_emp']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Empresas) \
                .pause(0) \
                .release()
            action.perform()

            Empresa = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='empresas']")))

            action = ActionChains(self.driver)
            action \
                .click(Empresa) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Abre la pantalla de Empresas")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        """Abre pantalla de listado de registros."""
        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("EMPRESAS", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Empresas")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Condicion si el registro existe

        try:
            Registrorepetido = self.driver.find_element(By.XPATH, "//span[text()='2021']")
            if Registrorepetido.is_displayed():
                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido) \
                        .pause(0) \
                        .double_click(Registrorepetido) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Stock de Mercaderías
                try:
                    Bresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_resolfiscales)))
                    Bresolfiscales.click()
                    Log().info("Se hace el cambio a la pestaña Resoluciones Fiscales para continuar con la eliminación del registro")

                except Exception as e:
                    Log().error("No se dió click en el botón Resolución Fiscales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Registroresolficales = self.driver.find_element(By.XPATH, "//span[text()='21302024']")
                    if Registroresolficales.is_displayed():
                        try:
                            action = ActionChains(self.driver)
                            action \
                                .move_to_element(Registroresolficales) \
                                .pause(0) \
                                .click(Registroresolficales) \
                                .pause(0) \
                                .release()
                            action.perform()
                            Log().info("Se da clic en el registro en el Registro de Resoluciones Fiscales, para proceder a modificarlo.")

                        except Exception as e:
                            Log().error("No se encontró el registro de Resoluciones Fiscales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                            time.sleep(3)
                            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                            self.driver.get_screenshot_as_file(img_name)
                            return False

                        try:
                            Eliminaresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_resolfiscales)))
                            Eliminaresolfiscales.click()
                            Log().info("Se presiona el boton 'Eliminar', para eliminar el registro de Resoluciones Fiscales.")

                        except Exception as e:
                            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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

                except NoSuchElementException:
                    pass

                Registro4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2021']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro4) \
                        .pause(0) \
                        .double_click(Registro4) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Series

                try:
                    Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
                    Bseries.click()
                    Log().info("Se hace el cambio a la pestaña Series para continuar con la eliminación del registro")

                except Exception as e:
                    Log().error("No se dió click en el botón Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registroseries = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='20']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registroseries) \
                        .pause(0) \
                        .double_click(Registroseries) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da doble click en el registro de series, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Configuración Vías

                try:
                    Bconfigvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_configvias)))
                    Bconfigvias.click()
                    Log().info("Se hace el cambio a la pestaña Coniguración Vias para continuar con la eliminación del registro")

                except Exception as e:
                    Log().error("No se dió click en el botón Configuracion de Vias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrovias = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM03']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrovias) \
                        .pause(0) \
                        .click(Registrovias) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de Configuración Vías, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de Configuración Vías, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminavias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_via)))
                    Eliminavias.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Configuración Vías.")

                except Exception as e:
                    Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guardaserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_series)))
                    Guardaserie.click()
                    Log().info("Se da clic en el boton Guardar; se debe modificar la informacion del registro Series.")
                    time.sleep(2)

                except Exception as e:
                    Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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

                Registro5 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2021']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro5) \
                        .pause(0) \
                        .double_click(Registro5) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Series

                try:
                    Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
                    Bseries.click()
                    Log().info("Se hace el cambio a la pestaña Series para continuar con la eliminación del registro")

                except Exception as e:
                    Log().error("No se dió click en el botón Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registroseries = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='20']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registroseries) \
                        .pause(0) \
                        .click(Registroseries) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro series, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminaseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_serie)))
                    Eliminaseries.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Series.")

                except Exception as e:
                    Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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

                Registro6 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='2021']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro6) \
                        .pause(0) \
                        .click(Registro6) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina)))
                    Elimina.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

                except Exception as e:
                    Log().error("No se dio click al botón Eliminar, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Confirma_Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_acepta_eliminar)))
                    Confirma_Elimina.click()
                    Log().info(" Se confirma el eliminado del registro")

                except Exception as e:
                    Log().error("No se dio click el botón Aceptar, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Refresca4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
                    Refresca4.click()
                    Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
                    time.sleep(2)

                except Exception as e:
                    Log().error(
                        "No se dio click el botón Refrescar, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

        except NoSuchElementException:
            pass

        # Da clic en nuevo
        try:
            Nuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo)))
            Nuevo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
