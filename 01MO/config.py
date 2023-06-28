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

    __CHROME_DRIVER_PATH = modify_name_for_windows(("C:\chromedriver\chromedriver"))

    Icodigo = "100"
    Idescripcion = "Esta es un prueba automatizada para validar el campo descripcion de moneda en la version 2.0 de PWST"
    Isimbolo = "XX"
    IsimboloISO = "YY"
    Mdescripcion = "Esta es un prueba automatizada para validar el campo descripcion de moneda en la version 2.0 de PWST"
    Msimbolo = "XY"
    MsimboloISO = "YX"

    Icambio  = "1000"
    Iventa = "100"
    Icompra = "100"
    Ifiscal = "100"
    Mcambio  = "2000"
    Mventa = "200"
    Mcompra = "200"
    Mfiscal = "200"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Monedas']"
    Iopcionbuscador = "Monedas"

    #Agregar, modificar y eliminar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@id, 'save_element')]"
    btn_Guarda2 = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "//button[text()= 'Aceptar']"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "//button[text()='Cerrar']"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_ctacont = "//button[contains(@id, 'ctascont_tabitem')]"
    btn_cotizacion = "//button[contains(@id, 'cotizaciones_tabitem')]"
    btn_nuevoctacont = "//div[contains(@id, 'add_ctascont_element')]"
    btn_nuevocot = "//div[contains(@id, 'add_cotizaciones_element')]"
    btn_aceptactacont = "//button[text()= 'Aceptar']"
    btn_elimcot = "//div[contains(@id, 'remove_cotizaciones_element')]"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"
    etiqueta_codigo = "//*[contains(@id, 'codigo_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'descripcion_label_element')]"
    etiqueta_simbolo = "//*[contains(@id, 'simbolo_label_element')]"
    etiqueta_fecha = "//*[contains(@id, 'fecha_label_element')]"
    etiqueta_cambio = "//*[contains(@id, 'cambio_label_element')]"
    etiqueta_venta = "//*[contains(@id, 'venta_label_element')]"
    etiqueta_compra = "//*[contains(@id, 'compra_label_element')]"
    etiqueta_fiscal = "//*[contains(@id, 'fiscal_label_element')]"
    etiqueta_simiso = "//*[contains(@id, 'simboloiso4217_label_element')]"
    etiqueta_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-label/div"
    etiqueta_cuentacont = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-label/div"
    etiqueta_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-label/div"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_simbolo = "//input[contains(@id, 'simbolo_element')]"
    campo_simiso = "//input[contains(@id, 'simboloiso4217_element')]"
    campo_cambio = "//input[contains(@id, 'cambio_element')]"
    campo_venta = "//input[contains(@id, 'venta_element')]"
    campo_compra = "//input[contains(@id, 'compra_element')]"
    campo_fiscal = "//input[contains(@id, 'fiscal_element')]"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_ctacont = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-lookup/span[1]"
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