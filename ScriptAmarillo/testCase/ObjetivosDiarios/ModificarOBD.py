from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class ModificarOBD:

    def ModificarOBD(self):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 20)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
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

        Registro = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[3]/ui-listview/div/div/div[2]/div/div")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(2) \
                .double_click(Registro) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da doble click en el registro creado, para proceder a modificarlo.")
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

        #Modifica los valores

        try:
            Cefectividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_efectividad)))
            Cefectividad.clear()
            Cefectividad.send_keys(Configuracion.Mefectividad)
            Log().info(" Se modifica el contenido del campo efectividad ")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para Modificar la efectividad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        #Cambio Pestaña grupos

        try:
            Bgrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_gruposOBD)))
            Bgrupos.click()
            Log().info("Se hace el cambio a la pestaña Grupos para continuar con la Modificación del registro")
            time.sleep(3)

        except Exception as e:
            Log().error("No se dió click en el botón grupos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        Registrogrupos = self.driver.find_element(By.XPATH, "//span[text()='CPM01']")

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrogrupos) \
                .pause(2) \
                .double_click(Registrogrupos) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da doble click en el registro de Grupos, para proceder a modificarlo.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Grupos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            raise

        # Modifica Valores

        try:
            Cgrupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupopoliticaOBD)))
            Cgrupopolitica.click()
            time.sleep(5)

            registro_grupopolitica = self.driver.find_element(By.XPATH, "//span[text()='CPM02']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupopolitica) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Grupos Politica.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el registro de Grupo Politica, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctipoobjetivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipoobjetivo)))
            Ctipoobjetivo.click()
            time.sleep(3)

            registro_tipoobjetivo = self.driver.find_element(By.XPATH, "//li[text()='Volumen Mensual']")

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoobjetivo) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Volumen Mensual.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se seleccinó la opción Volumen Mensual, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Ctipounidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipounidad)))
            Ctipounidad.click()
            time.sleep(3)

            registro_tipounidad = self.driver.find_element(By.XPATH, "//span[text()='Unidad']")

            action = ActionChains(self.driver)
            action \
                .click(registro_tipounidad) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Unidad.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se seleccionó la opción unidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Cobjetivocantidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_objetivocantidad)))
            Cobjetivocantidad.clear()
            Cobjetivocantidad.send_keys(Configuracion.Mobjetivocantidad)
            Log().info(" Se modifica el contenido del campo Objetivo Cantidad ")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el Objetivo Cantidad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Guardagrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_grupos)))
            Guardagrupos.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar el registro de Grupos.")
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