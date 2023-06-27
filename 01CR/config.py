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
   

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join("C:\chromedriver\chromedriver"))

    Icodigo = "10000"
    Idescripcion = "Esta es una prueba automatizada para validar la descripción de Categoría de Riesgo en la versión 2.0"
    Iporcentajelim = "100"
    Iperiodo = "100"
    Mdescripcion = "Esta es una prueba automatizada para validar la modificació de Categoría de Riesgo en la versión 2.0"
    Mporcentajelim = "99"
    Mperiodo = "111"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Categorías Riesgo']"
    Iopcionbuscador = "Categorías Riesgo"

    #Agregar, modificar y eliminar el registro
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

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"
    etiqueta_porcentajelim = "//div[contains(@id, 'porclimite_label_element')]"
    etiqueta_periodo = "//div[contains(@id, 'Periodo_label_element')]"
    etiqueta_alcance = "//div[contains(@id, 'alcance_label_element')]"
    etiqueta_mostrarmen = "//label[contains(@id, 'mostrarmsg_label')]"
    etiqueta_creditoabierto = "//label[contains(@id, 'creditoabierto_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_porcentajelim = "//input[@type = 'text' and contains(@id, 'porclimite_element')]"
    campo_periodo = "//input[@type = 'text' and contains(@id, 'Periodo_element')]"
    campo_alcance = "//div[contains(@id, 'alcance_select')]"
    campo_mostrarmen = "//input[@type = 'checkbox' and contains(@id, 'mostrarmsg_checkbox')]"
    campo_creditoabierto = "//input[@type = 'checkbox' and contains(@id, 'creditoabierto_checkbox')]"
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
