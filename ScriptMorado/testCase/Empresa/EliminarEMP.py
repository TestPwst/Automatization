from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class EliminarEMP:

    def EliminarEMP(self):

        self.wait = WebDriverWait(self.driver, 15)
        """Se selecciona el registro y se elimina."""
            # Da clic en refrescar
        try:
            Refresca3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca3.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a eliminar el registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registro3 = self.driver.find_element(By.XPATH, "//span[text()='2021']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro3) \
                .pause(2) \
                .double_click(Registro3) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Stock de Mercaderías

        try:
            Bresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_resolfiscales)))
            Bresolfiscales.click()
            Log().info("Se hace el cambio a la pestaña Resoluciones Fiscales para continuar con la eliminación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Resolución Fiscales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registroresolficales = self.driver.find_element(By.XPATH, "//span[text()='21302024']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroresolficales) \
                .pause(2) \
                .click(Registroresolficales) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro en el Registro de Resoluciones Fiscales, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Resoluciones Fiscales, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaresolfiscales = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_resolfiscales)))
            Eliminaresolfiscales.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Resoluciones Fiscales.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registro4 = self.driver.find_element(By.XPATH, "//span[text()='2021']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro4) \
                .pause(2) \
                .double_click(Registro4) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Series

        try:
            Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
            Bseries.click()
            Log().info("Se hace el cambio a la pestaña Series para continuar con la eliminación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registroseries = self.driver.find_element(By.XPATH, "//span[text()='20']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroseries) \
                .pause(2) \
                .double_click(Registroseries) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da doble click en el registro de series, para proceder a eliminarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Configuración Vías

        try:
            Bconfigvias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_configvias)))
            Bconfigvias.click()
            Log().info("Se hace el cambio a la pestaña Coniguración Vias para continuar con la eliminación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Configuracion de Vias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registrovias = self.driver.find_element(By.XPATH, "//span[text()='PM04']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrovias) \
                .pause(2) \
                .click(Registrovias) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro de Configuración Vías, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Configuración Vías, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminavias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_via)))
            Eliminavias.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Configuración Vías.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guardaserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_series)))
            Guardaserie.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro Series.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registro5 = self.driver.find_element(By.XPATH, "//span[text()='2021']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro5) \
                .pause(2) \
                .double_click(Registro5) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Cambio Pestaña Series

        try:
            Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
            Bseries.click()
            Log().info("Se hace el cambio a la pestaña Series para continuar con la eliminación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón Series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registroseries = self.driver.find_element(By.XPATH, "//span[text()='20']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroseries) \
                .pause(2) \
                .click(Registroseries) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro series, para proceder a eliminarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de series, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Eliminaseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_serie)))
            Eliminaseries.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro de Series.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registro6 = self.driver.find_element(By.XPATH, "//span[text()='2021']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro6) \
                .pause(2) \
                .click(Registro6) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina)))
            Elimina.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Confirma_Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_acepta_eliminar)))
            Confirma_Elimina.click()
            Log().info(" Se confirma el eliminado del registro")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Refresca4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca4.click()
            Log().info(" Se presiona el boton 'Refrescar', para verificar si el registro ha sido eliminado.")
            time.sleep(5)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        try:
            Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_pantalla)))
            Cierra_todo.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla de Empresas.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Cerrar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise