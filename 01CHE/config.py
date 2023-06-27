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

    Iserie = "100"
    Idesdenumero = "1"
    Ihastanumero = "99"
    Mserie = "100"
    Inumero = "1"
    Icomentario = "prueba automatizacion"
    Mnumero = "2"
    Mdesdenumero = "2"
    Mhastanumero = "88"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Chequeras']"
    Iopcionbuscador = "Chequeras"

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

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_banco = "//div[contains(@id, 'banco_label_element')]"
    etiqueta_serie = "//div[contains(@id, 'serie_label_element')]"
    etiqueta_moneda = "//div[contains(@id, 'moneda_label_element')]"
    etiqueta_desdenumero = "//div[contains(@id, 'desdenumero_label_element')]"
    etiqueta_hastanumero = "//div[contains(@id, 'hastanumero_label_element')]"
    etiqueta_proxionum = "//div[contains(@id, 'numerodisponibleB_label_element')]"
    etiqueta_chequeraactiva = "//div[contains(@id, 'activarCheqe_label_element')]"
    ayuda_banco = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_moneda = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-lookup/span[1]"
    campo_serie = "//input[@type = 'text' and contains(@id, 'serie_element')]"
    campo_desdenumero = "//input[@type = 'text' and contains(@id, 'desdenumero_element')]"
    campo_hastanumero = "//input[@type = 'text' and contains(@id, 'hastanumero_element')]"


    # cambio de pestaña cheques anulados
    btn_cheques_anulados = "//button[contains(@id, 'chequesanulados_tabitem')]"
    btn_Nuevo_cheques = "//div[contains(@id, 'add_chequesanulados_element')]"
    btn_Elimina_cheques = "//div[contains(@id, 'remove_chequesanulados_element')]"
    etiqueta_numero = "//div[contains(@id, 'numeroanulado_label_element')]"
    etiqueta_comentario = "//div[contains(@id, 'comentario_label_element')]"
    campo_chequera_numero = "//input[@type = 'text' and contains(@id, 'numeroanulado_element')]"
    campo_chequera_comentario = "//input[@type = 'text' and contains(@id, 'comentario_element')]"
    btn_guarda_cheques = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"











    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
