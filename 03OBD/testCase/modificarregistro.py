from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.log import Log
from common.globalparam import img_path
import os
import time

class modificarregistro:

    def modificarregistro(self, conditions, Configuracion):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 60)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modifcar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[3]/ui-listview/div/div/div[2]/div/div")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[3]/ui-listview/div/div/div[2]/div/div")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(0) \
                .double_click(Registro) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da doble click en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Cefectividad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_efectividad)))
            Cefectividad.clear()
            Cefectividad.send_keys(Configuracion.Mefectividad)
            Log().info(" Se Modifica el contenido del campo Efectividad ")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la efectividad, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Cambio Pestaña grupos

        try:
            Bgrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_grupos)))
            Bgrupos.click()
            Log().info("Se hace el cambio a la pestaña Grupos para continuar con modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón grupos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registrogrupos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CPM01']")))
            
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrogrupos) \
                .pause(0) \
                .double_click(Registrogrupos) \
                .pause(0) \
                .release()
            action.perform()
            
            Log().info(" Se da doble click en el registro de Grupos, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de Grupos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Cgrupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_grupopolitica)))
            Cgrupopolitica.click()

            registro_grupopolitica = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='CPM02']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_grupopolitica) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Grupos Politicas.")

        except Exception as e:
            Log().error("No se encontró el registro de Grupo Politica, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoobjetivo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipoobjetivo)))
            Ctipoobjetivo.click()

            registro_tipoobjetivo = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Distribución Diaria']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoobjetivo) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Distribucion Diaria.")

        except Exception as e:
            Log().error("No se dió click en la opción Distribución Diaria, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cobjetivodistribucion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_objetivodistribucion)))
            Cobjetivodistribucion.clear()
            Cobjetivodistribucion.send_keys(Configuracion.Mobjetivodistribucion)
            Log().info(" Se Modifica el contenido del campo Objetivo Distribucion ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para Modificar el objetivo distribucion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardagrupos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_grupos)))
            Guardagrupos.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar el registro de Grupos.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False