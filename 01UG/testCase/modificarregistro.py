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
            Log().info(" Se presiona el boton 'Refrescar', para crear un nuevo registro igual al anterior.")
            time.sleep(2)

        except Exception as e:
            Log().error(
                "No se dió click al botón Refrescar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Busca Registro

        try:
            Buscaregistro = self.wait.until(conditions.visibility((By.XPATH, Configuracion.buscar_registro)))
            Buscaregistro.click()
            time.sleep(1)
            Buscaregistro.click()
            Log().info(" Se presiona el boton 'Codigo', para buscar  un nuevo registro y poder modificarlo.")


        except Exception as e:
            Log().error(
                "No se dió click al botón codigo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100']")))

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
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativo)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
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
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
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
            Cviviendas.clear()
            Cviviendas.send_keys(Configuracion.Mviviendas)
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
            Chogares.clear()
            Chogares.send_keys(Configuracion.Mhogares)
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
            Chombres.clear()
            Chombres.send_keys(Configuracion.Mhombres)
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
            Cmujeres.clear()
            Cmujeres.send_keys(Configuracion.Mmujeres)
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
            Cpoblaciontotal.clear()
            Cpoblaciontotal.send_keys(Configuracion.Mptotal)
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
            Ccodigoiso.clear()
            Ccodigoiso.send_keys(Configuracion.Mcodigoiso)
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
            Registrodepartamentos = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='101']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrodepartamentos) \
                .pause(0) \
                .double_click(Registrodepartamentos) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica Valores

        try:
            Ccodigoalterdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativodep)))
            Ccodigoalterdep.clear()
            Ccodigoalterdep.send_keys(Configuracion.Mcodigoalterdep)
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
            Cdescripciondep.clear()
            Cdescripciondep.send_keys(Configuracion.Mdescripciondep)
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
            
            registro_impuestodep = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IVA 8%']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuestodep) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de impuesto, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviviendasdep = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_viviendasdep)))
            Cviviendasdep.clear()
            Cviviendasdep.send_keys(Configuracion.Mviviendasdep)
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
            Chogaresdep.clear()
            Chogaresdep.send_keys(Configuracion.Mhogaresdep)
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
            Chombresdep.clear()
            Chombresdep.send_keys(Configuracion.Mhombresdep)
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
            Cmujeresdep.clear()
            Cmujeresdep.send_keys(Configuracion.Mmujeresdep)
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
            Cpoblaciontotaldep.clear()
            Cpoblaciontotaldep.send_keys(Configuracion.Mptotaldep)
            Log().info(" Ingresa el número de Población Total del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el número de Población Total, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña localidades

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
            Registrolocalidades = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='102']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrolocalidades) \
                .pause(0) \
                .double_click(Registrolocalidades) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Ccodigoalterloc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativoloc)))
            Ccodigoalterloc.clear()
            Ccodigoalterloc.send_keys(Configuracion.Mcodigoalterloc)
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
            Cdescripcionloc.clear()
            Cdescripcionloc.send_keys(Configuracion.Mdescripcionloc)
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
            Cviviendasloc.clear()
            Cviviendasloc.send_keys(Configuracion.Mviviendasloc)
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
            Chogaresloc.clear()
            Chogaresloc.send_keys(Configuracion.Mhogaresloc)
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
            Chombresloc.clear()
            Chombresloc.send_keys(Configuracion.Mhombresloc)
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
            Cmujeresloc.clear()
            Cmujeresloc.send_keys(Configuracion.Mmujeresloc)
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
            Cpoblaciontotalloc.clear()
            Cpoblaciontotalloc.send_keys(Configuracion.Mptotalloc)
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
            Registrobarrios = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='103']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registrobarrios) \
                .pause(0) \
                .double_click(Registrobarrios) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modifica Valores

        try:
            Ccodigoalterbar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_alternativobar)))
            Ccodigoalterbar.clear()
            Ccodigoalterbar.send_keys(Configuracion.Mcodigoalterbar)
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
            Cdescripcionbar.clear()
            Cdescripcionbar.send_keys(Configuracion.Mdescripcionbar)
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
            Cviviendasbar.clear()
            Cviviendasbar.send_keys(Configuracion.Mviviendasbar)
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
            Chogaresbar.clear()
            Chogaresbar.send_keys(Configuracion.Mhogaresbar)
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
            Chombresbar.clear()
            Chombresbar.send_keys(Configuracion.Mhombresbar)
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
            Cmujeresbar.clear()
            Cmujeresbar.send_keys(Configuracion.Mmujeresbar)
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
            Cpoblaciontotalbar.clear()
            Cpoblaciontotalbar.send_keys(Configuracion.Mptotalbar)
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
            Registroimpuestoarticulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='40041615']")))

            action = ActionChains(self.driver)
            action \
                .move_to_element(Registroimpuestoarticulo) \
                .pause(0) \
                .double_click(Registroimpuestoarticulo) \
                .pause(0) \
                .release()
            action.perform()

            Log().info(" Se da clic en el registro creado, para proceder a modificarlo.")

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Modificamos Registro

        try:
            Carticulo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_articulo)))
            Carticulo.click()

            registro_articulo = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='40041602']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_articulo) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de articulo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cimpuestoart = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_impuestoart)))
            Cimpuestoart.click()

            registro_impuestoart = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='IVA 8%']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_impuestoart) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de articulo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe modificar la informacion del registro.")
            time.sleep(1)
            
        except Exception as e:
            Log().error("No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False