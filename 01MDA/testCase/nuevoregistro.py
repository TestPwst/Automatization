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
            self.assertEqual("MODELOS DE AJUSTE : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error("La pantalla ejecutada no es correcta, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                "El campo 'Codigo' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            codigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoalter))).text
            self.assertEqual("Código alternativo", codigoalter, "Campo visible")
            Log().info(" El campo 'Código alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código alternativo' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                "El campo 'Descripción' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            indicesalario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_indicesalario))).text
            self.assertEqual("Indice medio de salario", indicesalario, "Campo visible")
            Log().info(" El campo 'Indice medio de salario' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Indice medio de salario' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            incrementoipc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_incrementoipc))).text
            self.assertEqual("Incremento IPC", incrementoipc, "Campo visible")
            Log().info(" El campo 'Incremento IPC' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Incremento IPC' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            variaciondeldolar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_variaciondolar))).text
            self.assertEqual("Variación del dolar", variaciondeldolar, "Campo visible")
            Log().info(" El campo 'Variación del dolar' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'Variación del dolar' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                "No se pudo encontrar el campo para ingresar el codigo, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
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
            Cdescripcion.send_keys(Configuracion.Idescripcion)

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
            Cindicesalario.send_keys(Configuracion.Indicesalario)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el indice de salario, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cincrementoipc = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_incrementoipc)))
            Cincrementoipc.send_keys(Configuracion.IncrementoIPC)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el indice de salario, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cvariaciondolar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_variaciondolar)))
            Cvariaciondolar.send_keys(Configuracion.Variaciondolar)

        except Exception as e:
            Log().error("No se pudo encontrar el campo para ingresar el indice de salario, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # cambio de pestaña ajustes

        try:
            Bajustes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_ajustes)))
            Bajustes.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error("No se dió click al botón ajustes, validar que la acción anterior haya finalizado,"
                    "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoajustes = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_nuevo_ajustes)))
            Nuevoajustes.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")
            
        except Exception as e:
            Log().error("No se dió click al botón nuevo, validar que la acción anterior haya finalizado,"
                    "que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # validar etiquetas ajustes

        try:
            vipcinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_VIPCInicialajuste))).text
            self.assertEqual("VIPC Inicial", vipcinicial, "Campo visible")
            Log().info(" El campo 'VIPC Inicial' si se encuentra visible.")

        except Exception as e:
            Log().error("El campo 'VIPC Inicial' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vipcfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_VIPCFinalajuste))).text
            self.assertEqual("VIPC Final", vipcfinal, "Campo visible")
            Log().info(" El campo 'VIPC Final final' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'VIPC Final' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vimsinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_VIMSInicialajuste))).text
            self.assertEqual("VIMS Inicial", vimsinicial, "Campo visible")
            Log().info(" El campo 'VIMS Inicial' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'VIMS Inicial' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False
        try:
            vimsfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_VIMSFinalajuste))).text
            self.assertEqual("VIMS Final", vimsfinal, "Campo visible")
            Log().info(" El campo 'VIMS Final' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'VIMS Final' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tcinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_TCInicialajuste))).text
            self.assertEqual("TC Inicial", tcinicial, "Campo visible")
            Log().info(" El campo 'TC Inicial' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'TC Inicial' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tcfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_TCFinalajuste))).text
            self.assertEqual("TC Final", tcfinal, "Campo visible")
            Log().info(" El campo 'TC Final' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'TC Final' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            aporcentaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_Porcentajeajuste))).text
            self.assertEqual("Porcentaje", aporcentaje, "Campo visible")
            Log().info(" El campo 'Porcentaje' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Porcentaje' no se muestra visible, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # ingreso de los campos

        try:
            fechainicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fecha)))
            fechainicial.click()
            
            registro_inicial = self.wait.until(conditions.visibility((By.XPATH, "//button[text()='Hoy']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_inicial) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de la fecha inicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            fechafinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fecha2)))
            fechafinal.click()

            registro_fecha2 = self.wait.until(conditions.visibility((By.XPATH, "//html/body/div[7]/div[2]/div/div[2]/div/span[19]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_fecha2) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de la fecha final, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            fechaaplicacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_fecha3)))
            fechaaplicacion.click()

            registro_fecha3 = self.wait.until(conditions.visibility((By.XPATH, "/html/body/div[8]/div[2]/div/div[2]/div/span[18]")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_fecha3) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error("No se encontró el registro de la fecha aplicacion, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cviinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIPCInicialajuste)))
            Cviinicial.send_keys(Configuracion.VIPCInicial)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIPC inicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vipfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIPCFinalajuste)))
            vipfinal.send_keys(Configuracion.VIPCFinal)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIP final, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vimsinical = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIMSInicialajuste)))
            vimsinical.send_keys(Configuracion.VIMSInicial)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIMS inicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            vimsfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_VIMSFinalajuste)))
            vimsfinal.send_keys(Configuracion.VIMSFinal)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el VIMS final, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tcinicial = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_TCInicialajuste)))
            tcinicial.send_keys(Configuracion.TCInicial)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el TC inicial, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            tcfinal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_TCFinalajuste)))
            tcfinal.send_keys(Configuracion.TCFinal)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el TC final, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            porcentaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_Porcentajeajuste)))
            porcentaje.send_keys(Configuracion.Porcentaje)
            Log().info(" Ingresa el codigo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el porcentaje, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
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
                "No se encontró el botón Guardar Ajustes, revise si el xpath sigue siendo el mismo,validar que la acción anterior haya finalizado,"
                        "que el xpath sea el correcto o que la página no presente lentitud")
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
            Log().error(
                "No se dió click al botón Guardar, revise si el xpath sigue siendo el mismo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False