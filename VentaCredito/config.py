import os
import platform
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from settings import root_dir


def modify_name_for_windows(in_path):
    if platform.system().lower().startswith("win"):
        return in_path + ".exe"
    return in_path


#expected_conditions
class conditions:
    visibility = expected_conditions.visibility_of_element_located
    clickable = expected_conditions.element_to_be_clickable


class Configuracion:
    __DRIVER_DIR = os.path.join(root_dir, "drivers")

    __CHROME_DRIVER_PATH = modify_name_for_windows(("C:\chromedriver\chromedriver"))

    Imenu = "Explorador de reportes"
    Ibuscar = "toma de stock"
    Idesde = "PM01"
    Ihasta = "PM03"
    Ialmacen = "4151"
    Icuenta = "818H010947"
    Iarticulo2 = "FA03002"
    Iarticulo1 = "FA03001"
    Icantidad1 = "1"
    Icantidad2 = "5"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    campo_menu = "//*[@id='quickSearchInput']"
    btn_explorador = "//*[@id='quickSearchInputautocomplete-list']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"

    #Ingresar al reporte de stock
    campo_buscar = "//input[@type = 'text' and contains(@id, 'txtBuscarRep_element')]"
    btn_buscar = "//button[contains(@id, '7_element')]"
    campo_desde = "//input[@type = 'text' and contains(@id, 'variable_1_element')]"
    campo_hasta = "//input[@type = 'text' and contains(@id, 'variable_2_element')]"
    campo_almancen = "//input[@type = 'text' and contains(@id, 'variable_3_element')]"
    btn_ver = "//button[text()='Ver']"

    #Ingresar al documento de venta
    campo_cliente = "//input[@type = 'text' and contains(@id, 'cuenta_element')]"
    campo_ob = "//input[@type = 'text' and contains(@id, 'observaciones_element')]"
    btn_add_art = "//*[contains(@id, 'items|add_element')]"
    campo_art = "//input[@type = 'text' and contains(@id, 'articulo_element')]"
    campo_cant = "//input[@type = 'text' and contains(@id, 'cantidad_element')]"
    campo_numserie = "//input[@type = 'text' and contains(@id, 'numeroSerie_element')]"
    btn_aceptar_art = "//button[text()= 'Aceptar']"
    btn_cerrar_art = "//button[text()= 'Cancelar']"
    btn_Guarda = "//div[contains(@id, 'save_element')]"

    #Documentos emitidos
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    cerrar_doc = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    refrescar_report = "//div[contains(@id, '000_rptview1_element')]"

    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "//button[text()='Aceptar']"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "//button[text()='Cerrar']"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_ctacont = "//button[contains(@id, 'CtasCont_tabitem')]"
    btn_nuevoctacont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_aceptactacont = "//button[text()= 'Aceptar']"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
