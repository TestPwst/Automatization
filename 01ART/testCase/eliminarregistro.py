from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.log import Log
from common.globalparam import img_path
import os
import time


class eliminarregistro:

    def eliminarregistro(self, conditions, Configuracion):

        self.wait = WebDriverWait(self.driver, 60)
        """Se selecciona el registro y se elimina."""
        # Da clic en refrescar
        try:
            Refresca3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca3.click()
            Log().info(" Se presiona el boton 'Refrescar', para proceder a eliminar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro3 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='FA0102021']")))

        try:
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
            Log().error("No se encontró el registro desado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Impuestos

        try:
            Bimpuestos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impuestos)))
            Bimpuestos.click()
            Log().info("Se hace el cambio de pestaña impuestos para continuar con la eliminación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón impuestos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registroimpuestos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='4']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpuestos) \
                .pause(0) \
                .click(Registroimpuestos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de impuestos, para proceder a eliminarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña impuestos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Eliminaimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Elimina_impuesto)))
            Eliminaimpuesto.click()
            Log().info(" Se presiona el boton 'Eliminar de Impuesto', para eliminar el registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Eliminar de Impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio a la pestaña Custom Properties

        try:
            Bcustom = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_customproperties)))
            Bcustom.click()
            Log().info("Se hace el cambio a la pestaña Custom Properties para continuar con la eliminación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Custom Properties, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Caguascalientes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aguascalientes)))
            Caguascalientes.click()
            Log().info(" Se dió click en el checkbox Aguascalientes")

        except Exception as e:
            Log().error("No se dió click en el checkbox Aguascalientes, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbajacalifornia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_bajacalifornia)))
            Cbajacalifornia.click()
            Log().info(" Se dió click en el checkbox de Baja California ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Baja California, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cbajacaliforniasur = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_bajacaliforniasur)))
            Cbajacaliforniasur.click()
            Log().info(" Se dió click en el checkbox Baja California Sur ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Baja California Sur, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccampeche = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_campeche)))
            Ccampeche.click()
            Log().info(" Se dió click en el checkbox Campeche ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Campeche, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccoahuila = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_coahuila)))
            Ccoahuila.click()
            Log().info(" Se dió click en el checkbox Coahuila ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Coahuila, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccolima = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_colima)))
            Ccolima.click()
            Log().info(" Se dió click en el checkbox Colima ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Colima, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cchiapas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_chiapas)))
            Cchiapas.click()
            Log().info(" Se dió click en el checkbox Chiapas ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Chiapas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cchihuahua = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_chihuahua)))
            Cchihuahua.click()
            Log().info(" Se dió click en el checkbox Chihuahua ")

        except Exception as e:
            Log().error("No se dio click en el checkbox Chihuahua, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdf = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_df)))
            Cdf.click()
            Log().info(" Se dió click en el checkbox Distrito Federal ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Distrito Federal, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdurango = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_durango)))
            Cdurango.click()
            Log().info(" Se dió click en el checkbox Durango ")

        except Exception as e:
            Log().error("No se dió click en el checkbpx Durango, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cguanajuato = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_guanajuato)))
            Cguanajuato.click()
            Log().info(" Se dió click en el checkbox Guanajuato ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Guanajuato, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cguerrero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_guerrero)))
            Cguerrero.click()
            Log().info(" Se dió click en el checkbox Guerrero ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Guerrero, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chidalgo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hidalgo)))
            Chidalgo.click()
            Log().info(" Se dió click en el checkbox Hidalgo ")

        except Exception as e:
            Log().error("No se dió click en el checkbox Hidalgo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cjalisco = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_jalisco)))
            Cjalisco.click()
            Log().info(" Se dió click en el checkbox Jalisco")

        except Exception as e:
            Log().error("No se dió click en el checkbox Jalisco, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmexico = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_mexico)))
            Cmexico.click()
            Log().info(" Se dió click en el checkbox México")

        except Exception as e:
            Log().error("No se dió click en el checkbox México, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmichoacan = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_michoacan)))
            Cmichoacan.click()
            Log().info(" Se dió click en el checkbox Michoacan")

        except Exception as e:
            Log().error("No se dió click en el checkbox Michoacan, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmorelos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_morelos)))
            Cmorelos.click()
            Log().info(" Se dió click en el checkbox Morelos")

        except Exception as e:
            Log().error("No se dió click en el checkbox Morelos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnayarit = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nayarit)))
            Cnayarit.click()
            Log().info(" Se dió click en el checkbox Nayarit")

        except Exception as e:
            Log().error("No se dió click en el checkbox Nayarit, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnuevoleon = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nuevoleon)))
            Cnuevoleon.click()
            Log().info(" Se dió click en el checkbox Nuevo León")

        except Exception as e:
            Log().error("No se dió click en el checkbox Nuevo León, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Coaxaca = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_oaxaca)))
            Coaxaca.click()
            Log().info(" Se dió click en el checkbox Oaxaca")

        except Exception as e:
            Log().error("No se dió click en el checkbox Oaxaca,validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpuebla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_puebla)))
            Cpuebla.click()
            Log().info(" Se dió click en el checkbox Puebla")

        except Exception as e:
            Log().error("No se dió click en el checkbox Puebla, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cqueretaro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_queretaro)))
            Cqueretaro.click()
            Log().info(" Se dió click en el checkbox Queretaro")

        except Exception as e:
            Log().error("No se dió click en el checkbox Queretaro, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cquintanaroo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_quintanaroo)))
            Cquintanaroo.click()
            Log().info(" Se dió click en el checkbox Quintana Roo")

        except Exception as e:
            Log().error("No se dió click en el checkbox Quintana Roo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csanluis = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sanluis)))
            Csanluis.click()
            Log().info(" Se dió click en el checkbox San Luis Potosi")

        except Exception as e:
            Log().error("No se dió click en el checkbox San Luis Potosi, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csinaloa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sinaloa)))
            Csinaloa.click()
            Log().info(" Se dió click en el checkbox Sinaloa")

        except Exception as e:
            Log().error("No se dió click en el checkbox Sinaloa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csonora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_sonora)))
            Csonora.click()
            Log().info(" Se dió click en el checkbox Sonora")

        except Exception as e:
            Log().error("No se dió click en el checkbox Sonora, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctabasco = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tabasco)))
            Ctabasco.click()
            Log().info(" Se dió click en el checkbox Tabasco")

        except Exception as e:
            Log().error("No se dió click en el checkbox Tabasco, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctamaulipas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tamaulipas)))
            Ctamaulipas.click()
            Log().info(" Se dió click en el checkbox Tamaulipas")

        except Exception as e:
            Log().error("No se dió click en el checkbox Tamaulipas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctlaxcala = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tlaxcala)))
            Ctlaxcala.click()
            Log().info(" Se dió click en el checkbox Tlaxcala")

        except Exception as e:
            Log().error("No se dió click en el checkbox Tlaxcala, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cveracruz = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_veracruz)))
            Cveracruz.click()
            Log().info(" Se dió click en el checkbox Veracruz")

        except Exception as e:
            Log().error("No se dió click en el checkbox Veracruz, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cyucatan = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_yucatan)))
            Cyucatan.click()
            Log().info(" Se dió click en el checkbox Yucatan")

        except Exception as e:
            Log().error("No se dió click en el checkbox Yucatan, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Czacatecas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_zacatecas)))
            Czacatecas.click()
            Log().info(" Se dió click en el checkbox Zacatecas")

        except Exception as e:
            Log().error("No se dió click en el checkbox Zacatecas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro4 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='FA0102021']")))

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
            Log().error("No se dió click en el botón Eliminar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Confirma_Elimina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_acepta_eliminar)))
            Confirma_Elimina.click()
            Log().info(" Se confirma el eliminado del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Aceptar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Refresca4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca4.click()
            Log().info(" Se presiona el boton 'Refrescar', para verificar si el registro ha sido eliminado.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_pantalla)))
            Cierra_todo.click()
            Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla de Articulos.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Cerrar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False