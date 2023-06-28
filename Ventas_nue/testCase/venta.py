import os
import time
from tkinter import image_types
import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import Log
from config import Configuracion
from common.globalparam import img_path

class venta:
    def venta(self):
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
            nuevo = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[1]")
                )
            )
            nuevo.click()
        except Exception as e:
            Log().error("No se pudo seleccionar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # venta contado
            venta = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.TextView[7]")
                )
            )
            venta.click()
        except Exception as e:
            Log().error("No se pudo seleccionar seleccionar la opcion de venta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            añadir = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[1]")
                )
            )
            añadir.click()

            articulo = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[1]/android.widget.TextView[1]")
                )
            )
            articulo.click()

            cantidad_input =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
                )
            )
            cantidad_input.send_keys('1')

            aceptar =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button[1]")
                )
            )
            aceptar.click()
        except Exception as e:
            Log().error("No se pudo agregar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[1]")
                )
            )
            btn_guardar.click()

            time.sleep(5)
            
            confirmar =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                )
            )
            confirmar.click()

            btn_guardar =  WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
                )
            )
            btn_guardar.click()
        except Exception as e:
            Log().error("No se pudo guardar la venta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            #Cancelar impresion
            imprimir = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[1]")
                )
            )
            imprimir.click()

            cancelar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]")
                )
            )
            cancelar.click()
        except Exception as e:
            stock = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView")
                )
            )
            if(stock.text=='No hay stock suficiente para emitir 1.0 unidades del producto BENSON & HEDGES GOLD PEARL MNT 100 BOX 20, saldo actual: 0.0'):
                Log().error("No se hay suficiente stock, para mas detalles del error consulte el reporte")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.get_screenshot_as_file(img_name)
                raise

        Log().info("Se realizo la venta")
        timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        self.get_screenshot_as_file(img_name)
            

if __name__ == '__main__':
	unittest.main()