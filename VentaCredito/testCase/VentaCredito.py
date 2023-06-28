from importlib.machinery import SourceFileLoader
from config import Configuracion
import time
import unittest
from common.log import Log
from selenium.webdriver.common.by import By
from ingresoinventario import ingresoinventario
from realizaventa import realizaventa
from validardocumento import validardocumento
from validarstock import validarstock

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral
ingresologinP = SourceFileLoader("ingresologin", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ingresologin.py").load_module()
ingresologin = ingresologinP.ingresologin


class Test(unittest.TestCase):

	"""Venta Automatizada"""
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
		"""Ingresa al inventario del vendedor"""
		return ingresoinventario.ingresosinventario(self)

	def test_002(self):
		"""Se realiza la venta de 1 item"""
		return realizaventa.realizarventa(self)

	def test_003(self):
		"""Valida la modificación de stock"""
		return validarstock.validarstock(self)

	def test_004(self):
		"""Validar que la venta se realizó"""
		return validardocumento.validardocumento(self)

	def test_005(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")


if __name__ == '__main__':
	unittest.main()

