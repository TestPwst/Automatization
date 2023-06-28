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


ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral
ingresologinP = SourceFileLoader("ingresologin", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ingresologin.py").load_module()
ingresologin = ingresologinP.ingresologin


class Test(unittest.TestCase):

	"""Escenario 1 de Programación Sincronización"""
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
		return ingresopantalla.ingresopantalla(self)

	def test_002(self):
		"""Abre la ventana de nuevo y crear un registro"""
		return nuevoregistro.nuevoregistro(self)

	def test_003(self):
		"""Modificar el registro"""
		return modificarregistro.modificarregistro(self)

	def test_004(self):
		"""Eliminar el registro creado"""
		return eliminarregistro.eliminarregistro(self)

	def test_005(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")


if __name__ == '__main__':
	unittest.main()