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
            Clientes = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_clientes']")))

            action = ActionChains(self.driver)
            action \
                .click(Clientes) \
                .pause(0) \
                .release()
            action.perform()

            Matrices = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_cli_matrices']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Matrices) \
                .pause(0) \
                .release()
            action.perform()

            Matriz = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='matrices']")))

            action = ActionChains(self.driver)
            action \
                .click(Matriz) \
                .release()
            action.perform()
            Log().info(" Abre la pantalla de Matrices")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("MATRICES", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Matrices.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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

                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error(
                        "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio Pestaña Compañias

                try:
                    Bcompanias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_companias)))
                    Bcompanias.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                    
                except Exception as e:
                    Log().error(
                        "No se encontró el botón compañias, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 10)
                    Registrocompanias = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigocom+"']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrocompanias) \
                        .pause(0) \
                        .double_click(Registrocompanias) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")
                    
                except (NoSuchElementException, TimeoutException):
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                    # Cambio Pestaña Regional

                try:
                    Bregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_regional)))
                    Bregional.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                    
                except Exception as e:
                    Log().error(
                        "No se encontró el botón regional, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False


                try:
                    self.wait = WebDriverWait(self.driver, 10)
                    Registroregional = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigoreg+"']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registroregional) \
                        .pause(0) \
                        .click(Registroregional) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException):
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminaregional = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_regional)))
                    Eliminaregional.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

                except Exception as e:
                    Log().error(
                        "No se encontró el botón Eliminar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guardacompania = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_companias)))
                    Guardacompania.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
                    
                except Exception as e:
                    Log().error(
                        "No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
                    Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False


                try:
                    Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))

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
                        "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Bcompanias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_companias)))
                    Bcompanias.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                except Exception as e:
                    Log().error(
                        "No se encontró el botón compañias, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False


                try:
                    self.wait = WebDriverWait(self.driver, 10)
                    Registrocompanias = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigocom+"']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrocompanias) \
                        .pause(0) \
                        .click(Registrocompanias) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException):
                    pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminacompania = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_compania)))
                    Eliminacompania.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")
                    
                except Exception as e:
                    Log().error("No se encontró el botón Eliminar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
                    Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False


                try:
                    Registro4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))

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
                    Log().error(
                        "No se encontró el registro, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina)))
                    Elimina.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)

                except Exception as e:
                    Log().error("No se encontró el botón Eliminar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
                    Log().error("No se encontró el botón Aceptar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
                    Log().error("No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
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
            time.sleep(1)
            
        except Exception as e:
            Log().error(
                "No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, revise la accion anterior si el xpath es el correcto o el tiempo de la accion")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False