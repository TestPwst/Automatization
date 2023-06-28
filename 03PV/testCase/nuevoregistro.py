from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
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
            self.assertEqual("POLÍTICAS DE VENTA : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado, que el nombre de la pantalla sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        # Valida existencia de las etiquetas
        try:
            Codigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo))).text
            self.assertEqual("Código", Codigo, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Codigo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            CodigoAlter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo_alter))).text
            self.assertEqual("Código Alternativo", CodigoAlter, "Campo visible")
            Log().info(" El campo 'Codigo Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Codigo Alternativo' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Descripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcion))).text
            self.assertEqual("Descripción", Descripcion, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Descripción' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Moneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_moneda))).text
            self.assertEqual("Moneda", Moneda, "Campo visible")
            Log().info(" El campo 'Moneda' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Moneda' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Aplicableen = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_aplicableen))).text
            self.assertEqual("Aplicable en", Aplicableen, "Campo visible")
            Log().info(" El campo 'Aplicable en' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Aplicable en' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Activa = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_activa))).text
            self.assertEqual("Activa", Activa, "Campo visible")
            Log().info(" El campo 'Activa' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Activa' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Apliglobal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_apliglobal))).text
            self.assertEqual("Aplicación Global", Apliglobal, "Campo visible")
            Log().info(" El campo 'Aplicación Global' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Aplicación Global' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo_alter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Cmoneda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_moneda)))
            Cmoneda.click()

            registro_moneda = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PESO MEXICANO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_moneda) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió doble click en el registro de Moneda.")

        except Exception as e:
            Log().error("No se encontró el registro de Moneda, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Caplicableen = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_aplicableen)))
            Caplicableen.click()

            registro_aplicableen = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='BackOffice y Mobile']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_aplicableen) \
                .pause(0) \
                .release()
            action.perform()
            Log().info(" Se dió click en la opción BackOffice y Mobile .")

        except Exception as e:
            Log().error("No se dió click en la opción BackOffice y Mobile, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Cactiva = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_activa)))
            Cactiva.click()
            Log().info(" Se dió click en el checkbox Activa.")

        except Exception as e:
            Log().error("No se dió click en el chekcbox Activa, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Capliglobal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_apliglobal)))
            Capliglobal.click()
            Log().info(" Se dió click en el checkbox Aplicación Global.")

        except Exception as e:
            Log().error("No se dií click en el checkbox Aplicación Global, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        # Cambio de pestaña y agregar nuevo

        try:
            Bporarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_porarticulo)))
            Bporarticulo.click()
            Log().info("Se hace el cambio a la pestaña Por Articulo para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dio click en el botón Por Articulo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Nuevoporarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_porarticulo)))
            Nuevoporarticulo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro de Por Articulo.")

        except Exception as e:
            Log().error("No se dió click en el botón Nuevo, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

            # Valida la existencia de las etiquetas

        try:
            Grupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_grupopolitica))).text
            self.assertEqual("Grupo Política", Grupopolitica, "Campo visible")
            Log().info(" El campo 'Grupo Política' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Grupo Política' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Grupoabonificar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_grupoabonificar))).text
            self.assertEqual("Grupo Política a Bonificar", Grupoabonificar, "Campo visible")
            Log().info(" El campo 'Grupo Política a Bonificar' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Grupo Política a Bonificar' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Cantidadabonificar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cantidadabonificar))).text
            self.assertEqual("Cantidad a Bonificar(Packing)", Cantidadabonificar, "Campo visible")
            Log().info(" El campo 'Cantidad a Bonificar(Packing)' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cantidad a Bonificar(Packing)' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Cantidadenbonificacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cantidadenbonificacion))).text
            self.assertEqual("Cantidad en Bonificación(Unidad)", Cantidadenbonificacion, "Campo visible")
            Log().info(" El campo 'Cantidad en Bonificación(Unidad)' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Cantidad en Bonificación(Unidad)' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Topedescuento1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_topedescuento1))).text
            self.assertEqual("Tope Descuento 1", Topedescuento1, "Campo visible")
            Log().info(" El campo 'Tope Descuento 1' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tope Descuento 1' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Topedescuento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_topedescuento2))).text
            self.assertEqual("Tope Descuento 2", Topedescuento2, "Campo visible")
            Log().info(" El campo 'Tope Descuento 2' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Tope Descuento 2' no se muestra visible, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

            # ingresar los valores

        try:
            Cgrupopolitica = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_grupopolitica)))
            Cgrupopolitica.send_keys(Configuracion.Igrupopolitica)
            Log().info(" Ingresa el Grupo Politica del nuevo registro ")
            time.sleep(2)

        except Exception as e:
            Log().error("No se encontró el campo para ingresar el Grupo Politica, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Cgrupoabonificar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_grupoabonificar)))
            Cgrupoabonificar.send_keys(Configuracion.Igrupoabonif)
            Log().info(" Ingresa el Grupo a bonificar del nuevo registro ")
            time.sleep(2)

        except Exception as e:
            Log().error("No se encontró el campo para Grupo a Bonificar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Ccantidadabonif = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadabonificar)))
            Ccantidadabonif.send_keys(Configuracion.Icantidadabonificar)
            Log().info(" Ingresa la Cantidad a Bonificar del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Cantidad a Bonificar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Ccantidadenbonificacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_cantidadenbonificacion)))
            Ccantidadenbonificacion.send_keys(Configuracion.Icantidadenbonificacion)
            Log().info(" Ingresa la Cantidad en Bonificación del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la Cantidad en Bonificacion, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Ctopedescuento1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_topedescuento1)))
            Ctopedescuento1.send_keys(Configuracion.Itopedescuento1)
            Log().info(" Ingresa el Tope Descuento 1 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el tope descuento 1, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Ctopedescuento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_topedescuento2)))
            Ctopedescuento2.send_keys(Configuracion.Itopedescuento2)
            Log().info(" Ingresa el Tope Descuento 2 del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el tope descuento 2, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Guardarporarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_porarticulo)))
            Guardarporarticulo.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro de Pr Articulo.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dió click en el botón Guardar, validar que la acción anterior haya finalizado, que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return false
