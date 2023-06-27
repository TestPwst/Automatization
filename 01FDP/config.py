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

    Icodigo = "100"
    Idescripcion = "Prueba Automatizada"
    Icodigoalternativo = "100"
    IcodigoGLN = "100"
    Idescuento = "10"
    Irecargo = "15"
    Mdescripcion = "Prueba Cambio Automatizado"
    Mcodigoalternativo = "101"
    McodigoGLN = "101"
    Mdescuento = "5"
    Mrecargo = "10"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    btn_codigo = "//div[text()='Código']"
    texto_buscador = "//div[text()='Formas de pago']"
    Iopcionbuscador = "Formas de pago"

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
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"

    #pantalla general

    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descrip_label_element')]"
    etiqueta_codigoalternativo = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_codigoGLN = "//div[contains(@id, 'codigogln_label_element')]"
    etiqueta_descuento = "//div[contains(@id, 'descuento_label_element')]"
    etiqueta_recargo = "//div[contains(@id, 'recargo_label_element')]"
    etiqueta_modovencimiento = "//div[contains(@id, 'modovencimiento_label_element')]"
    etiqueta_plazo = "//div[contains(@id, 'diasplazo_label_element')]"
    etiqueta_tipovencimiento = "//div[contains(@id, 'tipovencimiento_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigoalternativo = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_codigoGLN = "//input[@type = 'text' and contains(@id, 'codigogln_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descrip_element')]"
    campo_descuento = "//input[@type = 'text' and contains(@id, 'descuento_element')]"
    campo_recargo = "//input[@type = 'text' and contains(@id, 'recargo_element')]"
    campo_modvencimiento = "//div[contains(@id, 'modovencimiento_select')]"
    accioncodigo = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-listview/div/div/div[1]/div[1]/div[2]/div[1]"



    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
