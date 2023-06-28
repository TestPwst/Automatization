from distutils.command.config import config
import time
from common.log import Log
from common.globalparam import img_path
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import Configuracion
from appium import webdriver

class descargar:
    def descargar(self):
        try:
            #driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[5]
            descargar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[3]")
                )
            )
            descargar.click()
            confirmar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
                )
            )
            confirmar.click()

            aceptar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button")
                )
            )
            
            aceptar.click()
            Log().info("Se descargo el movil")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
        except Exception as e:
            Log().error("No se pudo ingresar los cambios en configuracion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise