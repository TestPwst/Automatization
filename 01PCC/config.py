import os
import platform
from selenium import webdriver
from selenium.webdriver.support import expected_conditions

def modify_name_for_windows(in_path):
    if platform.system().lower().startswith("win"):
        return in_path + ".exe"
    return in_path

#expected_conditions
class conditions:
    visibility = expected_conditions.visibility_of_element_located
    clickable = expected_conditions.element_to_be_clickable

class Configuracion:

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join("C:\chromedriver\chromedriver"))

    # general
    Icodigo = "CódigoTest"
    Idescripcion = "Prueba Automatizada"
    Mdescripcion = "Prueba Cambio Automatizado"

    #pestaña centro costo
    Iporcentaje = "5"
    Mporcentaje = "15"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Prorrateo por centros de costo']"
    Iopcionbuscador = "Prorrateo por centros de costo"

    #Agregar, modificar y eliminar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@id, 'save_element')]"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "//button[text()='Aceptar']"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "//button[text()='Cerrar']"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"

    #pantalla general

    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"

    #pestaña centro de costo

    btn_centrocosto = "//button[contains(@id, 'items_tabitem')]"
    btn_Nuevo_centrocosto = "//div[contains(@id, 'add_items_element')]"
    btn_Elimina_centrocosto = "//div[contains(@id, 'remove_items_element')]"
    btn_guardarcosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    etiqueta_centrocosto = "//div[contains(@id, 'centrocosto_label_element')]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    selecciona = "//span[text()='Modifica C']"
    etiqueta_porcentaje = "//div[contains(@id, 'porcentaje_label_element')]"
    campo_porcentaje = "//input[@type = 'text' and contains(@id, 'porcentaje_element')]"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )