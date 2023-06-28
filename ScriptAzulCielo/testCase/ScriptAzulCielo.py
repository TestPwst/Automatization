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
CustomPropertiesPantalla = SourceFileLoader("Pantalla01CTP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CTP/testCase/ingresopantalla.py").load_module()
CustomPropertiesAgregar = SourceFileLoader("Agregar01CTP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CTP/testCase/nuevoregistro.py").load_module()
CustomPropertiesRepetir = SourceFileLoader("Repetir01CTP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CTP/testCase/repetirregistro.py").load_module()
CustomPropertiesModificar = SourceFileLoader("Modificar01CTP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CTP/testCase/modificarregistro.py").load_module()
CustomPropertiesEliminar = SourceFileLoader("Eliminar01CTP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CTP/testCase/eliminarregistro.py").load_module()
CustomPropertiesConfig = SourceFileLoader("config01CTP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CTP/config.py").load_module()

EntidadesMultiPantalla = SourceFileLoader("Pantalla01EM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EM/testCase/ingresopantalla.py").load_module()
EntidadesMultiAgregar = SourceFileLoader("Agregar01EM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EM/testCase/nuevoregistro.py").load_module()
EntidadesMultiRepetir = SourceFileLoader("Repetir01EM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EM/testCase/repetirregistro.py").load_module()
EntidadesMultiModificar = SourceFileLoader("Modificar01EM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EM/testCase/modificarregistro.py").load_module()
EntidadesMultiEliminar = SourceFileLoader("Eliminar01EM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EM/testCase/eliminarregistro.py").load_module()
EntidadesMultiConfig = SourceFileLoader("config01EM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EM/config.py").load_module()

Scheduler1Pantalla = SourceFileLoader("Pantalla01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/ingresopantalla.py").load_module()
Scheduler1Agregar = SourceFileLoader("Agregar01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/nuevoregistro.py").load_module()
Scheduler1Repetir = SourceFileLoader("Repetir01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/repetirregistro.py").load_module()
Scheduler1Modificar = SourceFileLoader("Modificar01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/modificarregistro.py").load_module()
Scheduler1Eliminar = SourceFileLoader("Eliminar01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/testCase/eliminarregistro.py").load_module()
Scheduler1Config = SourceFileLoader("config01ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ASCH/config.py").load_module()

Scheduler2Pantalla = SourceFileLoader("Pantalla02ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02ASCH/testCase/ingresopantalla.py").load_module()
Scheduler2Agregar = SourceFileLoader("Agregar02ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02ASCH/testCase/nuevoregistro.py").load_module()
Scheduler2Repetir = SourceFileLoader("Repetir02ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02ASCH/testCase/repetirregistro.py").load_module()
Scheduler2Modificar = SourceFileLoader("Modificar02ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02ASCH/testCase/modificarregistro.py").load_module()
Scheduler2Eliminar = SourceFileLoader("Eliminar02ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02ASCH/testCase/eliminarregistro.py").load_module()
Scheduler2Config = SourceFileLoader("config02ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02ASCH/config.py").load_module()

Scheduler3Pantalla = SourceFileLoader("Pantalla03ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03ASCH/testCase/ingresopantalla.py").load_module()
Scheduler3Agregar = SourceFileLoader("Agregar03ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03ASCH/testCase/nuevoregistro.py").load_module()
Scheduler3Repetir = SourceFileLoader("Repetir03ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03ASCH/testCase/repetirregistro.py").load_module()
Scheduler3Modificar = SourceFileLoader("Modificar03ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03ASCH/testCase/modificarregistro.py").load_module()
Scheduler3Eliminar = SourceFileLoader("Eliminar03ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03ASCH/testCase/eliminarregistro.py").load_module()
Scheduler3Config = SourceFileLoader("config03ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03ASCH/config.py").load_module()

Scheduler4Pantalla = SourceFileLoader("Pantalla04ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04ASCH/testCase/ingresopantalla.py").load_module()
Scheduler4Agregar = SourceFileLoader("Agregar04ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04ASCH/testCase/nuevoregistro.py").load_module()
Scheduler4Repetir = SourceFileLoader("Repetir04ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04ASCH/testCase/repetirregistro.py").load_module()
Scheduler4Modificar = SourceFileLoader("Modificar04ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04ASCH/testCase/modificarregistro.py").load_module()
Scheduler4Eliminar = SourceFileLoader("Eliminar04ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04ASCH/testCase/eliminarregistro.py").load_module()
Scheduler4Config = SourceFileLoader("config04ASCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04ASCH/config.py").load_module()

ContactosSchedulerPantalla = SourceFileLoader("Pantalla01CS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CS/testCase/ingresopantalla.py").load_module()
ContactosSchedulerAgregar = SourceFileLoader("Agregar01CS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CS/testCase/nuevoregistro.py").load_module()
ContactosSchedulerRepetir = SourceFileLoader("Repetir01CS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CS/testCase/repetirregistro.py").load_module()
ContactosSchedulerModificar = SourceFileLoader("Modificar01CS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CS/testCase/modificarregistro.py").load_module()
ContactosSchedulerEliminar = SourceFileLoader("Eliminar01CS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CS/testCase/eliminarregistro.py").load_module()
ContactosSchedulerConfig = SourceFileLoader("config01CS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CS/config.py").load_module()

ProgramasScheduler1Pantalla = SourceFileLoader("Pantalla01PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PSCH/testCase/ingresopantalla.py").load_module()
ProgramasScheduler1Agregar = SourceFileLoader("Agregar01PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PSCH/testCase/nuevoregistro.py").load_module()
ProgramasScheduler1Repetir = SourceFileLoader("Repetir01PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PSCH/testCase/repetirregistro.py").load_module()
ProgramasScheduler1Modificar = SourceFileLoader("Modificar01PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PSCH/testCase/modificarregistro.py").load_module()
ProgramasScheduler1Eliminar = SourceFileLoader("Eliminar01PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PSCH/testCase/eliminarregistro.py").load_module()
ProgramasScheduler1Config = SourceFileLoader("config01PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PSCH/config.py").load_module()

ProgramasScheduler2Pantalla = SourceFileLoader("Pantalla02PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PSCH/testCase/ingresopantalla.py").load_module()
ProgramasScheduler2Agregar = SourceFileLoader("Agregar02PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PSCH/testCase/nuevoregistro.py").load_module()
ProgramasScheduler2Repetir = SourceFileLoader("Repetir02PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PSCH/testCase/repetirregistro.py").load_module()
ProgramasScheduler2Modificar = SourceFileLoader("Modificar02PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PSCH/testCase/modificarregistro.py").load_module()
ProgramasScheduler2Eliminar = SourceFileLoader("Eliminar02PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PSCH/testCase/eliminarregistro.py").load_module()
ProgramasScheduler2Config = SourceFileLoader("config02PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PSCH/config.py").load_module()

ProgramasScheduler3Pantalla = SourceFileLoader("Pantalla03PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PSCH/testCase/ingresopantalla.py").load_module()
ProgramasScheduler3Agregar = SourceFileLoader("Agregar03PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PSCH/testCase/nuevoregistro.py").load_module()
ProgramasScheduler3Repetir = SourceFileLoader("Repetir03PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PSCH/testCase/repetirregistro.py").load_module()
ProgramasScheduler3Modificar = SourceFileLoader("Modificar03PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PSCH/testCase/modificarregistro.py").load_module()
ProgramasScheduler3Eliminar = SourceFileLoader("Eliminar03PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PSCH/testCase/eliminarregistro.py").load_module()
ProgramasScheduler3Config = SourceFileLoader("config03PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PSCH/config.py").load_module()

ProgramasScheduler4Pantalla = SourceFileLoader("Pantalla04PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PSCH/testCase/ingresopantalla.py").load_module()
ProgramasScheduler4Agregar = SourceFileLoader("Agregar04PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PSCH/testCase/nuevoregistro.py").load_module()
ProgramasScheduler4Repetir = SourceFileLoader("Repetir04PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PSCH/testCase/repetirregistro.py").load_module()
ProgramasScheduler4Modificar = SourceFileLoader("Modificar04PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PSCH/testCase/modificarregistro.py").load_module()
ProgramasScheduler4Eliminar = SourceFileLoader("Eliminar04PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PSCH/testCase/eliminarregistro.py").load_module()
ProgramasScheduler4Config = SourceFileLoader("config04PSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PSCH/config.py").load_module()

InstantaneasPantalla = SourceFileLoader("Pantalla01IT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IT/testCase/ingresopantalla.py").load_module()
InstantaneasAgregar = SourceFileLoader("Agregar01IT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IT/testCase/nuevoregistro.py").load_module()
InstantaneasRepetir = SourceFileLoader("Repetir01IT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IT/testCase/repetirregistro.py").load_module()
InstantaneasModificar = SourceFileLoader("Modificar01IT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IT/testCase/modificarregistro.py").load_module()
InstantaneasEliminar = SourceFileLoader("Eliminar01IT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IT/testCase/eliminarregistro.py").load_module()
InstantaneasConfig = SourceFileLoader("config01IT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IT/config.py").load_module()

MotivosConfirmacionPantalla = SourceFileLoader("Pantalla01MCS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCS/testCase/ingresopantalla.py").load_module()
MotivosConfirmacionAgregar = SourceFileLoader("Agregar01MCS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCS/testCase/nuevoregistro.py").load_module()
MotivosConfirmacionRepetir = SourceFileLoader("Repetir01MCS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCS/testCase/repetirregistro.py").load_module()
MotivosConfirmacionModificar = SourceFileLoader("Modificar01MCS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCS/testCase/modificarregistro.py").load_module()
MotivosConfirmacionEliminar = SourceFileLoader("Eliminar01MCS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCS/testCase/eliminarregistro.py").load_module()
MotivosConfirmacionConfig = SourceFileLoader("config01MCS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCS/config.py").load_module()

ModosCancelacionPantalla = SourceFileLoader("Pantalla01MDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MDC/testCase/ingresopantalla.py").load_module()
ModosCancelacionAgregar = SourceFileLoader("Agregar01MDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MDC/testCase/nuevoregistro.py").load_module()
ModosCancelacionRepetir = SourceFileLoader("Repetir01MDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MDC/testCase/repetirregistro.py").load_module()
ModosCancelacionModificar = SourceFileLoader("Modificar01MDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MDC/testCase/modificarregistro.py").load_module()
ModosCancelacionEliminar = SourceFileLoader("Eliminar01MDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MDC/testCase/eliminarregistro.py").load_module()
ModosCancelacionConfig = SourceFileLoader("config01MDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MDC/config.py").load_module()

PorcentajeDevolucionPantalla = SourceFileLoader("Pantalla01PDD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDD/testCase/ingresopantalla.py").load_module()
PorcentajeDevolucionAgregar = SourceFileLoader("Agregar01PDD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDD/testCase/nuevoregistro.py").load_module()
PorcentajeDevolucionRepetir = SourceFileLoader("Repetir01PDD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDD/testCase/repetirregistro.py").load_module()
PorcentajeDevolucionModificar = SourceFileLoader("Modificar01PDD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDD/testCase/modificarregistro.py").load_module()
PorcentajeDevolucionEliminar = SourceFileLoader("Eliminar01PDD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDD/testCase/eliminarregistro.py").load_module()
PorcentajeDevolucionConfig = SourceFileLoader("config01PDD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDD/config.py").load_module()

FranjasPantalla = SourceFileLoader("Pantalla01FRAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FRAH/testCase/ingresopantalla.py").load_module()
FranjasAgregar = SourceFileLoader("Agregar01FRAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FRAH/testCase/nuevoregistro.py").load_module()
FranjasRepetir = SourceFileLoader("Repetir01FRAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FRAH/testCase/repetirregistro.py").load_module()
FranjasModificar = SourceFileLoader("Modificar01FRAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FRAH/testCase/modificarregistro.py").load_module()
FranjasEliminar = SourceFileLoader("Eliminar01FRAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FRAH/testCase/eliminarregistro.py").load_module()
FranjasConfig = SourceFileLoader("config01FRAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FRAH/config.py").load_module()

ProgramacionPantalla = SourceFileLoader("Pantalla01PDS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDS/testCase/ingresopantalla.py").load_module()
ProgramacionAgregar = SourceFileLoader("Agregar01PDS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDS/testCase/nuevoregistro.py").load_module()
ProgramacionRepetir = SourceFileLoader("Repetir01PDS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDS/testCase/repetirregistro.py").load_module()
ProgramacionModificar = SourceFileLoader("Modificar01PDS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDS/testCase/modificarregistro.py").load_module()
ProgramacionEliminar = SourceFileLoader("Eliminar01PDS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDS/testCase/eliminarregistro.py").load_module()
ProgramacionConfig = SourceFileLoader("config01PDS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDS/config.py").load_module()

OpcionesPantalla = SourceFileLoader("Pantalla01OPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OPC/testCase/ingresopantalla.py").load_module()
OpcionesAgregar = SourceFileLoader("Agregar01OPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OPC/testCase/nuevoregistro.py").load_module()
OpcionesRepetir = SourceFileLoader("Repetir01OPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OPC/testCase/repetirregistro.py").load_module()
OpcionesModificar = SourceFileLoader("Modificar01OPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OPC/testCase/modificarregistro.py").load_module()
OpcionesEliminar = SourceFileLoader("Eliminar01OPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OPC/testCase/eliminarregistro.py").load_module()
OpcionesConfig = SourceFileLoader("config01OPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OPC/config.py").load_module()

ProgramacionSchedulerPantalla = SourceFileLoader("Pantalla01PRSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRSCH/testCase/ingresopantalla.py").load_module()
ProgramacionSchedulerAgregar = SourceFileLoader("Agregar01PRSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRSCH/testCase/nuevoregistro.py").load_module()
ProgramacionSchedulerRepetir = SourceFileLoader("Repetir01PRSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRSCH/testCase/repetirregistro.py").load_module()
ProgramacionSchedulerModificar = SourceFileLoader("Modificar01PRSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRSCH/testCase/modificarregistro.py").load_module()
ProgramacionSchedulerEliminar = SourceFileLoader("Eliminar01PRSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRSCH/testCase/eliminarregistro.py").load_module()
ProgramacionSchedulerConfig = SourceFileLoader("config01PRSCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRSCH/config.py").load_module()

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
			success = CustomPropertiesPantalla.ingresopantalla.ingresopantalla(self, conditions, CustomPropertiesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_pantalla)))
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
			success = CustomPropertiesAgregar.nuevoregistro.nuevoregistro(self, conditions, CustomPropertiesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_pantalla)))
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
			success = CustomPropertiesRepetir.repetirregistro.repetirregistro(self, conditions, CustomPropertiesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_pantalla)))
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
			success = CustomPropertiesModificar.modificarregistro.modificarregistro(self, conditions, CustomPropertiesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_pantalla)))
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
			success = CustomPropertiesEliminar.eliminarregistro.eliminarregistro(self, conditions, CustomPropertiesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CustomPropertiesConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Entidades Multiproposito"""
		global continua
		continua = True
		if(continua):
			success = EntidadesMultiPantalla.ingresopantalla.ingresopantalla(self, conditions, EntidadesMultiConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Entidades Multiproposito"""
		global continua
		if(continua):
			success = EntidadesMultiAgregar.nuevoregistro.nuevoregistro(self, conditions, EntidadesMultiConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Entidades Multiproposito"""
		global continua
		if(continua):
			success = EntidadesMultiRepetir.repetirregistro.repetirregistro(self, conditions, EntidadesMultiConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Entidades Multiproposito"""
		global continua
		if(continua):
			success = EntidadesMultiModificar.modificarregistro.modificarregistro(self, conditions, EntidadesMultiConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Entidades Multiproposito"""
		global continua
		if(continua):
			success = EntidadesMultiEliminar.eliminarregistro.eliminarregistro(self, conditions, EntidadesMultiConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntidadesMultiConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Scheduler 1"""
		global continua
		continua = True
		if(continua):
			success = Scheduler1Pantalla.ingresopantalla.ingresopantalla(self, conditions, Scheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Scheduler 1"""
		global continua
		if(continua):
			success = Scheduler1Agregar.nuevoregistro.nuevoregistro(self, conditions, Scheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Scheduler 1"""
		global continua
		if(continua):
			success = Scheduler1Repetir.repetirregistro.repetirregistro(self, conditions, Scheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Scheduler 1"""
		global continua
		if(continua):
			success = Scheduler1Modificar.modificarregistro.modificarregistro(self, conditions, Scheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Scheduler 1"""
		global continua
		if(continua):
			success = Scheduler1Eliminar.eliminarregistro.eliminarregistro(self, conditions, Scheduler1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Scheduler 2"""
		global continua
		continua = True
		if(continua):
			success = Scheduler2Pantalla.ingresopantalla.ingresopantalla(self, conditions, Scheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Scheduler 2"""
		global continua
		if(continua):
			success = Scheduler2Agregar.nuevoregistro.nuevoregistro(self, conditions, Scheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Scheduler 2"""
		global continua
		if(continua):
			success = Scheduler2Repetir.repetirregistro.repetirregistro(self, conditions, Scheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Scheduler 2"""
		global continua
		if(continua):
			success = Scheduler2Modificar.modificarregistro.modificarregistro(self, conditions, Scheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Scheduler 2"""
		global continua
		if(continua):
			success = Scheduler2Eliminar.eliminarregistro.eliminarregistro(self, conditions, Scheduler2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Scheduler 3"""
		global continua
		continua = True
		if(continua):
			success = Scheduler3Pantalla.ingresopantalla.ingresopantalla(self, conditions, Scheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Scheduler 3"""
		global continua
		if(continua):
			success = Scheduler3Agregar.nuevoregistro.nuevoregistro(self, conditions, Scheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Scheduler 3"""
		global continua
		if(continua):
			success = Scheduler3Repetir.repetirregistro.repetirregistro(self, conditions, Scheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Scheduler 3"""
		global continua
		if(continua):
			success = Scheduler3Modificar.modificarregistro.modificarregistro(self, conditions, Scheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Scheduler 3"""
		global continua
		if(continua):
			success = Scheduler3Eliminar.eliminarregistro.eliminarregistro(self, conditions, Scheduler3Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Scheduler 4"""
		global continua
		continua = True
		if(continua):
			success = Scheduler4Pantalla.ingresopantalla.ingresopantalla(self, conditions, Scheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Scheduler 4"""
		global continua
		if(continua):
			success = Scheduler4Agregar.nuevoregistro.nuevoregistro(self, conditions, Scheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Scheduler 4"""
		global continua
		if(continua):
			success = Scheduler4Repetir.repetirregistro.repetirregistro(self, conditions, Scheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Scheduler 4"""
		global continua
		if(continua):
			success = Scheduler4Modificar.modificarregistro.modificarregistro(self, conditions, Scheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Scheduler 4"""
		global continua
		if(continua):
			success = Scheduler4Eliminar.eliminarregistro.eliminarregistro(self, conditions, Scheduler4Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, Scheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Contactos Scheduler"""
		global continua
		continua = True
		if(continua):
			success = ContactosSchedulerPantalla.ingresopantalla.ingresopantalla(self, conditions, ContactosSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Contactos Scheduler"""
		global continua
		if(continua):
			success = ContactosSchedulerAgregar.nuevoregistro.nuevoregistro(self, conditions, ContactosSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Contactos Scheduler"""
		global continua
		if(continua):
			success = ContactosSchedulerRepetir.repetirregistro.repetirregistro(self, conditions, ContactosSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Contactos Scheduler"""
		global continua
		if(continua):
			success = ContactosSchedulerModificar.modificarregistro.modificarregistro(self, conditions, ContactosSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Contactos Scheduler"""
		global continua
		if(continua):
			success = ContactosSchedulerEliminar.eliminarregistro.eliminarregistro(self, conditions, ContactosSchedulerConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ContactosSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Programas Scheduler"""
		global continua
		continua = True
		if(continua):
			success = ProgramasScheduler1Pantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramasScheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Programas Scheduler"""
		global continua
		if(continua):
			success = ProgramasScheduler1Agregar.nuevoregistro.nuevoregistro(self, conditions, ProgramasScheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Programas Scheduler"""
		global continua
		if(continua):
			success = ProgramasScheduler1Repetir.repetirregistro.repetirregistro(self, conditions, ProgramasScheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Programas Scheduler"""
		global continua
		if(continua):
			success = ProgramasScheduler1Modificar.modificarregistro.modificarregistro(self, conditions, ProgramasScheduler1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Programas Scheduler"""
		global continua
		if(continua):
			success = ProgramasScheduler1Eliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramasScheduler1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Programas Scheduler 2"""
		global continua
		continua = True
		if(continua):
			success = ProgramasScheduler2Pantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramasScheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Programas Scheduler 2"""
		global continua
		if(continua):
			success = ProgramasScheduler2Agregar.nuevoregistro.nuevoregistro(self, conditions, ProgramasScheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Programas Scheduler 2"""
		global continua
		if(continua):
			success = ProgramasScheduler2Repetir.repetirregistro.repetirregistro(self, conditions, ProgramasScheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Programas Scheduler 2"""
		global continua
		if(continua):
			success = ProgramasScheduler2Modificar.modificarregistro.modificarregistro(self, conditions, ProgramasScheduler2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Programas Scheduler 2"""
		global continua
		if(continua):
			success = ProgramasScheduler2Eliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramasScheduler2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Programas Scheduler 3"""
		global continua
		continua = True
		if(continua):
			success = ProgramasScheduler3Pantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramasScheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Programas Scheduler 3"""
		global continua
		if(continua):
			success = ProgramasScheduler3Agregar.nuevoregistro.nuevoregistro(self, conditions, ProgramasScheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Programas Scheduler 3"""
		global continua
		if(continua):
			success = ProgramasScheduler3Repetir.repetirregistro.repetirregistro(self, conditions, ProgramasScheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Programas Scheduler 3"""
		global continua
		if(continua):
			success = ProgramasScheduler3Modificar.modificarregistro.modificarregistro(self, conditions, ProgramasScheduler3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Programas Scheduler 3"""
		global continua
		if(continua):
			success = ProgramasScheduler3Eliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramasScheduler3Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler3Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Programas Scheduler 4"""
		global continua
		continua = True
		if(continua):
			success = ProgramasScheduler4Pantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramasScheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Programas Scheduler 4"""
		global continua
		if(continua):
			success = ProgramasScheduler4Agregar.nuevoregistro.nuevoregistro(self, conditions, ProgramasScheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Programas Scheduler 4"""
		global continua
		if(continua):
			success = ProgramasScheduler4Repetir.repetirregistro.repetirregistro(self, conditions, ProgramasScheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Programas Scheduler 4"""
		global continua
		if(continua):
			success = ProgramasScheduler4Modificar.modificarregistro.modificarregistro(self, conditions, ProgramasScheduler4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Programas Scheduler 4"""
		global continua
		if(continua):
			success = ProgramasScheduler4Eliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramasScheduler4Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramasScheduler4Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Instantaneas"""
		global continua
		continua = True
		if(continua):
			success = InstantaneasPantalla.ingresopantalla.ingresopantalla(self, conditions, InstantaneasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Instantaneas"""
		global continua
		if(continua):
			success = InstantaneasAgregar.nuevoregistro.nuevoregistro(self, conditions, InstantaneasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Instantaneas"""
		global continua
		if(continua):
			success = InstantaneasRepetir.repetirregistro.repetirregistro(self, conditions, InstantaneasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Instantaneas"""
		global continua
		if(continua):
			success = InstantaneasModificar.modificarregistro.modificarregistro(self, conditions, InstantaneasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Instantaneas"""
		global continua
		if(continua):
			success = InstantaneasEliminar.eliminarregistro.eliminarregistro(self, conditions, InstantaneasConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstantaneasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Motivos Confirmacion"""
		global continua
		continua = True
		if(continua):
			success = MotivosConfirmacionPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosConfirmacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Motivos Confirmacion"""
		global continua
		if(continua):
			success = MotivosConfirmacionAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosConfirmacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Motivos Confirmacion"""
		global continua
		if(continua):
			success = MotivosConfirmacionRepetir.repetirregistro.repetirregistro(self, conditions, MotivosConfirmacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Motivos Confirmacion"""
		global continua
		if(continua):
			success = MotivosConfirmacionModificar.modificarregistro.modificarregistro(self, conditions, MotivosConfirmacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Motivos Confirmacion"""
		global continua
		if(continua):
			success = MotivosConfirmacionEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosConfirmacionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosConfirmacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Modos Cancelacion"""
		global continua
		continua = True
		if(continua):
			success = ModosCancelacionPantalla.ingresopantalla.ingresopantalla(self, conditions, ModosCancelacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Modos Cancelacion"""
		global continua
		if(continua):
			success = ModosCancelacionAgregar.nuevoregistro.nuevoregistro(self, conditions, ModosCancelacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Modos Cancelacion"""
		global continua
		if(continua):
			success = ModosCancelacionRepetir.repetirregistro.repetirregistro(self, conditions, ModosCancelacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Modos Cancelacion"""
		global continua
		if(continua):
			success = ModosCancelacionModificar.modificarregistro.modificarregistro(self, conditions, ModosCancelacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Modos Cancelacion"""
		global continua
		if(continua):
			success = ModosCancelacionEliminar.eliminarregistro.eliminarregistro(self, conditions, ModosCancelacionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModosCancelacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Porcentaje Devolucion"""
		global continua
		continua = True
		if(continua):
			success = PorcentajeDevolucionPantalla.ingresopantalla.ingresopantalla(self, conditions, PorcentajeDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Porcentaje Devolucion"""
		global continua
		if(continua):
			success = PorcentajeDevolucionAgregar.nuevoregistro.nuevoregistro(self, conditions, PorcentajeDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Porcentaje Devolucion"""
		global continua
		if(continua):
			success = PorcentajeDevolucionRepetir.repetirregistro.repetirregistro(self, conditions, PorcentajeDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Porcentaje Devolucion"""
		global continua
		if(continua):
			success = PorcentajeDevolucionModificar.modificarregistro.modificarregistro(self, conditions, PorcentajeDevolucionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Porcentaje Devolucion"""
		global continua
		if(continua):
			success = PorcentajeDevolucionEliminar.eliminarregistro.eliminarregistro(self, conditions, PorcentajeDevolucionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PorcentajeDevolucionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Franjas Horarias"""
		global continua
		continua = True
		if(continua):
			success = FranjasPantalla.ingresopantalla.ingresopantalla(self, conditions, FranjasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_072(self):
		"""Agregar Franjas Horarias"""
		global continua
		if(continua):
			success = FranjasAgregar.nuevoregistro.nuevoregistro(self, conditions, FranjasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_073(self):
		"""Repetir Registro Franjas Horarias"""
		global continua
		if(continua):
			success = FranjasRepetir.repetirregistro.repetirregistro(self, conditions, FranjasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_074(self):
		"""Modifica Franjas Horarias"""
		global continua
		if(continua):
			success = FranjasModificar.modificarregistro.modificarregistro(self, conditions, FranjasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_075(self):
		"""Elimina Franjas Horarias"""
		global continua
		if(continua):
			success = FranjasEliminar.eliminarregistro.eliminarregistro(self, conditions, FranjasConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FranjasConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_076(self):
		"""Ingresa a pantalla Programacion Sincronizacion"""
		global continua
		continua = True
		if(continua):
			success = ProgramacionPantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_077(self):
		"""Agregar Programacion Sincronizacion"""
		global continua
		if(continua):
			success = ProgramacionAgregar.nuevoregistro.nuevoregistro(self, conditions, ProgramacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_078(self):
		"""Repetir Registro Programacion Sincronizacion"""
		global continua
		if(continua):
			success = ProgramacionRepetir.repetirregistro.repetirregistro(self, conditions, ProgramacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_079(self):
		"""Modifica Programacion Sincronizacion"""
		global continua
		if(continua):
			success = ProgramacionModificar.modificarregistro.modificarregistro(self, conditions, ProgramacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_080(self):
		"""Elimina Programacion Sincronizacion"""
		global continua
		if(continua):
			success = ProgramacionEliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramacionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_081(self):
		"""Ingresa a pantalla Opciones Sistema"""
		global continua
		continua = True
		if(continua):
			success = OpcionesPantalla.ingresopantalla.ingresopantalla(self, conditions, OpcionesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_082(self):
		"""Agregar Opciones Sistema"""
		global continua
		if(continua):
			success = OpcionesAgregar.nuevoregistro.nuevoregistro(self, conditions, OpcionesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_083(self):
		"""Repetir Registro Opciones Sistema"""
		global continua
		if(continua):
			success = OpcionesRepetir.repetirregistro.repetirregistro(self, conditions, OpcionesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_084(self):
		"""Modifica Opciones Sistema"""
		global continua
		if(continua):
			success = OpcionesModificar.modificarregistro.modificarregistro(self, conditions, OpcionesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_085(self):
		"""Elimina Opciones Sistema"""
		global continua
		if(continua):
			success = OpcionesEliminar.eliminarregistro.eliminarregistro(self, conditions, OpcionesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, OpcionesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_086(self):
		"""Ingresa a pantalla Programacion Scheduler"""
		global continua
		continua = True
		if(continua):
			success = ProgramacionSchedulerPantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramacionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_087(self):
		"""Agregar Programacion Scheduler"""
		global continua
		if(continua):
			success = ProgramacionSchedulerAgregar.nuevoregistro.nuevoregistro(self, conditions, ProgramacionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_088(self):
		"""Repetir Registro Programacion Scheduler"""
		global continua
		if(continua):
			success = ProgramacionSchedulerRepetir.repetirregistro.repetirregistro(self, conditions, ProgramacionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_089(self):
		"""Modifica Programacion Scheduler"""
		global continua
		if(continua):
			success = ProgramacionSchedulerModificar.modificarregistro.modificarregistro(self, conditions, ProgramacionSchedulerConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_090(self):
		"""Elimina Programacion Scheduler"""
		global continua
		if(continua):
			success = ProgramacionSchedulerEliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramacionSchedulerConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionSchedulerConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_091(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")

if __name__ == '__main__':
	unittest.main()