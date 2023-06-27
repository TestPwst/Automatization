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
            self.assertEqual("CUENTAS CONTABLES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
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
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_usuario)))
            Ccodigousuario.send_keys(Configuracion.Icodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo usuario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
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
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CTipomoneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipomoneda)))
            CTipomoneda.click()

            registro_tipomoneda = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Nacional']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipomoneda) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción Nacional.")

        except Exception as e:
            Log().error("No se dió click en la opción Nacional, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CPerdidas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_perdidas)))
            CPerdidas.click()

            registro_perdida = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div[1]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_perdida) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Perdidas.")

        except Exception as e:
            Log().error("No se encontró el registro de Perdidas, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CGanancias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_ganancias)))
            CGanancias.click()

            registro_ganancia = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[2]/div/div[1]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_ganancia) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Ganancias.")

        except Exception as e:
            Log().error("No se encontró el registro de Ganancias, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CClasificacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_clasificacion)))
            CClasificacion.click()

            registro_clasificacion = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Prueba']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_clasificacion) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Clasificación.")

        except Exception as e:
            Log().error("No se encontró el registro de Clasificacion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CIgnorarAjuste = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_ignorarajuste)))
            CIgnorarAjuste.click()
            Log().info(" Se dió click en el checkbox Ignorar Ajuste.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox Ignorar Ajuste, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña observaciones

        try:
            Bobservaciones = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_observaciones)))
            Bobservaciones.click()
            Log().info("Se hace el cambio a la pestaña Observaciones para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón observaciones, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            CObservaciones1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observaciones1)))
            CObservaciones1.send_keys(Configuracion.Iobservacion1)
            Log().info(" Ingresa la Observación 1 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la observación 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CObservaciones2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observaciones2)))
            CObservaciones2.send_keys(Configuracion.Iobservacion2)
            Log().info(" Ingresa la Observación 2 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la observación 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CObservaciones3 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_observaciones3)))
            CObservaciones3.send_keys(Configuracion.Iobservacion3)
            Log().info(" Ingresa la Observación 3 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la observación 3, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Grupo de Centro de Costo

        try:
            Bgrupocc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_gruposcc)))
            Bgrupocc.click()
            Log().info("Se hace el cambio a la pestaña Grupo CC para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón grupocc, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevogruposcc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_gruposcc)))
            Nuevogruposcc.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Grupos CC.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

        try:
            CGruposcc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_gruposcc)))
            CGruposcc.click()

            registro_gruposcc = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Prueba  Centro de Costo']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_gruposcc) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Grups CC.")

        except Exception as e:
            Log().error("No se encontró el registro de Grupos CC, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardagruposcc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_gruposcc)))
            Guardagruposcc.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Grupos CC.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Prorrateos

        try:
            Bprorrateos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_prorrateos)))
            Bprorrateos.click()
            Log().info("Se hace el cambio a la pestaña Prorrateos para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click en el botón prorrateos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoprorrateos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_prorrateos)))
            Nuevoprorrateos.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Prorrateos.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa los datos

        try:
            Cprorrateos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_prorrateos)))
            Cprorrateos.click()

            registro_prorrateos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Prueba']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_prorrateos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Prorrateos.")

        except Exception as e:
            Log().error("No se encontró el registro de Prorrateos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CDefecto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_defecto)))
            CDefecto.click()
            Log().info(" Se dió click en el checkbox defecto.")

        except Exception as e:
            Log().error("No se dió click en el checkbox Defecto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaprorrateos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_prorrateos)))
            Guardaprorrateos.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro de Prorrateos.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió clcik en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
