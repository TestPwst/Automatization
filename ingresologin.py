from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from config import conditions
from common.log import Log
from common.globalparam import img_path
import os
import time

from importlib.machinery import SourceFileLoader

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/Versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral


class ingresologin:

	def ingresologin(self):

		self.wait = WebDriverWait(self.driver, 80)

		# PROCESO DE INICIAR SESIÓN#
		# Ingresar usuario

		try:
			Usuario = self.wait.until(conditions.visibility((By.XPATH, configgnral.id_usuario)))
			Usuario.send_keys(configgnral.usuario)
			Log().info(" Escribe el usuario")

		except Exception as e:
			Log().error("No se pudo encontrar el campo para ingresar el usuario, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		# Ingresar contraseña

		try:
			Contra = self.wait.until(conditions.visibility((By.XPATH, configgnral.id_contrasena)))
			Contra.send_keys(configgnral.contrasena)
			Log().info(" Escribe la contraseña")

		except Exception as e:
			Log().error("No se pudo encontrar el campo para ingresar la contraseña, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		"""Boton_Ingresar"""
		# Click en el boton de ingresar
		try:
			IniciarSesion = self.wait.until(conditions.clickable((By.XPATH, configgnral.btn_ingresar)))
			IniciarSesion.click()
			Log().info(" Se dio clic en el boton ingresar")

		except Exception as e:
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		"""Ingresar a PowerStreet Enterprise"""
		# Ejecuta Enterprise
		try:
			Enterprise = self.wait.until(conditions.visibility((By.XPATH, configgnral.btn_Enterprise)))
			Enterprise.click()
			Log().info(" Ejecutar Enterprise")

		except Exception as e:
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		# Cambia de pestaña
		try:
			self.driver.switch_to.window(self.driver.window_handles[0])
			time.sleep(2)
			self.driver.switch_to.window(self.driver.window_handles[1])
			time.sleep(2)
			Log().info(" Cambia entre pestañas")
			time.sleep(3)

		except Exception as e:
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		try:
			btn_cierrasesionactiva = self.driver.find_element(By.XPATH, "//button[@class = 'p-continuebutton']")
			if btn_cierrasesionactiva.is_displayed():
				btn_cierrasesionactiva.click()
				time.sleep(5)

		except NoSuchElementException:
			pass
