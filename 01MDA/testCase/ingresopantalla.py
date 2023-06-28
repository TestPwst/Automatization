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
        # Condición Sesiones Activas
        # Selecciona el menu

        try:
            Tablas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas']")))

            action = ActionChains(self.driver)
            action \
                .click(Tablas) \
                .pause(0) \
                .release()
            action.perform()

            Contratos = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas_contrato']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Contratos) \
                .pause(0) \
                .release()
            action.perform()

            Modelosajuste = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='modelosajustes']")))

            action = ActionChains(self.driver)
            action \
                .click(Modelosajuste) \
                .pause(0) \
                .release()
            action.perform()
            
            Log().info(" Abre la pantalla de modelos de ajuste")

        except Exception as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("MODELOS DE AJUSTE", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es modelos de ajuste")
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

            # Da clic en nuevo

        try:
            self.wait = WebDriverWait(self.driver, 10)
            Registrorepetido = self.driver.find_element(By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")
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

                # Cambio de pestaña ajustes

                try:
                    Bajustes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ajustes)))
                    Bajustes.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                    
                except Exception as e:
                    Log().error("No se dió click al botón ajustes, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    self.wait = WebDriverWait(self.driver, 5)
                    Registrodocumentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='7']")))
                    self.wait = WebDriverWait(self.driver, 60)

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registrodocumentos) \
                        .pause(0) \
                        .click(Registrodocumentos) \
                        .pause(0) \
                        .release()
                    action.perform()

                    Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

                except (NoSuchElementException, TimeoutException) as e:
                    try:
                        self.wait = WebDriverWait(self.driver, 5)
                        Registrodocumentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='7']")))
                        self.wait = WebDriverWait(self.driver, 60)

                        action = ActionChains(self.driver)
                        action \
                            .move_to_element(Registrodocumentos) \
                            .pause(0) \
                            .click(Registrodocumentos) \
                            .pause(0) \
                            .release()
                        action.perform()
                    except (NoSuchElementException, TimeoutException):
                        pass

                except Exception as e:
                    Log().error(
                        "No se encontró el registro deseado deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminarajustes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_eliminarajustes)))
                    Eliminarajustes.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

                except Exception as e:
                    Log().error("No se dió click al botón Eliminar Ajustes, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                    Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CódigoTest']")))

                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro) \
                        .pause(0) \
                        .click(Registro) \
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
                    Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina)))
                    Elimina.click()
                    Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")
                    time.sleep(2)
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
                    Log().error("No se dió click al botón Refrescar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

        except (NoSuchElementException, TimeoutException) as e:
            pass

        try:
            Nuevo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo)))
            Nuevo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False