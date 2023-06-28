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

    Icodigo = "100"
    Idescripcion = "Prueba Automatizada"
    Mdescripcion = "Prueba Cambio AutomatizadoM"
    Iimportelimite = "5000"
    Itope = "100"
    Icontrasena = "Contrasena123"
    Iconfirmacion = "Contrasena123"
    Mimportelimite = "10000"
    Mtope = "550"
    Mcontrasena = "Contrasena12345"
    Mconfirmacion = "Contrasena12345"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Perfiles de Crédito']"
    Iopcionbuscador = "Perfiles de Crédito"

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

    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"


    # cambio de pestaña limites credito
    btn_limitescredito = "//button[contains(@id, 'limitescredito_tabitem')]"
    btn_Nuevo_limitescredito = "//div[contains(@id, 'add_limitescredito_element')]"
    btn_Elimina_limitescredito = "//div[contains(@id, 'remove_limitescredito_element')]"
    campo_modolimite = "//div[contains(@id, 'Modo_select')]"
    ayuda_empresa = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span[2]/ui-lookup/span[1]"
    ayuda_moneda = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-lookup/span[1]"
    etiqueta_empresa = "//div[contains(@id, 'empresa_label_element')]"
    etiqueta_moneda = "//div[contains(@id, 'moneda_label_element')]"
    etiqueta_modolimite = "//div[contains(@id, 'Modo_label_element')]"
    etiqueta_importelimite = "//div[contains(@id, 'importelabel2_element')]"
    campo_importelimite = "//input[@type = 'text' and contains(@id, 'importe1_element')]"

    # cambio pestaña Autorizaciones
    btn_Autorizaciones = "//button[contains(@id, 'autorizaciones_tabitem')]"
    btn_Nuevo_Autorizaciones = "//div[contains(@id, 'add_autorizaciones_element')]"
    btn_Elimina_Autorizaciones = "//div[contains(@id, 'remove_autorizaciones_element')]"
    ayuda_usuario = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    etiqueta_usuario = "//div[contains(@id, 'usuario_label_element')]"
    etiqueta_tope = "//div[contains(@id, 'tope_label_element')]"
    etiqueta_contrasena = "//div[contains(@id, 'contra_label_element')]"
    etiqueta_confirmacion = "//div[contains(@id, 'contra2_label_element')]"
    campo_tope = "//input[@type = 'text' and contains(@id, 'tope_element')]"
    campo_contrasena = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-passwordbox/input"
    campo_confirmacion = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-passwordbox/input"
    btn_guardautorizacion = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_guardas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
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