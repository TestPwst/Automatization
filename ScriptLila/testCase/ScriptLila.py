from importlib.machinery import SourceFileLoader
from selenium.webdriver.support.ui import WebDriverWait
import os
from config import Configuracion
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import unittest
from common.log import Log
from common.globalparam import img_path
from selenium.webdriver.common.by import By
from config import conditions

#Custom Properties
ZonaBancariaPantalla = SourceFileLoader("Pantalla01ZB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZB/testCase/ingresopantalla.py").load_module()
ZonaBancariaAgregar = SourceFileLoader("Agregar01ZB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZB/testCase/nuevoregistro.py").load_module()
ZonaBancariaRepetir = SourceFileLoader("Repetir01ZB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZB/testCase/repetirregistro.py").load_module()
ZonaBancariaModificar = SourceFileLoader("Modificar01ZB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZB/testCase/modificarregistro.py").load_module()
ZonaBancariaEliminar = SourceFileLoader("Eliminar01ZB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZB/testCase/eliminarregistro.py").load_module()
ZonaBancariaConfig = SourceFileLoader("config01ZB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZB/config.py").load_module()

LenguajesPantalla = SourceFileLoader("Pantalla01LE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LE/testCase/ingresopantalla.py").load_module()
LenguajesAgregar = SourceFileLoader("Agregar01LE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LE/testCase/nuevoregistro.py").load_module()
LenguajesRepetir = SourceFileLoader("Repetir01LE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LE/testCase/repetirregistro.py").load_module()
LenguajesModificar = SourceFileLoader("Modificar01LE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LE/testCase/modificarregistro.py").load_module()
LenguajesEliminar = SourceFileLoader("Eliminar01LE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LE/testCase/eliminarregistro.py").load_module()
LenguajesConfig = SourceFileLoader("config01LE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LE/config.py").load_module()

FormasPago1Pantalla = SourceFileLoader("Pantalla01FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FDP/testCase/ingresopantalla.py").load_module()
FormasPago1Agregar = SourceFileLoader("Agregar01FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FDP/testCase/nuevoregistro.py").load_module()
FormasPago1Repetir = SourceFileLoader("Repetir01FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FDP/testCase/repetirregistro.py").load_module()
FormasPago1Modificar = SourceFileLoader("Modificar01FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FDP/testCase/modificarregistro.py").load_module()
FormasPago1Eliminar = SourceFileLoader("Eliminar01FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FDP/testCase/eliminarregistro.py").load_module()
FormasPago1Config = SourceFileLoader("config01FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FDP/config.py").load_module()

FormasPago2Pantalla = SourceFileLoader("Pantalla02FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02FDP/testCase/ingresopantalla.py").load_module()
FormasPago2Agregar = SourceFileLoader("Agregar02FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02FDP/testCase/nuevoregistro.py").load_module()
FormasPago2Repetir = SourceFileLoader("Repetir02FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02FDP/testCase/repetirregistro.py").load_module()
FormasPago2Modificar = SourceFileLoader("Modificar02FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02FDP/testCase/modificarregistro.py").load_module()
FormasPago2Eliminar = SourceFileLoader("Eliminar02FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02FDP/testCase/eliminarregistro.py").load_module()
FormasPago2Config = SourceFileLoader("config02FDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02FDP/config.py").load_module()

MotivosDevolucionPantalla = SourceFileLoader("Pantalla01MD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MD/testCase/ingresopantalla.py").load_module()
MotivosDevolucionAgregar = SourceFileLoader("Agregar01MD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MD/testCase/nuevoregistro.py").load_module()
MotivosDevolucionRepetir = SourceFileLoader("Repetir01MD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MD/testCase/repetirregistro.py").load_module()
MotivosDevolucionModificar = SourceFileLoader("Modificar01MD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MD/testCase/modificarregistro.py").load_module()
MotivosDevolucionEliminar = SourceFileLoader("Eliminar01MD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MD/testCase/eliminarregistro.py").load_module()
MotivosDevolucionConfig = SourceFileLoader("config01MD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MD/config.py").load_module()

MotivosRechazoPantalla = SourceFileLoader("Pantalla01MR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MR/testCase/ingresopantalla.py").load_module()
MotivosRechazoAgregar = SourceFileLoader("Agregar01MR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MR/testCase/nuevoregistro.py").load_module()
MotivosRechazoRepetir = SourceFileLoader("Repetir01MR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MR/testCase/repetirregistro.py").load_module()
MotivosRechazoModificar = SourceFileLoader("Modificar01MR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MR/testCase/modificarregistro.py").load_module()
MotivosRechazoEliminar = SourceFileLoader("Eliminar01MR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MR/testCase/eliminarregistro.py").load_module()
MotivosRechazoConfig = SourceFileLoader("config01MR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MR/config.py").load_module()

MotivosNoInventarioPantalla = SourceFileLoader("Pantalla01MNTI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNTI/testCase/ingresopantalla.py").load_module()
MotivosNoInventarioAgregar = SourceFileLoader("Agregar01MNTI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNTI/testCase/nuevoregistro.py").load_module()
MotivosNoInventarioRepetir = SourceFileLoader("Repetir01MNTI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNTI/testCase/repetirregistro.py").load_module()
MotivosNoInventarioModificar = SourceFileLoader("Modificar01MNTI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNTI/testCase/modificarregistro.py").load_module()
MotivosNoInventarioEliminar = SourceFileLoader("Eliminar01MNTI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNTI/testCase/eliminarregistro.py").load_module()
MotivosNoInventarioConfig = SourceFileLoader("config01MNTI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNTI/config.py").load_module()

TipoRubroPantalla = SourceFileLoader("Pantalla01TDR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDR/testCase/ingresopantalla.py").load_module()
TipoRubroAgregar = SourceFileLoader("Agregar01TDR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDR/testCase/nuevoregistro.py").load_module()
TipoRubroRepetir = SourceFileLoader("Repetir01TDR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDR/testCase/repetirregistro.py").load_module()
TipoRubroModificar = SourceFileLoader("Modificar01TDR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDR/testCase/modificarregistro.py").load_module()
TipoRubroEliminar = SourceFileLoader("Eliminar01TDR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDR/testCase/eliminarregistro.py").load_module()
TipoRubroConfig = SourceFileLoader("config01TDR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDR/config.py").load_module()

RubroCajaPantalla = SourceFileLoader("Pantalla01RC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RC/testCase/ingresopantalla.py").load_module()
RubroCajaAgregar = SourceFileLoader("Agregar01RC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RC/testCase/nuevoregistro.py").load_module()
RubroCajaRepetir = SourceFileLoader("Repetir01RC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RC/testCase/repetirregistro.py").load_module()
RubroCajaModificar = SourceFileLoader("Modificar01RC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RC/testCase/modificarregistro.py").load_module()
RubroCajaEliminar = SourceFileLoader("Eliminar01RC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RC/testCase/eliminarregistro.py").load_module()
RubroCajaConfig = SourceFileLoader("config01RC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RC/config.py").load_module()

RubroStockPantalla = SourceFileLoader("Pantalla01RS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RS/testCase/ingresopantalla.py").load_module()
RubroStockAgregar = SourceFileLoader("Agregar01RS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RS/testCase/nuevoregistro.py").load_module()
RubroStockRepetir = SourceFileLoader("Repetir01RS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RS/testCase/repetirregistro.py").load_module()
RubroStockModificar = SourceFileLoader("Modificar01RS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RS/testCase/modificarregistro.py").load_module()
RubroStockEliminar = SourceFileLoader("Eliminar01RS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RS/testCase/eliminarregistro.py").load_module()
RubroStockConfig = SourceFileLoader("config01RS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RS/config.py").load_module()

MotivosAnulacionPantalla = SourceFileLoader("Pantalla01MA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MA/testCase/ingresopantalla.py").load_module()
MotivosAnulacionAgregar = SourceFileLoader("Agregar01MA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MA/testCase/nuevoregistro.py").load_module()
MotivosAnulacionRepetir = SourceFileLoader("Repetir01MA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MA/testCase/repetirregistro.py").load_module()
MotivosAnulacionModificar = SourceFileLoader("Modificar01MA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MA/testCase/modificarregistro.py").load_module()
MotivosAnulacionEliminar = SourceFileLoader("Eliminar01MA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MA/testCase/eliminarregistro.py").load_module()
MotivosAnulacionConfig = SourceFileLoader("config01MA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MA/config.py").load_module()

MotivosBonificacionPantalla = SourceFileLoader("Pantalla01MB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MB/testCase/ingresopantalla.py").load_module()
MotivosBonificacionAgregar = SourceFileLoader("Agregar01MB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MB/testCase/nuevoregistro.py").load_module()
MotivosBonificacionRepetir = SourceFileLoader("Repetir01MB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MB/testCase/repetirregistro.py").load_module()
MotivosBonificacionModificar = SourceFileLoader("Modificar01MB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MB/testCase/modificarregistro.py").load_module()
MotivosBonificacionEliminar = SourceFileLoader("Eliminar01MB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MB/testCase/eliminarregistro.py").load_module()
MotivosBonificacionConfig = SourceFileLoader("config01MB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MB/config.py").load_module()

MotivosNoFotoPantalla = SourceFileLoader("Pantalla01MNF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNF/testCase/ingresopantalla.py").load_module()
MotivosNoFotoAgregar = SourceFileLoader("Agregar01MNF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNF/testCase/nuevoregistro.py").load_module()
MotivosNoFotoRepetir = SourceFileLoader("Repetir01MNF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNF/testCase/repetirregistro.py").load_module()
MotivosNoFotoModificar = SourceFileLoader("Modificar01MNF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNF/testCase/modificarregistro.py").load_module()
MotivosNoFotoEliminar = SourceFileLoader("Eliminar01MNF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNF/testCase/eliminarregistro.py").load_module()
MotivosNoFotoConfig = SourceFileLoader("config01MNF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNF/config.py").load_module()

AccionSchedulerPantalla = SourceFileLoader("Pantalla01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/ingresopantalla.py").load_module()
AccionSchedulerAgregar = SourceFileLoader("Agregar01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/nuevoregistro.py").load_module()
AccionSchedulerRepetir = SourceFileLoader("Repetir01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/repetirregistro.py").load_module()
AccionSchedulerModificar = SourceFileLoader("Modificar01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/modificarregistro.py").load_module()
AccionSchedulerEliminar = SourceFileLoader("Eliminar01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/eliminarregistro.py").load_module()
AccionSchedulerConfig = SourceFileLoader("config01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/config.py").load_module()

BloquesPantalla = SourceFileLoader("Pantalla01BL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01BL/testCase/ingresopantalla.py").load_module()
BloquesAgregar = SourceFileLoader("Agregar01BL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01BL/testCase/nuevoregistro.py").load_module()
BloquesRepetir = SourceFileLoader("Repetir01BL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01BL/testCase/repetirregistro.py").load_module()
BloquesModificar = SourceFileLoader("Modificar01BL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01BL/testCase/modificarregistro.py").load_module()
BloquesEliminar = SourceFileLoader("Eliminar01BL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01BL/testCase/eliminarregistro.py").load_module()
BloquesConfig = SourceFileLoader("config01BL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01BL/config.py").load_module()

ConfigGral = SourceFileLoader("ConfigGral", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ConfigGral.py").load_module()
configgnral = ConfigGral.configgnral
ingresologinP = SourceFileLoader("ingresologin", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/ingresologin.py").load_module()
ingresologin = ingresologinP.ingresologin

continua = True

class Test(unittest.TestCase):

	"""Script Amarillo"""
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
		"""Ingresa a pantalla Custom Properties"""
		global continua
		if(continua):
			success = ZonaBancariaPantalla.ingresopantalla.ingresopantalla(self, conditions, ZonaBancariaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_002(self):
		"""Agregar Custom Properties"""
		global continua
		if(continua):
			success = ZonaBancariaAgregar.nuevoregistro.nuevoregistro(self, conditions, ZonaBancariaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_003(self):
		"""Repetir Registro Custom Properties"""
		global continua
		if(continua):
			success = ZonaBancariaRepetir.repetirregistro.repetirregistro(self, conditions, ZonaBancariaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_004(self):
		"""Modifica Custom Properties"""
		global continua
		if(continua):
			success = ZonaBancariaModificar.modificarregistro.modificarregistro(self, conditions, ZonaBancariaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_005(self):
		"""Elimina Custom Properties"""
		global continua
		if(continua):
			success = ZonaBancariaEliminar.eliminarregistro.eliminarregistro(self, conditions, ZonaBancariaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonaBancariaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_006(self):
		"""Ingresa a pantalla Lenguajes"""
		global continua
		continua = True
		if(continua):
			success = LenguajesPantalla.ingresopantalla.ingresopantalla(self, conditions, LenguajesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_007(self):
		"""Agregar Lenguajes"""
		global continua
		if(continua):
			success = LenguajesAgregar.nuevoregistro.nuevoregistro(self, conditions, LenguajesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_008(self):
		"""Repetir Registro Lenguajes"""
		global continua
		if(continua):
			success = LenguajesRepetir.repetirregistro.repetirregistro(self, conditions, LenguajesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_009(self):
		"""Modifica Lenguajes"""
		global continua
		if(continua):
			success = LenguajesModificar.modificarregistro.modificarregistro(self, conditions, LenguajesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_010(self):
		"""Elimina Lenguajes"""
		global continua
		if(continua):
			success = LenguajesEliminar.eliminarregistro.eliminarregistro(self, conditions, LenguajesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LenguajesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_011(self):
		"""Ingresa a pantalla Formas Pago 1"""
		global continua
		continua = True
		if(continua):
			success = FormasPago1Pantalla.ingresopantalla.ingresopantalla(self, conditions, FormasPago1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_012(self):
		"""Agregar Formas Pago 1"""
		global continua
		if(continua):
			success = FormasPago1Agregar.nuevoregistro.nuevoregistro(self, conditions, FormasPago1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_013(self):
		"""Repetir Registro Formas Pago 1"""
		global continua
		if(continua):
			success = FormasPago1Repetir.repetirregistro.repetirregistro(self, conditions, FormasPago1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_014(self):
		"""Modifica Formas Pago 1"""
		global continua
		if(continua):
			success = FormasPago1Modificar.modificarregistro.modificarregistro(self, conditions, FormasPago1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_015(self):
		"""Elimina Formas Pago 1"""
		global continua
		if(continua):
			success = FormasPago1Eliminar.eliminarregistro.eliminarregistro(self, conditions, FormasPago1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_016(self):
		"""Ingresa a pantalla Formas Pago 2"""
		global continua
		continua = True
		if(continua):
			success = FormasPago2Pantalla.ingresopantalla.ingresopantalla(self, conditions, FormasPago2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_017(self):
		"""Agregar Formas Pago 2"""
		global continua
		if(continua):
			success = FormasPago2Agregar.nuevoregistro.nuevoregistro(self, conditions, FormasPago2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_018(self):
		"""Repetir Registro Formas Pago 2"""
		global continua
		if(continua):
			success = FormasPago2Repetir.repetirregistro.repetirregistro(self, conditions, FormasPago2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_019(self):
		"""Modifica Formas Pago 2"""
		global continua
		if(continua):
			success = FormasPago2Modificar.modificarregistro.modificarregistro(self, conditions, FormasPago2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_020(self):
		"""Elimina Formas Pago 2"""
		global continua
		if(continua):
			success = FormasPago2Eliminar.eliminarregistro.eliminarregistro(self, conditions, FormasPago2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FormasPago2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_021(self):
		"""Ingresa a pantalla Motivos Devolucion"""
		global continua
		continua = True
		if(continua):
			success = MotivosDevolucionPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_022(self):
		"""Agregar Motivos Devolucion"""
		global continua
		if(continua):
			success = MotivosDevolucionAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_023(self):
		"""Repetir Registro Motivos Devolucion"""
		global continua
		if(continua):
			success = MotivosDevolucionRepetir.repetirregistro.repetirregistro(self, conditions, MotivosDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_024(self):
		"""Modifica Motivos Devolucion"""
		global continua
		if(continua):
			success = MotivosDevolucionModificar.modificarregistro.modificarregistro(self, conditions, MotivosDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_025(self):
		"""Elimina Motivos Devolucion"""
		global continua
		if(continua):
			success = MotivosDevolucionEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosDevolucionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_026(self):
		"""Ingresa a pantalla Motivos Rechazo"""
		global continua
		continua = True
		if(continua):
			success = MotivosRechazoPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosRechazoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_027(self):
		"""Agregar Motivos Rechazo"""
		global continua
		if(continua):
			success = MotivosRechazoAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosRechazoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_028(self):
		"""Repetir Registro Motivos Rechazo"""
		global continua
		if(continua):
			success = MotivosRechazoRepetir.repetirregistro.repetirregistro(self, conditions, MotivosRechazoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_029(self):
		"""Modifica Motivos Rechazo"""
		global continua
		if(continua):
			success = MotivosRechazoModificar.modificarregistro.modificarregistro(self, conditions, MotivosRechazoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_030(self):
		"""Elimina Motivos Rechazo"""
		global continua
		if(continua):
			success = MotivosRechazoEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosRechazoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosRechazoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_031(self):
		"""Ingresa a pantalla Motivos No Toma Inventario"""
		global continua
		continua = True
		if(continua):
			success = MotivosNoInventarioPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosNoInventarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_032(self):
		"""Agregar Contactos Motivos No Toma Inventario"""
		global continua
		if(continua):
			success = MotivosNoInventarioAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosNoInventarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_033(self):
		"""Repetir Registro Motivos No Toma Inventario"""
		global continua
		if(continua):
			success = MotivosNoInventarioRepetir.repetirregistro.repetirregistro(self, conditions, MotivosNoInventarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_034(self):
		"""Modifica Contactos Motivos No Toma Inventario"""
		global continua
		if(continua):
			success = MotivosNoInventarioModificar.modificarregistro.modificarregistro(self, conditions, MotivosNoInventarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_035(self):
		"""Elimina Motivos No Toma Inventario"""
		global continua
		if(continua):
			success = MotivosNoInventarioEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosNoInventarioConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoInventarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_036(self):
		"""Ingresa a pantalla Tipo Rubro"""
		global continua
		continua = True
		if(continua):
			success = TipoRubroPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoRubroConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_032(self):
		"""Agregar Tipo Rubro"""
		global continua
		if(continua):
			success = TipoRubroAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoRubroConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_033(self):
		"""Repetir Registro Tipo Rubro"""
		global continua
		if(continua):
			success = TipoRubroRepetir.repetirregistro.repetirregistro(self, conditions, TipoRubroConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_034(self):
		"""Modifica Programas Tipo Rubro"""
		global continua
		if(continua):
			success = TipoRubroModificar.modificarregistro.modificarregistro(self, conditions, TipoRubroConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_035(self):
		"""Elimina Programas Tipo Rubro"""
		global continua
		if(continua):
			success = TipoRubroEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoRubroConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRubroConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_036(self):
		"""Ingresa a pantalla Rubro Caja"""
		global continua
		continua = True
		if(continua):
			success = RubroCajaPantalla.ingresopantalla.ingresopantalla(self, conditions, RubroCajaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_037(self):
		"""Agregar Programas Rubro Caja"""
		global continua
		if(continua):
			success = RubroCajaAgregar.nuevoregistro.nuevoregistro(self, conditions, RubroCajaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_038(self):
		"""Repetir Registro Rubro Caja"""
		global continua
		if(continua):
			success = RubroCajaRepetir.repetirregistro.repetirregistro(self, conditions, RubroCajaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_039(self):
		"""Modifica Rubro Caja"""
		global continua
		if(continua):
			success = RubroCajaModificar.modificarregistro.modificarregistro(self, conditions, RubroCajaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_040(self):
		"""Elimina Rubro Caja"""
		global continua
		if(continua):
			success = RubroCajaEliminar.eliminarregistro.eliminarregistro(self, conditions, RubroCajaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroCajaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_041(self):
		"""Ingresa a pantalla Rubros Stock"""
		global continua
		continua = True
		if(continua):
			success = RubroStockPantalla.ingresopantalla.ingresopantalla(self, conditions, RubroStockConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_042(self):
		"""Agregar Rubros Stock"""
		global continua
		if(continua):
			success = RubroStockAgregar.nuevoregistro.nuevoregistro(self, conditions, RubroStockConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_043(self):
		"""Repetir Registro Rubros Stock"""
		global continua
		if(continua):
			success = RubroStockRepetir.repetirregistro.repetirregistro(self, conditions, RubroStockConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_044(self):
		"""Modifica Rubros Stock"""
		global continua
		if(continua):
			success = RubroStockModificar.modificarregistro.modificarregistro(self, conditions, RubroStockConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_045(self):
		"""Elimina Rubros Stock"""
		global continua
		if(continua):
			success = RubroStockEliminar.eliminarregistro.eliminarregistro(self, conditions, RubroStockConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RubroStockConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_046(self):
		"""Ingresa a pantalla Motivos Anulacion"""
		global continua
		continua = True
		if(continua):
			success = MotivosAnulacionPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosAnulacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_047(self):
		"""Agregar Motivos Anulacion"""
		global continua
		if(continua):
			success = MotivosAnulacionAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosAnulacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_048(self):
		"""Repetir Registro Motivos Anulacion"""
		global continua
		if(continua):
			success = MotivosAnulacionRepetir.repetirregistro.repetirregistro(self, conditions, MotivosAnulacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_049(self):
		"""Modifica Motivos Anulacion"""
		global continua
		if(continua):
			success = MotivosAnulacionModificar.modificarregistro.modificarregistro(self, conditions, MotivosAnulacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_050(self):
		"""Elimina Motivos Anulacion"""
		global continua
		if(continua):
			success = MotivosAnulacionEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosAnulacionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosAnulacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_051(self):
		"""Ingresa a pantalla Motivos Bonificacion"""
		global continua
		continua = True
		if(continua):
			success = MotivosBonificacionPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosBonificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_052(self):
		"""Agregar Motivos Bonificacion"""
		global continua
		if(continua):
			success = MotivosBonificacionAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosBonificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_053(self):
		"""Repetir Registro Motivos onificacion"""
		global continua
		if(continua):
			success = MotivosBonificacionRepetir.repetirregistro.repetirregistro(self, conditions, MotivosBonificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_054(self):
		"""Modifica Motivos Bonificacion"""
		global continua
		if(continua):
			success = MotivosBonificacionModificar.modificarregistro.modificarregistro(self, conditions, MotivosBonificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_055(self):
		"""Elimina Motivos Bonificacion"""
		global continua
		if(continua):
			success = MotivosBonificacionEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosBonificacionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosBonificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_056(self):
		"""Ingresa a pantalla Motivos No Foto"""
		global continua
		continua = True
		if(continua):
			success = MotivosNoFotoPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosNoFotoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_057(self):
		"""Agregar Motivos No Foto"""
		global continua
		if(continua):
			success = MotivosNoFotoAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosNoFotoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_058(self):
		"""Repetir Registro Motivos No Foto"""
		global continua
		if(continua):
			success = MotivosNoFotoRepetir.repetirregistro.repetirregistro(self, conditions, MotivosNoFotoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_059(self):
		"""Modifica Motivos No Foto"""
		global continua
		if(continua):
			success = MotivosNoFotoModificar.modificarregistro.modificarregistro(self, conditions, MotivosNoFotoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_060(self):
		"""Elimina Motivos No Foto"""
		global continua
		if(continua):
			success = MotivosNoFotoEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosNoFotoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoFotoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_061(self):
		"""Ingresa a pantalla Acciones Scheduler"""
		global continua
		continua = True
		if(continua):
			success = AccionSchedulerPantalla.ingresopantalla.ingresopantalla(self, conditions, AccionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_062(self):
		"""Agregar Acciones Scheduler"""
		global continua
		if(continua):
			success = AccionSchedulerAgregar.nuevoregistro.nuevoregistro(self, conditions, AccionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_063(self):
		"""Repetir Registro Acciones Scheduler"""
		global continua
		if(continua):
			success = AccionSchedulerRepetir.repetirregistro.repetirregistro(self, conditions, AccionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_064(self):
		"""Modifica Acciones Scheduler"""
		global continua
		if(continua):
			success = AccionSchedulerModificar.modificarregistro.modificarregistro(self, conditions, AccionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_065(self):
		"""Elimina Acciones Scheduler"""
		global continua
		if(continua):
			success = AccionSchedulerEliminar.eliminarregistro.eliminarregistro(self, conditions, AccionSchedulerConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AccionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_066(self):
		"""Ingresa a pantalla Bloques"""
		global continua
		continua = True
		if(continua):
			success = BloquesPantalla.ingresopantalla.ingresopantalla(self, conditions, BloquesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_067(self):
		"""Agregar Bloques"""
		global continua
		if(continua):
			success = BloquesAgregar.nuevoregistro.nuevoregistro(self, conditions, BloquesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_068(self):
		"""Repetir Registro Bloques"""
		global continua
		if(continua):
			success = BloquesRepetir.repetirregistro.repetirregistro(self, conditions, BloquesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_069(self):
		"""Modifica Bloques"""
		global continua
		if(continua):
			success = BloquesModificar.modificarregistro.modificarregistro(self, conditions, BloquesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_070(self):
		"""Elimina Bloques"""
		global continua
		if(continua):
			success = BloquesEliminar.eliminarregistro.eliminarregistro(self, conditions, BloquesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, BloquesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_071(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")

if __name__ == '__main__':
	unittest.main()