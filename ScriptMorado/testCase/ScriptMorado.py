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
UbicacionGeoPantalla = SourceFileLoader("Pantalla01UG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UG/testCase/ingresopantalla.py").load_module()
UbicacionGeoAgregar = SourceFileLoader("Agregar01UG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UG/testCase/nuevoregistro.py").load_module()
UbicacionGeoRepetir = SourceFileLoader("Repetir01UG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UG/testCase/repetirregistro.py").load_module()
UbicacionGeoModificar = SourceFileLoader("Modificar01UG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UG/testCase/modificarregistro.py").load_module()
UbicacionGeoEliminar = SourceFileLoader("Eliminar01UG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UG/testCase/eliminarregistro.py").load_module()
UbicacionGeoConfig = SourceFileLoader("config01UG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UG/config.py").load_module()

ZonasGeoPantalla = SourceFileLoader("Pantalla01ZG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZG/testCase/ingresopantalla.py").load_module()
ZonasGeoAgregar = SourceFileLoader("Agregar01ZG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZG/testCase/nuevoregistro.py").load_module()
ZonasGeoRepetir = SourceFileLoader("Repetir01ZG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZG/testCase/repetirregistro.py").load_module()
ZonasGeoModificar = SourceFileLoader("Modificar01ZG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZG/testCase/modificarregistro.py").load_module()
ZonasGeoEliminar = SourceFileLoader("Eliminar01ZG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZG/testCase/eliminarregistro.py").load_module()
ZonasGeoConfig = SourceFileLoader("config01ZG", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZG/config.py").load_module()

ZonasVentaPantalla = SourceFileLoader("Pantalla01ZV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZV/testCase/ingresopantalla.py").load_module()
ZonasVentaAgregar = SourceFileLoader("Agregar01ZV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZV/testCase/nuevoregistro.py").load_module()
ZonasVentaRepetir = SourceFileLoader("Repetir01ZV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZV/testCase/repetirregistro.py").load_module()
ZonasVentaModificar = SourceFileLoader("Modificar01ZV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZV/testCase/modificarregistro.py").load_module()
ZonasVentaEliminar = SourceFileLoader("Eliminar01ZV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZV/testCase/eliminarregistro.py").load_module()
ZonasVentaConfig = SourceFileLoader("config01ZV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZV/config.py").load_module()

ZonasRepartoPantalla = SourceFileLoader("Pantalla01ZR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZR/testCase/ingresopantalla.py").load_module()
ZonasRepartoAgregar = SourceFileLoader("Agregar01ZR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZR/testCase/nuevoregistro.py").load_module()
ZonasRepartoRepetir = SourceFileLoader("Repetir01ZR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZR/testCase/repetirregistro.py").load_module()
ZonasRepartoModificar = SourceFileLoader("Modificar01ZR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZR/testCase/modificarregistro.py").load_module()
ZonasRepartoEliminar = SourceFileLoader("Eliminar01ZR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZR/testCase/eliminarregistro.py").load_module()
ZonasRepartoConfig = SourceFileLoader("config01ZR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ZR/config.py").load_module()

EmpresasPantalla = SourceFileLoader("Pantalla01EMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EMP/testCase/ingresopantalla.py").load_module()
EmpresasAgregar = SourceFileLoader("Agregar01EMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EMP/testCase/nuevoregistro.py").load_module()
EmpresasRepetir = SourceFileLoader("Repetir01EMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EMP/testCase/repetirregistro.py").load_module()
EmpresasModificar = SourceFileLoader("Modificar01EMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EMP/testCase/modificarregistro.py").load_module()
EmpresasEliminar = SourceFileLoader("Eliminar01EMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EMP/testCase/eliminarregistro.py").load_module()
EmpresasConfig = SourceFileLoader("config01EMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EMP/config.py").load_module()

TipoPresupuestoPantalla = SourceFileLoader("Pantalla01TPP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPP/testCase/ingresopantalla.py").load_module()
TipoPresupuestoAgregar = SourceFileLoader("Agregar01TPP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPP/testCase/nuevoregistro.py").load_module()
TipoPresupuestoRepetir = SourceFileLoader("Repetir01TPP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPP/testCase/repetirregistro.py").load_module()
TipoPresupuestoModificar = SourceFileLoader("Modificar01TPP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPP/testCase/modificarregistro.py").load_module()
TipoPresupuestoEliminar = SourceFileLoader("Eliminar01TPP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPP/testCase/eliminarregistro.py").load_module()
TipoPresupuestoConfig = SourceFileLoader("config01TPP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPP/config.py").load_module()

ListaEvalucionPantalla = SourceFileLoader("Pantalla01LEV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LEV/testCase/ingresopantalla.py").load_module()
ListaEvalucionAgregar = SourceFileLoader("Agregar01LEV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LEV/testCase/nuevoregistro.py").load_module()
ListaEvalucionRepetir = SourceFileLoader("Repetir01LEV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LEV/testCase/repetirregistro.py").load_module()
ListaEvalucionModificar = SourceFileLoader("Modificar01LEV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LEV/testCase/modificarregistro.py").load_module()
ListaEvalucionEliminar = SourceFileLoader("Eliminar01LEV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LEV/testCase/eliminarregistro.py").load_module()
ListaEvalucionConfig = SourceFileLoader("config01LEV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LEV/config.py").load_module()

ModeloRespuestaPantalla = SourceFileLoader("Pantalla01MRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MRE/testCase/ingresopantalla.py").load_module()
ModeloRespuestaAgregar = SourceFileLoader("Agregar01MRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MRE/testCase/nuevoregistro.py").load_module()
ModeloRespuestaRepetir = SourceFileLoader("Repetir01MRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MRE/testCase/repetirregistro.py").load_module()
ModeloRespuestaModificar = SourceFileLoader("Modificar01MRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MRE/testCase/modificarregistro.py").load_module()
ModeloRespuestaEliminar = SourceFileLoader("Eliminar01MRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MRE/testCase/eliminarregistro.py").load_module()
ModeloRespuestaConfig = SourceFileLoader("config01MRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MRE/config.py").load_module()

UbicacionesActivosPantalla = SourceFileLoader("Pantalla01UAF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UAF/testCase/ingresopantalla.py").load_module()
UbicacionesActivosAgregar = SourceFileLoader("Agregar01UAF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UAF/testCase/nuevoregistro.py").load_module()
UbicacionesActivosRepetir = SourceFileLoader("Repetir01UAF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UAF/testCase/repetirregistro.py").load_module()
UbicacionesActivosModificar = SourceFileLoader("Modificar01UAF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UAF/testCase/modificarregistro.py").load_module()
UbicacionesActivosEliminar = SourceFileLoader("Eliminar01UAF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UAF/testCase/eliminarregistro.py").load_module()
UbicacionesActivosConfig = SourceFileLoader("config01UAF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UAF/config.py").load_module()

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
		"""Ingresa a pantalla Ubicaciones Geograficas"""
		global continua
		if(continua):
			success = UbicacionGeoPantalla.ingresopantalla.ingresopantalla(self, conditions, UbicacionGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Ubicaciones Geograficas"""
		global continua
		if(continua):
			success = UbicacionGeoAgregar.nuevoregistro.nuevoregistro(self, conditions, UbicacionGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Ubicaciones Geograficas"""
		global continua
		if(continua):
			success = UbicacionGeoRepetir.repetirregistro.repetirregistro(self, conditions, UbicacionGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Ubicaciones Geograficas"""
		global continua
		if(continua):
			success = UbicacionGeoModificar.modificarregistro.modificarregistro(self, conditions, UbicacionGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Ubicaciones Geograficas"""
		global continua
		if(continua):
			success = UbicacionGeoEliminar.eliminarregistro.eliminarregistro(self, conditions, UbicacionGeoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Zonas Geograficas"""
		global continua
		continua = True
		if(continua):
			success = ZonasGeoPantalla.ingresopantalla.ingresopantalla(self, conditions, ZonasGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Zonas Geograficas"""
		global continua
		if(continua):
			success = ZonasGeoAgregar.nuevoregistro.nuevoregistro(self, conditions, ZonasGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Zonas Geograficas"""
		global continua
		if(continua):
			success = ZonasGeoRepetir.repetirregistro.repetirregistro(self, conditions, ZonasGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Zonas Geograficas"""
		global continua
		if(continua):
			success = ZonasGeoModificar.modificarregistro.modificarregistro(self, conditions, ZonasGeoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Zonas Geograficas"""
		global continua
		if(continua):
			success = ZonasGeoEliminar.eliminarregistro.eliminarregistro(self, conditions, ZonasGeoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasGeoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Zonas Venta"""
		global continua
		continua = True
		if(continua):
			success = ZonasVentaPantalla.ingresopantalla.ingresopantalla(self, conditions, ZonasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Zonas Venta"""
		global continua
		if(continua):
			success = ZonasVentaAgregar.nuevoregistro.nuevoregistro(self, conditions, ZonasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Zonas Venta"""
		global continua
		if(continua):
			success = ZonasVentaRepetir.repetirregistro.repetirregistro(self, conditions, ZonasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Zonas Venta"""
		global continua
		if(continua):
			success = ZonasVentaModificar.modificarregistro.modificarregistro(self, conditions, ZonasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Zonas Venta"""
		global continua
		if(continua):
			success = ZonasVentaEliminar.eliminarregistro.eliminarregistro(self, conditions, ZonasVentaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Zonas de Reparto"""
		global continua
		continua = True
		if(continua):
			success = ZonasRepartoPantalla.ingresopantalla.ingresopantalla(self, conditions, ZonasRepartoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Zonas de Reparto"""
		global continua
		if(continua):
			success = ZonasRepartoAgregar.nuevoregistro.nuevoregistro(self, conditions, ZonasRepartoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Zonas de Reparto"""
		global continua
		if(continua):
			success = ZonasRepartoRepetir.repetirregistro.repetirregistro(self, conditions, ZonasRepartoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Zonas de Reparto"""
		global continua
		if(continua):
			success = ZonasRepartoModificar.modificarregistro.modificarregistro(self, conditions, ZonasRepartoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Zonas de Reparto"""
		global continua
		if(continua):
			success = ZonasRepartoEliminar.eliminarregistro.eliminarregistro(self, conditions, ZonasRepartoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ZonasRepartoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Empresas"""
		global continua
		continua = True
		if(continua):
			success = EmpresasPantalla.ingresopantalla.ingresopantalla(self, conditions, EmpresasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Empresas"""
		global continua
		if(continua):
			success = EmpresasAgregar.nuevoregistro.nuevoregistro(self, conditions, EmpresasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Empresas"""
		global continua
		if(continua):
			success = EmpresasRepetir.repetirregistro.repetirregistro(self, conditions, EmpresasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Empresas"""
		global continua
		if(continua):
			success = EmpresasModificar.modificarregistro.modificarregistro(self, conditions, EmpresasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Empresas"""
		global continua
		if(continua):
			success = EmpresasEliminar.eliminarregistro.eliminarregistro(self, conditions, EmpresasConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EmpresasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Tipos Presupuesto"""
		global continua
		continua = True
		if(continua):
			success = TipoPresupuestoPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoPresupuestoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Tipos Presupuesto"""
		global continua
		if(continua):
			success = TipoPresupuestoAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoPresupuestoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Tipos Presupuesto"""
		global continua
		if(continua):
			success = TipoPresupuestoRepetir.repetirregistro.repetirregistro(self, conditions, TipoPresupuestoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Tipos Presupuesto"""
		global continua
		if(continua):
			success = TipoPresupuestoModificar.modificarregistro.modificarregistro(self, conditions, TipoPresupuestoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Tipos Presupuesto"""
		global continua
		if(continua):
			success = TipoPresupuestoEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoPresupuestoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoPresupuestoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Lista Evaluacion"""
		global continua
		continua = True
		if(continua):
			success = ListaEvalucionPantalla.ingresopantalla.ingresopantalla(self, conditions, ListaEvalucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Contactos Lista Evaluacion"""
		global continua
		if(continua):
			success = ListaEvalucionAgregar.nuevoregistro.nuevoregistro(self, conditions, ListaEvalucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Lista Evaluacion"""
		global continua
		if(continua):
			success = ListaEvalucionRepetir.repetirregistro.repetirregistro(self, conditions, ListaEvalucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Contactos Lista Evaluacion"""
		global continua
		if(continua):
			success = ListaEvalucionModificar.modificarregistro.modificarregistro(self, conditions, ListaEvalucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Lista Evaluacion"""
		global continua
		if(continua):
			success = ListaEvalucionEliminar.eliminarregistro.eliminarregistro(self, conditions, ListaEvalucionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaEvalucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Modelo de Respuesta"""
		global continua
		continua = True
		if(continua):
			success = ModeloRespuestaPantalla.ingresopantalla.ingresopantalla(self, conditions, ModeloRespuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Modelo de Respuesta"""
		global continua
		if(continua):
			success = ModeloRespuestaAgregar.nuevoregistro.nuevoregistro(self, conditions, ModeloRespuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Modelo de Respuesta"""
		global continua
		if(continua):
			success = ModeloRespuestaRepetir.repetirregistro.repetirregistro(self, conditions, ModeloRespuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Programas Modelo de Respuesta"""
		global continua
		if(continua):
			success = ModeloRespuestaModificar.modificarregistro.modificarregistro(self, conditions, ModeloRespuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Programas Modelo de Respuesta"""
		global continua
		if(continua):
			success = ModeloRespuestaEliminar.eliminarregistro.eliminarregistro(self, conditions, ModeloRespuestaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloRespuestaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Ubicaciones Activos Fijos"""
		global continua
		continua = True
		if(continua):
			success = UbicacionesActivosPantalla.ingresopantalla.ingresopantalla(self, conditions, UbicacionesActivosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Programas Ubicaciones Activos Fijos"""
		global continua
		if(continua):
			success = UbicacionesActivosAgregar.nuevoregistro.nuevoregistro(self, conditions, UbicacionesActivosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Ubicaciones Activos Fijos"""
		global continua
		if(continua):
			success = UbicacionesActivosRepetir.repetirregistro.repetirregistro(self, conditions, UbicacionesActivosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Ubicaciones Activos Fijos"""
		global continua
		if(continua):
			success = UbicacionesActivosModificar.modificarregistro.modificarregistro(self, conditions, UbicacionesActivosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Ubicaciones Activos Fijos"""
		global continua
		if(continua):
			success = UbicacionesActivosEliminar.eliminarregistro.eliminarregistro(self, conditions, UbicacionesActivosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionesActivosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")

if __name__ == '__main__':
	unittest.main()