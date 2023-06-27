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

            Articulo = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas_articulo']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Articulo) \
                .pause(0) \
                .release()
            action.perform()

            ArqProducto = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='arqprod01']")))

            action = ActionChains(self.driver)
            action \
                .click(ArqProducto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Abre la pantalla de Arquitectura de Productos")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        """Abre pantalla de listado de registros."""

        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("ARQUITECTURA DE PRODUCTO", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Clasificación de Artículo.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Condicion si el registro existe

        try:
            Registrorepetido = self.driver.find_element(By.XPATH, "//span[text()='Test1']")
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
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Bmarcas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_marcas)))
                    Bmarcas.click()
                    Log().info("Se hace el cambio a la pestaña marcas para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dio click al botón marcas, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test2']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido2) \
                        .pause(0) \
                        .double_click(Registrorepetido2) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Bfamilias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_fam)))
                    Bfamilias.click()
                    Log().info("Se hace el cambio a la pestaña familias para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dio click al botón familias, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test3']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido3) \
                        .pause(0) \
                        .double_click(Registrorepetido3) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Bgeneros = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_gen)))
                    Bgeneros.click()
                    Log().info("Se hace el cambio a la pestaña géneros para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dio click al botón generos, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test4']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido4) \
                        .pause(0) \
                        .click(Registrorepetido4) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    EliminaG = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_EliminaG)))
                    EliminaG.click()
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
                    GuardaF = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_GuardaF)))
                    GuardaF.click()
                    Log().info(" Se da clic en el boton Guardar Familia; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se dio click al botón Guardar Familia, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    GuardaM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_GuardaM)))
                    GuardaM.click()
                    Log().info(" Se da clic en el boton Guardar Marca; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se dio click al botón Guardar Marca, validar que la acción anterior haya finalizado,"
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
                    Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")

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
                    Refrescarepetido1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
                    Refrescarepetido1.click()
                    Log().info(" Se presiona el boton 'Refrescar', para proceder a eliminar el registro.")
                    time.sleep(2)

                except Exception as e:
                    Log().error("No se dio click al botón Refrescar, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido5 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test1']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido5) \
                        .pause(0) \
                        .double_click(Registrorepetido5) \
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

                try:
                    Bmarcas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_marcas)))
                    Bmarcas.click()
                    Log().info("Se hace el cambio a la pestaña marcas para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dio click al botón marcas, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido6 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test2']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido6) \
                        .pause(0) \
                        .double_click(Registrorepetido6) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Bfamilias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_fam)))
                    Bfamilias.click()
                    Log().info("Se hace el cambio a la pestaña familias para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dio click al botón familias, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido7 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test3']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido7) \
                        .pause(0) \
                        .click(Registrorepetido7) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    EliminaF = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_EliminaF)))
                    EliminaF.click()
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
                    GuardaM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_GuardaM)))
                    GuardaM.click()
                    Log().info(" Se da clic en el boton Guardar Marca; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se dio click al botón Guardar Marca, validar que la acción anterior haya finalizado,"
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
                    Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")

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
                    Refrescarepetido2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
                    Refrescarepetido2.click()
                    Log().info(" Se presiona el boton 'Refrescar', para proceder a eliminar el registro.")
                    time.sleep(2)

                except Exception as e:
                    Log().error("No se dio click el botón Refrescar, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido8 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test1']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido8) \
                        .pause(0) \
                        .double_click(Registrorepetido8) \
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

                try:
                    Bmarcas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_marcas)))
                    Bmarcas.click()
                    Log().info("Se hace el cambio a la pestaña marcas para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dio click al botón marcas, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido9 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test2']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido9) \
                        .pause(0) \
                        .click(Registrorepetido9) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    EliminaM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_EliminaM)))
                    EliminaM.click()
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
                    Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
                    Guarda.click()
                    Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")

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
                    Refrescarepetido3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
                    Refrescarepetido3.click()
                    Log().info(" Se presiona el boton 'Refrescar', para proceder a eliminar el registro.")
                    time.sleep(2)

                except Exception as e:
                    Log().error("No se dio click al botón Refrescar, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorepetido10 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test1']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorepetido10) \
                        .pause(0) \
                        .click(Registrorepetido10) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
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
                    Refrescarepetido4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
                    Refrescarepetido4.click()
                    Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
                    time.sleep(2)

                except Exception as e:
                    Log().error("No se dio click el botón Refrescar, validar que la acción anterior haya finalizado,"
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
            Log().error("No se dio click al botón Nuevo, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
