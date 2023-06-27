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
            Clientes = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_clientes']")))

            action = ActionChains(self.driver)
            action \
                .click(Clientes) \
                .pause(0) \
                .release()
            action.perform()

            ArqCliente = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='arqcli01']")))

            action = ActionChains(self.driver)
            action \
                .click(ArqCliente) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Abre la pantalla de Arquitectura de Cliente")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        """Abre pantalla de listado de registros."""

        # Valida que la pantalla ejecutada sea correcta
        try:
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("ARQUITECTURA DE CLIENTES", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Tipos de Cliente")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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

                # Cambio de pestaña segundo nivel para eliminar
                try:
                    Bsegundonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_segundonivel)))
                    Bsegundonivel.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se encontró el botón segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro6 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test2']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro6) \
                        .pause(0) \
                        .double_click(Registro6) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de segundo nivel creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio de pestaña tercer nivel para eliminar

                try:
                    Btercernivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_tercernivel)))
                    Btercernivel.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se encontró el botón tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro7 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test3']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro7) \
                        .pause(0) \
                        .double_click(Registro7) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de tercer nivel creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio de pestaña cuarto nivel para eliminar

                try:
                    Bcuartonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cuartonivel)))
                    Bcuartonivel.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se encontró el botón cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro8 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test4']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro8) \
                        .pause(0) \
                        .click(Registro8) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de cuarto nivel creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminacuarto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_cuartonivel)))
                    Eliminacuarto.click()
                    Log().info(" Se presiona el boton 'Eliminar' de cuarto nivel, para eliminar el registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Eliminar de cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guarda3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_tercero)))
                    Guarda3.click()
                    Log().info(" Se da clic en el boton Guardar de tercer nivel; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Guardar de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guarda2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_segundo)))
                    Guarda2.click()
                    Log().info(" Se da clic en el boton Guardar de segundo nivel; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Guardar de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guarda1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
                    Guarda1.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Volvemos a entrar

                Registro9 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test1']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro9) \
                        .pause(0) \
                        .double_click(Registro9) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio de pestaña segundo nivel para eliminar

                try:
                    Bsegundonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_segundonivel)))
                    Bsegundonivel.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se encontró el botón segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro10 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test2']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro10) \
                        .pause(0) \
                        .double_click(Registro10) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de segundo nivel creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio de pestaña tercer nivel para eliminar

                try:
                    Btercernivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_tercernivel)))
                    Btercernivel.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se encontró el botón tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro11 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test3']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro11) \
                        .pause(0) \
                        .click(Registro11) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de tercer nivel creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminatres = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_tercernivel)))
                    Eliminatres.click()
                    Log().info(" Se presiona el boton 'Eliminar' de tercer nivel, para eliminar el registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Eliminar de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guarda2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_segundo)))
                    Guarda2.click()
                    Log().info(" Se da clic en el boton Guardar de segundo nivel; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Guardar de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guarda1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
                    Guarda1.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # volvemos a entrar

                Registro12 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test1']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro12) \
                        .pause(0) \
                        .double_click(Registro12) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                # Cambio de pestaña segundo nivel para eliminar

                try:
                    Bsegundonivel = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_segundonivel)))
                    Bsegundonivel.click()
                    Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

                except Exception as e:
                    Log().error("No se encontró el botón segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro13 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test2']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro13) \
                        .pause(0) \
                        .click(Registro13) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro de segundo nivel creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Eliminados = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_segundonivel)))
                    Eliminados.click()
                    Log().info(" Se presiona el boton 'Eliminar' de segundo nivel, para eliminar el registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Eliminar de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                try:
                    Guarda1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
                    Guarda1.click()
                    Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

                except Exception as e:
                    Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                    time.sleep(2)
                    timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                    img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                    Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                    self.driver.get_screenshot_as_file(img_name)
                    return False

                Registro14 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Test1']")))

                try:
                    action = ActionChains(self.driver)
                    action \
                        .move_to_element(Registro14) \
                        .pause(0) \
                        .click(Registro14) \
                        .pause(0) \
                        .release()
                    action.perform()
                    Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

                except Exception as e:
                    Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
            Log().error("No se encontró el botón Nuevo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False