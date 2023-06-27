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
            self.assertEqual("ARQUITECTURA DE PRODUCTO : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos en la pestaña general.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro en la pestaña general")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo en la pestaña general, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalt)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalt)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en la pestaña general")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo en la pestaña general, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.send_keys(Configuracion.Idescripcion)
            Log().info(" Ingresa la descripción del nuevo registro en la pestaña general")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error("No se pudo ingresar el campo descripcion en la pestaña general, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y agregar nuevo

        try:
            Bmarcas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_marcas)))
            Bmarcas.click()
            Log().info("Se hace el cambio a la pestaña marcas para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dio click al botón marcas, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevomarcas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_nuevomarcas)))
            Nuevomarcas.click()
            Log().info(" Se presiona el boton 'Nuevo' en marcas, para continuar con el registro nuevo.")

        except Exception as e:
            Log().error("No se dio click al botón Nuevo en marcas, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos en la pestaña marcas.

        try:
            CcodigoM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoM)))
            CcodigoM.send_keys(Configuracion.IcodigoM)
            Log().info(" Ingresa el codigo del nuevo registro en la pestaña marcas")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo en la pestaña marcas, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CcodigoalterM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoaltM)))
            CcodigoalterM.send_keys(Configuracion.IcodigoaltM)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en la pestaña marcas")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo alternativo en la pestaña marcas, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CdescripcionM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionM)))
            CdescripcionM.send_keys(Configuracion.IdescripcionM)
            Log().info(" Ingresa la descripción del nuevo registro en la pestaña marcas")

        except Exception as e:
            Log().error("No se pudo ingresar el campo descripcion en la pestaña marcas, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña y agregar nuevo

        try:
            Bfamilias = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_fam)))
            Bfamilias.click()
            Log().info("Se hace el cambio a la pestaña familias para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dio click al botón familias, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevofam = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_nuevofam)))
            Nuevofam.click()
            Log().info(" Se presiona el boton 'Nuevo' en familias, para continuar con el registro nuevo.")

        except Exception as e:
            Log().error("No se dio click al botón Nuevo en familias, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos en la pestaña familias

        try:
            CcodigoF = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoF)))
            CcodigoF.send_keys(Configuracion.IcodigoF)
            Log().info(" Ingresa el codigo del nuevo registro en la pestaña familias")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo en la pestaña familias, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CcodigoalterF = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoaltF)))
            CcodigoalterF.send_keys(Configuracion.IcodigoaltF)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en la pestaña familias")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo alternativo en la pestaña familias, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CdescripcionF = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionF)))
            CdescripcionF.send_keys(Configuracion.IdescripcionF)
            Log().info(" Ingresa la descripción del nuevo registro en la pestaña familias")

        except Exception as e:
            Log().error("No se pudo ingresar el campo descripcion en la pestaña familias, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se hace el cambio a la pestaña géneros

        try:
            Bgeneros = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_gen)))
            Bgeneros.click()
            Log().info("Se hace el cambio a la pestaña géneros para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dio click el botón generos, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevogen = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_nuevogen)))
            Nuevogen.click()
            Log().info(" Se presiona el boton 'Nuevo' en géneros, para continuar con el registro nuevo.")

        except Exception as e:
            Log().error("No se dio click el botón Nuevo en géneros, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se ingresan los datos a los campos de la pestaña género

        try:
            CcodigoG = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoG)))
            CcodigoG.send_keys(Configuracion.IcodigoG)
            Log().info(" Ingresa el codigo del nuevo registro en la pestaña géneros")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo en la pestaña géneros, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CcodigoalterG = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoaltG)))
            CcodigoalterG.send_keys(Configuracion.IcodigoaltG)
            Log().info(" Ingresa el codigo alternativo del nuevo registro en la pestaña géneros")

        except Exception as e:
            Log().error("No se pudo ingresar el campo codigo alternativo en la pestaña géneros, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            CdescripcionG = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionG)))
            CdescripcionG.send_keys(Configuracion.IdescripcionG)
            Log().info(" Ingresa la descripción del nuevo registro en la pestaña géneros")

        except Exception as e:
            Log().error("No se pudo ingresar el campo descripcion en la pestaña géneros, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Guarda el registro
        try:
            GuardaG = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_GuardaG)))
            GuardaG.click()
            Log().info(" Se da clic en el boton Guardar Genero; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dio click al botón Guardar Genero, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardaF = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_GuardaF)))
            GuardaF.click()
            Log().info(" Se da clic en el boton Guardar Familia; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dio click al botón Guardar Familia, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            GuardaM = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_GuardaM)))
            GuardaM.click()
            Log().info(" Se da clic en el boton Guardar Marca; se debe crear un nuevo registro.")

        except Exception as e:
            Log().error("No se dio click al botón Guardar Marca, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
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
            Log().error("No se dio click al botón Guardar, validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
            time.sleep(2)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
