from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from common.log import Log
from common.globalparam import img_path
#from ConfigGral import configgnral
import os
import time
from config import Configuracion
from importlib.machinery import SourceFileLoader



class cerrarsesion:


	def cerrarsesion(self):

		self.wait = WebDriverWait(self.driver, 60)

		# PROCESO DE CERRAR SESIÓN#
		# Click en el perfil del usuario

		try:
			NombrePerfil = self.wait.until(conditions.visibility((By.ID, Configuracion.id_seleccionarelperfil)))
			NombrePerfil.click()
			Log().info("Da click en el perfil del usuario")

		except Exception as e:
			Log().error("No se pudo encontrar el boton para darle click al perfil del usuario y cerrar la sesion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		# Click en logout

		try:
			LogOut = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_logout)))
			LogOut.click()
			Log().info("Da click en LogOut")

		except Exception as e:
			Log().error(
				"No se le dio click al boton LogOut y cerrar la sesion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise

		# Confirma cierre de sesion

		try:
			Confirmar = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_confirmar)))
			Confirmar.click()
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			Log().info("Confirma el cierre de sesion")

		except Exception as e:
			Log().error(
				"No se pudo confirmar el cierre de sesion y cerrar la sesion, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
			timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
			img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
			Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
			self.driver.get_screenshot_as_file(img_name)
			raise



