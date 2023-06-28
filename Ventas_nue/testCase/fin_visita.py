import os
import time
import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import Log
from config import Configuracion
from common.globalparam import img_path

class fin_visita:
    def fin_visita(self):
        try:
            # seleccionar cliente
            cliente = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[1]")
                )
            )
            cliente.click()
        except Exception as e:
            Log().error("No se pudo seleccionar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise
        try:
            # nuevo documento
            nuevo = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]")
                )
            )
            nuevo.click()

            # inicio de visita
            fin_visita = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[2]")
                )
            )
            fin_visita.click()

            # rubro de visita
            #rubro_visita = WebDriverWait(self, 100).until(
            #        EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[5]")
            #    )
            #)
            #rubro_visita.click()

            # seleccionar rubro
            #seleccionar_rubro = WebDriverWait(self, 100).until(
            #        EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
            #    )
            #)
            #seleccionar_rubro.click()

            # ocultar teclado
            #self.hide_keyboard()

            # Boton guardar
            btn_guardar =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
                )
            )
            btn_guardar.click()
        except Exception as e:
            Log().error("No se pudo crear el final de visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise
        try:
            time.sleep(90)
            self.back()
            salir =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]")
                )
            )
            salir.click()
        except Exception as e:
            Log().error("No se pudo salir de la aplicacion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

if __name__ == '__main__':
	unittest.main()