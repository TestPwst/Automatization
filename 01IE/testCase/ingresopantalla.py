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

        # Selecciona el menu

        try:
            Tablas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas']")))

            action = ActionChains(self.driver)
            action \
                .click(Tablas) \
                .pause(0) \
                .release()
            action.perform()

            Encuestas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='_tablas_enc']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Encuestas) \
                .pause(0) \
                .release()
            action.perform()

            InstanciasEncuestas = self.wait.until(conditions.visibility((By.XPATH, "//*[@id='instanciasencuestas']")))

            action = ActionChains(self.driver)
            action \
                .click(InstanciasEncuestas) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Abre la pantalla de Instancias Encuestas")

        except (NoSuchElementException, TimeoutException) as e:
            Buscador.buscador(self)
            Log().info(" La función buscador funciona de manera correcta.")

        # Valida que la pantalla ejecutada sea correcta
        try:
            Pantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_pantalla))).text
            self.assertEqual("INSTANCIAS ENCUESTAS", Pantalla, "La pantalla ejecutada es correcta")
            Log().info(" La pantalla ejecutada es Instancias Encuestas.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Refresca = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca.click()
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")

        except Exception as e:
            Log().error(
                "No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            self.wait = WebDriverWait(self.driver, 10)
            Registro2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))
            self.wait = WebDriverWait(self.driver, 60)
            try:

                action = ActionChains(self.driver)
                action \
                    .click(Registro2) \
                    .pause(0) \
                    .double_click(Registro2) \
                    .pause(0) \
                    .release()
                action.perform()

                Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

            except Exception as e:
                Log().error(
                    "No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return False

            #Cambia Pestaña para eliminar registro
            try:
                Btipoencuestas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_tiposencuestas)))
                Btipoencuestas.click()
                Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
                
            except Exception as e:
                Log().error(
                    "No se encontró el botón Tipo Encuestas, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return False

            try:
                self.wait = WebDriverWait(self.driver, 5)
                Registrotipoencuestas = ''
                try:
                    Registrotipoencuestas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Iorden+"']")))
                except (NoSuchElementException, TimeoutException) as e:
                    pass

                try:
                    Registrotipoencuestas = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Morden+"']")))
                except (NoSuchElementException, TimeoutException) as e:
                    pass
                

                action = ActionChains(self.driver)
                action \
                    .click(Registrotipoencuestas) \
                    .pause(0) \
                    .release()
                action.perform()
                
                self.wait = WebDriverWait(self.driver, 60)

                Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

            except (NoSuchElementException, TimeoutException) as e:
                    pass

            try:
                Eliminatipoencuestas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_tipoencuesta)))
                Eliminatipoencuestas.click()
                Log().info(" Se presiona el boton 'Eliminar', para eliminar el registro.")

            except Exception as e:
                Log().error("No se encontró el botón Eliminar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
                Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
                    .click(Registro3) \
                    .pause(0) \
                    .release()
                action.perform()

                Log().info(" Se da clic en el registro creado, para proceder a eliminarlo.")

            except Exception as e:
                Log().error(
                    "No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
                Log().error("No se encontró el botón Eliminar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
                Log().error("No se encontró el botón Aceptar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return False

        except (NoSuchElementException, TimeoutException) as e:
            pass