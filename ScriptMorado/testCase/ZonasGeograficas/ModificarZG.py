from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time


class ModificarZG:

    def ModificarZG(self):
        """Se abre la ventana para modificar el registro existente """

        self.wait = WebDriverWait(self.driver, 20)

        # Da clic en refrescar
        try:
            Refresca2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Refresca)))
            Refresca2.click()
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        Registro = self.driver.find_element(By.XPATH, "//span[text()='12345']")

        try:

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(2) \
                .double_click(Registro) \
                .pause(2) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        # Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoaltZG)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.McodigoaltZG)
            Log().info(" Se modifica el contenido del campo Descripcion")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el código alternativo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionZG)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.MdescripcionZG)
            Log().info(" Se modifica el contenido del campo Descripcion")
            time.sleep(3)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la descripcion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            CUnidadNegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_unidadnegocioZG)))
            CUnidadNegocio.click()
            time.sleep(5)

            registro_unidadnegocio = self.driver.find_element(By.XPATH, "//span[text()='PM01']")

            action = ActionChains(self.driver)
            action \
                .move_to_element(registro_unidadnegocio) \
                .pause(2) \
                .double_click(registro_unidadnegocio) \
                .pause(2) \
                .release()
            action.perform()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de unidad de negocio, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            Bcuentascontables = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ctacontZG)))
            Bcuentascontables.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el botón cuentas contables, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        Registro2 = self.driver.find_element(By.XPATH, "//span[text()='prueba']")

        try:

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro2) \
                .pause(2) \
                .double_click(Registro2) \
                .pause(2) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            CTipoDoc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocZG)))
            CTipoDoc.click()
            time.sleep(5)

            registro_tipodoc = self.driver.find_element(By.XPATH, "//span[text()='PM86']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodoc) \
                .pause(2) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de tipo de documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            CCtaCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_ctacontZG)))
            CCtaCont.click()
            time.sleep(5)

            registro_ctacont = self.driver.find_element(By.XPATH, "//span[text()='prueba cambio']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ctacont) \
                .pause(2) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de cuenta contable, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            CCentroCosto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_centrocostoZG)))
            CCentroCosto.click()
            time.sleep(5)

            registro_centrocosto = self.driver.find_element(By.XPATH, "//span[text()='prueba cambio']")

            action = ActionChains(self.driver)
            action \
                .double_click(registro_centrocosto) \
                .pause(2) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de centro costo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            GuardarCtasCont = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_aceptactacontZG)))
            GuardarCtasCont.click()
            time.sleep(5)
            Log().info(" Se presiona el boton 'Aceptar', para guardar el registro.")

        except Exception as e:
            Log().error("No se encontró el botón Aceptar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(3)

        except Exception as e:
            Log().error("No se encontró el botón Guardar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.close()
            raise
