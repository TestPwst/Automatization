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
            Log().info(" Se presiona el boton 'Refrescar', para proceder a modificar el registro.")
            time.sleep(2)

        except Exception as e:
            Log().error("No se dió click en el botón Refrescar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='FA0102021']")))

        try:
            action = ActionChains(self.driver)
            action \
                .move_to_element(Registro) \
                .pause(0) \
                .double_click(Registro) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro deseado, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
            Log().info(" Se modifica el contenido del campo Codigo alternativo ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            Log().info(" Se modifica el contenido del campo Descripción ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcioncolector = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcioncolector)))
            Cdescripcioncolector.clear()
            Cdescripcioncolector.send_keys(Configuracion.Mdescripcioncolector)
            Log().info(" Se modifica el contenido del campo Descripción Colector ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Descripcion Colector, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfamilia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_familia)))
            Cfamilia.click()

            registro_familia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='DELICADOS']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_familia) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Familia ")

        except Exception as e:
            Log().error("No se encontró el registro de Familia, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigobarras = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigobarras)))
            Ccodigobarras.clear()
            Ccodigobarras.send_keys(Configuracion.Mcodigobarras)
            Log().info(" Se modifica el contenido del campo Codigo de Barras ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar el Codigo de Barras, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_packing)))
            Cpacking.click()

            registro_packing = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='SOFT PACK']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_packing) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Packing ")

        except Exception as e:
            Log().error("No se encontró el registro de Packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdiasvalidez = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_diasvalidez)))
            Cdiasvalidez.clear()
            Cdiasvalidez.send_keys(Configuracion.Mdiasvalidez)
            Log().info(" Se modifica el contenido del campo Días de Validez ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar los días de validez, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cunidadesxpacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_unidadesxpacking)))
            Cunidadesxpacking.clear()
            Cunidadesxpacking.send_keys(Configuracion.Munidadesxpacking)
            Log().info(" Se modifica el contenido del campo Unidades por Packing ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar las unidades por packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdecimalespacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_decimalespacking)))
            Cdecimalespacking.clear()
            Cdecimalespacking.send_keys(Configuracion.Mdecimalespacking)
            Log().info(" Se modifica el contenido del campo Decimales por Packing ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar los decimales de cada packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cfacturaxpacking = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_facturaxpacking)))
            Cfacturaxpacking.click()
            Log().info(" Se dió click en el checkbox Factura por Packing ")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se dió click en el checkbox Factura por packing, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Lista Precios

        try:
            Blistaprecios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_listaprecios)))
            Blistaprecios.click()
            Log().info("Se hace el cambio a la pestaña Lista de Precios para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Lista de Precios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores Lista Precios

        try:
            Cdescripcionlp = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionlp)))
            Cdescripcionlp.clear()
            Cdescripcionlp.send_keys(Configuracion.Mdescripcionlp)
            Log().info(" Se modifica el contenido del campo Descripción LP ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Descripcion LP, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Impuestos

        try:
            Bimpuestos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impuestos)))
            Bimpuestos.click()
            Log().info("Se hace el cambio a la pestaña impuestos para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón impuestos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modificando Valores Impuestos

        try:
            Cformulacpu = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_formulapu)))
            Cformulacpu.clear()
            Cformulacpu.send_keys(Configuracion.Mimpuesto)
            Log().info(" Se modifica el contenido del campo Fórmula cálculo precio unitario ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para modificar la Fórmula cálculo precio unitario, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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
                .double_click(Registroimpuestos) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se da clic en el registro de Impuestos, para proceder a modificarlo.")

        except Exception as e:
            Log().error("No se encontró el registro de la pestaña impuestos, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuesto)))
            Cimpuesto.click()

            registro_impuesto = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IMPUESTO CIGARRO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuesto) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Impuesto ")

        except Exception as e:
            Log().error("No se encontró el registro de Impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarimpuesto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impuesto)))
            Guardarimpuesto.click()
            Log().info(" Se presiona el boton 'Guardar de la pestaña impuesto', para guardar la modificación del registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar de la pestaña impuesto, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Varios

        try:
            Bvarios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_varios)))
            Bvarios.click()
            Log().info("Se hace el cambio a la pestaña Varios para continuar con la modificación del registro")

        except Exception as e:
            Log().error("No se dió click en el botón Varios, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Cclasifart1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_clasifart1)))
            Cclasifart1.click()

            registro_clasifart1 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Menthol']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_clasifart1) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Clasificación de Articulo 1 ")

        except Exception as e:
            Log().error("No se encontró el registro de Clasificación de Articulo 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Csabor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_sabor)))
            Csabor.click()

            registro_sabor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Menthol']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_sabor) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se selecciono el registro de Sabor ")

        except Exception as e:
            Log().error("No se encontró el registro de Sabor, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
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