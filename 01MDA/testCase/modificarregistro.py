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
                "No se encontró el botón Refrescar, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))
            time.sleep(1)
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='"+Configuracion.Icodigo+"']")))

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
                "No se encontró el registro, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Modifica los valores

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalter)))
            Ccodigoalter.clear()
            Ccodigoalter.send_keys(Configuracion.Mcodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el codigo alternativo, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdescripcion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_descripcion)))
            Cdescripcion.clear()
            Cdescripcion.send_keys(Configuracion.Mdescripcion)
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la descripcion, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cindicesalario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_indicesalario)))
            Cindicesalario.clear()
            Cindicesalario.send_keys(Configuracion.MIndicesalario)
        
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el indice de salario, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cincrementoipc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_incrementoipc)))
            Cincrementoipc.clear()
            Cincrementoipc.send_keys(Configuracion.MIncrementoIPC)
        
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el InvrementoIPC, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvariaciondolar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_variaciondolar)))
            Cvariaciondolar.clear()
            Cvariaciondolar.send_keys(Configuracion.MVariaciondolar)
        
        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar la variacion del dolar, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # cambio de pestaña para modificar ajustes

        try:
            Bajustes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ajustes)))
            Bajustes.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
        
        except Exception as e:
            Log().error("No se encontró el botón ajustes, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        try:
            Registro = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='7']")))

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
                "No se encontró el registro deseado, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIPCInicialajuste)))
            Cviinicial.clear()
            Cviinicial.send_keys(Configuracion.MVIPCInicial)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIPCInicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vipcfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIPCFinalajuste)))
            vipcfinal.clear()
            vipcfinal.send_keys(Configuracion.MVIPCFinal)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIPCFinal, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vimsinical = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIMSInicialajuste)))
            vimsinical.clear()
            vimsinical.send_keys(Configuracion.MVIMSInicial)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIMSInicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vimsfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIMSFinalajuste)))
            vimsfinal.clear()
            vimsfinal.send_keys(Configuracion.MVIMSFinal)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIMSFinal, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tcinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_TCInicialajuste)))
            tcinicial.clear()
            tcinicial.send_keys(Configuracion.MTCInicial)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el TCinicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tcfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_TCFinalajuste)))
            tcfinal.clear()
            tcfinal.send_keys(Configuracion.MTCFinal)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el TCFinal, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            porcentaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_Porcentajeajuste)))
            porcentaje.clear()
            porcentaje.send_keys(Configuracion.MPorcentaje)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Porcentaje, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarajustes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_ajustes)))
            Guardarajustes.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar Ajustes, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error("No se dió click al botón Guardar, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False