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

    __CHROME_DRIVER_PATH = modify_name_for_windows(("C:\chromedriver\chromedriver"))

    Icodigo = "100"
    Icodigoalt = "100"
    Idescripcion = "Prueba Automatizada"
    Mcodigoalt = "222"
    Mdescripcion = "Cambio Automatizado"
    Mequivalencia = "2"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Grupos de Política']"
    Iopcionbuscador = "Grupos de Política"

    #Agregar, modificar y eliminar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@id, 'save_element')]"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "//button[text()='Aceptar']"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "//button[text()='Cerrar']"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_articulos = "//button[contains(@id, 'articulosxgrupo_tabitem')]"
    btn_nuevoart = "//div[contains(@id, 'add_articulosxgrupo_element')]"
    btn_saveart = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_removeart = "//div[contains(@id, 'remove_articulosxgrupo_element')]"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"
    etiqueta_codigo = "//*[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigoalt = "//*[contains(@id, 'Codigoak_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'Descripcion_label_element')]"
    etiqueta_tipogrupo = "//*[contains(@id, 'tipogrupo_label_element')]"
    etiqueta_articulo = "//*[contains(@id, 'articulo_label_element')]"
    etiqueta_equivalencia = "//*[contains(@id, 'equivalenciaproductobase_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigoalt = "//input[@type = 'text' and contains(@id, 'Codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_tipogrupo = "//*[contains(@id, 'tipogrupo_select')]"
    tipogrupo1 = "//li[contains(@id, '2')]"
    tipogrupo2 = "//li[contains(@id, '1')]"
    ayuda_articulo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_equivalencia = "//input[@type = 'text' and contains(@id, 'equivalenciaproductobase_element')]"
    selecciona = "//span[text()='Modifica C']"
    btn_elimina_articulo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/ui-container/ui-row[1]/ui-toolband/div/span[2]/ui-toolbarbutton/div"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    equivalente = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-numericbox/input"
    btn_guarda_articulo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"
    btn_cerrar_ayuda = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[1]/div/span[4]"
    btn_cerrar_menu = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    
    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
