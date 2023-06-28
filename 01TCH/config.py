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

    __CHROME_DRIVER_PATH = modify_name_for_windows(("C:\chromedriver\chromedriver"))

    Icodigo = "Test"
    Idescripcion = "Esto es una prueba automatizada para validar la descripcion de cheque en la version 2.0 de PWST"
    Mdescripcion = "Esto es una prueba automatizada para validar la modificacion de cheque en la version 2.0 de PWST"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "//span[contains (@class, 'ui-window-title')]"

    #Agregar, modificar y eliminar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@id, 'save_element')]"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "//button[contains (@class, 'btn-accept')]"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "//button[text()='Cerrar']"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_ctacont = "//button[contains(@id, 'CtasCont_tabitem')]"
    btn_nuevoctacont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_aceptactacont = "//button[text()= 'Aceptar']"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"
    etiqueta_codigo = "//*[contains(@id, 'Codigo_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'descripcion_label_element')]"
    etiqueta_vencimiento = "//*[contains(@id, 'modocontrolfecha_label_element')]"
    etiqueta_adeudos = "//*[contains(@id, 'modocontrolchequesadeudados_label_element')]"
    etiqueta_mediopago = "//label[contains(@id, 'unicomediopago_label')]"
    etiqueta_gendoc = "//label[contains(@id, 'generacuentacorriente_label')]"
    etiqueta_tipodoccheque = "//*[contains(@id, 'tipodocumentocuentacorriente_label_element')]"
    etiqueta_verificacredito = "//*[contains(@id, 'verificarvencimientolimitecredito_label_element')]"
    etiqueta_liberar = "//label[contains(@id, 'liberarlimitecredito_label')]"
    etiqueta_tipodoc = "//div[text()= 'Tipo Documento' and contains(@id, '3_element')]"
    etiqueta_cuentacont = "//div[text()= 'Cuenta Contable' and contains(@id, '6_element')]"
    etiqueta_centrocosto = "//div[text()= 'Centro Costo' and contains(@id, '9_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_vencimiento = "//div[contains(@id, 'modocontrolfecha_select')]"
    campo_adeudos = "//div[contains(@id, 'modocontrolchequesadeudados_select')]"
    check_mediopago = "//input[@type = 'checkbox' and contains(@id, 'unicomediopago_checkbox')]"
    check_gendoc = "//input[@type = 'checkbox' and contains(@id, 'generacuentacorriente_checkbox')]"
    ayuda_tipodoccheque = "//span[@class = 'help']"
    campo_verificacredito = "//div[contains(@id, 'verificarvencimientolimitecredito_select')]"
    check_liberar = "//input[@type = 'checkbox' and contains(@id, 'liberarlimitecredito_checkbox')]"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_ctacont = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-lookup/span[1]"
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