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

            TiposDocumento = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas_tdoc']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(TiposDocumento) \
                .pause(0) \
                .release()
            action.perform()

            Documento = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='tiposdocumento']")))

            action = ActionChains(self.driver)
            action \
                .click(Documento) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Abre la pantalla de Tipos de Documento")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        """Abre pantalla de listado de registros."""
        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("TIPOS DE DOCUMENTOS", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Tipos de documento")
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
            Registrorepetido = self.driver.find_element(By.XPATH, "//span[text()='PM55']")
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

                # Cambio Pestaña Comportamiento

                try:
                    Bcomportamiento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_comportamiento)))
                    Bcomportamiento.click()
                    Log().info("Se hace el cambio a la pestaña Comportamiento para continuar con la eliminación del registro")

                except Exception as e:
                    Log().error("No se dió click en el botón comportamiento, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrorubropermitido = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM02                ']")))
                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrorubropermitido) \
                        .pause(0) \
                        .click(Registrorubropermitido) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de Rubro Permitido, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de Rubro Permitido, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminarubropermitido = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_tiposrubro)))
                    Eliminarubropermitido.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Rubro Permitido.")
                    time.sleep(1)

                except Exception as e:
                    Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Cheques

                try:
                    Bcheques = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cheques)))
                    Bcheques.click()
                    Log().info("Se hace el cambio a la pestaña Cheques para continuar con la eliminación del registro")

                except Exception as e:
                    Log().error("No se dió click en el botón Cheques, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrotipocheque = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Cheque al dia']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrotipocheque) \
                        .pause(0) \
                        .click(Registrotipocheque) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro Tipo Cheques, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de Tipo Cheques, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminatipocheque = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_tipocheque)))
                    Eliminatipocheque.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Tipos Cheques.")
                    time.sleep(1)

                except Exception as e:
                    Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Restricciones

                try:
                    Brestricciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_restricciones)))
                    Brestricciones.click()
                    Log().info("Se hace el cambio a la pestaña Restricciones para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dió click en el botón Restricciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrolineapermitida = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CIGARROS(PM01)']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrolineapermitida) \
                        .pause(0) \
                        .click(Registrolineapermitida) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de Linea Permitida, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de Linea Permitida, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminalineapermitida = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_lineanegpermitida)))
                    Eliminalineapermitida.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Linea Permitida.")
                    time.sleep(1)

                except Exception as e:
                    Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Generar Desde

                try:
                    Bgenerardesde = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_generardesde)))
                    Bgenerardesde.click()
                    Log().info("Se hace el cambio a la pestaña Generar Desde para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se dió click en el botón Generar Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registrogenerardesde = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[5]/span/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrogenerardesde) \
                        .pause(0) \
                        .click(Registrogenerardesde) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de Generar Desde, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de Generar Desde, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminageneradesde = self.wait.until( conditions.visibility((By.XPATH, Configuracion.btn_Elimina_incluiritem)))
                    Eliminageneradesde.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Generar Desde.")
                    time.sleep(1)

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
                    time.sleep(3)

                except Exception as e:
                    Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(3)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM55']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro4) \
                        .pause(0) \
                        .click(Registro4) \
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
