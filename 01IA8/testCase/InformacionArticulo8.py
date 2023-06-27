import os
from common.log import Log
import time
import unittest
from config import Configuracion
from ingresopantalla import ingresopantalla
from nuevoregistro import nuevoregistro
from repetirregistro import repetirregistro
from modificarregistro import modificarregistro
from eliminarregistro import eliminarregistro
from common.globalparam import img_path
from selenium.webdriver.common.by import By
from config import conditions

from importlib.machinery import SourceFileLoader

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/Versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral
ingresologinP = SourceFileLoader("ingresologin", "C:/xampp/htdocs/Versiones/automatizaciones/AutoPWST/ingresologin.py").load_module()
ingresologin = ingresologinP.ingresologin

continua = True

class Test(unittest.TestCase):
	"""Escenarios de Información de Artículos 8"""
	@classmethod
	def test(self):
		self.driver = Configuracion.create_chrome_driver()
		Log().info(" Se abre el chrome")
		self.driver.get(configgnral.URL)
		Log().info(" Entra a la URL")
		self.driver.maximize_window()
		Log().info(" Maximiza la pantalla")
		time.sleep(3)
		self.driver.switch_to.frame("mainFrame")
		Log().info(" Cambia al frame")
		time.sleep(3)

	def test_000(self):
		"""Ingresa a la base de datos"""
		return ingresologin.ingresologin(self)

	def test_001(self):
		"""Abre menu y ejecuta pantalla"""
		global continua
		if(continua):
			success = ingresopantalla.ingresopantalla(self, conditions, Configuracion)
			if(success==False):
				self.driver.close()
				self.driver.switch_to.window(self.driver.window_handles[0])
				time.sleep(2)
				self.driver.quit()
				Log().info(" Se cierra chrome")
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_002(self):
		"""Abre la ventana de nuevo y crear un registro"""
		global continua
		if(continua):
			success = nuevoregistro.nuevoregistro(self, conditions, Configuracion)
			if(success==False):
				self.driver.close()
				self.driver.switch_to.window(self.driver.window_handles[0])
				time.sleep(2)
				self.driver.quit()
				Log().info(" Se cierra chrome")
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_003(self):
		"""Repetir el registro creado anteriormente"""
		global continua
		if(continua):
			success = repetirregistro.repetirregistro(self, conditions, Configuracion)
			if(success==False):
				self.driver.close()
				self.driver.switch_to.window(self.driver.window_handles[0])
				time.sleep(2)
				self.driver.quit()
				Log().info(" Se cierra chrome")
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_004(self):
		"""Modificar el registro"""
		global continua
		if(continua):
			success = modificarregistro.modificarregistro(self, conditions, Configuracion)
			if(success==False):
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(2)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
					raise Exception()

		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_005(self):
		"""Eliminar el registro creado"""
		global continua
		if(continua):
			success = eliminarregistro.eliminarregistro(self, conditions, Configuracion)
			if(success==False):
				self.driver.close()
				self.driver.switch_to.window(self.driver.window_handles[0])
				time.sleep(2)
				self.driver.quit()
				Log().info(" Se cierra chrome")
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_006(self):
		"""Cerrar_Navegador"""
		if(continua):
			self.driver.close()
			self.driver.switch_to.window(self.driver.window_handles[0])
			time.sleep(2)
			self.driver.quit()
			Log().info(" Se cierra chrome")

if __name__ == '__main__':
	unittest.main()

