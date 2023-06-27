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

    Icodigo = "CódigoTest"
    Icodigo_alt = "CódigoTest"
    Idescripcion = "Esto es una prueba automatizada para validar el campo descripción de categorías fiscales en PWST 2.0"
    Mcodigo_alt = "CambioTest"
    Mdescripcion = "Esto es una prueba automatizada para validar el campo modificacio de categorías fiscales en PWST 2.0"

    # IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Categorías Fiscales']"
    Iopcionbuscador = "Categorías Fiscales"

    #Agregar nuevo, eliminar y modificar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@id, 'save_element')]"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "/html/body/div[3]/div[2]/ui-modal/div/div[3]/button[1]"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"

    etiqueta_codigo = "//*[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigo_alt = "//*[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'Descripcion_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigo_alt = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    selecciona = "//span[text()='Modifica C']"



    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
