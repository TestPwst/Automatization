from config import Configuracion
import time
import unittest
from common.log import Log
from ingresacliente import ingresacliente
from ingresaarticulos import ingresaarticulos
from realizarventa import realizarventa
from realizarventa2 import realizarventa2
from realizarventa3 import realizarventa3
from realizarventa4 import realizarventa4
from cierraticket import cierraticket
from ingresologin import ingresologin
from cerrarsesion import cerrarsesion


class Test(unittest.TestCase):

	"""Escenario 1 Ventas"""
	@classmethod
	def test(self):
		self.driver = Configuracion.create_chrome_driver()
		Log().info(" Se abre el chrome")
		self.driver.get(Configuracion.URL)
		Log().info(" Entra a la URL")
		self.driver.maximize_window()
		Log().info(" Maximiza la pantalla")
		time.sleep(3)


	def test_000(self):
		"""Ingresa datos para logearse"""
		return ingresologin.ingresologin(self)
	
	def test_001(self):
		"""Raliza venta"""
		return realizarventa.realizarventa(self)
	def test_002(self):
		"""Raliza venta2"""
		return realizarventa2.realizarventa2(self)
	def test_003(self):
		"""Raliza venta3"""
		return realizarventa3.realizarventa3(self)
	def test_004(self):
		"""Raliza venta4"""
		return realizarventa4.realizarventa4(self)
	

	
	def test_005(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		Log().info(" Se cierra chrome")


if __name__ == '__main__':
	unittest.main()