from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.log import Log
from common.globalparam import img_path
import os
import time
from importlib.machinery import SourceFileLoader
from config import conditions
from config import Configuracion

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral

class buscador:

    def buscador(self):
        self.wait = WebDriverWait(self.driver, 60)
        # Da clic en cerrar
        # Abre la pantalla
        try:
            BBuscador = self.wait.until(conditions.visibility((By.XPATH, configgnral.Buscador)))
            BBuscador.click()
            IBuscador = self.wait.until(conditions.visibility((By.XPATH, configgnral.input_buscador)))
            IBuscador.send_keys(Configuracion.Iopcionbuscador)

            registro_buscador = self.wait.until(conditions.visibility((By.XPATH, Configuracion.texto_buscador)))

            action = ActionChains(self.driver)
            action \
                .click(registro_buscador) \
                .pause(0) \
                .release()
            action.perform()
            Log().info("Se ingreso a la pantalla mediante el buscador porque fallo el ingreso por menus")

        except Exception as e:
            Log().error("No se pudo ingresar por medio del buscador, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

