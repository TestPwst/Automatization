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

    Idesdehora = "10:00"
    Ihastahora = "21:00"
    Ireintentosnum = "10"
    Ireintentoscon = "10"
    Ireintentossin = "10"

    Mdesdehora = "11:00"
    Mhastahora = "20:00"
    Mreintentosnum = "15"
    Mreintentoscon = "15"
    Mreintentossin = "15"


    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Franjas Horarias']"
    Iopcionbuscador = "Franjas Horarias"

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

    etiqueta_codigo = "//div[contains(@id, 'id_label_element')]"
    etiqueta_desdehora = "//div[contains(@id, 'desdehora_label_element')]"
    etiqueta_hastahora = "//div[contains(@id, 'hastahora_label_element')]"
    etiqueta_reintentosnum = "//div[contains(@id, 'reintentosnumero_label_element')]"
    etiqueta_reintentoscon = "//div[contains(@id, 'reintentosconexion_label_element')]"
    etiqueta_reintentossin = "//div[contains(@id, 'reintentossincronizacion_label_element')]"

    campo_desdehora = "//input[@type = 'text' and contains(@id, 'desdehora_element')]"
    campo_hastahora = "//input[@type = 'text' and contains(@id, 'hastahora_element')]"
    campo_reintentosnum = "//input[@type = 'text' and contains(@id, 'reintentosnumero_element')]"
    campo_reintentoscon = "//input[@type = 'text' and contains(@id, 'reintentosconexion_element')]"
    campo_reintentossin = "//input[@type = 'text' and contains(@id, 'reintentossincronizacion_element')]"


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
