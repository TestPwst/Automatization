from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import conditions
from common.log import Log
from common.globalparam import img_path
#from ConfigGral import configgnral
import os
import time
from config import Configuracion

from importlib.machinery import SourceFileLoader



class ingresologin:


	def ingresologin(self):

		self.wait = WebDriverWait(self.driver, 60)

		# PROCESO DE INICIAR SESIÓN#
		# Ingresar usuario

		try:
			Usuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.id_usuario)))
			Usuario.send_keys(Configuracion.usuario)
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
			Contra = self.wait.until(conditions.visibility((By.XPATH, Configuracion.id_contrasena)))
			Contra.send_keys(Configuracion.contrasena)
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
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
			IniciarSesion = self.wait.until(conditions.clickable((By.XPATH, Configuracion.btn_ingresar)))
			IniciarSesion.click()
			Log().info(" Se dio clic en el boton ingresar")
		except Exception as e:
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise
		# Cierra sesion si esta activa
		try:
			btn_cierrasesionactiva = self.wait.until(conditions.clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div/p[2]/a")))
			if btn_cierrasesionactiva.is_displayed():
				btn_cierrasesionactiva.click()
				time.sleep(5)

		except NoSuchElementException:
			pass




