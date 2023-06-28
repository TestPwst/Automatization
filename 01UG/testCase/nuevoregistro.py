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
            self.assertEqual("PAÍSES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error(
                "La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de las etiquetas
        try:
            Codigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo))).text
            self.assertEqual("Código", Codigo, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Codigo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_alternativo))).text
            self.assertEqual("Alternativo", Codigoalter, "Campo visible")
            Log().info(" El campo 'Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Alternativo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcion))).text
            self.assertEqual("Descripción", Descripcion, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Viviendas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_viviendas))).text
            self.assertEqual("Viviendas", Viviendas, "Campo visible")
            Log().info(" El campo 'Viviendas' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Viviendas' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hogares = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hogares))).text
            self.assertEqual("Hogares Particulares", Hogares, "Campo visible")
            Log().info(" El campo 'Hogares Particulares' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Hogares Particulares' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hombres = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionhombres))).text
            self.assertEqual("Población Hombres", Hombres, "Campo visible")
            Log().info(" El campo 'Población Hombres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Hombres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Mujeres = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionmujeres))).text
            self.assertEqual("Población Mujeres", Mujeres, "Campo visible")
            Log().info(" El campo 'Población Mujeres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Mujeres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Poblaciontotal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblaciontotal))).text
            self.assertEqual("Población Total", Poblaciontotal, "Campo visible")
            Log().info(" El campo 'Población Total' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Total' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoiso))).text
            self.assertEqual("Código ISO 3166", Codigoiso, "Campo visible")
            Log().info(" El campo 'Código ISO 3166' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código ISO 3166' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativo)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviviendas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viviendas)))
            Cviviendas.send_keys(Configuracion.Iviviendas)
            Log().info(" Ingresa el número de viviendas del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de viviendas, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chogares = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hogares)))
            Chogares.send_keys(Configuracion.Ihogares)
            Log().info(" Ingresa el número de hogares particulares del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de hogares particulares, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chombres = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionhombres)))
            Chombres.send_keys(Configuracion.Ihombres)
            Log().info(" Ingresa el número de Población de hombres del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de hombres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmujeres = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionmujeres)))
            Cmujeres.send_keys(Configuracion.Imujeres)
            Log().info(" Ingresa el número de Población de mujeres del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de mujeres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpoblaciontotal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblaciontotal)))
            Cpoblaciontotal.send_keys(Configuracion.Iptotal)
            Log().info(" Ingresa el número de Población Total del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población Total, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoiso = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoiso)))
            Ccodigoiso.send_keys(Configuracion.Icodigoiso)
            Log().info(" Ingresa el Codigo ISO del nuevo registro ")
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Codigo ISO, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña departamentos

        try:
            Bdepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_departamentos)))
            Bdepartamentos.click()
            time.sleep(1)
            Bdepartamentos.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
        
        except Exception as e:
            Log().error(
                "No se dió click al botón Departamentos, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevodepartamento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_departamento)))
            Nuevodepartamento.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida existencia de las etiquetas

        try:
            Codigodep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigodep))).text
            self.assertEqual("Código", Codigodep, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Codigo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalterdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_alternativodep))).text
            self.assertEqual("Alternativo", Codigoalterdep, "Campo visible")
            Log().info(" El campo 'Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Alternativo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripciondep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripciondep))).text
            self.assertEqual("Descripción", Descripciondep, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Impuestodep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_impuestodep))).text
            self.assertEqual("Impuesto", Impuestodep, "Campo visible")
            Log().info(" El campo 'Impuesto' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Impuesto' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Viviendasdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_viviendasdep))).text
            self.assertEqual("Viviendas", Viviendasdep, "Campo visible")
            Log().info(" El campo 'Viviendas' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Viviendas' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hogaresdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hogaresdep))).text
            self.assertEqual("Hogares Particulares", Hogaresdep, "Campo visible")
            Log().info(" El campo 'Hogares Particulares' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Hogares Particulares' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hombresdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionhombresdep))).text
            self.assertEqual("Población Hombres", Hombresdep, "Campo visible")
            Log().info(" El campo 'Población Hombres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Hombres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Mujeresdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionmujeresdep))).text
            self.assertEqual("Población Mujeres", Mujeresdep, "Campo visible")
            Log().info(" El campo 'Población Mujeres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Mujeres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Poblaciontotaldep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblaciontotaldep))).text
            self.assertEqual("Población Total", Poblaciontotaldep, "Campo visible")
            Log().info(" El campo 'Población Total' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Total' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigodep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigodep)))
            Ccodigodep.send_keys(Configuracion.Icodigodep)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalterdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativodep)))
            Ccodigoalterdep.send_keys(Configuracion.Icodigoalterdep)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripciondep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripciondep)))
            Cdescripciondep.send_keys(Configuracion.Idescripciondep)
            Log().info(" Ingresa la descripción del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpuestodep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuestodep)))
            Cimpuestodep.click()
            
            registro_impuestodep = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IVA 16%']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuestodep) \
                .pause(0) \
                .release()
            action.perform()
            
        except Exception as e:
            Log().error(
                "No se encontró el registro de impuesto, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviviendasdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viviendasdep)))
            Cviviendasdep.send_keys(Configuracion.Iviviendasdep)
            Log().info(" Ingresa el número de viviendas del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de viviendas, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chogaresdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hogaresdep)))
            Chogaresdep.send_keys(Configuracion.Ihogaresdep)
            Log().info(" Ingresa el número de hogares particulares del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de hogares particulares, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chombresdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionhombresdep)))
            Chombresdep.send_keys(Configuracion.Ihombresdep)
            Log().info(" Ingresa el número de Población de hombres del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de hombres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmujeresdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionmujeresdep)))
            Cmujeresdep.send_keys(Configuracion.Imujeresdep)
            Log().info(" Ingresa el número de Población de mujeres del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de mujeres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpoblaciontotaldep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblaciontotaldep)))
            Cpoblaciontotaldep.send_keys(Configuracion.Iptotaldep)
            Log().info(" Ingresa el número de Población Total del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población Total, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Cambio pestaña localidades

        try:
            Blocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_localidades)))
            Blocalidades.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Localidades, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevolocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_localidades)))
            Nuevolocalidades.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de etiquetas

        try:
            Localidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_localidad))).text
            self.assertEqual("Localidad", Localidad, "Campo visible")
            Log().info(" El campo 'Localidad' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Localidad' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalterloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_alternativoloc))).text
            self.assertEqual("Alternativo", Codigoalterloc, "Campo visible")
            Log().info(" El campo 'Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Alternativo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcionloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcionloc))).text
            self.assertEqual("Descripción", Descripcionloc, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Viviendasloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_viviendasloc))).text
            self.assertEqual("Viviendas", Viviendasloc, "Campo visible")
            Log().info(" El campo 'Viviendas' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Viviendas' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hogaresloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hogaresloc))).text
            self.assertEqual("Hogares Particulares", Hogaresloc, "Campo visible")
            Log().info(" El campo 'Hogares Particulares' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Hogares Particulares' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hombresloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionhombresloc))).text
            self.assertEqual("Población Hombres", Hombresloc, "Campo visible")
            Log().info(" El campo 'Población Hombres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Hombres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Mujeresloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionmujeresloc))).text
            self.assertEqual("Población Mujeres", Mujeresloc, "Campo visible")
            Log().info(" El campo 'Población Mujeres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Mujeres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Poblaciontotalloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblaciontotalloc))).text
            self.assertEqual("Población Total", Poblaciontotalloc, "Campo visible")
            Log().info(" El campo 'Población Total' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Total' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigoloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoloc)))
            Ccodigoloc.send_keys(Configuracion.Icodigoloc)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalterloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativoloc)))
            Ccodigoalterloc.send_keys(Configuracion.Icodigoalterloc)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionloc)))
            Cdescripcionloc.send_keys(Configuracion.Idescripcionloc)
            Log().info(" Ingresa la descripción del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviviendasloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viviendasloc)))
            Cviviendasloc.send_keys(Configuracion.Iviviendasloc)
            Log().info(" Ingresa el número de viviendas del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de viviendas, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chogaresloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hogaresloc)))
            Chogaresloc.send_keys(Configuracion.Ihogaresloc)
            Log().info(" Ingresa el número de hogares particulares del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de hogares particulares, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chombresloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionhombresloc)))
            Chombresloc.send_keys(Configuracion.Ihombresloc)
            Log().info(" Ingresa el número de Población de hombres del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de hombres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmujeresloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionmujeresloc)))
            Cmujeresloc.send_keys(Configuracion.Imujeresloc)
            Log().info(" Ingresa el número de Población de mujeres del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de mujeres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpoblaciontotalloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblaciontotalloc)))
            Cpoblaciontotalloc.send_keys(Configuracion.Iptotalloc)
            Log().info(" Ingresa el número de Población Total del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población Total, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio Pestaña Barrios

        try:
            Bbarrios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_barrios)))
            Bbarrios.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Barrios, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevobarrios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_barrios)))
            Nuevobarrios.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de etiquetas

        try:
            Codigobar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigobar))).text
            self.assertEqual("Código", Codigobar, "Campo visible")
            Log().info(" El campo 'Código' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalterbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_alternativobar))).text
            self.assertEqual("Alternativo", Codigoalterbar, "Campo visible")
            Log().info(" El campo 'Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Alternativo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Descripcionbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_descripcionbar))).text
            self.assertEqual("Descripción", Descripcionbar, "Campo visible")
            Log().info(" El campo 'Descrición' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Descripción' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Viviendasbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_viviendasbar))).text
            self.assertEqual("Viviendas", Viviendasbar, "Campo visible")
            Log().info(" El campo 'Viviendas' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Viviendas' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hogaresbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hogaresbar))).text
            self.assertEqual("Hogares Particulares", Hogaresbar, "Campo visible")
            Log().info(" El campo 'Hogares Particulares' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Hogares Particulares' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hombresbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionhombresbar))).text
            self.assertEqual("Población Hombres", Hombresbar, "Campo visible")
            Log().info(" El campo 'Población Hombres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Hombres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Mujeresbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblacionmujeresbar))).text
            self.assertEqual("Población Mujeres", Mujeresbar, "Campo visible")
            Log().info(" El campo 'Población Mujeres' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Mujeres' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Poblaciontotalbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_poblaciontotalbar))).text
            self.assertEqual("Población Total", Poblaciontotalbar, "Campo visible")
            Log().info(" El campo 'Población Total' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Población Total' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Se realiza el ingreso de datos en los campos.

        try:
            Ccodigobar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigobar)))
            Ccodigobar.send_keys(Configuracion.Icodigobar)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalterbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativobar)))
            Ccodigoalterbar.send_keys(Configuracion.Icodigoalterbar)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcionbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcionbar)))
            Cdescripcionbar.send_keys(Configuracion.Idescripcionbar)
            Log().info(" Ingresa la descripción del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviviendasbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viviendasbar)))
            Cviviendasbar.send_keys(Configuracion.Iviviendasbar)
            Log().info(" Ingresa el número de viviendas del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de viviendas, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chogaresbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hogaresbar)))
            Chogaresbar.send_keys(Configuracion.Ihogaresbar)
            Log().info(" Ingresa el número de hogares particulares del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de hogares particulares, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chombresbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionhombresbar)))
            Chombresbar.send_keys(Configuracion.Ihombresbar)
            Log().info(" Ingresa el número de Población de hombres del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de hombres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmujeresbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblacionmujeresbar)))
            Cmujeresbar.send_keys(Configuracion.Imujeresbar)
            Log().info(" Ingresa el número de Población de mujeres del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población de mujeres, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpoblaciontotalbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_poblaciontotalbar)))
            Cpoblaciontotalbar.send_keys(Configuracion.Iptotalbar)
            Log().info(" Ingresa el número de Población Total del nuevo registro ")
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población Total, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardabarrios = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_barrios)))
            Guardabarrios.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardalocalidades = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_localidades)))
            Guardalocalidades.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambia pestaña impuestos por articulo

        try:
            Bimpuestosarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_impuestoarticulo)))
            Bimpuestosarticulo.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Impuestos por Articulo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoimpuestoarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_impuestoarticulo)))
            Nuevoimpuestoarticulo.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

            # Valida existencia de etiquetas

        try:
            Articulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_articulo))).text
            self.assertEqual("Artículo", Articulo, "Campo visible")
            Log().info(" El campo 'Artículo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Artículo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Impuestoart = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_impuestoart))).text
            self.assertEqual("Impuesto", Impuestoart, "Campo visible")
            Log().info(" El campo 'Impuesto' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Impuesto' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_articulo)))
            Carticulo.click()

            registro_articulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='MONARCA CAJITA DE BOLSILLO']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_articulo) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de articulo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpuestoart = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuestoart)))
            Cimpuestoart.click()

            registro_impuestoart = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IVA 16%']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuestoart) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro de articulo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardaimpuestoarticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_impuestoarticulo)))
            Guardaimpuestoarticulo.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            time.sleep(1)
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardadepartamentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_departamentos)))
            Guardadepartamentos.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            time.sleep(1)
            
        except Exception as e:
            Log().error("No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            time.sleep(1)
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False