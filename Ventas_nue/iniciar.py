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
from appium.webdriver.common.touch_action import TouchAction

class iniciar:
    def iniciar(self):
        try:
            usuario = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@content-desc='Usuario']")
                )
            )
            usuario.send_keys(Configuracion.usuario)
            contraseña = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@content-desc='Contraseña']")
                )
            )
            contraseña.send_keys(Configuracion.contrasena)
            servidor = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@content-desc='Servidor']")
                )
            )
            servidor.send_keys(Configuracion.servidor)
            ssl = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox")
                )
            )
            ssl.click()
            iniciar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[2]")
                )
            )
            iniciar.click()
            Log().info("Se instalo la aplicacion.")
            time.sleep(3)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
        except Exception as e:
            Log().error("No se pudo instalar la aplicacion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise
        """
        try:
            #driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[5]
            btn_config = WebDriverWait(self, 500).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[5]")
                )
            )
            btn_config.click()
            self.hide_keyboard()
            servidor = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[3]")
                )
            )
            servidor.click()
            self.hide_keyboard()
            servidor.clear()
            servidor.send_keys(Configuracion.servidor)
            check = WebDriverWait(self, 100).until(
                   EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.CheckBox")
               )
            )
            #check.click()
            button = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[2]")
                )
            )
            button.click()
            #/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button
            #/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button
            aceptar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button")
                )
            )
            aceptar.click()
            #/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout
            Log().info("Se realizo la configuracion.")
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
        """

        try:
            cargar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, Configuracion.cargar)
                )
            )
            cargar.click()
            
            aceptarCarga = WebDriverWait(self, 1000).until(
                    EC.element_to_be_clickable((By.XPATH, Configuracion.aceptar)
                )
            )
            aceptarCarga.click()

            aceptarreinicio = WebDriverWait(self, 1000).until(
                EC.element_to_be_clickable((By.XPATH, Configuracion.aceptarreinicio)
                                           )
            )
            aceptarreinicio.click()
            
            Log().info("Se cargo el dispositivo.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
        except Exception as e:
            Log().error("No se pudo cargar el dispositivo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise
        try:
            iniciar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]")
                )
            )
            iniciar.click()

            confirmar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[1]")
                )
            )
            confirmar.click()

            #/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button
            #/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout

            #aceptar = WebDriverWait(self, 100).until(
            #        EC.visibility_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button")
            #    )
            #)

            #aceptar.click()

            #self.back()
            # self.back()
            # self.back()
            # self.back()
            # self.back()

            #actions = TouchAction(self).tap(aceptar).perform()

            #self.back()

            Log().info("Se inicio la aplicacion.")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
        except Exception as e:
            Log().error("No se pudo iniciar la aplicacion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise