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

    Icodigo = "Test"
    Idescripcion = "Prueba automatizada del campo descripción tipos de cheque PWST 2.0"
    Mdescripcion = "Prueba automatizada de la Modificación del campo descripción tipos de cheque PWST 2.0"


    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"
    btn_cerrarsesion = "//a[@title= 'cerrar sesión']"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Tipos de cheque']"
    Iopcionbuscador = "Tipos de cheque"

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

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_modocontrolven = "//div[contains(@id, 'modocontrolfecha_label_element')]"
    etiqueta_modocontrolcheques = "//div[contains(@id, 'modocontrolchequesadeudados_label_element')]"
    etiqueta_unicomediopago = "//label[contains(@id, 'unicomediopago_label')]"
    etiqueta_generadoc = "//label[contains(@id, 'generacuentacorriente_label')]"
    etiqueta_tipodoccheque = "//div[contains(@id, 'tipodocumentocuentacorriente_label_element')]"
    etiqueta_vencimientolimite = "//div[contains(@id, 'verificarvencimientolimitecredito_label_element')]"
    etiqueta_liberarcredito = "//label[contains(@id, 'liberarlimitecredito_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_modocontrolven = "//div[contains(@id, 'modocontrolfecha_select')]"
    campo_modocontrolcheques = "//div[contains(@id, 'modocontrolchequesadeudados_select')]"
    campo_unicomediopago = "//input[@type = 'checkbox' and contains(@id, 'unicomediopago_checkbox')]"
    campo_generadoc = "//input[@type = 'checkbox' and contains(@id, 'generacuentacorriente_checkbox')]"
    ayuda_tipodoccheque = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-lookup/span[1]"
    campo_vencimientolimite = "//div[contains(@id, 'verificarvencimientolimitecredito_select')]"
    campo_liberarcredito = "//input[@type = 'checkbox' and contains(@id, 'liberarlimitecredito_checkbox')]"

    btn_CuentasCont = "//button[contains(@id, 'CtasCont_tabitem')]"
    btn_Nuevo_CuentasCont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_Elimina_CuentasCont = "//div[contains(@id, 'rem_CtasCont_element')]"
    btn_acepta_ctacont = "//button[text()='Aceptar']"
    etiqueta_tipodoc = "//div[text()='Tipo Documento']"
    etiqueta_cuentacont = "//div[text()='Cuenta Contable']"
    etiqueta_centrocosto = "//div[text()='Centro Costo']"
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