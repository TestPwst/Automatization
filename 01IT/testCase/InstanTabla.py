from importlib.machinery import SourceFileLoader

from config import Configuracion
import time
import unittest
from common.log import Log
from ingresopantalla import ingresopantalla
from nuevoregistro import nuevoregistro
from repetirregistro import repetirregistro
from modificarregistro import modificarregistro
from eliminarregistro import eliminarregistro
from config import conditions
from config import Configuracion

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral
ingresologinP = SourceFileLoader("ingresologin", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ingresologin.py").load_module()
ingresologin = ingresologinP.ingresologin

continua = True

class Test(unittest.TestCase):

	"""Escenario 1 de Instantanea Tabla """
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