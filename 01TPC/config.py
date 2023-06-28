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

    Icodigo = "test"
    Icodigoalter = "Codi"
    Idescripcion = "Prueba Automatizada"
    Mcodigoalter = "Camb"
    Mdescripcion = "Prueba Cambio AutomatizadoM"
    Icodigousuario = "CódigoTest1"
    Mcodigousuario = "Cambiotest1"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Tipos de Compañia']"
    Iopcionbuscador = "Tipos de Compañia"

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

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigoalter = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigoalter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    etiqueta_codigousuario = "//div[contains(@id, 'codigousuario_label_element')]"
    selecciona = "//span[text()='Modifica C']"
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