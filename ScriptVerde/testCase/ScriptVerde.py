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
ArticulosPantalla = SourceFileLoader("Pantalla01ART", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ART/testCase/ingresopantalla.py").load_module()
ArticulosAgregar = SourceFileLoader("Agregar01ART", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ART/testCase/nuevoregistro.py").load_module()
ArticulosRepetir = SourceFileLoader("Repetir01ART", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ART/testCase/repetirregistro.py").load_module()
ArticulosModificar = SourceFileLoader("Modificar01ART", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ART/testCase/modificarregistro.py").load_module()
ArticulosEliminar = SourceFileLoader("Eliminar01ART", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ART/testCase/eliminarregistro.py").load_module()
ArticulosConfig = SourceFileLoader("config01ART", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ART/config.py").load_module()

FamiliaArticulosPantalla = SourceFileLoader("Pantalla01FA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FA/testCase/ingresopantalla.py").load_module()
FamiliaArticulosAgregar = SourceFileLoader("Agregar01FA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FA/testCase/nuevoregistro.py").load_module()
FamiliaArticulosRepetir = SourceFileLoader("Repetir01FA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FA/testCase/repetirregistro.py").load_module()
FamiliaArticulosModificar = SourceFileLoader("Modificar01FA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FA/testCase/modificarregistro.py").load_module()
FamiliaArticulosEliminar = SourceFileLoader("Eliminar01FA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FA/testCase/eliminarregistro.py").load_module()
FamiliaArticulosConfig = SourceFileLoader("config01FA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FA/config.py").load_module()

UnidadesPantalla = SourceFileLoader("Pantalla01UN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UN/testCase/ingresopantalla.py").load_module()
UnidadesAgregar = SourceFileLoader("Agregar01UN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UN/testCase/nuevoregistro.py").load_module()
UnidadesRepetir = SourceFileLoader("Repetir01UN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UN/testCase/repetirregistro.py").load_module()
UnidadesModificar = SourceFileLoader("Modificar01UN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UN/testCase/modificarregistro.py").load_module()
UnidadesEliminar = SourceFileLoader("Eliminar01UN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UN/testCase/eliminarregistro.py").load_module()
UnidadesConfig = SourceFileLoader("config01UN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UN/config.py").load_module()

TiposEmpaquePantalla = SourceFileLoader("Pantalla01TEM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEM/testCase/ingresopantalla.py").load_module()
TiposEmpaqueAgregar = SourceFileLoader("Agregar01TEM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEM/testCase/nuevoregistro.py").load_module()
TiposEmpaqueRepetir = SourceFileLoader("Repetir01TEM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEM/testCase/repetirregistro.py").load_module()
TiposEmpaqueModificar = SourceFileLoader("Modificar01TEM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEM/testCase/modificarregistro.py").load_module()
TiposEmpaqueEliminar = SourceFileLoader("Eliminar01TEM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEM/testCase/eliminarregistro.py").load_module()
TiposEmpaqueConfig = SourceFileLoader("config01TEM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEM/config.py").load_module()

FamiliasLPPantalla = SourceFileLoader("Pantalla01FLP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FLP/testCase/ingresopantalla.py").load_module()
FamiliasLPAgregar = SourceFileLoader("Agregar01FLP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FLP/testCase/nuevoregistro.py").load_module()
FamiliasLPRepetir = SourceFileLoader("Repetir01FLP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FLP/testCase/repetirregistro.py").load_module()
FamiliasLPModificar = SourceFileLoader("Modificar01FLP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FLP/testCase/modificarregistro.py").load_module()
FamiliasLPEliminar = SourceFileLoader("Eliminar01FLP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FLP/testCase/eliminarregistro.py").load_module()
FamiliasLPConfig = SourceFileLoader("config01FLP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FLP/config.py").load_module()

LineasNegocioPantalla = SourceFileLoader("Pantalla01LC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LC/testCase/ingresopantalla.py").load_module()
LineasNegocioAgregar = SourceFileLoader("Agregar01LC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LC/testCase/nuevoregistro.py").load_module()
LineasNegocioRepetir = SourceFileLoader("Repetir01LC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LC/testCase/repetirregistro.py").load_module()
LineasNegocioModificar = SourceFileLoader("Modificar01LC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LC/testCase/modificarregistro.py").load_module()
LineasNegocioEliminar = SourceFileLoader("Eliminar01LC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LC/testCase/eliminarregistro.py").load_module()
LineasNegocioConfig = SourceFileLoader("config01LC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LC/config.py").load_module()

ArquitecturaProd1Pantalla = SourceFileLoader("Pantalla01AP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP/testCase/ingresopantalla.py").load_module()
ArquitecturaProd1Agregar = SourceFileLoader("Agregar01AP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP/testCase/nuevoregistro.py").load_module()
ArquitecturaProd1Repetir = SourceFileLoader("Repetir01AP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP/testCase/repetirregistro.py").load_module()
ArquitecturaProd1Modificar = SourceFileLoader("Modificar01AP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP/testCase/modificarregistro.py").load_module()
ArquitecturaProd1Eliminar = SourceFileLoader("Eliminar01AP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP/testCase/eliminarregistro.py").load_module()
ArquitecturaProd1Config = SourceFileLoader("config01AP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP/config.py").load_module()

ArquitecturaProd2Pantalla = SourceFileLoader("Pantalla01AP2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP2/testCase/ingresopantalla.py").load_module()
ArquitecturaProd2Agregar = SourceFileLoader("Agregar01AP2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP2/testCase/nuevoregistro.py").load_module()
ArquitecturaProd2Repetir = SourceFileLoader("Repetir01AP2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP2/testCase/repetirregistro.py").load_module()
ArquitecturaProd2Modificar = SourceFileLoader("Modificar01AP2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP2/testCase/modificarregistro.py").load_module()
ArquitecturaProd2Eliminar = SourceFileLoader("Eliminar01AP2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP2/testCase/eliminarregistro.py").load_module()
ArquitecturaProd2Config = SourceFileLoader("config01AP2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AP2/config.py").load_module()

MarcasEquipoPantalla = SourceFileLoader("Pantalla01ME", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ME/testCase/ingresopantalla.py").load_module()
MarcasEquipoAgregar = SourceFileLoader("Agregar01ME", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ME/testCase/nuevoregistro.py").load_module()
MarcasEquipoRepetir = SourceFileLoader("Repetir01ME", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ME/testCase/repetirregistro.py").load_module()
MarcasEquipoModificar = SourceFileLoader("Modificar01ME", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ME/testCase/modificarregistro.py").load_module()
MarcasEquipoEliminar = SourceFileLoader("Eliminar01ME", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ME/testCase/eliminarregistro.py").load_module()
MarcasEquipoConfig = SourceFileLoader("config01ME", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ME/config.py").load_module()

ClasesEquipoPantalla = SourceFileLoader("Pantalla01CLE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLE/testCase/ingresopantalla.py").load_module()
ClasesEquipoAgregar = SourceFileLoader("Agregar01CLE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLE/testCase/nuevoregistro.py").load_module()
ClasesEquipoRepetir = SourceFileLoader("Repetir01CLE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLE/testCase/repetirregistro.py").load_module()
ClasesEquipoModificar = SourceFileLoader("Modificar01CLE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLE/testCase/modificarregistro.py").load_module()
ClasesEquipoEliminar = SourceFileLoader("Eliminar01CLE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLE/testCase/eliminarregistro.py").load_module()
ClasesEquipoConfig = SourceFileLoader("config01CLE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLE/config.py").load_module()

SaboresPantalla = SourceFileLoader("Pantalla01SB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01SB/testCase/ingresopantalla.py").load_module()
SaboresAgregar = SourceFileLoader("Agregar01SB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01SB/testCase/nuevoregistro.py").load_module()
SaboresRepetir = SourceFileLoader("Repetir01SB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01SB/testCase/repetirregistro.py").load_module()
SaboresModificar = SourceFileLoader("Modificar01SB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01SB/testCase/modificarregistro.py").load_module()
SaboresEliminar = SourceFileLoader("Eliminar01SB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01SB/testCase/eliminarregistro.py").load_module()
SaboresConfig = SourceFileLoader("config01SB", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01SB/config.py").load_module()

TiposProductosPantalla = SourceFileLoader("Pantalla01TDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDP/testCase/ingresopantalla.py").load_module()
TiposProductosAgregar = SourceFileLoader("Agregar01TDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDP/testCase/nuevoregistro.py").load_module()
TiposProductosRepetir = SourceFileLoader("Repetir01TDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDP/testCase/repetirregistro.py").load_module()
TiposProductosModificar = SourceFileLoader("Modificar01TDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDP/testCase/modificarregistro.py").load_module()
TiposProductosEliminar = SourceFileLoader("Eliminar01TDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDP/testCase/eliminarregistro.py").load_module()
TiposProductosConfig = SourceFileLoader("config01TDP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDP/config.py").load_module()

ClasificArticulo1Pantalla = SourceFileLoader("Pantalla01CLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA/testCase/ingresopantalla.py").load_module()
ClasificArticulo1Agregar = SourceFileLoader("Agregar01CLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA/testCase/nuevoregistro.py").load_module()
ClasificArticulo1Repetir = SourceFileLoader("Repetir01CLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA/testCase/repetirregistro.py").load_module()
ClasificArticulo1Modificar = SourceFileLoader("Modificar01CLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA/testCase/modificarregistro.py").load_module()
ClasificArticulo1Eliminar = SourceFileLoader("Eliminar01CLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA/testCase/eliminarregistro.py").load_module()
ClasificArticulo1Config = SourceFileLoader("config01CLA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA/config.py").load_module()

ClasificArticulo2Pantalla = SourceFileLoader("Pantalla01CLA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA2/testCase/ingresopantalla.py").load_module()
ClasificArticulo2Agregar = SourceFileLoader("Agregar01CLA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA2/testCase/nuevoregistro.py").load_module()
ClasificArticulo2Repetir = SourceFileLoader("Repetir01CLA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA2/testCase/repetirregistro.py").load_module()
ClasificArticulo2Modificar = SourceFileLoader("Modificar01CLA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA2/testCase/modificarregistro.py").load_module()
ClasificArticulo2Eliminar = SourceFileLoader("Eliminar01CLA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA2/testCase/eliminarregistro.py").load_module()
ClasificArticulo2Config = SourceFileLoader("config01CLA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA2/config.py").load_module()

ClasificArticulo3Pantalla = SourceFileLoader("Pantalla01CLA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA3/testCase/ingresopantalla.py").load_module()
ClasificArticulo3Agregar = SourceFileLoader("Agregar01CLA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA3/testCase/nuevoregistro.py").load_module()
ClasificArticulo3Repetir = SourceFileLoader("Repetir01CLA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA3/testCase/repetirregistro.py").load_module()
ClasificArticulo3Modificar = SourceFileLoader("Modificar01CLA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA3/testCase/modificarregistro.py").load_module()
ClasificArticulo3Eliminar = SourceFileLoader("Eliminar01CLA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA3/testCase/eliminarregistro.py").load_module()
ClasificArticulo3Config = SourceFileLoader("config01CLA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA3/config.py").load_module()

ClasificArticulo4Pantalla = SourceFileLoader("Pantalla01CLA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA4/testCase/ingresopantalla.py").load_module()
ClasificArticulo4Agregar = SourceFileLoader("Agregar01CLA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA4/testCase/nuevoregistro.py").load_module()
ClasificArticulo4Repetir = SourceFileLoader("Repetir01CLA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA4/testCase/repetirregistro.py").load_module()
ClasificArticulo4Modificar = SourceFileLoader("Modificar01CLA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA4/testCase/modificarregistro.py").load_module()
ClasificArticulo4Eliminar = SourceFileLoader("Eliminar01CLA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA4/testCase/eliminarregistro.py").load_module()
ClasificArticulo4Config = SourceFileLoader("config01CLA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLA4/config.py").load_module()

InfoArticulo1Pantalla = SourceFileLoader("Pantalla01IA1", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA1/testCase/ingresopantalla.py").load_module()
InfoArticulo1Agregar = SourceFileLoader("Agregar01IA1", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA1/testCase/nuevoregistro.py").load_module()
InfoArticulo1Repetir = SourceFileLoader("Repetir01IA1", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA1/testCase/repetirregistro.py").load_module()
InfoArticulo1Modificar = SourceFileLoader("Modificar01IA1", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA1/testCase/modificarregistro.py").load_module()
InfoArticulo1Eliminar = SourceFileLoader("Eliminar01IA1", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA1/testCase/eliminarregistro.py").load_module()
InfoArticulo1Config = SourceFileLoader("config01IA1", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA1/config.py").load_module()

InfoArticulo2Pantalla = SourceFileLoader("Pantalla01IA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA2/testCase/ingresopantalla.py").load_module()
InfoArticulo2Agregar = SourceFileLoader("Agregar01IA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA2/testCase/nuevoregistro.py").load_module()
InfoArticulo2Repetir = SourceFileLoader("Repetir01IA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA2/testCase/repetirregistro.py").load_module()
InfoArticulo2Modificar = SourceFileLoader("Modificar01IA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA2/testCase/modificarregistro.py").load_module()
InfoArticulo2Eliminar = SourceFileLoader("Eliminar01IA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA2/testCase/eliminarregistro.py").load_module()
InfoArticulo2Config = SourceFileLoader("config01IA2", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA2/config.py").load_module()

InfoArticulo3Pantalla = SourceFileLoader("Pantalla01IA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA3/testCase/ingresopantalla.py").load_module()
InfoArticulo3Agregar = SourceFileLoader("Agregar01IA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA3/testCase/nuevoregistro.py").load_module()
InfoArticulo3Repetir = SourceFileLoader("Repetir01IA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA3/testCase/repetirregistro.py").load_module()
InfoArticulo3Modificar = SourceFileLoader("Modificar01IA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA3/testCase/modificarregistro.py").load_module()
InfoArticulo3Eliminar = SourceFileLoader("Eliminar01IA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA3/testCase/eliminarregistro.py").load_module()
InfoArticulo3Config = SourceFileLoader("config01IA3", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA3/config.py").load_module()

InfoArticulo4Pantalla = SourceFileLoader("Pantalla01IA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA4/testCase/ingresopantalla.py").load_module()
InfoArticulo4Agregar = SourceFileLoader("Agregar01IA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA4/testCase/nuevoregistro.py").load_module()
InfoArticulo4Repetir = SourceFileLoader("Repetir01IA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA4/testCase/repetirregistro.py").load_module()
InfoArticulo4Modificar = SourceFileLoader("Modificar01IA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA4/testCase/modificarregistro.py").load_module()
InfoArticulo4Eliminar = SourceFileLoader("Eliminar01IA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA4/testCase/eliminarregistro.py").load_module()
InfoArticulo4Config = SourceFileLoader("config01IA4", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA4/config.py").load_module()

InfoArticulo5Pantalla = SourceFileLoader("Pantalla01IA5", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA5/testCase/ingresopantalla.py").load_module()
InfoArticulo5Agregar = SourceFileLoader("Agregar01IA5", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA5/testCase/nuevoregistro.py").load_module()
InfoArticulo5Repetir = SourceFileLoader("Repetir01IA5", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA5/testCase/repetirregistro.py").load_module()
InfoArticulo5Modificar = SourceFileLoader("Modificar01IA5", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA5/testCase/modificarregistro.py").load_module()
InfoArticulo5Eliminar = SourceFileLoader("Eliminar01IA5", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA5/testCase/eliminarregistro.py").load_module()
InfoArticulo5Config = SourceFileLoader("config01IA5", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA5/config.py").load_module()

InfoArticulo6Pantalla = SourceFileLoader("Pantalla01IA6", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA6/testCase/ingresopantalla.py").load_module()
InfoArticulo6Agregar = SourceFileLoader("Agregar01IA6", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA6/testCase/nuevoregistro.py").load_module()
InfoArticulo6Repetir = SourceFileLoader("Repetir01IA6", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA6/testCase/repetirregistro.py").load_module()
InfoArticulo6Modificar = SourceFileLoader("Modificar01IA6", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA6/testCase/modificarregistro.py").load_module()
InfoArticulo6Eliminar = SourceFileLoader("Eliminar01IA6", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA6/testCase/eliminarregistro.py").load_module()
InfoArticulo6Config = SourceFileLoader("config01IA6", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA6/config.py").load_module()

InfoArticulo7Pantalla = SourceFileLoader("Pantalla01IA7", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA7/testCase/ingresopantalla.py").load_module()
InfoArticulo7Agregar = SourceFileLoader("Agregar01IA7", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA7/testCase/nuevoregistro.py").load_module()
InfoArticulo7Repetir = SourceFileLoader("Repetir01IA7", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA7/testCase/repetirregistro.py").load_module()
InfoArticulo7Modificar = SourceFileLoader("Modificar01IA7", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA7/testCase/modificarregistro.py").load_module()
InfoArticulo7Eliminar = SourceFileLoader("Eliminar01IA7", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA7/testCase/eliminarregistro.py").load_module()
InfoArticulo7Config = SourceFileLoader("config01IA7", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA7/config.py").load_module()

InfoArticulo8Pantalla = SourceFileLoader("Pantalla01IA8", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA8/testCase/ingresopantalla.py").load_module()
InfoArticulo8Agregar = SourceFileLoader("Agregar01IA8", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA8/testCase/nuevoregistro.py").load_module()
InfoArticulo8Repetir = SourceFileLoader("Repetir01IA8", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA8/testCase/repetirregistro.py").load_module()
InfoArticulo8Modificar = SourceFileLoader("Modificar01IA8", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA8/testCase/modificarregistro.py").load_module()
InfoArticulo8Eliminar = SourceFileLoader("Eliminar01IA8", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA8/testCase/eliminarregistro.py").load_module()
InfoArticulo8Config = SourceFileLoader("config01IA8", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA8/config.py").load_module()

InfoArticulo9Pantalla = SourceFileLoader("Pantalla01IA9", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA9/testCase/ingresopantalla.py").load_module()
InfoArticulo9Agregar = SourceFileLoader("Agregar01IA9", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA9/testCase/nuevoregistro.py").load_module()
InfoArticulo9Repetir = SourceFileLoader("Repetir01IA9", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA9/testCase/repetirregistro.py").load_module()
InfoArticulo9Modificar = SourceFileLoader("Modificar01IA9", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA9/testCase/modificarregistro.py").load_module()
InfoArticulo9Eliminar = SourceFileLoader("Eliminar01IA9", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA9/testCase/eliminarregistro.py").load_module()
InfoArticulo9Config = SourceFileLoader("config01IA9", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA9/config.py").load_module()

InfoArticulo10Pantalla = SourceFileLoader("Pantalla01IA10", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA10/testCase/ingresopantalla.py").load_module()
InfoArticulo10Agregar = SourceFileLoader("Agregar01IA10", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA10/testCase/nuevoregistro.py").load_module()
InfoArticulo10Repetir = SourceFileLoader("Repetir01IA10", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA10/testCase/repetirregistro.py").load_module()
InfoArticulo10Modificar = SourceFileLoader("Modificar01IA10", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA10/testCase/modificarregistro.py").load_module()
InfoArticulo10Eliminar = SourceFileLoader("Eliminar01IA10", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA10/testCase/eliminarregistro.py").load_module()
InfoArticulo10Config = SourceFileLoader("config01IA10", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IA10/config.py").load_module()

ClientesPantalla = SourceFileLoader("Pantalla01CLN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLN/testCase/ingresopantalla.py").load_module()
ClientesAgregar = SourceFileLoader("Agregar01CLN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLN/testCase/nuevoregistro.py").load_module()
ClientesRepetir = SourceFileLoader("Repetir01CLN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLN/testCase/repetirregistro.py").load_module()
ClientesModificar = SourceFileLoader("Modificar01CLN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLN/testCase/modificarregistro.py").load_module()
ClientesEliminar = SourceFileLoader("Eliminar01CLN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLN/testCase/eliminarregistro.py").load_module()
ClientesConfig = SourceFileLoader("config01CLN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CLN/config.py").load_module()

CanalesPantalla = SourceFileLoader("Pantalla01CA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CA/testCase/ingresopantalla.py").load_module()
CanalesAgregar = SourceFileLoader("Agregar01CA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CA/testCase/nuevoregistro.py").load_module()
CanalesRepetir = SourceFileLoader("Repetir01CA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CA/testCase/repetirregistro.py").load_module()
CanalesModificar = SourceFileLoader("Modificar01CA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CA/testCase/modificarregistro.py").load_module()
CanalesEliminar = SourceFileLoader("Eliminar01CA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CA/testCase/eliminarregistro.py").load_module()
CanalesConfig = SourceFileLoader("config01CA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CA/config.py").load_module()

GruposClientesPantalla = SourceFileLoader("Pantalla01GC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GC/testCase/ingresopantalla.py").load_module()
GruposClientesAgregar = SourceFileLoader("Agregar01GC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GC/testCase/nuevoregistro.py").load_module()
GruposClientesRepetir = SourceFileLoader("Repetir01GC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GC/testCase/repetirregistro.py").load_module()
GruposClientesModificar = SourceFileLoader("Modificar01GC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GC/testCase/modificarregistro.py").load_module()
GruposClientesEliminar = SourceFileLoader("Eliminar01GC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GC/testCase/eliminarregistro.py").load_module()
GruposClientesConfig = SourceFileLoader("config01GC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GC/config.py").load_module()

PerfilCuentaPantalla = SourceFileLoader("Pantalla01PCL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCL/testCase/ingresopantalla.py").load_module()
PerfilCuentaAgregar = SourceFileLoader("Agregar01PCL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCL/testCase/nuevoregistro.py").load_module()
PerfilCuentaRepetir = SourceFileLoader("Repetir01PCL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCL/testCase/repetirregistro.py").load_module()
PerfilCuentaModificar = SourceFileLoader("Modificar01PCL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCL/testCase/modificarregistro.py").load_module()
PerfilCuentaEliminar = SourceFileLoader("Eliminar01PCL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCL/testCase/eliminarregistro.py").load_module()
PerfilCuentaConfig = SourceFileLoader("config01PCL", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCL/config.py").load_module()

CategoriaFiscalPantalla = SourceFileLoader("Pantalla01CF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CF/testCase/ingresopantalla.py").load_module()
CategoriaFiscalAgregar = SourceFileLoader("Agregar01CF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CF/testCase/nuevoregistro.py").load_module()
CategoriaFiscalRepetir = SourceFileLoader("Repetir01CF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CF/testCase/repetirregistro.py").load_module()
CategoriaFiscalModificar = SourceFileLoader("Modificar01CF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CF/testCase/modificarregistro.py").load_module()
CategoriaFiscalEliminar = SourceFileLoader("Eliminar01CF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CF/testCase/eliminarregistro.py").load_module()
CategoriaFiscalConfig = SourceFileLoader("config01CF", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CF/config.py").load_module()

TipoClientePantalla = SourceFileLoader("Pantalla01TC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TC/testCase/ingresopantalla.py").load_module()
TipoClienteAgregar = SourceFileLoader("Agregar01TC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TC/testCase/nuevoregistro.py").load_module()
TipoClienteRepetir = SourceFileLoader("Repetir01TC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TC/testCase/repetirregistro.py").load_module()
TipoClienteModificar = SourceFileLoader("Modificar01TC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TC/testCase/modificarregistro.py").load_module()
TipoClienteEliminar = SourceFileLoader("Eliminar01TC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TC/testCase/eliminarregistro.py").load_module()
TipoClienteConfig = SourceFileLoader("config01TC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TC/config.py").load_module()

AutoCredit1Pantalla = SourceFileLoader("Pantalla01AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AC/testCase/ingresopantalla.py").load_module()
AutoCredit1Agregar = SourceFileLoader("Agregar01AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AC/testCase/nuevoregistro.py").load_module()
AutoCredit1Repetir = SourceFileLoader("Repetir01AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AC/testCase/repetirregistro.py").load_module()
AutoCredit1Modificar = SourceFileLoader("Modificar01AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AC/testCase/modificarregistro.py").load_module()
AutoCredit1Eliminar = SourceFileLoader("Eliminar01AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AC/testCase/eliminarregistro.py").load_module()
AutoCredit1Config = SourceFileLoader("config01AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01AC/config.py").load_module()

AutoCredit2Pantalla = SourceFileLoader("Pantalla02AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02AC/testCase/ingresopantalla.py").load_module()
AutoCredit2Agregar = SourceFileLoader("Agregar02AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02AC/testCase/nuevoregistro.py").load_module()
AutoCredit2Repetir = SourceFileLoader("Repetir02AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02AC/testCase/repetirregistro.py").load_module()
AutoCredit2Modificar = SourceFileLoader("Modificar02AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02AC/testCase/modificarregistro.py").load_module()
AutoCredit2Eliminar = SourceFileLoader("Eliminar02AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02AC/testCase/eliminarregistro.py").load_module()
AutoCredit2Config = SourceFileLoader("config02AC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02AC/config.py").load_module()

TipoExclusividadPantalla = SourceFileLoader("Pantalla01TEX", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEX/testCase/ingresopantalla.py").load_module()
TipoExclusividadAgregar = SourceFileLoader("Agregar01TEX", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEX/testCase/nuevoregistro.py").load_module()
TipoExclusividadRepetir = SourceFileLoader("Repetir01TEX", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEX/testCase/repetirregistro.py").load_module()
TipoExclusividadModificar = SourceFileLoader("Modificar01TEX", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEX/testCase/modificarregistro.py").load_module()
TipoExclusividadEliminar = SourceFileLoader("Eliminar01TEX", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEX/testCase/eliminarregistro.py").load_module()
TipoExclusividadConfig = SourceFileLoader("config01TEX", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TEX/config.py").load_module()

DistribuidorPantalla = SourceFileLoader("Pantalla01DIS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DIS/testCase/ingresopantalla.py").load_module()
DistribuidorAgregar = SourceFileLoader("Agregar01DIS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DIS/testCase/nuevoregistro.py").load_module()
DistribuidorRepetir = SourceFileLoader("Repetir01DIS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DIS/testCase/repetirregistro.py").load_module()
DistribuidorModificar = SourceFileLoader("Modificar01DIS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DIS/testCase/modificarregistro.py").load_module()
DistribuidorEliminar = SourceFileLoader("Eliminar01DIS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DIS/testCase/eliminarregistro.py").load_module()
DistribuidorConfig = SourceFileLoader("config01DIS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DIS/config.py").load_module()

TipoDistribuidorPantalla = SourceFileLoader("Pantalla01TPD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPD/testCase/ingresopantalla.py").load_module()
TipoDistribuidorAgregar = SourceFileLoader("Agregar01TPD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPD/testCase/nuevoregistro.py").load_module()
TipoDistribuidorRepetir = SourceFileLoader("Repetir01TPD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPD/testCase/repetirregistro.py").load_module()
TipoDistribuidorModificar = SourceFileLoader("Modificar01TPD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPD/testCase/modificarregistro.py").load_module()
TipoDistribuidorEliminar = SourceFileLoader("Eliminar01TPD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPD/testCase/eliminarregistro.py").load_module()
TipoDistribuidorConfig = SourceFileLoader("config01TPD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPD/config.py").load_module()

TipoAgenciaPantalla = SourceFileLoader("Pantalla01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TA/testCase/ingresopantalla.py").load_module()
TipoAgenciaAgregar = SourceFileLoader("Agregar01TA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TA/testCase/nuevoregistro.py").load_module()
TipoAgenciaRepetir = SourceFileLoader("Repetir01TA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TA/testCase/repetirregistro.py").load_module()
TipoAgenciaModificar = SourceFileLoader("Modificar01TA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TA/testCase/modificarregistro.py").load_module()
TipoAgenciaEliminar = SourceFileLoader("Eliminar01TA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TA/testCase/eliminarregistro.py").load_module()
TipoAgenciaConfig = SourceFileLoader("config01TA", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TA/config.py").load_module()

TipoOficinaPantalla = SourceFileLoader("Pantalla01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TO/testCase/ingresopantalla.py").load_module()
TipoOficinaAgregar = SourceFileLoader("Agregar01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TO/testCase/nuevoregistro.py").load_module()
TipoOficinaRepetir = SourceFileLoader("Repetir01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TO/testCase/repetirregistro.py").load_module()
TipoOficinaModificar = SourceFileLoader("Modificar01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TO/testCase/modificarregistro.py").load_module()
TipoOficinaEliminar = SourceFileLoader("Eliminar01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TO/testCase/eliminarregistro.py").load_module()
TipoOficinaConfig = SourceFileLoader("config01TO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TO/config.py").load_module()

MatricesPantalla = SourceFileLoader("Pantalla01MAT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MAT/testCase/ingresopantalla.py").load_module()
MatricesAgregar = SourceFileLoader("Agregar01MAT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MAT/testCase/nuevoregistro.py").load_module()
MatricesRepetir = SourceFileLoader("Repetir01MAT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MAT/testCase/repetirregistro.py").load_module()
MatricesModificar = SourceFileLoader("Modificar01MAT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MAT/testCase/modificarregistro.py").load_module()
MatricesEliminar = SourceFileLoader("Eliminar01MAT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MAT/testCase/eliminarregistro.py").load_module()
MatricesConfig = SourceFileLoader("config01MAT", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MAT/config.py").load_module()

TipoMatrizPantalla = SourceFileLoader("Pantalla01TM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TM/testCase/ingresopantalla.py").load_module()
TipoMatrizAgregar = SourceFileLoader("Agregar01TM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TM/testCase/nuevoregistro.py").load_module()
TipoMatrizRepetir = SourceFileLoader("Repetir01TM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TM/testCase/repetirregistro.py").load_module()
TipoMatrizModificar = SourceFileLoader("Modificar01TM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TM/testCase/modificarregistro.py").load_module()
TipoMatrizEliminar = SourceFileLoader("Eliminar01TM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TM/testCase/eliminarregistro.py").load_module()
TipoMatrizConfig = SourceFileLoader("config01TM", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TM/config.py").load_module()

TipoCompañiaPantalla = SourceFileLoader("Pantalla01TPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPC/testCase/ingresopantalla.py").load_module()
TipoCompañiaAgregar = SourceFileLoader("Agregar01TPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPC/testCase/nuevoregistro.py").load_module()
TipoCompañiaRepetir = SourceFileLoader("Repetir01TPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPC/testCase/repetirregistro.py").load_module()
TipoCompañiaModificar = SourceFileLoader("Modificar01TPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPC/testCase/modificarregistro.py").load_module()
TipoCompañiaEliminar = SourceFileLoader("Eliminar01TPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPC/testCase/eliminarregistro.py").load_module()
TipoCompañiaConfig = SourceFileLoader("config01TPC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPC/config.py").load_module()

TipoRegionalPantalla = SourceFileLoader("Pantalla01TPR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPR/testCase/ingresopantalla.py").load_module()
TipoRegionalAgregar = SourceFileLoader("Agregar01TPR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPR/testCase/nuevoregistro.py").load_module()
TipoRegionalRepetir = SourceFileLoader("Repetir01TPR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPR/testCase/repetirregistro.py").load_module()
TipoRegionalModificar = SourceFileLoader("Modificar01TPR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPR/testCase/modificarregistro.py").load_module()
TipoRegionalEliminar = SourceFileLoader("Eliminar01TPR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPR/testCase/eliminarregistro.py").load_module()
TipoRegionalConfig = SourceFileLoader("config01TPR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TPR/config.py").load_module()

DiasCreditoPantalla = SourceFileLoader("Pantalla01DCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DCC/testCase/ingresopantalla.py").load_module()
DiasCreditoAgregar = SourceFileLoader("Agregar01DCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DCC/testCase/nuevoregistro.py").load_module()
DiasCreditoRepetir = SourceFileLoader("Repetir01DCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DCC/testCase/repetirregistro.py").load_module()
DiasCreditoModificar = SourceFileLoader("Modificar01DCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DCC/testCase/modificarregistro.py").load_module()
DiasCreditoEliminar = SourceFileLoader("Eliminar01DCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DCC/testCase/eliminarregistro.py").load_module()
DiasCreditoConfig = SourceFileLoader("config01DCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DCC/config.py").load_module()

EntornoPDVPantalla = SourceFileLoader("Pantalla01ETN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ETN/testCase/ingresopantalla.py").load_module()
EntornoPDVAgregar = SourceFileLoader("Agregar01ETN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ETN/testCase/nuevoregistro.py").load_module()
EntornoPDVRepetir = SourceFileLoader("Repetir01ETN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ETN/testCase/repetirregistro.py").load_module()
EntornoPDVModificar = SourceFileLoader("Modificar01ETN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ETN/testCase/modificarregistro.py").load_module()
EntornoPDVEliminar = SourceFileLoader("Eliminar01ETN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ETN/testCase/eliminarregistro.py").load_module()
EntornoPDVConfig = SourceFileLoader("config01ETN", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ETN/config.py").load_module()

EstadoExhibidorPantalla = SourceFileLoader("Pantalla01EE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EE/testCase/ingresopantalla.py").load_module()
EstadoExhibidorAgregar = SourceFileLoader("Agregar01EE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EE/testCase/nuevoregistro.py").load_module()
EstadoExhibidorRepetir = SourceFileLoader("Repetir01EE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EE/testCase/repetirregistro.py").load_module()
EstadoExhibidorModificar = SourceFileLoader("Modificar01EE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EE/testCase/modificarregistro.py").load_module()
EstadoExhibidorEliminar = SourceFileLoader("Eliminar01EE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EE/testCase/eliminarregistro.py").load_module()
EstadoExhibidorConfig = SourceFileLoader("config01EE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EE/config.py").load_module()

TipoEjecucionEEVPantalla = SourceFileLoader("Pantalla01TE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TE/testCase/ingresopantalla.py").load_module()
TipoEjecucionEEVAgregar = SourceFileLoader("Agregar01TE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TE/testCase/nuevoregistro.py").load_module()
TipoEjecucionEEVRepetir = SourceFileLoader("Repetir01TE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TE/testCase/repetirregistro.py").load_module()
TipoEjecucionEEVModificar = SourceFileLoader("Modificar01TE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TE/testCase/modificarregistro.py").load_module()
TipoEjecucionEEVEliminar = SourceFileLoader("Eliminar01TE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TE/testCase/eliminarregistro.py").load_module()
TipoEjecucionEEVConfig = SourceFileLoader("config01TE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TE/config.py").load_module()

RutasPantalla = SourceFileLoader("Pantalla01RU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RU/testCase/ingresopantalla.py").load_module()
RutasAgregar = SourceFileLoader("Agregar01RU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RU/testCase/nuevoregistro.py").load_module()
RutasRepetir = SourceFileLoader("Repetir01RU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RU/testCase/repetirregistro.py").load_module()
RutasModificar = SourceFileLoader("Modificar01RU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RU/testCase/modificarregistro.py").load_module()
RutasEliminar = SourceFileLoader("Eliminar01RU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RU/testCase/eliminarregistro.py").load_module()
RutasConfig = SourceFileLoader("config01RU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01RU/config.py").load_module()

TipoIdentificacionPantalla = SourceFileLoader("Pantalla01TI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TI/testCase/ingresopantalla.py").load_module()
TipoIdentificacionAgregar = SourceFileLoader("Agregar01TI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TI/testCase/nuevoregistro.py").load_module()
TipoIdentificacionRepetir = SourceFileLoader("Repetir01TI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TI/testCase/repetirregistro.py").load_module()
TipoIdentificacionModificar = SourceFileLoader("Modificar01TI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TI/testCase/modificarregistro.py").load_module()
TipoIdentificacionEliminar = SourceFileLoader("Eliminar01TI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TI/testCase/eliminarregistro.py").load_module()
TipoIdentificacionConfig = SourceFileLoader("config01TI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TI/config.py").load_module()

ArqClientePantalla = SourceFileLoader("Pantalla01ARC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ARC/testCase/ingresopantalla.py").load_module()
ArqClienteAgregar = SourceFileLoader("Agregar01ARC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ARC/testCase/nuevoregistro.py").load_module()
ArqClienteRepetir = SourceFileLoader("Repetir01ARC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ARC/testCase/repetirregistro.py").load_module()
ArqClienteModificar = SourceFileLoader("Modificar01ARC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ARC/testCase/modificarregistro.py").load_module()
ArqClienteEliminar = SourceFileLoader("Eliminar01ARC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ARC/testCase/eliminarregistro.py").load_module()
ArqClienteConfig = SourceFileLoader("config01ARC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ARC/config.py").load_module()

CatClientePantalla = SourceFileLoader("Pantalla01CCLI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CCLI/testCase/ingresopantalla.py").load_module()
CatClienteAgregar = SourceFileLoader("Agregar01CCLI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CCLI/testCase/nuevoregistro.py").load_module()
CatClienteRepetir = SourceFileLoader("Repetir01CCLI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CCLI/testCase/repetirregistro.py").load_module()
CatClienteModificar = SourceFileLoader("Modificar01CCLI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CCLI/testCase/modificarregistro.py").load_module()
CatClienteEliminar = SourceFileLoader("Eliminar01CCLI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CCLI/testCase/eliminarregistro.py").load_module()
CatClienteConfig = SourceFileLoader("config01CCLI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CCLI/config.py").load_module()

PerfilCreditoPantalla = SourceFileLoader("Pantalla01PCR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCR/testCase/ingresopantalla.py").load_module()
PerfilCreditoAgregar = SourceFileLoader("Agregar01PCR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCR/testCase/nuevoregistro.py").load_module()
PerfilCreditoRepetir = SourceFileLoader("Repetir01PCR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCR/testCase/repetirregistro.py").load_module()
PerfilCreditoModificar = SourceFileLoader("Modificar01PCR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCR/testCase/modificarregistro.py").load_module()
PerfilCreditoEliminar = SourceFileLoader("Eliminar01PCR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCR/testCase/eliminarregistro.py").load_module()
PerfilCreditoConfig = SourceFileLoader("config01PCR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PCR/config.py").load_module()

ListaPreciosPantalla = SourceFileLoader("Pantalla01LP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LP/testCase/ingresopantalla.py").load_module()
ListaPreciosAgregar = SourceFileLoader("Agregar01LP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LP/testCase/nuevoregistro.py").load_module()
ListaPreciosRepetir = SourceFileLoader("Repetir01LP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LP/testCase/repetirregistro.py").load_module()
ListaPreciosModificar = SourceFileLoader("Modificar01LP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LP/testCase/modificarregistro.py").load_module()
ListaPreciosEliminar = SourceFileLoader("Eliminar01LP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LP/testCase/eliminarregistro.py").load_module()
ListaPreciosConfig = SourceFileLoader("config01LP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01LP/config.py").load_module()

PreciosPantalla = SourceFileLoader("Pantalla01PRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRE/testCase/ingresopantalla.py").load_module()
PreciosAgregar = SourceFileLoader("Agregar01PRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRE/testCase/nuevoregistro.py").load_module()
PreciosRepetir = SourceFileLoader("Repetir01PRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRE/testCase/repetirregistro.py").load_module()
PreciosModificar = SourceFileLoader("Modificar01PRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRE/testCase/modificarregistro.py").load_module()
PreciosEliminar = SourceFileLoader("Eliminar01PRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRE/testCase/eliminarregistro.py").load_module()
PreciosConfig = SourceFileLoader("config01PRE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRE/config.py").load_module()

ImpuestosPantalla = SourceFileLoader("Pantalla01IMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IMP/testCase/ingresopantalla.py").load_module()
ImpuestosAgregar = SourceFileLoader("Agregar01IMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IMP/testCase/nuevoregistro.py").load_module()
ImpuestosRepetir = SourceFileLoader("Repetir01IMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IMP/testCase/repetirregistro.py").load_module()
ImpuestosModificar = SourceFileLoader("Modificar01IMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IMP/testCase/modificarregistro.py").load_module()
ImpuestosEliminar = SourceFileLoader("Eliminar01IMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IMP/testCase/eliminarregistro.py").load_module()
ImpuestosConfig = SourceFileLoader("config01IMP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01IMP/config.py").load_module()

FamiliaImpuestosPantalla = SourceFileLoader("Pantalla01FI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FI/testCase/ingresopantalla.py").load_module()
FamiliaImpuestosAgregar = SourceFileLoader("Agregar01FI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FI/testCase/nuevoregistro.py").load_module()
FamiliaImpuestosRepetir = SourceFileLoader("Repetir01FI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FI/testCase/repetirregistro.py").load_module()
FamiliaImpuestosModificar = SourceFileLoader("Modificar01FI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FI/testCase/modificarregistro.py").load_module()
FamiliaImpuestosEliminar = SourceFileLoader("Eliminar01FI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FI/testCase/eliminarregistro.py").load_module()
FamiliaImpuestosConfig = SourceFileLoader("config01FI", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01FI/config.py").load_module()

TipoDocPantalla = SourceFileLoader("Pantalla01TDOC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDOC/testCase/ingresopantalla.py").load_module()
TipoDocAgregar = SourceFileLoader("Agregar01TDOC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDOC/testCase/nuevoregistro.py").load_module()
TipoDocRepetir = SourceFileLoader("Repetir01TDOC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDOC/testCase/repetirregistro.py").load_module()
TipoDocModificar = SourceFileLoader("Modificar01TDOC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDOC/testCase/modificarregistro.py").load_module()
TipoDocEliminar = SourceFileLoader("Eliminar01TDOC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDOC/testCase/eliminarregistro.py").load_module()
TipoDocConfig = SourceFileLoader("config01TDOC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDOC/config.py").load_module()

GrupoDocPantalla = SourceFileLoader("Pantalla01GD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GD/testCase/ingresopantalla.py").load_module()
GrupoDocAgregar = SourceFileLoader("Agregar01GD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GD/testCase/nuevoregistro.py").load_module()
GrupoDocRepetir = SourceFileLoader("Repetir01GD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GD/testCase/repetirregistro.py").load_module()
GrupoDocModificar = SourceFileLoader("Modificar01GD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GD/testCase/modificarregistro.py").load_module()
GrupoDocEliminar = SourceFileLoader("Eliminar01GD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GD/testCase/eliminarregistro.py").load_module()
GrupoDocConfig = SourceFileLoader("config01GD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GD/config.py").load_module()

TipoChequePantalla = SourceFileLoader("Pantalla01TCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TCH/testCase/ingresopantalla.py").load_module()
TipoChequeAgregar = SourceFileLoader("Agregar01TCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TCH/testCase/nuevoregistro.py").load_module()
TipoChequeRepetir = SourceFileLoader("Repetir01TCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TCH/testCase/repetirregistro.py").load_module()
TipoChequeModificar = SourceFileLoader("Modificar01TCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TCH/testCase/modificarregistro.py").load_module()
TipoChequeEliminar = SourceFileLoader("Eliminar01TCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TCH/testCase/eliminarregistro.py").load_module()
TipoChequeConfig = SourceFileLoader("config01TCH", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TCH/config.py").load_module()

DestinoChequePantalla = SourceFileLoader("Pantalla01DC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DC/testCase/ingresopantalla.py").load_module()
DestinoChequeAgregar = SourceFileLoader("Agregar01DC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DC/testCase/nuevoregistro.py").load_module()
DestinoChequeRepetir = SourceFileLoader("Repetir01DC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DC/testCase/repetirregistro.py").load_module()
DestinoChequeModificar = SourceFileLoader("Modificar01DC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DC/testCase/modificarregistro.py").load_module()
DestinoChequeEliminar = SourceFileLoader("Eliminar01DC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DC/testCase/eliminarregistro.py").load_module()
DestinoChequeConfig = SourceFileLoader("config01DC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DC/config.py").load_module()

ChequerasPantalla = SourceFileLoader("Pantalla01CHE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CHE/testCase/ingresopantalla.py").load_module()
ChequerasAgregar = SourceFileLoader("Agregar01CHE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CHE/testCase/nuevoregistro.py").load_module()
ChequerasRepetir = SourceFileLoader("Repetir01CHE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CHE/testCase/repetirregistro.py").load_module()
ChequerasModificar = SourceFileLoader("Modificar01CHE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CHE/testCase/modificarregistro.py").load_module()
ChequerasEliminar = SourceFileLoader("Eliminar01CHE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CHE/testCase/eliminarregistro.py").load_module()
ChequerasConfig = SourceFileLoader("config01CHE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CHE/config.py").load_module()

MotivosNoEncuestaPantalla = SourceFileLoader("Pantalla01MNE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNE/testCase/ingresopantalla.py").load_module()
MotivosNoEncuestaAgregar = SourceFileLoader("Agregar01MNE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNE/testCase/nuevoregistro.py").load_module()
MotivosNoEncuestaRepetir = SourceFileLoader("Repetir01MNE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNE/testCase/repetirregistro.py").load_module()
MotivosNoEncuestaModificar = SourceFileLoader("Modificar01MNE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNE/testCase/modificarregistro.py").load_module()
MotivosNoEncuestaEliminar = SourceFileLoader("Eliminar01MNE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNE/testCase/eliminarregistro.py").load_module()
MotivosNoEncuestaConfig = SourceFileLoader("config01MNE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MNE/config.py").load_module()

TipoEncuestas1Pantalla = SourceFileLoader("Pantalla01TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDE/testCase/ingresopantalla.py").load_module()
TipoEncuestas1Agregar = SourceFileLoader("Agregar01TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDE/testCase/nuevoregistro.py").load_module()
TipoEncuestas1Repetir = SourceFileLoader("Repetir01TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDE/testCase/repetirregistro.py").load_module()
TipoEncuestas1Modificar = SourceFileLoader("Modificar01TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDE/testCase/modificarregistro.py").load_module()
TipoEncuestas1Eliminar = SourceFileLoader("Eliminar01TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDE/testCase/eliminarregistro.py").load_module()
TipoEncuestas1Config = SourceFileLoader("config01TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01TDE/config.py").load_module()

TipoEncuestas2Pantalla = SourceFileLoader("Pantalla02TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TDE/testCase/ingresopantalla.py").load_module()
TipoEncuestas2Agregar = SourceFileLoader("Agregar02TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TDE/testCase/nuevoregistro.py").load_module()
TipoEncuestas2Repetir = SourceFileLoader("Repetir02TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TDE/testCase/repetirregistro.py").load_module()
TipoEncuestas2Modificar = SourceFileLoader("Modificar02TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TDE/testCase/modificarregistro.py").load_module()
TipoEncuestas2Eliminar = SourceFileLoader("Eliminar02TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TDE/testCase/eliminarregistro.py").load_module()
TipoEncuestas2Config = SourceFileLoader("config02TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/02TDE/config.py").load_module()

TipoEncuestas3Pantalla = SourceFileLoader("Pantalla03TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03TDE/testCase/ingresopantalla.py").load_module()
TipoEncuestas3Agregar = SourceFileLoader("Agregar03TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03TDE/testCase/nuevoregistro.py").load_module()
TipoEncuestas3Repetir = SourceFileLoader("Repetir03TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03TDE/testCase/repetirregistro.py").load_module()
TipoEncuestas3Modificar = SourceFileLoader("Modificar03TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03TDE/testCase/modificarregistro.py").load_module()
TipoEncuestas3Eliminar = SourceFileLoader("Eliminar03TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03TDE/testCase/eliminarregistro.py").load_module()
TipoEncuestas3Config = SourceFileLoader("config03TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/03TDE/config.py").load_module()

TipoEncuestas4Pantalla = SourceFileLoader("Pantalla04TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04TDE/testCase/ingresopantalla.py").load_module()
TipoEncuestas4Agregar = SourceFileLoader("Agregar04TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04TDE/testCase/nuevoregistro.py").load_module()
TipoEncuestas4Repetir = SourceFileLoader("Repetir04TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04TDE/testCase/repetirregistro.py").load_module()
TipoEncuestas4Modificar = SourceFileLoader("Modificar04TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04TDE/testCase/modificarregistro.py").load_module()
TipoEncuestas4Eliminar = SourceFileLoader("Eliminar04TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04TDE/testCase/eliminarregistro.py").load_module()
TipoEncuestas4Config = SourceFileLoader("config04TDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/04TDE/config.py").load_module()

ProveedoresPantalla = SourceFileLoader("Pantalla01PRV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRV/testCase/ingresopantalla.py").load_module()
ProveedoresAgregar = SourceFileLoader("Agregar01PRV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRV/testCase/nuevoregistro.py").load_module()
ProveedoresRepetir = SourceFileLoader("Repetir01PRV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRV/testCase/repetirregistro.py").load_module()
ProveedoresModificar = SourceFileLoader("Modificar01PRV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRV/testCase/modificarregistro.py").load_module()
ProveedoresEliminar = SourceFileLoader("Eliminar01PRV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRV/testCase/eliminarregistro.py").load_module()
ProveedoresConfig = SourceFileLoader("config01PRV", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PRV/config.py").load_module()

MonedasPantalla = SourceFileLoader("Pantalla01MO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MO/testCase/ingresopantalla.py").load_module()
MonedasAgregar = SourceFileLoader("Agregar01MO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MO/testCase/nuevoregistro.py").load_module()
MonedasRepetir = SourceFileLoader("Repetir01MO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MO/testCase/repetirregistro.py").load_module()
MonedasModificar = SourceFileLoader("Modificar01MO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MO/testCase/modificarregistro.py").load_module()
MonedasEliminar = SourceFileLoader("Eliminar01MO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MO/testCase/eliminarregistro.py").load_module()
MonedasConfig = SourceFileLoader("config01MO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MO/config.py").load_module()

PerfilUsuarioPantalla = SourceFileLoader("Pantalla01PDU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDU/testCase/ingresopantalla.py").load_module()
PerfilUsuarioAgregar = SourceFileLoader("Agregar01PDU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDU/testCase/nuevoregistro.py").load_module()
PerfilUsuarioRepetir = SourceFileLoader("Repetir01PDU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDU/testCase/repetirregistro.py").load_module()
PerfilUsuarioModificar = SourceFileLoader("Modificar01PDU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDU/testCase/modificarregistro.py").load_module()
PerfilUsuarioEliminar = SourceFileLoader("Eliminar01PDU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDU/testCase/eliminarregistro.py").load_module()
PerfilUsuarioConfig = SourceFileLoader("config01PDU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDU/config.py").load_module()

ProcedEventoPantalla = SourceFileLoader("Pantalla01PDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDE/testCase/ingresopantalla.py").load_module()
ProcedEventoAgregar = SourceFileLoader("Agregar01PDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDE/testCase/nuevoregistro.py").load_module()
ProcedEventoRepetir = SourceFileLoader("Repetir01PDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDE/testCase/repetirregistro.py").load_module()
ProcedEventoModificar = SourceFileLoader("Modificar01PDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDE/testCase/modificarregistro.py").load_module()
ProcedEventoEliminar = SourceFileLoader("Eliminar01PDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDE/testCase/eliminarregistro.py").load_module()
ProcedEventoConfig = SourceFileLoader("config01PDE", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01PDE/config.py").load_module()

DepositosPantalla = SourceFileLoader("Pantalla01DEP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DEP/testCase/ingresopantalla.py").load_module()
DepositosAgregar = SourceFileLoader("Agregar01DEP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DEP/testCase/nuevoregistro.py").load_module()
DepositosRepetir = SourceFileLoader("Repetir01DEP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DEP/testCase/repetirregistro.py").load_module()
DepositosModificar = SourceFileLoader("Modificar01DEP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DEP/testCase/modificarregistro.py").load_module()
DepositosEliminar = SourceFileLoader("Eliminar01DEP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DEP/testCase/eliminarregistro.py").load_module()
DepositosConfig = SourceFileLoader("config01DEP", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01DEP/config.py").load_module()

UbicacionDepositosPantalla = SourceFileLoader("Pantalla01UD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UD/testCase/ingresopantalla.py").load_module()
UbicacionDepositosAgregar = SourceFileLoader("Agregar01UD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UD/testCase/nuevoregistro.py").load_module()
UbicacionDepositosRepetir = SourceFileLoader("Repetir01UD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UD/testCase/repetirregistro.py").load_module()
UbicacionDepositosModificar = SourceFileLoader("Modificar01UD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UD/testCase/modificarregistro.py").load_module()
UbicacionDepositosEliminar = SourceFileLoader("Eliminar01UD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UD/testCase/eliminarregistro.py").load_module()
UbicacionDepositosConfig = SourceFileLoader("config01UD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01UD/config.py").load_module()

ClasificacionDepositosPantalla = SourceFileLoader("Pantalla01CD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CD/testCase/ingresopantalla.py").load_module()
ClasificacionDepositosAgregar = SourceFileLoader("Agregar01CD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CD/testCase/nuevoregistro.py").load_module()
ClasificacionDepositosRepetir = SourceFileLoader("Repetir01CD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CD/testCase/repetirregistro.py").load_module()
ClasificacionDepositosModificar = SourceFileLoader("Modificar01CD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CD/testCase/modificarregistro.py").load_module()
ClasificacionDepositosEliminar = SourceFileLoader("Eliminar01CD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CD/testCase/eliminarregistro.py").load_module()
ClasificacionDepositosConfig = SourceFileLoader("config01CD", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CD/config.py").load_module()

CentroCostosPantalla = SourceFileLoader("Pantalla01CC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CC/testCase/ingresopantalla.py").load_module()
CentroCostosAgregar = SourceFileLoader("Agregar01CC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CC/testCase/nuevoregistro.py").load_module()
CentroCostosRepetir = SourceFileLoader("Repetir01CC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CC/testCase/repetirregistro.py").load_module()
CentroCostosModificar = SourceFileLoader("Modificar01CC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CC/testCase/modificarregistro.py").load_module()
CentroCostosEliminar = SourceFileLoader("Eliminar01CC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CC/testCase/eliminarregistro.py").load_module()
CentroCostosConfig = SourceFileLoader("config01CC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CC/config.py").load_module()

ClasifAsientosPantalla = SourceFileLoader("Pantalla01CAS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CAS/testCase/ingresopantalla.py").load_module()
ClasifAsientosAgregar = SourceFileLoader("Agregar01CAS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CAS/testCase/nuevoregistro.py").load_module()
ClasifAsientosRepetir = SourceFileLoader("Repetir01CAS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CAS/testCase/repetirregistro.py").load_module()
ClasifAsientosModificar = SourceFileLoader("Modificar01CAS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CAS/testCase/modificarregistro.py").load_module()
ClasifAsientosEliminar = SourceFileLoader("Eliminar01CAS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CAS/testCase/eliminarregistro.py").load_module()
ClasifAsientosConfig = SourceFileLoader("config01CAS", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CAS/config.py").load_module()

CuentasContablesPantalla = SourceFileLoader("Pantalla01CU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CU/testCase/ingresopantalla.py").load_module()
CuentasContablesAgregar = SourceFileLoader("Agregar01CU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CU/testCase/nuevoregistro.py").load_module()
CuentasContablesRepetir = SourceFileLoader("Repetir01CU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CU/testCase/repetirregistro.py").load_module()
CuentasContablesModificar = SourceFileLoader("Modificar01CU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CU/testCase/modificarregistro.py").load_module()
CuentasContablesEliminar = SourceFileLoader("Eliminar01CU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CU/testCase/eliminarregistro.py").load_module()
CuentasContablesConfig = SourceFileLoader("config01CU", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CU/config.py").load_module()

ClasifCuentasContablesPantalla = SourceFileLoader("Pantalla01CUC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CUC/testCase/ingresopantalla.py").load_module()
ClasifCuentasContablesAgregar = SourceFileLoader("Agregar01CUC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CUC/testCase/nuevoregistro.py").load_module()
ClasifCuentasContablesRepetir = SourceFileLoader("Repetir01CUC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CUC/testCase/repetirregistro.py").load_module()
ClasifCuentasContablesModificar = SourceFileLoader("Modificar01CUC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CUC/testCase/modificarregistro.py").load_module()
ClasifCuentasContablesEliminar = SourceFileLoader("Eliminar01CUC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CUC/testCase/eliminarregistro.py").load_module()
ClasifCuentasContablesConfig = SourceFileLoader("config01CUC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CUC/config.py").load_module()

EventosContablesPantalla = SourceFileLoader("Pantalla01EC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EC/testCase/ingresopantalla.py").load_module()
EventosContablesAgregar = SourceFileLoader("Agregar01EC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EC/testCase/nuevoregistro.py").load_module()
EventosContablesRepetir = SourceFileLoader("Repetir01EC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EC/testCase/repetirregistro.py").load_module()
EventosContablesModificar = SourceFileLoader("Modificar01EC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EC/testCase/modificarregistro.py").load_module()
EventosContablesEliminar = SourceFileLoader("Eliminar01EC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EC/testCase/eliminarregistro.py").load_module()
EventosContablesConfig = SourceFileLoader("config01EC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01EC/config.py").load_module()

GrupoCentroCostosPantalla = SourceFileLoader("Pantalla01GCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GCC/testCase/ingresopantalla.py").load_module()
GrupoCentroCostosAgregar = SourceFileLoader("Agregar01GCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GCC/testCase/nuevoregistro.py").load_module()
GrupoCentroCostosRepetir = SourceFileLoader("Repetir01GCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GCC/testCase/repetirregistro.py").load_module()
GrupoCentroCostosModificar = SourceFileLoader("Modificar01GCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GCC/testCase/modificarregistro.py").load_module()
GrupoCentroCostosEliminar = SourceFileLoader("Eliminar01GCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GCC/testCase/eliminarregistro.py").load_module()
GrupoCentroCostosConfig = SourceFileLoader("config01GCC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01GCC/config.py").load_module()

AcuerdosComercialesPantalla = SourceFileLoader("Pantalla01ACC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ACC/testCase/ingresopantalla.py").load_module()
AcuerdosComercialesAgregar = SourceFileLoader("Agregar01ACC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ACC/testCase/nuevoregistro.py").load_module()
AcuerdosComercialesRepetir = SourceFileLoader("Repetir01ACC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ACC/testCase/repetirregistro.py").load_module()
AcuerdosComercialesModificar = SourceFileLoader("Modificar01ACC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ACC/testCase/modificarregistro.py").load_module()
AcuerdosComercialesEliminar = SourceFileLoader("Eliminar01ACC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ACC/testCase/eliminarregistro.py").load_module()
AcuerdosComercialesConfig = SourceFileLoader("config01ACC", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01ACC/config.py").load_module()

CategoriaRiesgoPantalla = SourceFileLoader("Pantalla01CR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CR/testCase/ingresopantalla.py").load_module()
CategoriaRiesgoAgregar = SourceFileLoader("Agregar01CR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CR/testCase/nuevoregistro.py").load_module()
CategoriaRiesgoRepetir = SourceFileLoader("Repetir01CR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CR/testCase/repetirregistro.py").load_module()
CategoriaRiesgoModificar = SourceFileLoader("Modificar01CR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CR/testCase/modificarregistro.py").load_module()
CategoriaRiesgoEliminar = SourceFileLoader("Eliminar01CR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CR/testCase/eliminarregistro.py").load_module()
CategoriaRiesgoConfig = SourceFileLoader("config01CR", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01CR/config.py").load_module()

ModeloCobranzaPantalla = SourceFileLoader("Pantalla01MCO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCO/testCase/ingresopantalla.py").load_module()
ModeloCobranzaAgregar = SourceFileLoader("Agregar01MCO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCO/testCase/nuevoregistro.py").load_module()
ModeloCobranzaRepetir = SourceFileLoader("Repetir01MCO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCO/testCase/repetirregistro.py").load_module()
ModeloCobranzaModificar = SourceFileLoader("Modificar01MCO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCO/testCase/modificarregistro.py").load_module()
ModeloCobranzaEliminar = SourceFileLoader("Eliminar01MCO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCO/testCase/eliminarregistro.py").load_module()
ModeloCobranzaConfig = SourceFileLoader("config01MCO", "C:/xampp/htdocs/versiones/automatizaciones/AutoPWST/01MCO/config.py").load_module()

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
		"""Ingresa a pantalla Articulos"""
		global continua
		if(continua):
			success = ArticulosPantalla.ingresopantalla.ingresopantalla(self, conditions, ArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Articulos"""
		global continua
		if(continua):
			success = ArticulosAgregar.nuevoregistro.nuevoregistro(self, conditions, ArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Articulos"""
		global continua
		if(continua):
			success = ArticulosRepetir.repetirregistro.repetirregistro(self, conditions, ArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Articulos"""
		global continua
		if(continua):
			success = ArticulosModificar.modificarregistro.modificarregistro(self, conditions, ArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Articulos"""
		global continua
		if(continua):
			success = ArticulosEliminar.eliminarregistro.eliminarregistro(self, conditions, ArticulosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_barrios = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_barrios)))
					Cierra_barrios.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_localidades = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_localidades)))
					Cierra_localidades.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_departamentos = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_departamentos)))
					Cierra_departamentos.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Familia Articulos"""
		global continua
		continua = True
		if(continua):
			success = FamiliaArticulosPantalla.ingresopantalla.ingresopantalla(self, conditions, FamiliaArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Familia Articulos"""
		global continua
		if(continua):
			success = FamiliaArticulosAgregar.nuevoregistro.nuevoregistro(self, conditions, FamiliaArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Familia Articulos"""
		global continua
		if(continua):
			success = FamiliaArticulosRepetir.repetirregistro.repetirregistro(self, conditions, FamiliaArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Familia Articulos"""
		global continua
		if(continua):
			success = FamiliaArticulosModificar.modificarregistro.modificarregistro(self, conditions, FamiliaArticulosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Familia Articulos"""
		global continua
		if(continua):
			success = FamiliaArticulosEliminar.eliminarregistro.eliminarregistro(self, conditions, FamiliaArticulosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaArticulosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Unidades"""
		global continua
		continua = True
		if(continua):
			success = UnidadesPantalla.ingresopantalla.ingresopantalla(self, conditions, UnidadesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Unidades"""
		global continua
		if(continua):
			success = UnidadesAgregar.nuevoregistro.nuevoregistro(self, conditions, UnidadesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Unidades"""
		global continua
		if(continua):
			success = UnidadesRepetir.repetirregistro.repetirregistro(self, conditions, UnidadesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Unidades"""
		global continua
		if(continua):
			success = UnidadesModificar.modificarregistro.modificarregistro(self, conditions, UnidadesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Unidades"""
		global continua
		if(continua):
			success = UnidadesEliminar.eliminarregistro.eliminarregistro(self, conditions, UnidadesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_ventana = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_ventana)))
					Cierra_ventana.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UnidadesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Tipos Empaque"""
		global continua
		continua = True
		if(continua):
			success = TiposEmpaquePantalla.ingresopantalla.ingresopantalla(self, conditions, TiposEmpaqueConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Tipos Empaque"""
		global continua
		if(continua):
			success = TiposEmpaqueAgregar.nuevoregistro.nuevoregistro(self, conditions, TiposEmpaqueConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Tipos Empaque"""
		global continua
		if(continua):
			success = TiposEmpaqueRepetir.repetirregistro.repetirregistro(self, conditions, TiposEmpaqueConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Tipos Empaque"""
		global continua
		if(continua):
			success = TiposEmpaqueModificar.modificarregistro.modificarregistro(self, conditions, TiposEmpaqueConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Tipos Empaque"""
		global continua
		if(continua):
			success = TiposEmpaqueEliminar.eliminarregistro.eliminarregistro(self, conditions, TiposEmpaqueConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_ayuda = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_ayuda)))
					Cierra_ayuda.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposEmpaqueConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Familias LP"""
		global continua
		continua = True
		if(continua):
			success = FamiliasLPPantalla.ingresopantalla.ingresopantalla(self, conditions, FamiliasLPConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Familias LP"""
		global continua
		if(continua):
			success = FamiliasLPAgregar.nuevoregistro.nuevoregistro(self, conditions, FamiliasLPConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Familias LP"""
		global continua
		if(continua):
			success = FamiliasLPRepetir.repetirregistro.repetirregistro(self, conditions, FamiliasLPConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Familias LP"""
		global continua
		if(continua):
			success = FamiliasLPModificar.modificarregistro.modificarregistro(self, conditions, FamiliasLPConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Familias LP"""
		global continua
		if(continua):
			success = FamiliasLPEliminar.eliminarregistro.eliminarregistro(self, conditions, FamiliasLPConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")
				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliasLPConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Lineas de Negocio"""
		global continua
		continua = True
		if(continua):
			success = LineasNegocioPantalla.ingresopantalla.ingresopantalla(self, conditions, LineasNegocioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Lineas de Negocio"""
		global continua
		if(continua):
			success = LineasNegocioAgregar.nuevoregistro.nuevoregistro(self, conditions, LineasNegocioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Lineas de Negocio"""
		global continua
		if(continua):
			success = LineasNegocioRepetir.repetirregistro.repetirregistro(self, conditions, LineasNegocioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Lineas de Negocio"""
		global continua
		if(continua):
			success = LineasNegocioModificar.modificarregistro.modificarregistro(self, conditions, LineasNegocioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				try:
					Cierra_menu = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_menu)))
					Cierra_menu.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Lineas de Negocio"""
		global continua
		if(continua):
			success = LineasNegocioEliminar.eliminarregistro.eliminarregistro(self, conditions, LineasNegocioConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, LineasNegocioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Arquitectura de Producto 1"""
		global continua
		continua = True
		if(continua):
			success = ArquitecturaProd1Pantalla.ingresopantalla.ingresopantalla(self, conditions, ArquitecturaProd1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Contactos Arquitectura de Producto 1"""
		global continua
		if(continua):
			success = ArquitecturaProd1Agregar.nuevoregistro.nuevoregistro(self, conditions, ArquitecturaProd1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Arquitectura de Producto 1"""
		global continua
		if(continua):
			success = ArquitecturaProd1Repetir.repetirregistro.repetirregistro(self, conditions, ArquitecturaProd1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Contactos Arquitectura de Producto 1"""
		global continua
		if(continua):
			success = ArquitecturaProd1Modificar.modificarregistro.modificarregistro(self, conditions, ArquitecturaProd1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Arquitectura de Producto 1"""
		global continua
		if(continua):
			success = ArquitecturaProd1Eliminar.eliminarregistro.eliminarregistro(self, conditions, ArquitecturaProd1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Arquitectura de Producto 2"""
		global continua
		continua = True
		if(continua):
			success = ArquitecturaProd2Pantalla.ingresopantalla.ingresopantalla(self, conditions, ArquitecturaProd2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Arquitectura de Producto 2"""
		global continua
		if(continua):
			success = ArquitecturaProd2Agregar.nuevoregistro.nuevoregistro(self, conditions, ArquitecturaProd2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Arquitectura de Producto 2"""
		global continua
		if(continua):
			success = ArquitecturaProd2Repetir.repetirregistro.repetirregistro(self, conditions, ArquitecturaProd2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Programas Arquitectura de Producto 2"""
		global continua
		if(continua):
			success = ArquitecturaProd2Modificar.modificarregistro.modificarregistro(self, conditions, ArquitecturaProd2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Programas Arquitectura de Producto 2"""
		global continua
		if(continua):
			success = ArquitecturaProd2Eliminar.eliminarregistro.eliminarregistro(self, conditions, ArquitecturaProd2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)
				
				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArquitecturaProd2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Marcas Equipo"""
		global continua
		continua = True
		if(continua):
			success = MarcasEquipoPantalla.ingresopantalla.ingresopantalla(self, conditions, MarcasEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Marcas Equipo"""
		global continua
		if(continua):
			success = MarcasEquipoAgregar.nuevoregistro.nuevoregistro(self, conditions, MarcasEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Marcas Equipo"""
		global continua
		if(continua):
			success = MarcasEquipoRepetir.repetirregistro.repetirregistro(self, conditions, MarcasEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Marcas Equipo"""
		global continua
		if(continua):
			success = MarcasEquipoModificar.modificarregistro.modificarregistro(self, conditions, MarcasEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Marcas Equipo"""
		global continua
		if(continua):
			success = MarcasEquipoEliminar.eliminarregistro.eliminarregistro(self, conditions, MarcasEquipoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MarcasEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Clases Equipo"""
		global continua
		continua = True
		if(continua):
			success = ClasesEquipoPantalla.ingresopantalla.ingresopantalla(self, conditions, ClasesEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Clases Equipo"""
		global continua
		if(continua):
			success = ClasesEquipoAgregar.nuevoregistro.nuevoregistro(self, conditions, ClasesEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Clases Equipo"""
		global continua
		if(continua):
			success = ClasesEquipoRepetir.repetirregistro.repetirregistro(self, conditions, ClasesEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Clases Equipo"""
		global continua
		if(continua):
			success = ClasesEquipoModificar.modificarregistro.modificarregistro(self, conditions, ClasesEquipoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Clases Equipo"""
		global continua
		if(continua):
			success = ClasesEquipoEliminar.eliminarregistro.eliminarregistro(self, conditions, ClasesEquipoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasesEquipoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Sabores"""
		global continua
		continua = True
		if(continua):
			success = SaboresPantalla.ingresopantalla.ingresopantalla(self, conditions, SaboresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Sabores"""
		global continua
		if(continua):
			success = SaboresAgregar.nuevoregistro.nuevoregistro(self, conditions, SaboresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Sabores"""
		global continua
		if(continua):
			success = SaboresRepetir.repetirregistro.repetirregistro(self, conditions, SaboresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Sabores"""
		global continua
		if(continua):
			success = SaboresModificar.modificarregistro.modificarregistro(self, conditions, SaboresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Sabores"""
		global continua
		if(continua):
			success = SaboresEliminar.eliminarregistro.eliminarregistro(self, conditions, SaboresConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, SaboresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Tipos Productos"""
		global continua
		continua = True
		if(continua):
			success = TiposProductosPantalla.ingresopantalla.ingresopantalla(self, conditions, TiposProductosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Tipos Productos"""
		global continua
		if(continua):
			success = TiposProductosAgregar.nuevoregistro.nuevoregistro(self, conditions, TiposProductosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Tipos Productos"""
		global continua
		if(continua):
			success = TiposProductosRepetir.repetirregistro.repetirregistro(self, conditions, TiposProductosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Tipos Productos"""
		global continua
		if(continua):
			success = TiposProductosModificar.modificarregistro.modificarregistro(self, conditions, TiposProductosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Tipos Productos"""
		global continua
		if(continua):
			success = TiposProductosEliminar.eliminarregistro.eliminarregistro(self, conditions, TiposProductosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TiposProductosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Clasificacion Articulos 1"""
		global continua
		continua = True
		if(continua):
			success = ClasificArticulo1Pantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Clasificacion Articulos 1"""
		global continua
		if(continua):
			success = ClasificArticulo1Agregar.nuevoregistro.nuevoregistro(self, conditions, ClasificArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Clasificacion Articulos 1"""
		global continua
		if(continua):
			success = ClasificArticulo1Repetir.repetirregistro.repetirregistro(self, conditions, ClasificArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Clasificacion Articulos 1"""
		global continua
		if(continua):
			success = ClasificArticulo1Modificar.modificarregistro.modificarregistro(self, conditions, ClasificArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Clasificacion Articulos 1"""
		global continua
		if(continua):
			success = ClasificArticulo1Eliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificArticulo1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Clasificacion Articulos 2"""
		global continua
		continua = True
		if(continua):
			success = ClasificArticulo2Pantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Clasificacion Articulos 2"""
		global continua
		if(continua):
			success = ClasificArticulo2Agregar.nuevoregistro.nuevoregistro(self, conditions, ClasificArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Clasificacion Articulos 2"""
		global continua
		if(continua):
			success = ClasificArticulo2Repetir.repetirregistro.repetirregistro(self, conditions, ClasificArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Clasificacion Articulos 2"""
		global continua
		if(continua):
			success = ClasificArticulo2Modificar.modificarregistro.modificarregistro(self, conditions, ClasificArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Clasificacion Articulos 2"""
		global continua
		if(continua):
			success = ClasificArticulo2Eliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificArticulo2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Clasificacion Articulos 3"""
		global continua
		continua = True
		if(continua):
			success = ClasificArticulo3Pantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Clasificacion Articulos 3"""
		global continua
		if(continua):
			success = ClasificArticulo3Agregar.nuevoregistro.nuevoregistro(self, conditions, ClasificArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Clasificacion Articulos 3"""
		global continua
		if(continua):
			success = ClasificArticulo3Repetir.repetirregistro.repetirregistro(self, conditions, ClasificArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Clasificacion Articulos 3"""
		global continua
		if(continua):
			success = ClasificArticulo3Modificar.modificarregistro.modificarregistro(self, conditions, ClasificArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Clasificacion Articulos 3"""
		global continua
		if(continua):
			success = ClasificArticulo3Eliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificArticulo3Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Clasificacion Articulos 4"""
		global continua
		continua = True
		if(continua):
			success = ClasificArticulo4Pantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Clasificacion Articulos 4"""
		global continua
		if(continua):
			success = ClasificArticulo4Agregar.nuevoregistro.nuevoregistro(self, conditions, ClasificArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Clasificacion Articulos 4"""
		global continua
		if(continua):
			success = ClasificArticulo4Repetir.repetirregistro.repetirregistro(self, conditions, ClasificArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Clasificacion Articulos 4"""
		global continua
		if(continua):
			success = ClasificArticulo4Modificar.modificarregistro.modificarregistro(self, conditions, ClasificArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Clasificacion Articulos 4"""
		global continua
		if(continua):
			success = ClasificArticulo4Eliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificArticulo4Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 1"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo1Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 1"""
		global continua
		if(continua):
			success = InfoArticulo1Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 1"""
		global continua
		if(continua):
			success = InfoArticulo1Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 1"""
		global continua
		if(continua):
			success = InfoArticulo1Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 1"""
		global continua
		if(continua):
			success = InfoArticulo1Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 2"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo2Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 2"""
		global continua
		if(continua):
			success = InfoArticulo2Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 2"""
		global continua
		if(continua):
			success = InfoArticulo2Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 2"""
		global continua
		if(continua):
			success = InfoArticulo2Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 2"""
		global continua
		if(continua):
			success = InfoArticulo2Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 3"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo3Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 3"""
		global continua
		if(continua):
			success = InfoArticulo3Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 3"""
		global continua
		if(continua):
			success = InfoArticulo3Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 3"""
		global continua
		if(continua):
			success = InfoArticulo3Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 3"""
		global continua
		if(continua):
			success = InfoArticulo3Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo3Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 4"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo4Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 4"""
		global continua
		if(continua):
			success = InfoArticulo4Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 4"""
		global continua
		if(continua):
			success = InfoArticulo4Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 4"""
		global continua
		if(continua):
			success = InfoArticulo4Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 4"""
		global continua
		if(continua):
			success = InfoArticulo4Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo4Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 5"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo5Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo5Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 5"""
		global continua
		if(continua):
			success = InfoArticulo5Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo5Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 5"""
		global continua
		if(continua):
			success = InfoArticulo5Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo5Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 5"""
		global continua
		if(continua):
			success = InfoArticulo5Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo5Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 5"""
		global continua
		if(continua):
			success = InfoArticulo5Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo5Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo5Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 6"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo6Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo6Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 6"""
		global continua
		if(continua):
			success = InfoArticulo6Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo6Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 6"""
		global continua
		if(continua):
			success = InfoArticulo6Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo6Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 6"""
		global continua
		if(continua):
			success = InfoArticulo6Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo6Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 6"""
		global continua
		if(continua):
			success = InfoArticulo6Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo6Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo6Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 7"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo7Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo7Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 7"""
		global continua
		if(continua):
			success = InfoArticulo7Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo7Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 7"""
		global continua
		if(continua):
			success = InfoArticulo7Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo7Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 7"""
		global continua
		if(continua):
			success = InfoArticulo7Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo7Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 7"""
		global continua
		if(continua):
			success = InfoArticulo7Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo7Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo7Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 8"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo8Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo8Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 8"""
		global continua
		if(continua):
			success = InfoArticulo8Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo8Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 8"""
		global continua
		if(continua):
			success = InfoArticulo8Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo8Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 8"""
		global continua
		if(continua):
			success = InfoArticulo8Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo8Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 8"""
		global continua
		if(continua):
			success = InfoArticulo8Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo8Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo8Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 9"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo9Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo9Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 9"""
		global continua
		if(continua):
			success = InfoArticulo9Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo9Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 9"""
		global continua
		if(continua):
			success = InfoArticulo9Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo9Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 9"""
		global continua
		if(continua):
			success = InfoArticulo9Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo9Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 9"""
		global continua
		if(continua):
			success = InfoArticulo9Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo9Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo9Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Informacion de Articulos 10"""
		global continua
		continua = True
		if(continua):
			success = InfoArticulo10Pantalla.ingresopantalla.ingresopantalla(self, conditions, InfoArticulo10Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Informacion de Articulos 10"""
		global continua
		if(continua):
			success = InfoArticulo10Agregar.nuevoregistro.nuevoregistro(self, conditions, InfoArticulo10Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Informacion de Articulos 10"""
		global continua
		if(continua):
			success = InfoArticulo10Repetir.repetirregistro.repetirregistro(self, conditions, InfoArticulo10Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Informacion de Articulos 10"""
		global continua
		if(continua):
			success = InfoArticulo10Modificar.modificarregistro.modificarregistro(self, conditions, InfoArticulo10Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Informacion de Articulos 10"""
		global continua
		if(continua):
			success = InfoArticulo10Eliminar.eliminarregistro.eliminarregistro(self, conditions, InfoArticulo10Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, InfoArticulo10Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Ingresa a pantalla Clientes"""
		global continua
		continua = True
		if(continua):
			success = ClientesPantalla.ingresopantalla.ingresopantalla(self, conditions, ClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Agregar Programas Clientes"""
		global continua
		if(continua):
			success = ClientesAgregar.nuevoregistro.nuevoregistro(self, conditions, ClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Repetir Registro Clientes"""
		global continua
		if(continua):
			success = ClientesRepetir.repetirregistro.repetirregistro(self, conditions, ClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Modifica Clientes"""
		global continua
		if(continua):
			success = ClientesModificar.modificarregistro.modificarregistro(self, conditions, ClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
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
		"""Elimina Clientes"""
		global continua
		if(continua):
			success = ClientesEliminar.eliminarregistro.eliminarregistro(self, conditions, ClientesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_126(self):
		"""Ingresa a pantalla Canales"""
		global continua
		continua = True
		if(continua):
			success = CanalesPantalla.ingresopantalla.ingresopantalla(self, conditions, CanalesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_127(self):
		"""Agregar Programas Canales"""
		global continua
		if(continua):
			success = CanalesAgregar.nuevoregistro.nuevoregistro(self, conditions, CanalesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_128(self):
		"""Repetir Registro Canales"""
		global continua
		if(continua):
			success = CanalesRepetir.repetirregistro.repetirregistro(self, conditions, CanalesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_129(self):
		"""Modifica Canales"""
		global continua
		if(continua):
			success = CanalesModificar.modificarregistro.modificarregistro(self, conditions, CanalesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_130(self):
		"""Elimina Canales"""
		global continua
		if(continua):
			success = CanalesEliminar.eliminarregistro.eliminarregistro(self, conditions, CanalesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CanalesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_131(self):
		"""Ingresa a pantalla Grupos Clientes"""
		global continua
		continua = True
		if(continua):
			success = GruposClientesPantalla.ingresopantalla.ingresopantalla(self, conditions, GruposClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_132(self):
		"""Agregar Programas Grupos Clientes"""
		global continua
		if(continua):
			success = GruposClientesAgregar.nuevoregistro.nuevoregistro(self, conditions, GruposClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_133(self):
		"""Repetir Registro Grupos Clientes"""
		global continua
		if(continua):
			success = GruposClientesRepetir.repetirregistro.repetirregistro(self, conditions, GruposClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_134(self):
		"""Modifica Grupos Clientes"""
		global continua
		if(continua):
			success = GruposClientesModificar.modificarregistro.modificarregistro(self, conditions, GruposClientesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_135(self):
		"""Elimina Grupos Clientes"""
		global continua
		if(continua):
			success = GruposClientesEliminar.eliminarregistro.eliminarregistro(self, conditions, GruposClientesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GruposClientesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_136(self):
		"""Ingresa a pantalla Perfiles de Cuenta"""
		global continua
		continua = True
		if(continua):
			success = PerfilCuentaPantalla.ingresopantalla.ingresopantalla(self, conditions, PerfilCuentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_137(self):
		"""Agregar Programas Perfiles de Cuenta"""
		global continua
		if(continua):
			success = PerfilCuentaAgregar.nuevoregistro.nuevoregistro(self, conditions, PerfilCuentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_138(self):
		"""Repetir Registro Perfiles de Cuenta"""
		global continua
		if(continua):
			success = PerfilCuentaRepetir.repetirregistro.repetirregistro(self, conditions, PerfilCuentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_139(self):
		"""Modifica Perfiles de Cuenta"""
		global continua
		if(continua):
			success = PerfilCuentaModificar.modificarregistro.modificarregistro(self, conditions, PerfilCuentaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_140(self):
		"""Elimina Perfiles de Cuenta"""
		global continua
		if(continua):
			success = PerfilCuentaEliminar.eliminarregistro.eliminarregistro(self, conditions, PerfilCuentaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCuentaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_141(self):
		"""Ingresa a pantalla Categorias Fiscales"""
		global continua
		continua = True
		if(continua):
			success = CategoriaFiscalPantalla.ingresopantalla.ingresopantalla(self, conditions, CategoriaFiscalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_142(self):
		"""Agregar Programas Categorias Fiscales"""
		global continua
		if(continua):
			success = CategoriaFiscalAgregar.nuevoregistro.nuevoregistro(self, conditions, CategoriaFiscalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_143(self):
		"""Repetir Registro Categorias Fiscales"""
		global continua
		if(continua):
			success = CategoriaFiscalRepetir.repetirregistro.repetirregistro(self, conditions, CategoriaFiscalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_144(self):
		"""Modifica Categorias Fiscales"""
		global continua
		if(continua):
			success = CategoriaFiscalModificar.modificarregistro.modificarregistro(self, conditions, CategoriaFiscalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_145(self):
		"""Elimina Categorias Fiscales"""
		global continua
		if(continua):
			success = CategoriaFiscalEliminar.eliminarregistro.eliminarregistro(self, conditions, CategoriaFiscalConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaFiscalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_146(self):
		"""Ingresa a pantalla Tipos de Clientes"""
		global continua
		continua = True
		if(continua):
			success = TipoClientePantalla.ingresopantalla.ingresopantalla(self, conditions, TipoClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_147(self):
		"""Agregar Tipos de Clientes"""
		global continua
		if(continua):
			success = TipoClienteAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_148(self):
		"""Repetir Registro Tipos de Clientes"""
		global continua
		if(continua):
			success = TipoClienteRepetir.repetirregistro.repetirregistro(self, conditions, TipoClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_149(self):
		"""Modifica Tipos de Clientes"""
		global continua
		if(continua):
			success = TipoClienteModificar.modificarregistro.modificarregistro(self, conditions, TipoClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_150(self):
		"""Elimina Tipos de Clientes"""
		global continua
		if(continua):
			success = TipoClienteEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoClienteConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()
	
	def test_151(self):
		"""Ingresa a pantalla Autorizacion de Credito 1"""
		global continua
		continua = True
		if(continua):
			success = AutoCredit1Pantalla.ingresopantalla.ingresopantalla(self, conditions, AutoCredit1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_152(self):
		"""Agregar Autorizacion de Credito 1"""
		global continua
		if(continua):
			success = AutoCredit1Agregar.nuevoregistro.nuevoregistro(self, conditions, AutoCredit1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_153(self):
		"""Repetir Registro Autorizacion de Credito 1"""
		global continua
		if(continua):
			success = AutoCredit1Repetir.repetirregistro.repetirregistro(self, conditions, AutoCredit1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_154(self):
		"""Modifica Autorizacion de Credito 1"""
		global continua
		if(continua):
			success = AutoCredit1Modificar.modificarregistro.modificarregistro(self, conditions, AutoCredit1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_155(self):
		"""Elimina Autorizacion de Credito 1"""
		global continua
		if(continua):
			success = AutoCredit1Eliminar.eliminarregistro.eliminarregistro(self, conditions, AutoCredit1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_156(self):
		"""Ingresa a pantalla Autorizacion de Credito 2"""
		global continua
		continua = True
		if(continua):
			success = AutoCredit2Pantalla.ingresopantalla.ingresopantalla(self, conditions, AutoCredit2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_157(self):
		"""Agregar Autorizacion de Credito 2"""
		global continua
		if(continua):
			success = AutoCredit2Agregar.nuevoregistro.nuevoregistro(self, conditions, AutoCredit2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_158(self):
		"""Repetir Registro Autorizacion de Credito 2"""
		global continua
		if(continua):
			success = AutoCredit2Repetir.repetirregistro.repetirregistro(self, conditions, AutoCredit2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_159(self):
		"""Modifica Autorizacion de Credito 2"""
		global continua
		if(continua):
			success = AutoCredit2Modificar.modificarregistro.modificarregistro(self, conditions, AutoCredit2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_160(self):
		"""Elimina Autorizacion de Credito 2"""
		global continua
		if(continua):
			success = AutoCredit2Eliminar.eliminarregistro.eliminarregistro(self, conditions, AutoCredit2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AutoCredit2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_161(self):
		"""Ingresa a pantalla Tipos de Exclusividad"""
		global continua
		continua = True
		if(continua):
			success = TipoExclusividadPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoExclusividadConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_162(self):
		"""Agregar Tipos de Exclusividad"""
		global continua
		if(continua):
			success = TipoExclusividadAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoExclusividadConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_163(self):
		"""Repetir Registro Tipos de Exclusividad"""
		global continua
		if(continua):
			success = TipoExclusividadRepetir.repetirregistro.repetirregistro(self, conditions, TipoExclusividadConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_164(self):
		"""Modifica Tipos de Exclusividad"""
		global continua
		if(continua):
			success = TipoExclusividadModificar.modificarregistro.modificarregistro(self, conditions, TipoExclusividadConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_165(self):
		"""Elimina Tipos de Exclusividad"""
		global continua
		if(continua):
			success = TipoExclusividadEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoExclusividadConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoExclusividadConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_166(self):
		"""Ingresa a pantalla Distribuidor"""
		global continua
		continua = True
		if(continua):
			success = DistribuidorPantalla.ingresopantalla.ingresopantalla(self, conditions, DistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_167(self):
		"""Agregar Distribuidor"""
		global continua
		if(continua):
			success = DistribuidorAgregar.nuevoregistro.nuevoregistro(self, conditions, DistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_168(self):
		"""Repetir Registro Distribuidor"""
		global continua
		if(continua):
			success = DistribuidorRepetir.repetirregistro.repetirregistro(self, conditions, DistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_169(self):
		"""Modifica Distribuidor"""
		global continua
		if(continua):
			success = DistribuidorModificar.modificarregistro.modificarregistro(self, conditions, DistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_170(self):
		"""Elimina Distribuidor"""
		global continua
		if(continua):
			success = DistribuidorEliminar.eliminarregistro.eliminarregistro(self, conditions, DistribuidorConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_171(self):
		"""Ingresa a pantalla Tipo de Distribuidor"""
		global continua
		continua = True
		if(continua):
			success = TipoDistribuidorPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoDistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_172(self):
		"""Agregar Tipo de Distribuidor"""
		global continua
		if(continua):
			success = TipoDistribuidorAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoDistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_173(self):
		"""Repetir Registro Tipo Distribuidor"""
		global continua
		if(continua):
			success = TipoDistribuidorRepetir.repetirregistro.repetirregistro(self, conditions, TipoDistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_174(self):
		"""Modifica Tipo de Distribuidor"""
		global continua
		if(continua):
			success = TipoDistribuidorModificar.modificarregistro.modificarregistro(self, conditions, TipoDistribuidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_175(self):
		"""Elimina Tipo Distribuidor"""
		global continua
		if(continua):
			success = TipoDistribuidorEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoDistribuidorConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDistribuidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_176(self):
		"""Ingresa a pantalla Tipos de Agencias"""
		global continua
		continua = True
		if(continua):
			success = TipoAgenciaPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoAgenciaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_177(self):
		"""Agregar Tipos de Agencias"""
		global continua
		if(continua):
			success = TipoAgenciaAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoAgenciaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_178(self):
		"""Repetir Registro Tipos de Agencias"""
		global continua
		if(continua):
			success = TipoAgenciaRepetir.repetirregistro.repetirregistro(self, conditions, TipoAgenciaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_179(self):
		"""Modifica Tipos de Agencias"""
		global continua
		if(continua):
			success = TipoAgenciaModificar.modificarregistro.modificarregistro(self, conditions, TipoAgenciaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_180(self):
		"""Elimina Tipos de Agencias"""
		global continua
		if(continua):
			success = TipoAgenciaEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoAgenciaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoAgenciaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_181(self):
		"""Ingresa a pantalla Tipos de Oficina"""
		global continua
		continua = True
		if(continua):
			success = TipoOficinaPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoOficinaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_182(self):
		"""Agregar Tipos de Oficina"""
		global continua
		if(continua):
			success = TipoOficinaAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoOficinaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_183(self):
		"""Repetir Registro Tipos de Oficina"""
		global continua
		if(continua):
			success = TipoOficinaRepetir.repetirregistro.repetirregistro(self, conditions, TipoOficinaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_184(self):
		"""Modifica Tipos de Oficina"""
		global continua
		if(continua):
			success = TipoOficinaModificar.modificarregistro.modificarregistro(self, conditions, TipoOficinaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_185(self):
		"""Elimina Tipos de Oficina"""
		global continua
		if(continua):
			success = TipoOficinaEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoOficinaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoOficinaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_186(self):
		"""Ingresa a pantalla Matrices"""
		global continua
		continua = True
		if(continua):
			success = MatricesPantalla.ingresopantalla.ingresopantalla(self, conditions, MatricesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_187(self):
		"""Agregar Matrices"""
		global continua
		if(continua):
			success = MatricesAgregar.nuevoregistro.nuevoregistro(self, conditions, MatricesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_188(self):
		"""Repetir Registro Matrices"""
		global continua
		if(continua):
			success = MatricesRepetir.repetirregistro.repetirregistro(self, conditions, MatricesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_189(self):
		"""Modifica Matrices"""
		global continua
		if(continua):
			success = MatricesModificar.modificarregistro.modificarregistro(self, conditions, MatricesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_190(self):
		"""Elimina Matrices"""
		global continua
		if(continua):
			success = MatricesEliminar.eliminarregistro.eliminarregistro(self, conditions, MatricesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MatricesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_191(self):
		"""Ingresa a pantalla Tipos de Compañia"""
		global continua
		continua = True
		if(continua):
			success = TipoCompañiaPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoCompañiaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_192(self):
		"""Agregar Tipos de Compañia"""
		global continua
		if(continua):
			success = TipoCompañiaAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoCompañiaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_193(self):
		"""Repetir Registro Tipos de Compañia"""
		global continua
		if(continua):
			success = TipoCompañiaRepetir.repetirregistro.repetirregistro(self, conditions, TipoCompañiaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_194(self):
		"""Modifica Tipos de Compañia"""
		global continua
		if(continua):
			success = TipoCompañiaModificar.modificarregistro.modificarregistro(self, conditions, TipoCompañiaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_195(self):
		"""Elimina Tipos de Compañia"""
		global continua
		if(continua):
			success = TipoCompañiaEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoCompañiaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoCompañiaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_196(self):
		"""Ingresa a pantalla Tipos de Regional"""
		global continua
		continua = True
		if(continua):
			success = TipoRegionalPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoRegionalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_197(self):
		"""Agregar Tipos de Regional"""
		global continua
		if(continua):
			success = TipoRegionalAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoRegionalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_198(self):
		"""Repetir Registro Tipos de Regional"""
		global continua
		if(continua):
			success = TipoRegionalRepetir.repetirregistro.repetirregistro(self, conditions, TipoRegionalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_199(self):
		"""Modifica Tipos de Regional"""
		global continua
		if(continua):
			success = TipoRegionalModificar.modificarregistro.modificarregistro(self, conditions, TipoRegionalConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_200(self):
		"""Elimina Tipos de Regional"""
		global continua
		if(continua):
			success = TipoRegionalEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoRegionalConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoRegionalConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_201(self):
		"""Ingresa a pantalla Dias Credito Competencia"""
		global continua
		continua = True
		if(continua):
			success = DiasCreditoPantalla.ingresopantalla.ingresopantalla(self, conditions, DiasCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_202(self):
		"""Agregar Dias Credito Competencia"""
		global continua
		if(continua):
			success = DiasCreditoAgregar.nuevoregistro.nuevoregistro(self, conditions, DiasCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_203(self):
		"""Repetir Registro Dias Credito Competencia"""
		global continua
		if(continua):
			success = DiasCreditoRepetir.repetirregistro.repetirregistro(self, conditions, DiasCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_204(self):
		"""Modifica Dias Credito Competencia"""
		global continua
		if(continua):
			success = DiasCreditoModificar.modificarregistro.modificarregistro(self, conditions, DiasCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_205(self):
		"""Elimina Dias Credito Competencia"""
		global continua
		if(continua):
			success = DiasCreditoEliminar.eliminarregistro.eliminarregistro(self, conditions, DiasCreditoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DiasCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_206(self):
		"""Ingresa a pantalla Entorno PDV"""
		global continua
		continua = True
		if(continua):
			success = EntornoPDVPantalla.ingresopantalla.ingresopantalla(self, conditions, EntornoPDVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_207(self):
		"""Agregar Entorno PDV"""
		global continua
		if(continua):
			success = EntornoPDVAgregar.nuevoregistro.nuevoregistro(self, conditions, EntornoPDVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_208(self):
		"""Repetir Registro Entorno PDV"""
		global continua
		if(continua):
			success = EntornoPDVRepetir.repetirregistro.repetirregistro(self, conditions, EntornoPDVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_209(self):
		"""Modifica Entorno PDV"""
		global continua
		if(continua):
			success = EntornoPDVModificar.modificarregistro.modificarregistro(self, conditions, EntornoPDVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_210(self):
		"""Elimina Entorno PDV"""
		global continua
		if(continua):
			success = EntornoPDVEliminar.eliminarregistro.eliminarregistro(self, conditions, EntornoPDVConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EntornoPDVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_211(self):
		"""Ingresa a pantalla Estado Exhibidor"""
		global continua
		continua = True
		if(continua):
			success = EstadoExhibidorPantalla.ingresopantalla.ingresopantalla(self, conditions, EstadoExhibidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_212(self):
		"""Agregar Estado Exhibidor"""
		global continua
		if(continua):
			success = EstadoExhibidorAgregar.nuevoregistro.nuevoregistro(self, conditions, EstadoExhibidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_213(self):
		"""Repetir Registro Estado Exhibidor"""
		global continua
		if(continua):
			success = EstadoExhibidorRepetir.repetirregistro.repetirregistro(self, conditions, EstadoExhibidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_214(self):
		"""Modifica Estado Exhibidor"""
		global continua
		if(continua):
			success = EstadoExhibidorModificar.modificarregistro.modificarregistro(self, conditions, EstadoExhibidorConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_215(self):
		"""Elimina Estado Exhibidor"""
		global continua
		if(continua):
			success = EstadoExhibidorEliminar.eliminarregistro.eliminarregistro(self, conditions, EstadoExhibidorConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EstadoExhibidorConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_216(self):
		"""Ingresa a pantalla Tipo Ejecucion EEV"""
		global continua
		continua = True
		if(continua):
			success = TipoEjecucionEEVPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoEjecucionEEVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_217(self):
		"""Agregar Tipo Ejecucion EEV"""
		global continua
		if(continua):
			success = TipoEjecucionEEVAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoEjecucionEEVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_218(self):
		"""Repetir Registro Tipo Ejecucion EEV"""
		global continua
		if(continua):
			success = TipoEjecucionEEVRepetir.repetirregistro.repetirregistro(self, conditions, TipoEjecucionEEVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_219(self):
		"""Modifica Tipo Ejecucion EEV"""
		global continua
		if(continua):
			success = TipoEjecucionEEVModificar.modificarregistro.modificarregistro(self, conditions, TipoEjecucionEEVConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_220(self):
		"""Elimina Tipo Ejecucion EEV"""
		global continua
		if(continua):
			success = TipoEjecucionEEVEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoEjecucionEEVConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEjecucionEEVConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_221(self):
		"""Ingresa a pantalla Rutas"""
		global continua
		continua = True
		if(continua):
			success = RutasPantalla.ingresopantalla.ingresopantalla(self, conditions, RutasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_222(self):
		"""Agregar Rutas"""
		global continua
		if(continua):
			success = RutasAgregar.nuevoregistro.nuevoregistro(self, conditions, RutasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_223(self):
		"""Repetir Registro Rutas"""
		global continua
		if(continua):
			success = RutasRepetir.repetirregistro.repetirregistro(self, conditions, RutasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_224(self):
		"""Modifica Rutas"""
		global continua
		if(continua):
			success = RutasModificar.modificarregistro.modificarregistro(self, conditions, RutasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_225(self):
		"""Elimina Rutas"""
		global continua
		if(continua):
			success = RutasEliminar.eliminarregistro.eliminarregistro(self, conditions, RutasConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, RutasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_226(self):
		"""Ingresa a pantalla Tipos de Identificacion"""
		global continua
		continua = True
		if(continua):
			success = TipoIdentificacionPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoIdentificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_227(self):
		"""Agregar Tipos de Identificacion"""
		global continua
		if(continua):
			success = TipoIdentificacionAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoIdentificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_228(self):
		"""Repetir Registro Tipos de Identificacion"""
		global continua
		if(continua):
			success = TipoIdentificacionRepetir.repetirregistro.repetirregistro(self, conditions, TipoIdentificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_229(self):
		"""Modifica Tipos de Identificacion"""
		global continua
		if(continua):
			success = TipoIdentificacionModificar.modificarregistro.modificarregistro(self, conditions, TipoIdentificacionConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_230(self):
		"""Elimina Tipos de Identificacion"""
		global continua
		if(continua):
			success = TipoIdentificacionEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoIdentificacionConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoIdentificacionConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_231(self):
		"""Ingresa a pantalla Arquitectura de Cliente"""
		global continua
		continua = True
		if(continua):
			success = ArqClientePantalla.ingresopantalla.ingresopantalla(self, conditions, ArqClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_232(self):
		"""Agregar Arquitectura de Cliente"""
		global continua
		if(continua):
			success = ArqClienteAgregar.nuevoregistro.nuevoregistro(self, conditions, ArqClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_233(self):
		"""Repetir Registro Arquitectura de Cliente"""
		global continua
		if(continua):
			success = ArqClienteRepetir.repetirregistro.repetirregistro(self, conditions, ArqClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_234(self):
		"""Modifica Arquitectura de Cliente"""
		global continua
		if(continua):
			success = ArqClienteModificar.modificarregistro.modificarregistro(self, conditions, ArqClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_235(self):
		"""Elimina Arquitectura de Cliente"""
		global continua
		if(continua):
			success = ArqClienteEliminar.eliminarregistro.eliminarregistro(self, conditions, ArqClienteConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ArqClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_236(self):
		"""Ingresa a pantalla Categoria de Cliente"""
		global continua
		continua = True
		if(continua):
			success = CatClientePantalla.ingresopantalla.ingresopantalla(self, conditions, CatClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_237(self):
		"""Agregar Categoria de Cliente"""
		global continua
		if(continua):
			success = CatClienteAgregar.nuevoregistro.nuevoregistro(self, conditions, CatClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_238(self):
		"""Repetir Registro Categoria de Cliente"""
		global continua
		if(continua):
			success = CatClienteRepetir.repetirregistro.repetirregistro(self, conditions, CatClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_239(self):
		"""Modifica Categoria de Cliente"""
		global continua
		if(continua):
			success = CatClienteModificar.modificarregistro.modificarregistro(self, conditions, CatClienteConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_240(self):
		"""Elimina Categoria de Cliente"""
		global continua
		if(continua):
			success = CatClienteEliminar.eliminarregistro.eliminarregistro(self, conditions, CatClienteConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CatClienteConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_241(self):
		"""Ingresa a pantalla Perfiles de Credito"""
		global continua
		continua = True
		if(continua):
			success = PerfilCreditoPantalla.ingresopantalla.ingresopantalla(self, conditions, PerfilCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_242(self):
		"""Agregar Perfiles de Credito"""
		global continua
		if(continua):
			success = PerfilCreditoAgregar.nuevoregistro.nuevoregistro(self, conditions, PerfilCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_243(self):
		"""Repetir Registro Perfiles de Credito"""
		global continua
		if(continua):
			success = PerfilCreditoRepetir.repetirregistro.repetirregistro(self, conditions, PerfilCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_244(self):
		"""Modifica Perfiles de Credito"""
		global continua
		if(continua):
			success = PerfilCreditoModificar.modificarregistro.modificarregistro(self, conditions, PerfilCreditoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_245(self):
		"""Elimina Perfiles de Credito"""
		global continua
		if(continua):
			success = PerfilCreditoEliminar.eliminarregistro.eliminarregistro(self, conditions, PerfilCreditoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilCreditoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_246(self):
		"""Ingresa a pantalla Lista de Precios"""
		global continua
		continua = True
		if(continua):
			success = ListaPreciosPantalla.ingresopantalla.ingresopantalla(self, conditions, ListaPreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_247(self):
		"""Agregar Lista de Precios"""
		global continua
		if(continua):
			success = ListaPreciosAgregar.nuevoregistro.nuevoregistro(self, conditions, ListaPreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_248(self):
		"""Repetir Registro Lista de Precios"""
		global continua
		if(continua):
			success = ListaPreciosRepetir.repetirregistro.repetirregistro(self, conditions, ListaPreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_249(self):
		"""Modifica Lista de Precios"""
		global continua
		if(continua):
			success = ListaPreciosModificar.modificarregistro.modificarregistro(self, conditions, ListaPreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_250(self):
		"""Elimina Lista de Precios"""
		global continua
		if(continua):
			success = ListaPreciosEliminar.eliminarregistro.eliminarregistro(self, conditions, ListaPreciosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ListaPreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_251(self):
		"""Ingresa a pantalla Precios"""
		global continua
		continua = True
		if(continua):
			success = PreciosPantalla.ingresopantalla.ingresopantalla(self, conditions, PreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_252(self):
		"""Agregar Precios"""
		global continua
		if(continua):
			success = PreciosAgregar.nuevoregistro.nuevoregistro(self, conditions, PreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_253(self):
		"""Repetir Registro Precios"""
		global continua
		if(continua):
			success = PreciosRepetir.repetirregistro.repetirregistro(self, conditions, PreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_254(self):
		"""Modifica Precios"""
		global continua
		if(continua):
			success = PreciosModificar.modificarregistro.modificarregistro(self, conditions, PreciosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_255(self):
		"""Elimina Precios"""
		global continua
		if(continua):
			success = PreciosEliminar.eliminarregistro.eliminarregistro(self, conditions, PreciosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PreciosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_256(self):
		"""Ingresa a pantalla Impuestos"""
		global continua
		continua = True
		if(continua):
			success = ImpuestosPantalla.ingresopantalla.ingresopantalla(self, conditions, ImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_257(self):
		"""Agregar Impuestos"""
		global continua
		if(continua):
			success = ImpuestosAgregar.nuevoregistro.nuevoregistro(self, conditions, ImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_258(self):
		"""Repetir Registro Impuestos"""
		global continua
		if(continua):
			success = ImpuestosRepetir.repetirregistro.repetirregistro(self, conditions, ImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_259(self):
		"""Modifica Impuestos"""
		global continua
		if(continua):
			success = ImpuestosModificar.modificarregistro.modificarregistro(self, conditions, ImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_260(self):
		"""Elimina Impuestos"""
		global continua
		if(continua):
			success = ImpuestosEliminar.eliminarregistro.eliminarregistro(self, conditions, ImpuestosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_261(self):
		"""Ingresa a pantalla Familia Impuestos"""
		global continua
		continua = True
		if(continua):
			success = FamiliaImpuestosPantalla.ingresopantalla.ingresopantalla(self, conditions, FamiliaImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_262(self):
		"""Agregar Familia Impuestos"""
		global continua
		if(continua):
			success = FamiliaImpuestosAgregar.nuevoregistro.nuevoregistro(self, conditions, FamiliaImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_263(self):
		"""Repetir Registro Familia Impuestos"""
		global continua
		if(continua):
			success = FamiliaImpuestosRepetir.repetirregistro.repetirregistro(self, conditions, FamiliaImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_264(self):
		"""Modifica Familia Impuestos"""
		global continua
		if(continua):
			success = FamiliaImpuestosModificar.modificarregistro.modificarregistro(self, conditions, FamiliaImpuestosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_265(self):
		"""Elimina Familia Impuestos"""
		global continua
		if(continua):
			success = FamiliaImpuestosEliminar.eliminarregistro.eliminarregistro(self, conditions, FamiliaImpuestosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, FamiliaImpuestosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_266(self):
		"""Ingresa a pantalla Tipo de Documento"""
		global continua
		continua = True
		if(continua):
			success = TipoDocPantalla.ingresopantalla.ingresopantalla(self, conditions, TipoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_267(self):
		"""Agregar Tipo de Documento"""
		global continua
		if(continua):
			success = TipoDocAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_268(self):
		"""Repetir Registro Tipo de Documento"""
		global continua
		if(continua):
			success = TipoDocRepetir.repetirregistro.repetirregistro(self, conditions, TipoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_269(self):
		"""Modifica Tipo de Documento"""
		global continua
		if(continua):
			success = TipoDocModificar.modificarregistro.modificarregistro(self, conditions, TipoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_270(self):
		"""Elimina Tipo de Documento"""
		global continua
		if(continua):
			success = TipoDocEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoDocConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_271(self):
		"""Ingresa a pantalla Grupo Documento"""
		global continua
		continua = True
		if(continua):
			success = GrupoDocPantalla.ingresopantalla.ingresopantalla(self, conditions, GrupoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_272(self):
		"""Agregar Grupo Documento"""
		global continua
		if(continua):
			success = GrupoDocAgregar.nuevoregistro.nuevoregistro(self, conditions, GrupoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_273(self):
		"""Repetir Registro Grupo Documento"""
		global continua
		if(continua):
			success = GrupoDocRepetir.repetirregistro.repetirregistro(self, conditions, GrupoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_274(self):
		"""Modifica Grupo Documento"""
		global continua
		if(continua):
			success = GrupoDocModificar.modificarregistro.modificarregistro(self, conditions, GrupoDocConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_275(self):
		"""Elimina Grupo Documento"""
		global continua
		if(continua):
			success = GrupoDocEliminar.eliminarregistro.eliminarregistro(self, conditions, GrupoDocConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoDocConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_276(self):
		"""Ingresa a pantalla Tipo Cheque"""
		global continua
		continua = True
		if(continua):
			success = TipoChequePantalla.ingresopantalla.ingresopantalla(self, conditions, TipoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_277(self):
		"""Agregar Tipo Cheque"""
		global continua
		if(continua):
			success = TipoChequeAgregar.nuevoregistro.nuevoregistro(self, conditions, TipoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_278(self):
		"""Repetir Registro Tipo Cheque"""
		global continua
		if(continua):
			success = TipoChequeRepetir.repetirregistro.repetirregistro(self, conditions, TipoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_279(self):
		"""Modifica Tipo Cheque"""
		global continua
		if(continua):
			success = TipoChequeModificar.modificarregistro.modificarregistro(self, conditions, TipoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_280(self):
		"""Elimina Tipo Cheque"""
		global continua
		if(continua):
			success = TipoChequeEliminar.eliminarregistro.eliminarregistro(self, conditions, TipoChequeConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_281(self):
		"""Ingresa a pantalla Destino Cheque"""
		global continua
		continua = True
		if(continua):
			success = DestinoChequePantalla.ingresopantalla.ingresopantalla(self, conditions, DestinoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_282(self):
		"""Agregar Destino Cheque"""
		global continua
		if(continua):
			success = DestinoChequeAgregar.nuevoregistro.nuevoregistro(self, conditions, DestinoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_283(self):
		"""Repetir Registro Destino Cheque"""
		global continua
		if(continua):
			success = DestinoChequeRepetir.repetirregistro.repetirregistro(self, conditions, DestinoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_284(self):
		"""Modifica Destino Cheque"""
		global continua
		if(continua):
			success = DestinoChequeModificar.modificarregistro.modificarregistro(self, conditions, DestinoChequeConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_285(self):
		"""Elimina Destino Cheque"""
		global continua
		if(continua):
			success = DestinoChequeEliminar.eliminarregistro.eliminarregistro(self, conditions, DestinoChequeConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DestinoChequeConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_286(self):
		"""Ingresa a pantalla Chequeras"""
		global continua
		continua = True
		if(continua):
			success = ChequerasPantalla.ingresopantalla.ingresopantalla(self, conditions, ChequerasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_287(self):
		"""Agregar Chequeras"""
		global continua
		if(continua):
			success = ChequerasAgregar.nuevoregistro.nuevoregistro(self, conditions, ChequerasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_288(self):
		"""Repetir Registro Chequeras"""
		global continua
		if(continua):
			success = ChequerasRepetir.repetirregistro.repetirregistro(self, conditions, ChequerasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_289(self):
		"""Modifica Chequeras"""
		global continua
		if(continua):
			success = ChequerasModificar.modificarregistro.modificarregistro(self, conditions, ChequerasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_290(self):
		"""Elimina Chequeras"""
		global continua
		if(continua):
			success = ChequerasEliminar.eliminarregistro.eliminarregistro(self, conditions, ChequerasConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ChequerasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_286(self):
		"""Ingresa a pantalla Motivos No Encuentas"""
		global continua
		continua = True
		if(continua):
			success = MotivosNoEncuestaPantalla.ingresopantalla.ingresopantalla(self, conditions, MotivosNoEncuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_287(self):
		"""Agregar Motivos No Encuentas"""
		global continua
		if(continua):
			success = MotivosNoEncuestaAgregar.nuevoregistro.nuevoregistro(self, conditions, MotivosNoEncuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_288(self):
		"""Repetir Registro Motivos No Encuentas"""
		global continua
		if(continua):
			success = MotivosNoEncuestaRepetir.repetirregistro.repetirregistro(self, conditions, MotivosNoEncuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_289(self):
		"""Modifica Motivos No Encuentas"""
		global continua
		if(continua):
			success = MotivosNoEncuestaModificar.modificarregistro.modificarregistro(self, conditions, MotivosNoEncuestaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_290(self):
		"""Elimina Motivos No Encuentas"""
		global continua
		if(continua):
			success = MotivosNoEncuestaEliminar.eliminarregistro.eliminarregistro(self, conditions, MotivosNoEncuestaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MotivosNoEncuestaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_291(self):
		"""Ingresa a pantalla Tipos de Encuestas 1"""
		global continua
		continua = True
		if(continua):
			success = TipoEncuestas1Pantalla.ingresopantalla.ingresopantalla(self, conditions, TipoEncuestas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_292(self):
		"""Agregar Tipos de Encuestas 1"""
		global continua
		if(continua):
			success = TipoEncuestas1Agregar.nuevoregistro.nuevoregistro(self, conditions, TipoEncuestas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_293(self):
		"""Repetir Registro Tipos de Encuestas 1"""
		global continua
		if(continua):
			success = TipoEncuestas1Repetir.repetirregistro.repetirregistro(self, conditions, TipoEncuestas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_294(self):
		"""Modifica Tipos de Encuestas 1"""
		global continua
		if(continua):
			success = TipoEncuestas1Modificar.modificarregistro.modificarregistro(self, conditions, TipoEncuestas1Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_295(self):
		"""Elimina Tipos de Encuestas 1"""
		global continua
		if(continua):
			success = TipoEncuestas1Eliminar.eliminarregistro.eliminarregistro(self, conditions, TipoEncuestas1Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas1Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_296(self):
		"""Ingresa a pantalla Tipos de Encuestas 2"""
		global continua
		continua = True
		if(continua):
			success = TipoEncuestas2Pantalla.ingresopantalla.ingresopantalla(self, conditions, TipoEncuestas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_297(self):
		"""Agregar Tipos de Encuestas 2"""
		global continua
		if(continua):
			success = TipoEncuestas2Agregar.nuevoregistro.nuevoregistro(self, conditions, TipoEncuestas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_298(self):
		"""Repetir Registro Tipos de Encuestas 2"""
		global continua
		if(continua):
			success = TipoEncuestas2Repetir.repetirregistro.repetirregistro(self, conditions, TipoEncuestas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_299(self):
		"""Modifica Tipos de Encuestas 2"""
		global continua
		if(continua):
			success = TipoEncuestas2Modificar.modificarregistro.modificarregistro(self, conditions, TipoEncuestas2Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_300(self):
		"""Elimina Tipos de Encuestas 2"""
		global continua
		if(continua):
			success = TipoEncuestas2Eliminar.eliminarregistro.eliminarregistro(self, conditions, TipoEncuestas2Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas2Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()
	
	def test_301(self):
		"""Ingresa a pantalla Tipos de Encuestas 3"""
		global continua
		continua = True
		if(continua):
			success = TipoEncuestas3Pantalla.ingresopantalla.ingresopantalla(self, conditions, TipoEncuestas3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_302(self):
		"""Agregar Tipos de Encuestas 3"""
		global continua
		if(continua):
			success = TipoEncuestas3Agregar.nuevoregistro.nuevoregistro(self, conditions, TipoEncuestas3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_303(self):
		"""Repetir Registro Tipos de Encuestas 3"""
		global continua
		if(continua):
			success = TipoEncuestas3Repetir.repetirregistro.repetirregistro(self, conditions, TipoEncuestas3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_304(self):
		"""Modifica Tipos de Encuestas 3"""
		global continua
		if(continua):
			success = TipoEncuestas3Modificar.modificarregistro.modificarregistro(self, conditions, TipoEncuestas3Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_305(self):
		"""Elimina Tipos de Encuestas 3"""
		global continua
		if(continua):
			success = TipoEncuestas3Eliminar.eliminarregistro.eliminarregistro(self, conditions, TipoEncuestas3Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas3Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_306(self):
		"""Ingresa a pantalla Tipos de Encuestas 4"""
		global continua
		continua = True
		if(continua):
			success = TipoEncuestas4Pantalla.ingresopantalla.ingresopantalla(self, conditions, TipoEncuestas4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_307(self):
		"""Agregar Tipos de Encuestas 4"""
		global continua
		if(continua):
			success = TipoEncuestas4Agregar.nuevoregistro.nuevoregistro(self, conditions, TipoEncuestas4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_308(self):
		"""Repetir Registro Tipos de Encuestas 4"""
		global continua
		if(continua):
			success = TipoEncuestas4Repetir.repetirregistro.repetirregistro(self, conditions, TipoEncuestas4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_309(self):
		"""Modifica Tipos de Encuestas 4"""
		global continua
		if(continua):
			success = TipoEncuestas4Modificar.modificarregistro.modificarregistro(self, conditions, TipoEncuestas4Config.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_310(self):
		"""Elimina Tipos de Encuestas 4"""
		global continua
		if(continua):
			success = TipoEncuestas4Eliminar.eliminarregistro.eliminarregistro(self, conditions, TipoEncuestas4Config.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, TipoEncuestas4Config.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_311(self):
		"""Ingresa a pantalla Proveedores"""
		global continua
		continua = True
		if(continua):
			success = ProveedoresPantalla.ingresopantalla.ingresopantalla(self, conditions, ProveedoresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_312(self):
		"""Agregar Proveedores"""
		global continua
		if(continua):
			success = ProveedoresAgregar.nuevoregistro.nuevoregistro(self, conditions, ProveedoresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_313(self):
		"""Repetir Registro Proveedores"""
		global continua
		if(continua):
			success = ProveedoresRepetir.repetirregistro.repetirregistro(self, conditions, ProveedoresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_314(self):
		"""Modifica Proveedores"""
		global continua
		if(continua):
			success = ProveedoresModificar.modificarregistro.modificarregistro(self, conditions, ProveedoresConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_315(self):
		"""Elimina Proveedores"""
		global continua
		if(continua):
			success = ProveedoresEliminar.eliminarregistro.eliminarregistro(self, conditions, ProveedoresConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProveedoresConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_316(self):
		"""Ingresa a pantalla Monedas"""
		global continua
		continua = True
		if(continua):
			success = MonedasPantalla.ingresopantalla.ingresopantalla(self, conditions, MonedasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_317(self):
		"""Agregar Monedas"""
		global continua
		if(continua):
			success = MonedasAgregar.nuevoregistro.nuevoregistro(self, conditions, MonedasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_318(self):
		"""Repetir Registro Monedas"""
		global continua
		if(continua):
			success = MonedasRepetir.repetirregistro.repetirregistro(self, conditions, MonedasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_319(self):
		"""Modifica Monedas"""
		global continua
		if(continua):
			success = MonedasModificar.modificarregistro.modificarregistro(self, conditions, MonedasConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_320(self):
		"""Elimina Monedas"""
		global continua
		if(continua):
			success = MonedasEliminar.eliminarregistro.eliminarregistro(self, conditions, MonedasConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, MonedasConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_321(self):
		"""Ingresa a pantalla Perfiles de Usuario"""
		global continua
		continua = True
		if(continua):
			success = PerfilUsuarioPantalla.ingresopantalla.ingresopantalla(self, conditions, PerfilUsuarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_322(self):
		"""Agregar Perfiles de Usuario"""
		global continua
		if(continua):
			success = PerfilUsuarioAgregar.nuevoregistro.nuevoregistro(self, conditions, PerfilUsuarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_323(self):
		"""Repetir Registro Perfiles de Usuario"""
		global continua
		if(continua):
			success = PerfilUsuarioRepetir.repetirregistro.repetirregistro(self, conditions, PerfilUsuarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_324(self):
		"""Modifica Perfiles de Usuario"""
		global continua
		if(continua):
			success = PerfilUsuarioModificar.modificarregistro.modificarregistro(self, conditions, PerfilUsuarioConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_325(self):
		"""Elimina Perfiles de Usuario"""
		global continua
		if(continua):
			success = PerfilUsuarioEliminar.eliminarregistro.eliminarregistro(self, conditions, PerfilUsuarioConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, PerfilUsuarioConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_326(self):
		"""Ingresa a pantalla Procedimientos de Evento"""
		global continua
		continua = True
		if(continua):
			success = ProcedEventoPantalla.ingresopantalla.ingresopantalla(self, conditions, ProcedEventoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_327(self):
		"""Agregar Procedimientos de Evento"""
		global continua
		if(continua):
			success = ProcedEventoAgregar.nuevoregistro.nuevoregistro(self, conditions, ProcedEventoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_328(self):
		"""Repetir Registro Procedimientos de Evento"""
		global continua
		if(continua):
			success = ProcedEventoRepetir.repetirregistro.repetirregistro(self, conditions, ProcedEventoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_329(self):
		"""Modifica Procedimientos de Evento"""
		global continua
		if(continua):
			success = ProcedEventoModificar.modificarregistro.modificarregistro(self, conditions, ProcedEventoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_330(self):
		"""Elimina Procedimientos de Evento"""
		global continua
		if(continua):
			success = ProcedEventoEliminar.eliminarregistro.eliminarregistro(self, conditions, ProcedEventoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ProcedEventoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_331(self):
		"""Ingresa a pantalla Depositos"""
		global continua
		continua = True
		if(continua):
			success = DepositosPantalla.ingresopantalla.ingresopantalla(self, conditions, DepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_332(self):
		"""Agregar Depositos"""
		global continua
		if(continua):
			success = DepositosAgregar.nuevoregistro.nuevoregistro(self, conditions, DepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_333(self):
		"""Repetir Registro Depositos"""
		global continua
		if(continua):
			success = DepositosRepetir.repetirregistro.repetirregistro(self, conditions, DepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_334(self):
		"""Modifica Depositos"""
		global continua
		if(continua):
			success = DepositosModificar.modificarregistro.modificarregistro(self, conditions, DepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_335(self):
		"""Elimina Depositos"""
		global continua
		if(continua):
			success = DepositosEliminar.eliminarregistro.eliminarregistro(self, conditions, DepositosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, DepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_336(self):
		"""Ingresa a pantalla Ubicacion de Depositos"""
		global continua
		continua = True
		if(continua):
			success = UbicacionDepositosPantalla.ingresopantalla.ingresopantalla(self, conditions, UbicacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_337(self):
		"""Agregar Ubicacion de Depositos"""
		global continua
		if(continua):
			success = UbicacionDepositosAgregar.nuevoregistro.nuevoregistro(self, conditions, UbicacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_338(self):
		"""Repetir Registro Ubicacion de Depositos"""
		global continua
		if(continua):
			success = UbicacionDepositosRepetir.repetirregistro.repetirregistro(self, conditions, UbicacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_339(self):
		"""Modifica Ubicacion de Depositos"""
		global continua
		if(continua):
			success = UbicacionDepositosModificar.modificarregistro.modificarregistro(self, conditions, UbicacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_340(self):
		"""Elimina Ubicacion de Depositos"""
		global continua
		if(continua):
			success = UbicacionDepositosEliminar.eliminarregistro.eliminarregistro(self, conditions, UbicacionDepositosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, UbicacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_341(self):
		"""Ingresa a pantalla Clasificacion de Depositos"""
		global continua
		continua = True
		if(continua):
			success = ClasificacionDepositosPantalla.ingresopantalla.ingresopantalla(self, conditions, ClasificacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_342(self):
		"""Agregar Clasificacion de Depositos"""
		global continua
		if(continua):
			success = ClasificacionDepositosAgregar.nuevoregistro.nuevoregistro(self, conditions, ClasificacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_343(self):
		"""Repetir Registro Clasificacion de Depositos"""
		global continua
		if(continua):
			success = ClasificacionDepositosRepetir.repetirregistro.repetirregistro(self, conditions, ClasificacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_344(self):
		"""Modifica Clasificacion de Depositos"""
		global continua
		if(continua):
			success = ClasificacionDepositosModificar.modificarregistro.modificarregistro(self, conditions, ClasificacionDepositosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_345(self):
		"""Elimina Clasificacion de Depositos"""
		global continua
		if(continua):
			success = ClasificacionDepositosEliminar.eliminarregistro.eliminarregistro(self, conditions, ClasificacionDepositosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasificacionDepositosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_346(self):
		"""Ingresa a pantalla Centro Costos"""
		global continua
		continua = True
		if(continua):
			success = CentroCostosPantalla.ingresopantalla.ingresopantalla(self, conditions, CentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_347(self):
		"""Agregar Centro Costos"""
		global continua
		if(continua):
			success = CentroCostosAgregar.nuevoregistro.nuevoregistro(self, conditions, CentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_348(self):
		"""Repetir Registro Centro Costos"""
		global continua
		if(continua):
			success = CentroCostosRepetir.repetirregistro.repetirregistro(self, conditions, CentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_349(self):
		"""Modifica Centro Costos"""
		global continua
		if(continua):
			success = CentroCostosModificar.modificarregistro.modificarregistro(self, conditions, CentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_350(self):
		"""Elimina Centro Costos"""
		global continua
		if(continua):
			success = CentroCostosEliminar.eliminarregistro.eliminarregistro(self, conditions, CentroCostosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_351(self):
		"""Ingresa a pantalla Clasificacion de Asientos"""
		global continua
		continua = True
		if(continua):
			success = ClasifAsientosPantalla.ingresopantalla.ingresopantalla(self, conditions, ClasifAsientosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_352(self):
		"""Agregar Clasificacion de Asientos"""
		global continua
		if(continua):
			success = ClasifAsientosAgregar.nuevoregistro.nuevoregistro(self, conditions, ClasifAsientosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_353(self):
		"""Repetir Registro Clasificacion de Asientos"""
		global continua
		if(continua):
			success = ClasifAsientosRepetir.repetirregistro.repetirregistro(self, conditions, ClasifAsientosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_354(self):
		"""Modifica Clasificacion de Asientos"""
		global continua
		if(continua):
			success = ClasifAsientosModificar.modificarregistro.modificarregistro(self, conditions, ClasifAsientosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_355(self):
		"""Elimina Clasificacion de Asientos"""
		global continua
		if(continua):
			success = ClasifAsientosEliminar.eliminarregistro.eliminarregistro(self, conditions, ClasifAsientosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifAsientosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_356(self):
		"""Ingresa a pantalla Cuentas Contables"""
		global continua
		continua = True
		if(continua):
			success = CuentasContablesPantalla.ingresopantalla.ingresopantalla(self, conditions, CuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_357(self):
		"""Agregar Cuentas Contables"""
		global continua
		if(continua):
			success = CuentasContablesAgregar.nuevoregistro.nuevoregistro(self, conditions, CuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_358(self):
		"""Repetir Registro Cuentas Contables"""
		global continua
		if(continua):
			success = CuentasContablesRepetir.repetirregistro.repetirregistro(self, conditions, CuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_359(self):
		"""Modifica Cuentas Contables"""
		global continua
		if(continua):
			success = CuentasContablesModificar.modificarregistro.modificarregistro(self, conditions, CuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_360(self):
		"""Elimina Cuentas Contables"""
		global continua
		if(continua):
			success = CuentasContablesEliminar.eliminarregistro.eliminarregistro(self, conditions, CuentasContablesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_361(self):
		"""Ingresa a pantalla Clasificacion Cuentas Contables"""
		global continua
		continua = True
		if(continua):
			success = ClasifCuentasContablesPantalla.ingresopantalla.ingresopantalla(self, conditions, ClasifCuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_362(self):
		"""Agregar Clasificacion Cuentas Contables"""
		global continua
		if(continua):
			success = ClasifCuentasContablesAgregar.nuevoregistro.nuevoregistro(self, conditions, ClasifCuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_363(self):
		"""Repetir Registro Clasificacion Cuentas Contables"""
		global continua
		if(continua):
			success = ClasifCuentasContablesRepetir.repetirregistro.repetirregistro(self, conditions, ClasifCuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_364(self):
		"""Modifica Clasificacion Cuentas Contables"""
		global continua
		if(continua):
			success = ClasifCuentasContablesModificar.modificarregistro.modificarregistro(self, conditions, ClasifCuentasContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_365(self):
		"""Elimina Clasificacion Cuentas Contables"""
		global continua
		if(continua):
			success = ClasifCuentasContablesEliminar.eliminarregistro.eliminarregistro(self, conditions, ClasifCuentasContablesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ClasifCuentasContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_366(self):
		"""Ingresa a pantalla Eventos Contables"""
		global continua
		continua = True
		if(continua):
			success = EventosContablesPantalla.ingresopantalla.ingresopantalla(self, conditions, EventosContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_367(self):
		"""Agregar Eventos Contables"""
		global continua
		if(continua):
			success = EventosContablesAgregar.nuevoregistro.nuevoregistro(self, conditions, EventosContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_368(self):
		"""Repetir Registro Eventos Contables"""
		global continua
		if(continua):
			success = EventosContablesRepetir.repetirregistro.repetirregistro(self, conditions, EventosContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_369(self):
		"""Modifica Eventos Contables"""
		global continua
		if(continua):
			success = EventosContablesModificar.modificarregistro.modificarregistro(self, conditions, EventosContablesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_370(self):
		"""Elimina Eventos Contables"""
		global continua
		if(continua):
			success = EventosContablesEliminar.eliminarregistro.eliminarregistro(self, conditions, EventosContablesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, EventosContablesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_371(self):
		"""Ingresa a pantalla Grupo Centro Costos"""
		global continua
		continua = True
		if(continua):
			success = GrupoCentroCostosPantalla.ingresopantalla.ingresopantalla(self, conditions, GrupoCentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_372(self):
		"""Agregar Grupo Centro Costos"""
		global continua
		if(continua):
			success = GrupoCentroCostosAgregar.nuevoregistro.nuevoregistro(self, conditions, GrupoCentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_373(self):
		"""Repetir Registro Grupo Centro Costos"""
		global continua
		if(continua):
			success = GrupoCentroCostosRepetir.repetirregistro.repetirregistro(self, conditions, GrupoCentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_374(self):
		"""Modifica Grupo Centro Costos"""
		global continua
		if(continua):
			success = GrupoCentroCostosModificar.modificarregistro.modificarregistro(self, conditions, GrupoCentroCostosConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_375(self):
		"""Elimina Grupo Centro Costos"""
		global continua
		if(continua):
			success = GrupoCentroCostosEliminar.eliminarregistro.eliminarregistro(self, conditions, GrupoCentroCostosConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, GrupoCentroCostosConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_376(self):
		"""Ingresa a pantalla Acuerdos Comerciales"""
		global continua
		continua = True
		if(continua):
			success = AcuerdosComercialesPantalla.ingresopantalla.ingresopantalla(self, conditions, AcuerdosComercialesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_377(self):
		"""Agregar Acuerdos Comerciales"""
		global continua
		if(continua):
			success = AcuerdosComercialesAgregar.nuevoregistro.nuevoregistro(self, conditions, AcuerdosComercialesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_378(self):
		"""Repetir Registro Acuerdos Comerciales"""
		global continua
		if(continua):
			success = AcuerdosComercialesRepetir.repetirregistro.repetirregistro(self, conditions, AcuerdosComercialesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_379(self):
		"""Modifica Acuerdos Comerciales"""
		global continua
		if(continua):
			success = AcuerdosComercialesModificar.modificarregistro.modificarregistro(self, conditions, AcuerdosComercialesConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_380(self):
		"""Elimina Acuerdos Comerciales"""
		global continua
		if(continua):
			success = AcuerdosComercialesEliminar.eliminarregistro.eliminarregistro(self, conditions, AcuerdosComercialesConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, AcuerdosComercialesConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_381(self):
		"""Ingresa a pantalla Categorias de Riesgo"""
		global continua
		continua = True
		if(continua):
			success = CategoriaRiesgoPantalla.ingresopantalla.ingresopantalla(self, conditions, CategoriaRiesgoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_382(self):
		"""Agregar Categorias de Riesgo"""
		global continua
		if(continua):
			success = CategoriaRiesgoAgregar.nuevoregistro.nuevoregistro(self, conditions, CategoriaRiesgoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_383(self):
		"""Repetir Registro Categorias de Riesgo"""
		global continua
		if(continua):
			success = CategoriaRiesgoRepetir.repetirregistro.repetirregistro(self, conditions, CategoriaRiesgoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_384(self):
		"""Modifica Categorias de Riesgo"""
		global continua
		if(continua):
			success = CategoriaRiesgoModificar.modificarregistro.modificarregistro(self, conditions, CategoriaRiesgoConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_385(self):
		"""Elimina Categorias de Riesgo"""
		global continua
		if(continua):
			success = CategoriaRiesgoEliminar.eliminarregistro.eliminarregistro(self, conditions, CategoriaRiesgoConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, CategoriaRiesgoConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_386(self):
		"""Ingresa a pantalla Modelo de Cobranza"""
		global continua
		continua = True
		if(continua):
			success = ModeloCobranzaPantalla.ingresopantalla.ingresopantalla(self, conditions, ModeloCobranzaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_387(self):
		"""Agregar Modelo de Cobranza"""
		global continua
		if(continua):
			success = ModeloCobranzaAgregar.nuevoregistro.nuevoregistro(self, conditions, ModeloCobranzaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_388(self):
		"""Repetir Registro Modelo de Cobranza"""
		global continua
		if(continua):
			success = ModeloCobranzaRepetir.repetirregistro.repetirregistro(self, conditions, ModeloCobranzaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_389(self):
		"""Modifica Modelo de Cobranza"""
		global continua
		if(continua):
			success = ModeloCobranzaModificar.modificarregistro.modificarregistro(self, conditions, ModeloCobranzaConfig.Configuracion)
			if(success==False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_390(self):
		"""Elimina Modelo de Cobranza"""
		global continua
		if(continua):
			success = ModeloCobranzaEliminar.eliminarregistro.eliminarregistro(self, conditions, ModeloCobranzaConfig.Configuracion)
			if(success == False):
				self.wait = WebDriverWait(self.driver, 5)

				try:
					Cierra_modal = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_modal)))
					Cierra_modal.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la ventana modal.")

				except (NoSuchElementException, TimeoutException) as e:
					pass

				try:
					Cierra_todo = self.wait.until(conditions.visibility((By.XPATH, ModeloCobranzaConfig.Configuracion.btn_cerrar_pantalla)))
					Cierra_todo.click()
					Log().info(" Se presiona el boton 'Cerrar', para cerrar la pantalla.")

				except Exception as e:
					Log().error("No se encontró el botón Cerrar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
					time.sleep(3)
					timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
					img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
					Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
					self.driver.get_screenshot_as_file(img_name)
				continua = False
				raise Exception()
		else:
			Log().error("La pantalla anterior fallo por lo que esta no funcionara, para mas detalles del error consulte el reporte")
			raise Exception()

	def test_391(self):
		"""Cerrar_Navegador"""
		self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		time.sleep(2)
		self.driver.quit()
		Log().info(" Se cierra chrome")

if __name__ == '__main__':
	unittest.main()