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
            # Venta con Mecanica Bonificación
            # seleccionar cliente
            cliente = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Abarrotes San Miguel']")
                                           )
            )
            cliente.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            nuevo = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Iniciar Visita']")
                                           )
            )
            nuevo.click()
        except Exception as e:
            Log().error("No se dió click en la opcion iniciar visita")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     rubrovisita = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[5]")
        #                                    )
        #     )
        #     rubrovisita.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     rubrovisita2 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Etiqueta Dañada']")
        #                                    )
        #     )
        #     rubrovisita2.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        # try:
        #     guardarinicio = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
        #                                    )
        #     )
        #     guardarinicio.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            # preventa contado
            preventa = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Preventa de Contado']")
                                           )
            )
            preventa.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar seleccionar la opcion de preventa de Contado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            articulo = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.EditText")
                                           )
            )
            articulo.send_keys(Configuracion.articulo1)

        except Exception as e:
            Log().error(
                "No se pudo escribir el articulo a comprar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            sandwich = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
                                           )
            )
            sandwich.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el sandwich, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            mostrardescrip = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Mostrar descripción']")
                                           )
            )
            mostrardescrip.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en Mostrar descripción, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            descripcorta = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='descripción corta']")
                                           )
            )
            descripcorta.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en la opción de descripción corta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            sarticulo1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='BEBIDA VEGETAL - BVES010']")
                                           )
            )
            sarticulo1.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            cantidad_art1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_art1.clear()
            cantidad_art1.send_keys('15')

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btnaceptar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            btnaceptar.click()

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # quitar teclado
            teclado = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Encabezado']")
                                           )
            )
            teclado.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                                           )
            )
            btn_guardar.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            artmecanicabonif = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//android.widget.TextView[@text='            BEBIDA VEGETAL ALMENDRA UHT SEEDS COMBIFIT 946ML (BVES015)']")
                                           )
            )
            artmecanicabonif.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            cantidadmeca_art1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
                                           )
            )
            cantidadmeca_art1.clear()
            cantidadmeca_art1.send_keys('1')

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            aceptarmecanica = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
                                           )
            )
            aceptarmecanica.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            aceptarmecanica2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[1]")
                                           )
            )
            aceptarmecanica2.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                                           )
            )
            btn_guardar2.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton guardar, para guardar el documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_otrasmeca = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Si']")
                                           )
            )
            btn_otrasmeca.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton guardar, para guardar el documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_confirmguardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='SI']")
                                           )
            )
            btn_confirmguardar.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton para confirmar el guardado del documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     btn_imprimir = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
        #                                    )
        #     )
        #     btn_imprimir.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se pudo dar click en el boton para cancelar la impresión, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            finvisitaauto = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            finvisitaauto.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton para finalizar visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

            # Venta con mecanica de Descuento

        try:
            # seleccionar cliente
            cliente = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='La Rosita']")
                                           )
            )
            cliente.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            nuevo2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Iniciar Visita']")
                                           )
            )
            nuevo2.click()
        except Exception as e:
            Log().error("No se dió click en la opcion iniciar visita")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     rubrovisita2 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[5]")
        #                                    )
        #     )
        #     rubrovisita2.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     rubrovisita3 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Sin Etiqueta']")
        #                                    )
        #     )
        #     rubrovisita3.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     guardarinicio2 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
        #                                    )
        #     )
        #     guardarinicio2.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            # preventa contado
            preventa2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Preventa de Contado']")
                                           )
            )
            preventa2.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar seleccionar la opcion de preventa de Contado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            articulo2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.EditText")
                                           )
            )
            articulo2.send_keys(Configuracion.articulo2)

        except Exception as e:
            Log().error(
                "No se pudo escribir el articulo a comprar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            sandwich = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.ImageButton")
                                           )
            )
            sandwich.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el sandwich, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            mostrardescrip = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Mostrar descripción']")
                                           )
            )
            mostrardescrip.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en Mostrar descripción, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            descriplarga = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='descripción larga']")
                                           )
            )
            descriplarga.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en la opción de descripción larga, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            sarticulo2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//android.widget.TextView[@text='BEBIDA VEGETAL COCO UHT SEEDS COMBIFIT 946ML CHEP - BVES020']")
                                           )
            )
            sarticulo2.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            cantidad_art1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_art1.clear()
            cantidad_art1.send_keys('25')

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btnaceptar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            btnaceptar.click()

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # quitar teclado
            teclado = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Encabezado']")
                                           )
            )
            teclado.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                                           )
            )
            btn_guardar.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_otrasmeca = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Si']")
                                           )
            )
            btn_otrasmeca.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton guardar, para guardar el documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_confirmguardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='SI']")
                                           )
            )
            btn_confirmguardar.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton para confirmar el guardado del documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     btn_imprimir = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
        #                                    )
        #     )
        #     btn_imprimir.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se pudo dar click en el boton para cancelar la impresión, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            finvisitaauto = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            finvisitaauto.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton para finalizar visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

            # Venta con Mecanica de Bonificación y Descuento

        try:
            # seleccionar cliente
            cliente3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Abarrotes Los Gueros']")
                                           )
            )
            cliente3.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            nuevo3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Iniciar Visita']")
                                           )
            )
            nuevo3.click()
        except Exception as e:
            Log().error("No se dió click en la opcion iniciar visita")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     rubrovisita4 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[5]")
        #                                    )
        #     )
        #     rubrovisita4.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     rubrovisita5 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Etiqueta no accesible']")
        #                                    )
        #     )
        #     rubrovisita5.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     guardarinicio = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
        #                                    )
        #     )
        #     guardarinicio.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            # preventa contado
            preventa = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Preventa de Contado']")
                                           )
            )
            preventa.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar seleccionar la opcion de preventa de Contado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            articulo3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.EditText")
                                           )
            )
            articulo3.send_keys(Configuracion.articulo3)

        except Exception as e:
            Log().error(
                "No se pudo escribir el articulo a comprar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            sarticulo3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//android.widget.TextView[@text='BEBIDA VEGETAL ALMENDRA UHT SEEDS COMBIFIT 946ML CHEP - BVES025']")
                                           )
            )
            sarticulo3.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            cantidad_art3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_art3.clear()
            cantidad_art3.send_keys('30')

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btnaceptar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            btnaceptar.click()

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            articulo4 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.EditText")
                                           )
            )
            articulo4.clear()
            articulo4.send_keys(Configuracion.articulo1)

        except Exception as e:
            Log().error(
                "No se pudo escribir el articulo a comprar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            sarticulo4 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//android.widget.TextView[@text='BEBIDA VEGETAL COCO UHT SEEDS COMBIFIT 946ML - BVES010']")
                                           )
            )
            sarticulo4.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            cantidad_art4 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_art4.clear()
            cantidad_art4.send_keys('30')

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btnaceptar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            btnaceptar.click()

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # quitar teclado
            teclado = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Encabezado']")
                                           )
            )
            teclado.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                                           )
            )
            btn_guardar.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            artmecanicabonif2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//android.widget.TextView[@text='            BEBIDA VEGETAL ALMENDRA UHT SEEDS COMBIFIT 946ML (BVES015)']")
                                           )
            )
            artmecanicabonif2.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            cantidadmeca_art1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
                                           )
            )
            cantidadmeca_art1.clear()
            cantidadmeca_art1.send_keys('1')

        except Exception as e:
            Log().error(
                "No se pudo ingresar la cantidad en el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            aceptarmecanica = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
                                           )
            )
            aceptarmecanica.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            aceptarmecanica2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[1]")
                                           )
            )
            aceptarmecanica2.click()

        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo a bonificar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                                           )
            )
            btn_guardar2.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton guardar, para guardar el documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     btn_otrasmeca = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Si']")
        #                                    )
        #     )
        #     btn_otrasmeca.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se pudo dar click en el boton guardar, para guardar el documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            btn_confirmguardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='SI']")
                                           )
            )
            btn_confirmguardar.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton para confirmar el guardado del documento, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     btn_imprimir = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
        #                                    )
        #     )
        #     btn_imprimir.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se pudo dar click en el boton para cancelar la impresión, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            finvisitaauto = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            finvisitaauto.click()

        except Exception as e:
            Log().error(
                "No se pudo dar click en el boton para finalizar visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

            # Ventas con 5 Articulos

        try:
            # seleccionar cliente
            cliente = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='LA UNION']")
                                           )
            )
            cliente.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el cliente, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            nuevo = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Iniciar Visita']")
                                           )
            )
            nuevo.click()
        except Exception as e:
            Log().error("No se dió click en la opcion iniciar visita")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # try:
        #     rubrovisita = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[5]")
        #                                    )
        #     )
        #     rubrovisita.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     rubrovisita2 = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Etiqueta Dañada']")
        #                                    )
        #     )
        #     rubrovisita2.click()
        #
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise
        #
        # try:
        #     guardarinicio = WebDriverWait(self, 100).until(
        #         EC.element_to_be_clickable((By.XPATH,
        #                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
        #                                    )
        #     )
        #     guardarinicio.click()
        # except Exception as e:
        #     Log().error(
        #         "No se dió click en rubro visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.get_screenshot_as_file(img_name)
        #     raise

        try:
            # preventa contado
            preventa = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Preventa de Contado']")
                                           )
            )
            preventa.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar seleccionar la opcion de preventa de Contado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            menu_desplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Todos']")
                                           )
            )
            menu_desplegable.click()

            seleccion_menu = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='CREMAS']")
                                           )
            )
            seleccion_menu.click()

            # Articulo Imperdonable 1

            articulo_imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                    )
            )
            articulo_imp.click()

            cantidad_inputimp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_inputimp.clear()
            cantidad_inputimp.send_keys('5')

            aceptarimp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptarimp.click()

            # Articulo Imperdonable 2

            menu_desplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='CREMAS']")
                                           )
            )
            menu_desplegable.click()

            seleccion_menu = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='FRUTAL']")
                                           )
            )
            seleccion_menu.click()

            articulo2imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[4]/android.widget.TextView[1]")
                                           )
            )
            articulo2imp.click()

            cantidad_input2imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input2imp.clear()
            cantidad_input2imp.send_keys('5')

            aceptar2imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar2imp.click()

            # Articulo imperdonable 3

            articulo3imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[5]/android.widget.TextView[1]")
                    )
            )
            articulo3imp.click()

            cantidad_input3imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input3imp.clear()
            cantidad_input3imp.send_keys('5')

            aceptar3imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar3imp.click()
            time.sleep(1)

        except Exception as e:
            Log().error(
                "No se pudiero agregar los articulos imperdonables, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            menudesplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='FRUTAL']")
                                           )
            )
            menudesplegable.click()

            seleccionmenu = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='DESLACTOSADAS']")
                                           )
            )
            seleccionmenu.click()

            # Articulo Normal 1

            articulo = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                                           )
            )
            articulo.click()

            cantidad_input = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input.clear()
            cantidad_input.send_keys('5')

            aceptar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar.click()

            # Articulo Normal 2

            menudesplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='DESLACTOSADAS']")
                                           )
            )
            menudesplegable.click()

            seleccionmenu2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='YOGHURT BATIDO']")
                                           )
            )
            seleccionmenu2.click()

            articulo2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                                           )
            )
            articulo2.click()

            cantidad_input2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input2.clear()
            cantidad_input2.send_keys('5')

            aceptar2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar2.click()

        except Exception as e:
            Log().error(
                "No se pudiero agregar los articulos Normales, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # quitar teclado
            teclado = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Encabezado']")
                                           )
            )
            teclado.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                                           )
            )
            btn_guardar.click()

            btn_otrasmeca = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Si']")
                                           )
            )
            btn_otrasmeca.click()

            confirmar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='SI']")
                                           )
            )
            confirmar.click()

            # impresion = WebDriverWait(self, 100).until(
            #     EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
            #                                )
            # )
            # impresion.click()

            btn_finvisita = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
                                           )
            )
            btn_finvisita.click()
        except Exception as e:
            Log().error(
                "No se pudo finalizar la venta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # Final de Visita
            finvisita = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Final de Visita']")
                                           )
            )
            finvisita.click()
        except Exception as e:
            Log().error(
                "No se pudo seleccionar seleccionar la opcion de Final de Visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardarfin = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
                                           )
            )
            btn_guardarfin.click()

        except Exception as e:
            Log().error(
                "No se pudo guardar el fin de visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        # Venta desde Mapa
        try:
            # seleccionar cliente
            cliente = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Abarrotes Alison']")
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
            georeferencia = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Geo-referenciar']")
                )
            )
            georeferencia.click()
        except Exception as e:
            Log().error("No se pudo seleccionar la opción de Georeferenciar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            aceptargeoreferencia = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                )
            )
            aceptargeoreferencia.click()
        except Exception as e:
            Log().error("No se pudo dar click en el botón aceptar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btngps = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[4]")
                )
            )
            btngps.click()
        except Exception as e:
            Log().error("No se pudo dar click en el botón GPS, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btnpdv = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='PDVs']")
                )
            )
            btnpdv.click()
        except Exception as e:
            Log().error("No se pudo dar click en el botón PDV, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btncliente = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.view.View[@content-desc='25. ']")
                )
            )
            btncliente.click()

        except Exception as e:
            Log().error("No se pudo dar click en el boton del cliente revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btniniciarvisita = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Iniciar visita']")
                )
            )
            btniniciarvisita.click()
        except Exception as e:
            Log().error("No se pudo dar click en el boton para iniciar la visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # preventa contado
            preventa = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Preventa de Contado']")
                )
            )
            preventa.click()
        except Exception as e:
            Log().error("No se pudo seleccionar seleccionar la opcion de preventa de Contado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            menu_desplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Todos']")
                                           )
            )
            menu_desplegable.click()

            seleccion_menu = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='CREMAS']")
                                           )
            )
            seleccion_menu.click()

            # Articulo Imperdonable 1

            articulo_imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                )
            )
            articulo_imp.click()

            cantidad_inputimp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_inputimp.clear()
            cantidad_inputimp.send_keys('5')

            aceptarimp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptarimp.click()

            # Articulo Imperdonable 2

            menu_desplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='CREMAS']")
                                           )
            )
            menu_desplegable.click()

            seleccion_menu = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='FRUTAL']")
                                           )
            )
            seleccion_menu.click()

            articulo2imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[4]/android.widget.TextView[1]")
                                           )
            )
            articulo2imp.click()

            cantidad_input2imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input2imp.clear()
            cantidad_input2imp.send_keys('5')

            aceptar2imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar2imp.click()

            # Articulo imperdonable 3

            articulo3imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[5]/android.widget.TextView[1]")
                )
            )
            articulo3imp.click()

            cantidad_input3imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input3imp.clear()
            cantidad_input3imp.send_keys('5')

            aceptar3imp = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar3imp.click()
            time.sleep(1)

        except Exception as e:
            Log().error(
                "No se pudiero agregar los articulos imperdonables, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            menudesplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='FRUTAL']")
                                           )
            )
            menudesplegable.click()

            seleccionmenu = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='DESLACTOSADAS']")
                                           )
            )
            seleccionmenu.click()

            # Articulo Normal 1

            articulo = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                                           )
            )
            articulo.click()

            cantidad_input = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input.clear()
            cantidad_input.send_keys('5')

            aceptar = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar.click()

            # Articulo Normal 2

            menudesplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='DESLACTOSADAS']")
                                           )
            )
            menudesplegable.click()

            seleccionmenu2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='YOGHURT BATIDO']")
                                           )
            )
            seleccionmenu2.click()

            articulo2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                                           )
            )
            articulo2.click()

            cantidad_input2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_input2.clear()
            cantidad_input2.send_keys('5')

            aceptar2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptar2.click()

        except Exception as e:
            Log().error(
                "No se pudiero agregar los articulos Normales, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

            # Articulos Varios
        try:

            menudesplegable = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='YOGHURT BATIDO']")
                                           )
            )
            menudesplegable.click()

            seleccionmenu2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Todos']")
                                           )
            )
            seleccionmenu2.click()

            articulov1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[2]/android.widget.TextView[1]")
                                           )
            )
            articulov1.click()

            cantidad_inputv1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_inputv1.clear()
            cantidad_inputv1.send_keys('5')

            aceptarv1 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptarv1.click()

            articulov2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[3]/android.widget.TextView[1]")
                    )
            )
            articulov2.click()

            cantidad_inputv2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_inputv2.clear()
            cantidad_inputv2.send_keys('5')

            aceptarv2 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptarv2.click()

            articulov3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ListView/android.view.ViewGroup[4]/android.widget.TextView[1]")
                )
            )
            articulov3.click()

            cantidad_inputv3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]")
                                           )
            )
            cantidad_inputv3.clear()
            cantidad_inputv3.send_keys('5')

            aceptarv3 = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Aceptar']")
                                           )
            )
            aceptarv3.click()

        except Exception as e:
            Log().error("No se pudiero agregar los articulos Normales, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # quitar teclado
            teclado = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Encabezado']")
                )
            )
            teclado.click()
        except Exception as e:
            Log().error("No se pudo seleccionar el encabezado, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[3]")
                )
            )
            btn_guardar.click()

            btn_otrasmeca = WebDriverWait(self, 100).until(
                EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Si']")
                                           )
            )
            btn_otrasmeca.click()

            confirmar = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='SI']")
                )
            )
            confirmar.click()

            # impresion = WebDriverWait(self, 100).until(
            #     EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
            #                                )
            # )
            # impresion.click()

            btn_finvisita = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Cancelar']")
                )
            )
            btn_finvisita.click()
        except Exception as e:
            Log().error("No se pudo finalizar la venta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            # Final de Visita
            finvisita = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Final de Visita']")
                )
            )
            finvisita.click()
        except Exception as e:
            Log().error("No se pudo seleccionar seleccionar la opcion de Final de Visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            btn_guardarfin = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageButton[1]")
                )
            )
            btn_guardarfin.click()

        except Exception as e:
            Log().error("No se pudo guardar el fin de visita, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.get_screenshot_as_file(img_name)
            raise

        try:
            gps = WebDriverWait(self, 100).until(
                    EC.element_to_be_clickable((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ImageButton[1]")
                )
            )
            time.sleep(2)
            gps.click()
            Log().info("Se dio click en el boton de la casita")

        except Exception as e:
            Log().error("No se pudo cerrar el sell out, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
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