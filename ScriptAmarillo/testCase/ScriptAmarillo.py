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

#Objetivos Diarios
ObjetivosDiarios1Pantalla = SourceFileLoader("Pantalla01OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OBD/testCase/ingresopantalla.py").load_module()
ObjetivosDiarios1Agregar = SourceFileLoader("Agregar01OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OBD/testCase/nuevoregistro.py").load_module()
ObjetivosDiarios1Repetir = SourceFileLoader("Repetir01OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OBD/testCase/repetirregistro.py").load_module()
ObjetivosDiarios1Modificar = SourceFileLoader("Modificar01OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OBD/testCase/modificarregistro.py").load_module()
ObjetivosDiarios1Eliminar = SourceFileLoader("Eliminar01OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OBD/testCase/eliminarregistro.py").load_module()
ObjetivosDiarios1Config = SourceFileLoader("config01OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01OBD/config.py").load_module()

ObjetivosDiarios2Pantalla = SourceFileLoader("Pantalla02OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02OBD/testCase/ingresopantalla.py").load_module()
ObjetivosDiarios2Agregar = SourceFileLoader("Agregar02OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02OBD/testCase/nuevoregistro.py").load_module()
ObjetivosDiarios2Repetir = SourceFileLoader("Repetir02OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02OBD/testCase/repetirregistro.py").load_module()
ObjetivosDiarios2Modificar = SourceFileLoader("Modificar02OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02OBD/testCase/modificarregistro.py").load_module()
ObjetivosDiarios2Eliminar = SourceFileLoader("Eliminar02OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02OBD/testCase/eliminarregistro.py").load_module()
ObjetivosDiarios2Config = SourceFileLoader("config02OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02OBD/config.py").load_module()

ObjetivosDiarios3Pantalla = SourceFileLoader("Pantalla03OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03OBD/testCase/ingresopantalla.py").load_module()
ObjetivosDiarios3Agregar = SourceFileLoader("Agregar03OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03OBD/testCase/nuevoregistro.py").load_module()
ObjetivosDiarios3Repetir = SourceFileLoader("Repetir03OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03OBD/testCase/repetirregistro.py").load_module()
ObjetivosDiarios3Modificar = SourceFileLoader("Modificar03OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03OBD/testCase/modificarregistro.py").load_module()
ObjetivosDiarios3Eliminar = SourceFileLoader("Eliminar03OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03OBD/testCase/eliminarregistro.py").load_module()
ObjetivosDiarios3Config = SourceFileLoader("config03OBD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03OBD/config.py").load_module()

#Pop Ups
PopUpsPantalla = SourceFileLoader("Pantalla01PU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PU/testCase/ingresopantalla.py").load_module()
PopUpsAgregar = SourceFileLoader("Agregar01PU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PU/testCase/nuevoregistro.py").load_module()
PopUpsRepetir = SourceFileLoader("Repetir01PU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PU/testCase/repetirregistro.py").load_module()
PopUpsModificar = SourceFileLoader("Modificar01PU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PU/testCase/modificarregistro.py").load_module()
PopUpsEliminar = SourceFileLoader("Eliminar01PU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PU/testCase/eliminarregistro.py").load_module()
PopUpsConfig = SourceFileLoader("config01PU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PU/config.py").load_module()

PaquetesFormPantalla = SourceFileLoader("Pantalla01PF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PF/testCase/ingresopantalla.py").load_module()
PaquetesFormAgregar = SourceFileLoader("Agregar01PF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PF/testCase/nuevoregistro.py").load_module()
PaquetesFormModificar = SourceFileLoader("Modificar01PF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PF/testCase/modificarregistro.py").load_module()
PaquetesFormEliminar = SourceFileLoader("Eliminar01PF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PF/testCase/eliminarregistro.py").load_module()
PaquetesFormConfig = SourceFileLoader("config01PF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PF/config.py").load_module()

PerfilesComisionPantalla = SourceFileLoader("Pantalla01PDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDC/testCase/ingresopantalla.py").load_module()
PerfilesComisionAgregar = SourceFileLoader("Agregar01PDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDC/testCase/nuevoregistro.py").load_module()
PerfilesComisionRepetir = SourceFileLoader("Repetir01PDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDC/testCase/repetirregistro.py").load_module()
PerfilesComisionModificar = SourceFileLoader("Modificar01PDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDC/testCase/modificarregistro.py").load_module()
PerfilesComisionEliminar = SourceFileLoader("Eliminar01PDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDC/testCase/eliminarregistro.py").load_module()
PerfilesComisionConfig = SourceFileLoader("config01PDC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDC/config.py").load_module()

PoliticasVentaPantalla = SourceFileLoader("Pantalla01PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PV/testCase/ingresopantalla.py").load_module()
PoliticasVentaAgregar = SourceFileLoader("Agregar01PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PV/testCase/nuevoregistro.py").load_module()
PoliticasVentaRepetir = SourceFileLoader("Repetir01PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PV/testCase/repetirregistro.py").load_module()
PoliticasVentaModificar = SourceFileLoader("Modificar01PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PV/testCase/modificarregistro.py").load_module()
PoliticasVentaEliminar = SourceFileLoader("Eliminar01PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PV/testCase/eliminarregistro.py").load_module()
PoliticasVentaConfig = SourceFileLoader("config01PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PV/config.py").load_module()

PoliticasVenta2Pantalla = SourceFileLoader("Pantalla02PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta2Agregar = SourceFileLoader("Agregar02PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta2Repetir = SourceFileLoader("Repetir02PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PV/testCase/repetirregistro.py").load_module()
PoliticasVenta2Modificar = SourceFileLoader("Modificar02PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PV/testCase/modificarregistro.py").load_module()
PoliticasVenta2Eliminar = SourceFileLoader("Eliminar02PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta2Config = SourceFileLoader("config02PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02PV/config.py").load_module()

PoliticasVenta3Pantalla = SourceFileLoader("Pantalla03PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta3Agregar = SourceFileLoader("Agregar03PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta3Repetir = SourceFileLoader("Repetir03PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PV/testCase/repetirregistro.py").load_module()
PoliticasVenta3Modificar = SourceFileLoader("Modificar03PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PV/testCase/modificarregistro.py").load_module()
PoliticasVenta3Eliminar = SourceFileLoader("Eliminar03PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta3Config = SourceFileLoader("config03PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03PV/config.py").load_module()

PoliticasVenta4Pantalla = SourceFileLoader("Pantalla04PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta4Agregar = SourceFileLoader("Agregar04PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta4Repetir = SourceFileLoader("Repetir04PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PV/testCase/repetirregistro.py").load_module()
PoliticasVenta4Modificar = SourceFileLoader("Modificar04PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PV/testCase/modificarregistro.py").load_module()
PoliticasVenta4Eliminar = SourceFileLoader("Eliminar04PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta4Config = SourceFileLoader("config04PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04PV/config.py").load_module()

PoliticasVenta5Pantalla = SourceFileLoader("Pantalla05PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/05PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta5Agregar = SourceFileLoader("Agregar05PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/05PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta5Repetir = SourceFileLoader("Repetir05PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/05PV/testCase/repetirregistro.py").load_module()
PoliticasVenta5Modificar = SourceFileLoader("Modificar05PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/05PV/testCase/modificarregistro.py").load_module()
PoliticasVenta5Eliminar = SourceFileLoader("Eliminar05PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/05PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta5Config = SourceFileLoader("config05PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/05PV/config.py").load_module()

PoliticasVenta6Pantalla = SourceFileLoader("Pantalla06PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/06PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta6Agregar = SourceFileLoader("Agregar06PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/06PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta6Repetir = SourceFileLoader("Repetir06PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/06PV/testCase/repetirregistro.py").load_module()
PoliticasVenta6Modificar = SourceFileLoader("Modificar06PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/06PV/testCase/modificarregistro.py").load_module()
PoliticasVenta6Eliminar = SourceFileLoader("Eliminar06PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/06PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta6Config = SourceFileLoader("config06PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/06PV/config.py").load_module()

PoliticasVenta7Pantalla = SourceFileLoader("Pantalla07PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/07PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta7Agregar = SourceFileLoader("Agregar07PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/07PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta7Repetir = SourceFileLoader("Repetir07PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/07PV/testCase/repetirregistro.py").load_module()
PoliticasVenta7Modificar = SourceFileLoader("Modificar07PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/07PV/testCase/modificarregistro.py").load_module()
PoliticasVenta7Eliminar = SourceFileLoader("Eliminar07PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/07PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta7Config = SourceFileLoader("config07PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/07PV/config.py").load_module()

PoliticasVenta8Pantalla = SourceFileLoader("Pantalla08PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/08PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta8Agregar = SourceFileLoader("Agregar08PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/08PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta8Repetir = SourceFileLoader("Repetir08PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/08PV/testCase/repetirregistro.py").load_module()
PoliticasVenta8Modificar = SourceFileLoader("Modificar08PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/08PV/testCase/modificarregistro.py").load_module()
PoliticasVenta8Eliminar = SourceFileLoader("Eliminar08PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/08PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta8Config = SourceFileLoader("config08PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/08PV/config.py").load_module()

PoliticasVenta9Pantalla = SourceFileLoader("Pantalla09PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/09PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta9Agregar = SourceFileLoader("Agregar09PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/09PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta9Repetir = SourceFileLoader("Repetir09PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/09PV/testCase/repetirregistro.py").load_module()
PoliticasVenta9Modificar = SourceFileLoader("Modificar09PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/09PV/testCase/modificarregistro.py").load_module()
PoliticasVenta9Eliminar = SourceFileLoader("Eliminar09PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/09PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta9Config = SourceFileLoader("config09PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/09PV/config.py").load_module()

PoliticasVenta10Pantalla = SourceFileLoader("Pantalla10PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/10PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta10Agregar = SourceFileLoader("Agregar10PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/10PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta10Repetir = SourceFileLoader("Repetir10PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/10PV/testCase/repetirregistro.py").load_module()
PoliticasVenta10Modificar = SourceFileLoader("Modificar10PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/10PV/testCase/modificarregistro.py").load_module()
PoliticasVenta10Eliminar = SourceFileLoader("Eliminar10PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/10PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta10Config = SourceFileLoader("config10PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/10PV/config.py").load_module()

PoliticasVenta11Pantalla = SourceFileLoader("Pantalla11PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/11PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta11Agregar = SourceFileLoader("Agregar11PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/11PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta11Repetir = SourceFileLoader("Repetir11PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/11PV/testCase/repetirregistro.py").load_module()
PoliticasVenta11Modificar = SourceFileLoader("Modificar11PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/11PV/testCase/modificarregistro.py").load_module()
PoliticasVenta11Eliminar = SourceFileLoader("Eliminar11PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/11PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta11Config = SourceFileLoader("config11PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/11PV/config.py").load_module()

PoliticasVenta12Pantalla = SourceFileLoader("Pantalla12PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/12PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta12Agregar = SourceFileLoader("Agregar12PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/12PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta12Repetir = SourceFileLoader("Repetir12PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/12PV/testCase/repetirregistro.py").load_module()
PoliticasVenta12Modificar = SourceFileLoader("Modificar12PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/12PV/testCase/modificarregistro.py").load_module()
PoliticasVenta12Eliminar = SourceFileLoader("Eliminar12PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/12PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta12Config = SourceFileLoader("config12PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/12PV/config.py").load_module()

PoliticasVenta13Pantalla = SourceFileLoader("Pantalla13PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/13PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta13Agregar = SourceFileLoader("Agregar13PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/13PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta13Repetir = SourceFileLoader("Repetir13PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/13PV/testCase/repetirregistro.py").load_module()
PoliticasVenta13Modificar = SourceFileLoader("Modificar13PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/13PV/testCase/modificarregistro.py").load_module()
PoliticasVenta13Eliminar = SourceFileLoader("Eliminar13PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/13PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta13Config = SourceFileLoader("config13PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/13PV/config.py").load_module()

PoliticasVenta14Pantalla = SourceFileLoader("Pantalla14PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/14PV/testCase/ingresopantalla.py").load_module()
PoliticasVenta14Agregar = SourceFileLoader("Agregar14PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/14PV/testCase/nuevoregistro.py").load_module()
PoliticasVenta14Repetir = SourceFileLoader("Repetir14PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/14PV/testCase/repetirregistro.py").load_module()
PoliticasVenta14Modificar = SourceFileLoader("Modificar14PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/14PV/testCase/modificarregistro.py").load_module()
PoliticasVenta14Eliminar = SourceFileLoader("Eliminar14PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/14PV/testCase/eliminarregistro.py").load_module()
PoliticasVenta14Config = SourceFileLoader("config14PV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/14PV/config.py").load_module()

TiposPoliticasPantalla = SourceFileLoader("Pantalla01TP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TP/testCase/ingresopantalla.py").load_module()
TiposPoliticasAgregar = SourceFileLoader("Agregar01TP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TP/testCase/nuevoregistro.py").load_module()
TiposPoliticasRepetir = SourceFileLoader("Repetir01TP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TP/testCase/repetirregistro.py").load_module()
TiposPoliticasModificar = SourceFileLoader("Modificar01TP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TP/testCase/modificarregistro.py").load_module()
TiposPoliticasEliminar = SourceFileLoader("Eliminar01TP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TP/testCase/eliminarregistro.py").load_module()
TiposPoliticasConfig = SourceFileLoader("config01TP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TP/config.py").load_module()

ModeloLiquidacionPantalla = SourceFileLoader("Pantalla01ML", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ML/testCase/ingresopantalla.py").load_module()
ModeloLiquidacionAgregar = SourceFileLoader("Agregar01ML", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ML/testCase/nuevoregistro.py").load_module()
ModeloLiquidacionRepetir = SourceFileLoader("Repetir01ML", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ML/testCase/repetirregistro.py").load_module()
ModeloLiquidacionModificar = SourceFileLoader("Modificar01ML", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ML/testCase/modificarregistro.py").load_module()
ModeloLiquidacionEliminar = SourceFileLoader("Eliminar01ML", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ML/testCase/eliminarregistro.py").load_module()
ModeloLiquidacionConfig = SourceFileLoader("config01ML", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ML/config.py").load_module()

AdHocPantalla = SourceFileLoader("Pantalla01PAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PAH/testCase/ingresopantalla.py").load_module()
AdHocAgregar = SourceFileLoader("Agregar01PAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PAH/testCase/nuevoregistro.py").load_module()
AdHocRepetir = SourceFileLoader("Repetir01PAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PAH/testCase/repetirregistro.py").load_module()
AdHocModificar = SourceFileLoader("Modificar01PAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PAH/testCase/modificarregistro.py").load_module()
AdHocEliminar = SourceFileLoader("Eliminar01PAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PAH/testCase/eliminarregistro.py").load_module()
AdHocConfig = SourceFileLoader("config01PAH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PAH/config.py").load_module()

ProgramacionPoliticasPantalla = SourceFileLoader("Pantalla01PPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PPV/testCase/ingresopantalla.py").load_module()
ProgramacionPoliticasAgregar = SourceFileLoader("Agregar01PPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PPV/testCase/nuevoregistro.py").load_module()
ProgramacionPoliticasRepetir = SourceFileLoader("Repetir01PPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PPV/testCase/repetirregistro.py").load_module()
ProgramacionPoliticasModificar = SourceFileLoader("Modificar01PPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PPV/testCase/modificarregistro.py").load_module()
ProgramacionPoliticasEliminar = SourceFileLoader("Eliminar01PPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PPV/testCase/eliminarregistro.py").load_module()
ProgramacionPoliticasConfig = SourceFileLoader("config01PPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PPV/config.py").load_module()

InstanciasEncuestasPantalla = SourceFileLoader("Pantalla01IE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IE/testCase/ingresopantalla.py").load_module()
InstanciasEncuestasAgregar = SourceFileLoader("Agregar01IE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IE/testCase/nuevoregistro.py").load_module()
InstanciasEncuestasRepetir = SourceFileLoader("Repetir01IE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IE/testCase/repetirregistro.py").load_module()
InstanciasEncuestasModificar = SourceFileLoader("Modificar01IE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IE/testCase/modificarregistro.py").load_module()
InstanciasEncuestasEliminar = SourceFileLoader("Eliminar01IE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IE/testCase/eliminarregistro.py").load_module()
InstanciasEncuestasConfig = SourceFileLoader("config01IE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IE/config.py").load_module()

ClasificacionVendedorPantalla = SourceFileLoader("Pantalla01CLV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV/testCase/ingresopantalla.py").load_module()
ClasificacionVendedorAgregar = SourceFileLoader("Agregar01CLV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV/testCase/nuevoregistro.py").load_module()
ClasificacionVendedorRepetir = SourceFileLoader("Repetir01CLV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV/testCase/repetirregistro.py").load_module()
ClasificacionVendedorModificar = SourceFileLoader("Modificar01CLV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV/testCase/modificarregistro.py").load_module()
ClasificacionVendedorEliminar = SourceFileLoader("Eliminar01CLV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV/testCase/eliminarregistro.py").load_module()
ClasificacionVendedorConfig = SourceFileLoader("config01CLV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV/config.py").load_module()

ClasificacionVendedor2Pantalla = SourceFileLoader("Pantalla01CLV2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV2/testCase/ingresopantalla.py").load_module()
ClasificacionVendedor2Agregar = SourceFileLoader("Agregar01CLV2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV2/testCase/nuevoregistro.py").load_module()
ClasificacionVendedor2Repetir = SourceFileLoader("Repetir01CLV2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV2/testCase/repetirregistro.py").load_module()
ClasificacionVendedor2Modificar = SourceFileLoader("Modificar01CLV2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV2/testCase/modificarregistro.py").load_module()
ClasificacionVendedor2Eliminar = SourceFileLoader("Eliminar01CLV2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV2/testCase/eliminarregistro.py").load_module()
ClasificacionVendedor2Config = SourceFileLoader("config01CLV2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLV2/config.py").load_module()

PlanometriaPantalla = SourceFileLoader("Pantalla01PLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PLA/testCase/ingresopantalla.py").load_module()
PlanometriaAgregar = SourceFileLoader("Agregar01PLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PLA/testCase/nuevoregistro.py").load_module()
PlanometriaRepetir = SourceFileLoader("Repetir01PLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PLA/testCase/repetirregistro.py").load_module()
PlanometriaModificar = SourceFileLoader("Modificar01PLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PLA/testCase/modificarregistro.py").load_module()
PlanometriaEliminar = SourceFileLoader("Eliminar01PLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PLA/testCase/eliminarregistro.py").load_module()
PlanometriaConfig = SourceFileLoader("config01PLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PLA/config.py").load_module()

ClasificacionPoliticasPantalla = SourceFileLoader("Pantalla01CPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CPV/testCase/ingresopantalla.py").load_module()
ClasificacionPoliticasAgregar = SourceFileLoader("Agregar01CPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CPV/testCase/nuevoregistro.py").load_module()
ClasificacionPoliticasRepetir = SourceFileLoader("Repetir01CPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CPV/testCase/repetirregistro.py").load_module()
ClasificacionPoliticasModificar = SourceFileLoader("Modificar01CPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CPV/testCase/modificarregistro.py").load_module()
ClasificacionPoliticasEliminar = SourceFileLoader("Eliminar01CPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CPV/testCase/eliminarregistro.py").load_module()
ClasificacionPoliticasConfig = SourceFileLoader("config01CPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CPV/config.py").load_module()

GruposPoliticas1Pantalla = SourceFileLoader("Pantalla01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/ingresopantalla.py").load_module()
GruposPoliticas1Agregar = SourceFileLoader("Agregar01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/nuevoregistro.py").load_module()
GruposPoliticas1Repetir = SourceFileLoader("Repetir01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/repetirregistro.py").load_module()
GruposPoliticas1Modificar = SourceFileLoader("Modificar01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/modificarregistro.py").load_module()
GruposPoliticas1Eliminar = SourceFileLoader("Eliminar01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/eliminarregistro.py").load_module()
GruposPoliticas1Config = SourceFileLoader("config01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/config.py").load_module()

GruposPoliticas2Pantalla = SourceFileLoader("Pantalla01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/ingresopantalla.py").load_module()
GruposPoliticas2Agregar = SourceFileLoader("Agregar01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/nuevoregistro.py").load_module()
GruposPoliticas2Repetir = SourceFileLoader("Repetir01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/repetirregistro.py").load_module()
GruposPoliticas2Modificar = SourceFileLoader("Modificar01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/modificarregistro.py").load_module()
GruposPoliticas2Eliminar = SourceFileLoader("Eliminar01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/testCase/eliminarregistro.py").load_module()
GruposPoliticas2Config = SourceFileLoader("config01GPV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GPV/config.py").load_module()

TareaRelevamientoPantalla = SourceFileLoader("Pantalla01TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TAR/testCase/ingresopantalla.py").load_module()
TareaRelevamientoAgregar = SourceFileLoader("Agregar01TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TAR/testCase/nuevoregistro.py").load_module()
TareaRelevamientoRepetir = SourceFileLoader("Repetir01TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TAR/testCase/repetirregistro.py").load_module()
TareaRelevamientoModificar = SourceFileLoader("Modificar01TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TAR/testCase/modificarregistro.py").load_module()
TareaRelevamientoEliminar = SourceFileLoader("Eliminar01TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TAR/testCase/eliminarregistro.py").load_module()
TareaRelevamientoConfig = SourceFileLoader("config01TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TAR/config.py").load_module()

TareaRelevamiento2Pantalla = SourceFileLoader("Pantalla02TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TAR/testCase/ingresopantalla.py").load_module()
TareaRelevamiento2Agregar = SourceFileLoader("Agregar02TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TAR/testCase/nuevoregistro.py").load_module()
TareaRelevamiento2Repetir = SourceFileLoader("Repetir02TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TAR/testCase/repetirregistro.py").load_module()
TareaRelevamiento2Modificar = SourceFileLoader("Modificar02TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TAR/testCase/modificarregistro.py").load_module()
TareaRelevamiento2Eliminar = SourceFileLoader("Eliminar02TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TAR/testCase/eliminarregistro.py").load_module()
TareaRelevamiento2Config = SourceFileLoader("config02TAR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TAR/config.py").load_module()

TiposPopUpPantalla = SourceFileLoader("Pantalla01TPU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPU/testCase/ingresopantalla.py").load_module()
TiposPopUpAgregar = SourceFileLoader("Agregar01TPU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPU/testCase/nuevoregistro.py").load_module()
TiposPopUpRepetir = SourceFileLoader("Repetir01TPU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPU/testCase/repetirregistro.py").load_module()
TiposPopUpModificar = SourceFileLoader("Modificar01TPU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPU/testCase/modificarregistro.py").load_module()
TiposPopUpEliminar = SourceFileLoader("Eliminar01TPU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPU/testCase/eliminarregistro.py").load_module()
TiposPopUpConfig = SourceFileLoader("config01TPU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPU/config.py").load_module()

VehiculosPantalla = SourceFileLoader("Pantalla01V", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01V/testCase/ingresopantalla.py").load_module()
VehiculosAgregar = SourceFileLoader("Agregar01V", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01V/testCase/nuevoregistro.py").load_module()
VehiculosRepetir = SourceFileLoader("Repetir01V", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01V/testCase/repetirregistro.py").load_module()
VehiculosModificar = SourceFileLoader("Modificar01V", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01V/testCase/modificarregistro.py").load_module()
VehiculosEliminar = SourceFileLoader("Eliminar01V", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01V/testCase/eliminarregistro.py").load_module()
VehiculosConfig = SourceFileLoader("config01V", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01V/config.py").load_module()

WorkFlowsPantalla = SourceFileLoader("Pantalla01WF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01WF/testCase/ingresopantalla.py").load_module()
WorkFlowsAgregar = SourceFileLoader("Agregar01WF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01WF/testCase/nuevoregistro.py").load_module()
WorkFlowsRepetir = SourceFileLoader("Repetir01WF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01WF/testCase/repetirregistro.py").load_module()
WorkFlowsModificar = SourceFileLoader("Modificar01WF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01WF/testCase/modificarregistro.py").load_module()
WorkFlowsEliminar = SourceFileLoader("Eliminar01WF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01WF/testCase/eliminarregistro.py").load_module()
WorkFlowsConfig = SourceFileLoader("config01WF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01WF/config.py").load_module()

PerfilesMovilesPantalla = SourceFileLoader("Pantalla01PM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PM/testCase/ingresopantalla.py").load_module()
PerfilesMovilesAgregar = SourceFileLoader("Agregar01PM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PM/testCase/nuevoregistro.py").load_module()
PerfilesMovilesRepetir = SourceFileLoader("Repetir01PM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PM/testCase/repetirregistro.py").load_module()
PerfilesMovilesModificar = SourceFileLoader("Modificar01PM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PM/testCase/modificarregistro.py").load_module()
PerfilesMovilesEliminar = SourceFileLoader("Eliminar01PM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PM/testCase/eliminarregistro.py").load_module()
PerfilesMovilesConfig = SourceFileLoader("config01PM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PM/config.py").load_module()

TipoVendedorPantalla = SourceFileLoader("Pantalla01TV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TV/testCase/ingresopantalla.py").load_module()
TipoVendedorAgregar = SourceFileLoader("Agregar01TV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TV/testCase/nuevoregistro.py").load_module()
TipoVendedorRepetir = SourceFileLoader("Repetir01TV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TV/testCase/repetirregistro.py").load_module()
TipoVendedorModificar = SourceFileLoader("Modificar01TV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TV/testCase/modificarregistro.py").load_module()
TipoVendedorEliminar = SourceFileLoader("Eliminar01TV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TV/testCase/eliminarregistro.py").load_module()
TipoVendedorConfig = SourceFileLoader("config01TV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TV/config.py").load_module()

VendedorPantalla = SourceFileLoader("Pantalla01VE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01VE/testCase/ingresopantalla.py").load_module()
VendedorAgregar = SourceFileLoader("Agregar01VE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01VE/testCase/nuevoregistro.py").load_module()
VendedorRepetir = SourceFileLoader("Repetir01VE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01VE/testCase/repetirregistro.py").load_module()
VendedorModificar = SourceFileLoader("Modificar01VE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01VE/testCase/modificarregistro.py").load_module()
VendedorEliminar = SourceFileLoader("Eliminar01VE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01VE/testCase/eliminarregistro.py").load_module()
VendedorConfig = SourceFileLoader("config01VE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01VE/config.py").load_module()

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
		"""Ingresa a pantalla Objetivos Diarios"""
		global continua
		if(continua):
			success = ObjetivosDiarios1Pantalla.ingresopantalla.ingresopantalla(self, conditions, ObjetivosDiarios1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Objetivos Diarios"""
		global continua
		if(continua):
			success = ObjetivosDiarios1Agregar.nuevoregistro.nuevoregistro(self, conditions, ObjetivosDiarios1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Objetivos Diarios"""
		global continua
		if(continua):
			success = ObjetivosDiarios1Repetir.repetirregistro.repetirregistro(self, conditions, ObjetivosDiarios1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Objetivos Diarios"""
		global continua
		if(continua):
			success = ObjetivosDiarios1Modificar.modificarregistro.modificarregistro(self, conditions, ObjetivosDiarios1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Objetivos Diarios"""
		global continua
		if(continua):
			success = ObjetivosDiarios1Eliminar.eliminarregistro.eliminarregistro(self, conditions, ObjetivosDiarios1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Pop Ups"""
		global continua
		continua = True
		if(continua):
			success = PopUpsPantalla.ingresopantalla.ingresopantalla(self, conditions, PopUpsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Pop Ups"""
		global continua
		if(continua):
			success = PopUpsAgregar.nuevoregistro.nuevoregistro(self, conditions, PopUpsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Pop Ups"""
		global continua
		if(continua):
			success = PopUpsRepetir.repetirregistro.repetirregistro(self, conditions, PopUpsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Pop Ups"""
		global continua
		if(continua):
			success = PopUpsModificar.modificarregistro.modificarregistro(self, conditions, PopUpsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina PopUps"""
		global continua
		if(continua):
			success = PopUpsEliminar.eliminarregistro.eliminarregistro(self, conditions, PopUpsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Paquetes Formulario"""
		global continua
		continua = True
		if(continua):
			success = PaquetesFormPantalla.ingresopantalla.ingresopantalla(self, conditions, PaquetesFormConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Paquetes Formulario"""
		global continua
		if(continua):
			success = PaquetesFormAgregar.nuevoregistro.nuevoregistro(self, conditions, PaquetesFormConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Paquetes Formulario"""
		global continua
		if(continua):
			success = PaquetesFormModificar.modificarregistro.modificarregistro(self, conditions, PaquetesFormConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Paquetes Formulario"""
		global continua
		if(continua):
			success = PaquetesFormEliminar.eliminarregistro.eliminarregistro(self, conditions, PaquetesFormConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PaquetesFormConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Perfiles Comision"""
		global continua
		continua = True
		if(continua):
			success = PerfilesComisionPantalla.ingresopantalla.ingresopantalla(self, conditions, PerfilesComisionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_busqueda = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_busqueda)))
					Cierra_busqueda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Comision"""
		global continua
		if(continua):
			success = PerfilesComisionAgregar.nuevoregistro.nuevoregistro(self, conditions, PerfilesComisionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Perfiles Comision"""
		global continua
		if(continua):
			success = PerfilesComisionRepetir.repetirregistro.repetirregistro(self, conditions, PerfilesComisionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Perfiles Comision"""
		global continua
		if(continua):
			success = PerfilesComisionModificar.modificarregistro.modificarregistro(self, conditions, PerfilesComisionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Perfiles Comision"""
		global continua
		if(continua):
			success = PerfilesComisionEliminar.eliminarregistro.eliminarregistro(self, conditions, PerfilesComisionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PopUpsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesComisionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Politicas de Venta"""
		global continua
		continua = True
		if(continua):
			success = PoliticasVentaPantalla.ingresopantalla.ingresopantalla(self, conditions, PoliticasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Politicas de Venta"""
		global continua
		if(continua):
			success = PoliticasVentaAgregar.nuevoregistro.nuevoregistro(self, conditions, PoliticasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Politicas de Venta"""
		global continua
		if(continua):
			success = PoliticasVentaRepetir.repetirregistro.repetirregistro(self, conditions, PoliticasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Politicas de Venta"""
		global continua
		if(continua):
			success = PoliticasVentaModificar.modificarregistro.modificarregistro(self, conditions, PoliticasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Politicas de Venta"""
		global continua
		if(continua):
			success = PoliticasVentaEliminar.eliminarregistro.eliminarregistro(self, conditions, PoliticasVentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PoliticasVentaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Modelos de Liquidacion"""
		global continua
		continua = True
		if(continua):
			success = ModeloLiquidacionPantalla.ingresopantalla.ingresopantalla(self, conditions, ModeloLiquidacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Modelos de Liquidacion"""
		global continua
		if(continua):
			success = ModeloLiquidacionAgregar.nuevoregistro.nuevoregistro(self, conditions, ModeloLiquidacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Modelos de Liquidacion"""
		global continua
		if(continua):
			success = ModeloLiquidacionRepetir.repetirregistro.repetirregistro(self, conditions, ModeloLiquidacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Modelos de Liquidacion"""
		global continua
		if(continua):
			success = ModeloLiquidacionModificar.modificarregistro.modificarregistro(self, conditions, ModeloLiquidacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Modelos de Liquidacion"""
		global continua
		if(continua):
			success = ModeloLiquidacionEliminar.eliminarregistro.eliminarregistro(self, conditions, ModeloLiquidacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Politicas AdHoc"""
		global continua
		continua = True
		if(continua):
			success = AdHocPantalla.ingresopantalla.ingresopantalla(self, conditions, AdHocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Politicas AdHoc"""
		global continua
		if(continua):
			success = AdHocAgregar.nuevoregistro.nuevoregistro(self, conditions, AdHocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Politicas AdHoc"""
		global continua
		if(continua):
			success = AdHocRepetir.repetirregistro.repetirregistro(self, conditions, AdHocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Politicas AdHoc"""
		global continua
		if(continua):
			success = AdHocModificar.modificarregistro.modificarregistro(self, conditions, AdHocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloLiquidacionConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Politicas AdHoc"""
		global continua
		if(continua):
			success = AdHocEliminar.eliminarregistro.eliminarregistro(self, conditions, AdHocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AdHocConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Programacion de Politicas"""
		global continua
		continua = True
		if(continua):
			success = ProgramacionPoliticasPantalla.ingresopantalla.ingresopantalla(self, conditions, ProgramacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Programacion de Politicas"""
		global continua
		if(continua):
			success = ProgramacionPoliticasAgregar.nuevoregistro.nuevoregistro(self, conditions, ProgramacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Programacion de Politicas"""
		global continua
		if(continua):
			success = ProgramacionPoliticasRepetir.repetirregistro.repetirregistro(self, conditions, ProgramacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Programacion de Politicas"""
		global continua
		if(continua):
			success = ProgramacionPoliticasModificar.modificarregistro.modificarregistro(self, conditions, ProgramacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Programacion de Politicas"""
		global continua
		if(continua):
			success = ProgramacionPoliticasEliminar.eliminarregistro.eliminarregistro(self, conditions, ProgramacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProgramacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Instancias Encuestas"""
		global continua
		continua = True
		if(continua):
			success = InstanciasEncuestasPantalla.ingresopantalla.ingresopantalla(self, conditions, InstanciasEncuestasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Instancias Encuestas"""
		global continua
		if(continua):
			success = InstanciasEncuestasAgregar.nuevoregistro.nuevoregistro(self, conditions, InstanciasEncuestasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Instancias Encuestas"""
		global continua
		if(continua):
			success = InstanciasEncuestasRepetir.repetirregistro.repetirregistro(self, conditions, InstanciasEncuestasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Instancias Encuestas"""
		global continua
		if(continua):
			success = InstanciasEncuestasModificar.modificarregistro.modificarregistro(self, conditions, InstanciasEncuestasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Instancias Encuestas"""
		global continua
		if(continua):
			success = InstanciasEncuestasEliminar.eliminarregistro.eliminarregistro(self, conditions, InstanciasEncuestasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InstanciasEncuestasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Clasificacion Vendedor"""
		global continua
		continua = True
		if(continua):
			success = ClasificacionVendedorPantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificacionVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Clasificacion Vendedor"""
		global continua
		if(continua):
			success = ClasificacionVendedorAgregar.nuevoregistro.nuevoregistro(self, conditions, ClasificacionVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Clasificacion Vendedor"""
		global continua
		if(continua):
			success = ClasificacionVendedorRepetir.repetirregistro.repetirregistro(self, conditions, ClasificacionVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Clasificacion Vendedor"""
		global continua
		if(continua):
			success = ClasificacionVendedorModificar.modificarregistro.modificarregistro(self, conditions, ClasificacionVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Clasificacion Vendedor"""
		global continua
		if(continua):
			success = ClasificacionVendedorEliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificacionVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Clasificacion Vendedor 2"""
		global continua
		continua = True
		if(continua):
			success = ClasificacionVendedor2Pantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificacionVendedor2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Clasificacion Vendedor 2"""
		global continua
		if(continua):
			success = ClasificacionVendedor2Agregar.nuevoregistro.nuevoregistro(self, conditions, ClasificacionVendedor2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Clasificacion Vendedor 2"""
		global continua
		if(continua):
			success = ClasificacionVendedor2Repetir.repetirregistro.repetirregistro(self, conditions, ClasificacionVendedor2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Clasificacion Vendedor 2"""
		global continua
		if(continua):
			success = ClasificacionVendedor2Modificar.modificarregistro.modificarregistro(self, conditions, ClasificacionVendedor2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Clasificacion Vendedor 2"""
		global continua
		if(continua):
			success = ClasificacionVendedor2Eliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificacionVendedor2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionVendedor2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Planometria"""
		global continua
		continua = True
		if(continua):
			success = PlanometriaPantalla.ingresopantalla.ingresopantalla(self, conditions, PlanometriaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Planometria"""
		global continua
		if(continua):
			success = PlanometriaAgregar.nuevoregistro.nuevoregistro(self, conditions, PlanometriaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Planometria"""
		global continua
		if(continua):
			success = PlanometriaRepetir.repetirregistro.repetirregistro(self, conditions, PlanometriaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Planometria"""
		global continua
		if(continua):
			success = PlanometriaModificar.modificarregistro.modificarregistro(self, conditions, PlanometriaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Planometria"""
		global continua
		if(continua):
			success = PlanometriaEliminar.eliminarregistro.eliminarregistro(self, conditions, PlanometriaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PlanometriaConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Clasificacion Politicas"""
		global continua
		continua = True
		if(continua):
			success = ClasificacionPoliticasPantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Clasificacion Politicas"""
		global continua
		if(continua):
			success = ClasificacionPoliticasAgregar.nuevoregistro.nuevoregistro(self, conditions, ClasificacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Clasificacion Politicas"""
		global continua
		if(continua):
			success = ClasificacionPoliticasRepetir.repetirregistro.repetirregistro(self, conditions, ClasificacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Clasificacion Politicas"""
		global continua
		if(continua):
			success = ClasificacionPoliticasModificar.modificarregistro.modificarregistro(self, conditions, ClasificacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Clasificacion Politicas"""
		global continua
		if(continua):
			success = ClasificacionPoliticasEliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificacionPoliticasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionPoliticasConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Grupos Politicas"""
		global continua
		continua = True
		if(continua):
			success = GruposPoliticas1Pantalla.ingresopantalla.ingresopantalla(self, conditions, GruposPoliticas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Grupos Politicas"""
		global continua
		if(continua):
			success = GruposPoliticas1Agregar.nuevoregistro.nuevoregistro(self, conditions, GruposPoliticas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Grupos Politicas"""
		global continua
		if(continua):
			success = GruposPoliticas1Repetir.repetirregistro.repetirregistro(self, conditions, GruposPoliticas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Grupos Politicas"""
		global continua
		if(continua):
			success = GruposPoliticas1Modificar.modificarregistro.modificarregistro(self, conditions, GruposPoliticas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Grupos Politicas"""
		global continua
		if(continua):
			success = GruposPoliticas1Eliminar.eliminarregistro.eliminarregistro(self, conditions, GruposPoliticas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas1Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Tareas Relevamiento"""
		global continua
		continua = True
		if(continua):
			success = TareaRelevamientoPantalla.ingresopantalla.ingresopantalla(self, conditions, TareaRelevamientoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Tareas Relevamiento"""
		global continua
		if(continua):
			success = TareaRelevamientoAgregar.nuevoregistro.nuevoregistro(self, conditions, TareaRelevamientoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Tareas Relevamiento"""
		global continua
		if(continua):
			success = TareaRelevamientoRepetir.repetirregistro.repetirregistro(self, conditions, TareaRelevamientoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Tareas Relevamiento"""
		global continua
		if(continua):
			success = TareaRelevamientoModificar.modificarregistro.modificarregistro(self, conditions, TareaRelevamientoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Tareas Relevamiento"""
		global continua
		if(continua):
			success = TareaRelevamientoEliminar.eliminarregistro.eliminarregistro(self, conditions, TareaRelevamientoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamientoConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Tareas Relevamiento 2"""
		global continua
		continua = True
		if(continua):
			success = TareaRelevamiento2Pantalla.ingresopantalla.ingresopantalla(self, conditions, TareaRelevamiento2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Tareas Relevamiento 2"""
		global continua
		if(continua):
			success = TareaRelevamiento2Agregar.nuevoregistro.nuevoregistro(self, conditions, TareaRelevamiento2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Tareas Relevamiento 2"""
		global continua
		if(continua):
			success = TareaRelevamiento2Repetir.repetirregistro.repetirregistro(self, conditions, TareaRelevamiento2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Tareas Relevamiento 2"""
		global continua
		if(continua):
			success = TareaRelevamiento2Modificar.modificarregistro.modificarregistro(self, conditions, TareaRelevamiento2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Tareas Relevamiento 2"""
		global continua
		if(continua):
			success = TareaRelevamiento2Eliminar.eliminarregistro.eliminarregistro(self, conditions, TareaRelevamiento2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TareaRelevamiento2Config.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Tipos Pop Up"""
		global continua
		continua = True
		if(continua):
			success = TiposPopUpPantalla.ingresopantalla.ingresopantalla(self, conditions, TiposPopUpConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Tipos Pop Up"""
		global continua
		if(continua):
			success = TiposPopUpAgregar.nuevoregistro.nuevoregistro(self, conditions, TiposPopUpConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Tipos Pop Up"""
		global continua
		if(continua):
			success = TiposPopUpRepetir.repetirregistro.repetirregistro(self, conditions, TiposPopUpConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Tipos Pop Up"""
		global continua
		if(continua):
			success = TiposPopUpModificar.modificarregistro.modificarregistro(self, conditions, TiposPopUpConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Tipos Pop Up"""
		global continua
		if(continua):
			success = TiposPopUpEliminar.eliminarregistro.eliminarregistro(self, conditions, TiposPopUpConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposPopUpConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla Vehiculos"""
		global continua
		continua = True
		if(continua):
			success = VehiculosPantalla.ingresopantalla.ingresopantalla(self, conditions, VehiculosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles Vehiculos"""
		global continua
		if(continua):
			success = VehiculosAgregar.nuevoregistro.nuevoregistro(self, conditions, VehiculosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Repetir Registro Vehiculos"""
		global continua
		if(continua):
			success = VehiculosRepetir.repetirregistro.repetirregistro(self, conditions, VehiculosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Modifica Tipos Pop Up"""
		global continua
		if(continua):
			success = VehiculosModificar.modificarregistro.modificarregistro(self, conditions, VehiculosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Elimina Vehiculos"""
		global continua
		if(continua):
			success = VehiculosEliminar.eliminarregistro.eliminarregistro(self, conditions, VehiculosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VehiculosConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Ingresa a pantalla WorkFlows"""
		global continua
		continua = True
		if(continua):
			success = WorkFlowsPantalla.ingresopantalla.ingresopantalla(self, conditions, WorkFlowsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_pantalla)))
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
		"""Agregar Perfiles WorkFlows"""
		global continua
		if(continua):
			success = WorkFlowsAgregar.nuevoregistro.nuevoregistro(self, conditions, WorkFlowsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_092(self):
		"""Repetir Registro WorkFlows"""
		global continua
		if(continua):
			success = WorkFlowsRepetir.repetirregistro.repetirregistro(self, conditions, WorkFlowsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_093(self):
		"""Modifica Tipos Pop Up"""
		global continua
		if(continua):
			success = WorkFlowsModificar.modificarregistro.modificarregistro(self, conditions, WorkFlowsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_094(self):
		"""Elimina WorkFlows"""
		global continua
		if(continua):
			success = WorkFlowsEliminar.eliminarregistro.eliminarregistro(self, conditions, WorkFlowsConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, WorkFlowsConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_095(self):
		"""Ingresa a pantalla Objetivos Diarios 2"""
		global continua
		if(continua):
			success = ObjetivosDiarios2Pantalla.ingresopantalla.ingresopantalla(self, conditions, ObjetivosDiarios2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_096(self):
		"""Agregar Objetivos Diarios 2"""
		global continua
		if(continua):
			success = ObjetivosDiarios2Agregar.nuevoregistro.nuevoregistro(self, conditions, ObjetivosDiarios2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_097(self):
		"""Repetir Registro Objetivos Diarios 2"""
		global continua
		if(continua):
			success = ObjetivosDiarios2Repetir.repetirregistro.repetirregistro(self, conditions, ObjetivosDiarios2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_098(self):
		"""Modifica Objetivos Diarios 2"""
		global continua
		if(continua):
			success = ObjetivosDiarios2Modificar.modificarregistro.modificarregistro(self, conditions, ObjetivosDiarios2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_099(self):
		"""Elimina Objetivos Diarios 2"""
		global continua
		if(continua):
			success = ObjetivosDiarios2Eliminar.eliminarregistro.eliminarregistro(self, conditions, ObjetivosDiarios2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_100(self):
		"""Ingresa a pantalla Tipo Vendedor"""
		global continua
		if(continua):
			success = ObjetivosDiarios3Pantalla.ingresopantalla.ingresopantalla(self, conditions, ObjetivosDiarios3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_101(self):
		"""Agregar Tipo Vendedor"""
		global continua
		if(continua):
			success = ObjetivosDiarios3Agregar.nuevoregistro.nuevoregistro(self, conditions, ObjetivosDiarios3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_102(self):
		"""Repetir Registro Tipo Vendedor"""
		global continua
		if(continua):
			success = ObjetivosDiarios3Repetir.repetirregistro.repetirregistro(self, conditions, ObjetivosDiarios3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_103(self):
		"""Modifica Tipo Vendedor"""
		global continua
		if(continua):
			success = ObjetivosDiarios3Modificar.modificarregistro.modificarregistro(self, conditions, ObjetivosDiarios3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_104(self):
		"""Elimina Tipo Vendedor"""
		global continua
		if(continua):
			success = ObjetivosDiarios3Eliminar.eliminarregistro.eliminarregistro(self, conditions, ObjetivosDiarios3Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ObjetivosDiarios3Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_105(self):
		"""Ingresa a pantalla Objetivos Diarios 3"""
		global continua
		if(continua):
			success = PerfilesMovilesPantalla.ingresopantalla.ingresopantalla(self, conditions, PerfilesMovilesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_106(self):
		"""Agregar Perfiles Moviles"""
		global continua
		if(continua):
			success = PerfilesMovilesAgregar.nuevoregistro.nuevoregistro(self, conditions, PerfilesMovilesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_107(self):
		"""Repetir Registro Perfiles Moviles"""
		global continua
		if(continua):
			success = PerfilesMovilesRepetir.repetirregistro.repetirregistro(self, conditions, PerfilesMovilesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_108(self):
		"""Modifica Perfiles Moviles"""
		global continua
		if(continua):
			success = PerfilesMovilesModificar.modificarregistro.modificarregistro(self, conditions, PerfilesMovilesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_109(self):
		"""Elimina Perfiles Moviles"""
		global continua
		if(continua):
			success = PerfilesMovilesEliminar.eliminarregistro.eliminarregistro(self, conditions, PerfilesMovilesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda_grupos)))
					Cierra_ayuda_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal_grupos = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal_grupos)))
					Cierra_modal_grupos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilesMovilesConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_110(self):
		"""Ingresa a pantalla Grupos Politicas 2"""
		global continua
		continua = True
		if(continua):
			success = GruposPoliticas2Pantalla.ingresopantalla.ingresopantalla(self, conditions, GruposPoliticas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_111(self):
		"""Agregar Perfiles Grupos Politicas 2"""
		global continua
		if(continua):
			success = GruposPoliticas2Agregar.nuevoregistro.nuevoregistro(self, conditions, GruposPoliticas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_112(self):
		"""Repetir Registro Grupos Politicas 2"""
		global continua
		if(continua):
			success = GruposPoliticas2Repetir.repetirregistro.repetirregistro(self, conditions, GruposPoliticas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_113(self):
		"""Modifica Grupos Politicas"""
		global continua
		if(continua):
			success = GruposPoliticas2Modificar.modificarregistro.modificarregistro(self, conditions, GruposPoliticas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_114(self):
		"""Elimina Grupos Politicas 2"""
		global continua
		if(continua):
			success = GruposPoliticas2Eliminar.eliminarregistro.eliminarregistro(self, conditions, GruposPoliticas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposPoliticas2Config.Configuracion.btn_cerrar_pantalla)))
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

	def test_115(self):
		"""Ingresa a pantalla Tipo Vendedor"""
		global continua
		if(continua):
			success = TipoVendedorPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_116(self):
		"""Agregar Tipo Vendedor"""
		global continua
		if(continua):
			success = TipoVendedorAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_117(self):
		"""Repetir Registro Tipo Vendedor"""
		global continua
		if(continua):
			success = TipoVendedorRepetir.repetirregistro.repetirregistro(self, conditions, TipoVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_118(self):
		"""Modifica Tipo Vendedor"""
		global continua
		if(continua):
			success = TipoVendedorModificar.modificarregistro.modificarregistro(self, conditions, TipoVendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_119(self):
		"""Elimina Tipo Vendedor"""
		global continua
		if(continua):
			success = TipoVendedorEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoVendedorConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoVendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_120(self):
		"""Ingresa a pantalla Vendedor"""
		global continua
		if(continua):
			success = VendedorPantalla.ingresopantalla.ingresopantalla(self, conditions, VendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_121(self):
		"""Agregar Vendedor"""
		global continua
		if(continua):
			success = VendedorAgregar.nuevoregistro.nuevoregistro(self, conditions, VendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_122(self):
		"""Repetir Registro Vendedor"""
		global continua
		if(continua):
			success = VendedorRepetir.repetirregistro.repetirregistro(self, conditions, VendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_123(self):
		"""Modifica Vendedor"""
		global continua
		if(continua):
			success = VendedorModificar.modificarregistro.modificarregistro(self, conditions, VendedorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_124(self):
		"""Elimina Vendedor"""
		global continua
		if(continua):
			success = VendedorEliminar.eliminarregistro.eliminarregistro(self, conditions, VendedorConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, VendedorConfig.Configuracion.btn_cerrar_pantalla)))
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

	def test_125(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")

if __name__ == '__main__':
	unittest.main()