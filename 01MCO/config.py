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

    Icodigo = "CódigoTes"
    Idescripcion = "Prueba Automatizada"
    Mdescripcion = "Prueba Cambio AutomatizadoM"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Modelos de cobranza']"
    Iopcionbuscador = "Modelos de cobranza"

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
    etiqueta_Generardocumento = "//div[contains(@id, 'MyCheckBoxGenerarDocCobranza_label')]"
    etiqueta_descuento = "//div[contains(@id, 'MyCheckBoxGenerarDocDescuento_label')]"
    etiqueta_retencion = "//div[contains(@id, 'MyCheckBoxGenerarDocRetencion_label')]"
    campo_Generarcobranza = "//input[@type = 'checkbox' and contains(@id, 'MyCheckBoxGenerarDocCobranza_checkbox')]"
    campo_Generardescuento = "//input[@type = 'checkbox' and contains(@id, 'MyCheckBoxGenerarDocDescuento_checkbox')]"
    campo_Generarretencion = "//input[@type = 'checkbox' and contains(@id, 'MyCheckBoxGenerarDocRetencion_checkbox')]"
    etiqueta_tipodocgenerar = "//div[contains(@id, 'tipodoccobranza_label_element')]"
    etiqueta_tipodocdescuento = "//div[contains(@id, 'tipodocdescuento_label_element')]"
    etiqueta_tipodocretencion = "//div[contains(@id, 'tipodocretencion_label_element')]"
    ayuda_tipodocgenerar = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_tipodocdescuento = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_tipodocretencion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-container/ui-row[2]/ui-lookup/span[1]"
    etiqueta_accioncobranza = "//div[contains(@id, 'accioncobranza_label_element')]"
    etiqueta_acciondescuent = "//div[contains(@id, 'acciondescuento_label_element')]"
    etiqueta_accionretencion = "//div[contains(@id, 'accionretencion_label_element')]"
    etiqueta_modogenerar = "//div[contains(@id, 'generarcobranza_label_element')]"
    etiqueta_mododescuento = "//div[contains(@id, 'generardescuento_label_element')]"
    etiqueta_modoretencion = "//div[contains(@id, '_generarretencion_label_element')]"
    campo_accioncobranza = "//div[contains(@id, 'accioncobranza_select')]"
    campo_acciondescuent = "//div[contains(@id, 'acciondescuento_select')]"
    campo_accionretencion = "//div[contains(@id, 'accionretencion_select')]"
    campo_modogenerar = "//div[contains(@id, 'generarcobranza_select')]"
    campo_mododescuento = "//div[contains(@id, 'generardescuento_select')]"
    campo_modoretencion = "//div[contains(@id, 'generarretencion_select')]"
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