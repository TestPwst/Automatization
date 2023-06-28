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

    #pestaña general

    Icodigo = "100"
    Icodigoalter = "100"
    Idescripcion = "Prueba Automatizada"
    Mcodigoalter = "150"
    Mdescripcion = "Prueba Cambio AutomatizadoM"
    IMaximodehorasEntrega = "1"
    MMaximodehorasEntrega = "2"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Perfiles']"
    Iopcionbuscador = "Perfiles"

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

    # pestaña general

    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_codigoalter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_Maximohoras = "//div[contains(@id, 'horasmaximoentrega_label_element')]"
    etiqueta_PerfilCredito = "//div[contains(@id, 'perfilcredito_label_element')]"
    etiqueta_CategoriaRiesgo = "//div[contains(@id, 'categoriariesgo_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigoalter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_Maximohoras = "//input[@type = 'text' and contains(@id, 'horasmaximoentrega_element')]"
    ayuda_PerfilCredito = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span[2]/ui-lookup/span[1]"
    ayuda_CategoriaRiesgo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span[2]/ui-lookup/span[1]"
    btn_aceptar = "/html/body/div[3]/div[2]/ui-modal/div/div[3]/button[1]"

    #cambio de pestaña tipos documentos

    btn_tiposdoc = "//button[contains(@id, 'tiposdocumento_tabitem')]"
    btn_Nuevo_tipodoc = "//div[contains(@id, 'add_tiposdocumento_element')]"
    btn_Elimina_tipodoc = "//div[contains(@id, 'remove_tiposdocumento_element')]"
    btn_guardartipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    # pestaña respuestas

    etiqueta_tipodoc = "//div[contains(@id, 'id_label_element')]"
    ayuda_tiposdocumentos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
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