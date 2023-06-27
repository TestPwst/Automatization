from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.log import Log
from common.globalparam import img_path
import os
import time


class nuevoregistro:

    def nuevoregistro(self, conditions, Configuracion):
        """Abre la ventana para crear un nuevo registro"""
        self.wait = WebDriverWait(self.driver, 60)

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta
        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("ARQUITECTURA DE CLIENTES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CUnidadNegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_unidadnegocio)))
            CUnidadNegocio.click()

            registro_unidadnegocio = self.wait.until(conditions.visibility((By.XPATH, "//span[text()= 'PM01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_unidadnegocio) \
                .pause(0) \
                .release()
            action.perform()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se encontró el registro de unidad de negocio, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña segundo nivel y agregar nuevo

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

        try:
            Nuevo2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_segundonivel)))
            Nuevo2.click()
            Log().info(" Se presiona el boton de segundo nivel 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón de segundo nivel Nuevo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Ccodigosegundo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_segundonivel)))
            Ccodigosegundo.send_keys(Configuracion.Icodigosegundo)
            Log().info(" Ingresa el codigo del nuevo registro en segundo nivel")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo de segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoaltersegundo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter_segundonivel)))
            Ccodigoaltersegundo.send_keys(Configuracion.Icodigoaltersegundo)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en segundo nivel ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo del segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionsegundo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion_segundonivel)))
            Cdescripcionsegundo.send_keys(Configuracion.Idescripcionsegundo)
            Log().info(" Ingresa la descripción del nuevo registro del segundo nivel")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion del segundo nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña tercer nivel y agregar nuevo

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

        try:
            Nuevo3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_tercernivel)))
            Nuevo3.click()
            Log().info(" Se presiona el boton 'Nuevo' de tercer nivel, para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Ccodigotercero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_tercernivel)))
            Ccodigotercero.send_keys(Configuracion.Icodigotercero)
            Log().info(" Ingresa el codigo del nuevo registro en tercer nivel")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoaltertercero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter_tercernivel)))
            Ccodigoaltertercero.send_keys(Configuracion.Icodigoaltertercero)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en tercer nivel ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo de tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripciontercero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion_tercernivel)))
            Cdescripciontercero.send_keys(Configuracion.Idescripciontercero)
            Log().info(" Ingresa la descripción del nuevo registro del tercer nivel")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion del tercer nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña cuarto nivel y agregar nuevo

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

        try:
            Nuevo4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_cuartonivel)))
            Nuevo4.click()
            Log().info(" Se presiona el boton 'Nuevo' de cuarto nivel, para crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Nuevo de cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingresar los valores

        try:
            Ccodigocuarto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_cuartonivel)))
            Ccodigocuarto.send_keys(Configuracion.Icodigocuarto)
            Log().info(" Ingresa el codigo del nuevo registro en cuarto nivel")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo de cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoaltercuarto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter_cuartonivel)))
            Ccodigoaltercuarto.send_keys(Configuracion.Icodigoaltercuarto)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en cuarto nivel ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo de cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcioncuarto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion_cuartonivel)))
            Cdescripcioncuarto.send_keys(Configuracion.Idescripcioncuarto)
            Log().info(" Ingresa la descripción del nuevo registro del cuarto nivel")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion del cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda4 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_cuarto)))
            Guarda4.click()
            Log().info(" Se da clic en el boton Guardar de cuarto nivel; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se encontró el botón Guardar de cuarto nivel, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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
