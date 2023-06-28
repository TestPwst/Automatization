from importlib.machinery import SourceFileLoader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
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
        # Abre la pantalla

        # Selecciona el menu

        try:
            Tablas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas']")))

            action = ActionChains(self.driver)
            action \
                .click(Tablas) \
                .pause(0) \
                .release()
            action.perform()

            ZonasUbicaciones = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas_zonas']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(ZonasUbicaciones) \
                .pause(0) \
                .release()
            action.perform()

            Ubicacionesgeo = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='paises']")))

            action = ActionChains(self.driver)
            action \
                .click(Ubicacionesgeo) \
                .release()
            action.perform()
            Log().info(" Abre la pantalla de Paises")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("PAÍSES", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Paises.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 10)
            Registrorepetido = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))
            self.wait = WebDriverWait(self.driver, 60)
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
                    Bdepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_departamentos)))
                    Bdepartamentos.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error(
                        "No se dió click al botón Departamentos, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False


                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrodepartamentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='101']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrodepartamentos) \
                        .pause(0) \
                        .double_click(Registrodepartamentos) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio pestaña Localidades

                try:
                    Blocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_localidades)))
                    Blocalidades.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                        
                except Exception as e:
                    Log().error(
                        "No se dió click al botón Localidades, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrolocalidades = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='102']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrolocalidades) \
                        .pause(0) \
                        .double_click(Registrolocalidades) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Barrios

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Bbarrios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_barrios)))
                    self.wait = WebDriverWait(self.driver, 60)

                    Bbarrios.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except (NoSuchElementException, TimeoutException) as e:
                    pass
                
                except Exception as e:
                    Log().error(
                        "No se dió click al botón Barrios, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrobarrios = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='103']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrobarrios) \
                        .pause(0) \
                        .click(Registrobarrios) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Eliminabarrios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_barrios)))
                    self.wait = WebDriverWait(self.driver, 60)
                    Eliminabarrios.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass
                    
                except Exception as e:
                    Log().error("No se dió click al botón Eliminar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Guardalocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_localidades)))
                    self.wait = WebDriverWait(self.driver, 60)
                    Guardalocalidades.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass
                    
                except Exception as e:
                    Log().error(
                        "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guardadepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_departamentos)))
                    Guardadepartamentos.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
                    
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
                    Guarda.click()
                    Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
                    
                except Exception as e:
                    Log().error("No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100']")))

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro3) \
                        .pause(0) \
                        .double_click(Registro3) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambia pestaña departamentos

                try:
                    Bdepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_departamentos)))
                    Bdepartamentos.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error(
                        "No se dió click al botón Departamentos, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrodepartamentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='101']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrodepartamentos) \
                        .pause(0) \
                        .double_click(Registrodepartamentos) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambia pestaña impuestos por articulo

                try:
                    Bimpuestosarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impuestoarticulo)))
                    Bimpuestosarticulo.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                except Exception as e:
                   Log().error(
                       "No se dió click al botón Impuestos por Articulo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                   timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                   img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                   Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                   self.driver.get_screenshot_as_file(img_name)
                   
                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registroimpuestoarticulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='40041615']")))
                    self.wait = WebDriverWait(self.driver, 60)
                    
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registroimpuestoarticulo) \
                        .pause(0) \
                        .click(Registroimpuestoarticulo) \
                        .pause(0) \
                        .release()
                    action.perform()
                
                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    try:
                        self.wait = WebDriverWait(self.driver, 5)
                        Registroimpuestoarticulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='40041602']")))
                        self.wait = WebDriverWait(self.driver, 60)
                        
                        action = ActionChains(self.driver)
                        action \
                            .move_to_element(Registroimpuestoarticulo) \
                            .pause(0) \
                            .click(Registroimpuestoarticulo) \
                            .pause(0) \
                            .release()
                        action.perform()
                    
                        Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
                    except (NoSuchElementException, TimeoutException) as e:
                        pass
                
                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                
                try:
                   Eliminaimpuestoart = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impuestoarticulo)))
                   Eliminaimpuestoart.click()
                   Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")
                
                except Exception as e:
                   Log().error("No se dió click al botón Eliminar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                   timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                   img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                   Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                   self.driver.get_screenshot_as_file(img_name)
                   
                # Cambio pestaña localidades

                try:
                    Blocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_localidades)))
                    Blocalidades.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                
                except Exception as e:
                    Log().error(
                        "No se dió click al botón Localidades, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrolocalidades = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='102']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrolocalidades) \
                        .pause(0) \
                        .click(Registrolocalidades) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Eliminalocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_localidades)))
                    self.wait = WebDriverWait(self.driver, 60)
                    Eliminalocalidades.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error("No se dió click al botón Eliminar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guardadepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_departamentos)))
                    Guardadepartamentos.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

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
                    Guarda.click()
                    Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")

                except Exception as e:
                    Log().error("No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Registro4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100']")))

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
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambia pestaña departamentos

                try:
                    Bdepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_departamentos)))
                    Bdepartamentos.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error(
                        "No se dió click al botón Departamentos, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrodepartamentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='101']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrodepartamentos) \
                        .pause(0) \
                        .click(Registrodepartamentos) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminadepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_departamento)))
                    Eliminadepartamentos.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

                except Exception as e:
                    Log().error("No se dió click al botón Eliminar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                    Log().error("No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Registro5 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100']")))

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro5) \
                        .pause(0) \
                        .click(Registro5) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina)))
                    Elimina.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")
                    time.sleep(1)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)

                except Exception as e:
                    Log().error("No se dió click al botón Eliminar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                    Log().error("No se dió click al botón Aceptar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Refresca4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
                    Refresca4.click()
                    Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")

                except Exception as e:
                    Log().error("No se dio click el botón Refrescar, validar que la acción anterior haya finalizado,"
                                "que el xpath sea el correcto o que la página no presente lentitud")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

        except (NoSuchElementException, TimeoutException) as e:
            pass

            # Da clic en nuevo
        try:
            Nuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo)))
            Nuevo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")
            
        except Exception as e:
            Log().error(
                "No se encontró el botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False