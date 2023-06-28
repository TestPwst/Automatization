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

    Icodigo = "CódigoTest"
    Idescripcion = "Prueba Automatizada"
    Iporcentajeglobal = "12"
    Mdescripcion = "Prueba Cambio Automatizado"
    Mporcentajeglobal = "25"

    Itope = "10"
    Iporcentajetopes = "7"
    Mtope = "12"
    Mporcentajetopes = "9"

    Iporcentajectaart = "17"
    Mporcentajectaart = "15"

    Iporcentajecuentas = "5"
    Mporcentajecuentas = "3"

    Iporcentajearticulos = "11"
    Mporcentajearticulos = "9"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Perfiles de comisión']"
    Iopcionbuscador = "Perfiles de comisión"


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

    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_porcentajeglobal = "//div[contains(@id, 'porcentaje_label_element')]"
    etiqueta_conimpuesto = "//label[contains(@id, 'conimpuesto_label')]"
    etiqueta_comisionrepartidor = "//label[contains(@id, 'comisionrepartidor_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_porcentajeglobal = "//input[@type = 'text' and contains(@id, 'porcentaje_element')]"
    campo_conimpuesto = "//input[@type = 'checkbox' and contains(@id, 'conimpuesto_checkbox')]"
    campo_comisionrepartidor = "//input[@type = 'checkbox' and contains(@id, 'comisionrepartidor_checkbox')]"

    btn_topes = "//button[contains(@id, 'topescomision_tabitem')]"
    btn_Nuevo_topes = "//div[contains(@id, 'add_topescomision_element')]"
    btn_Elimina_topes = "//div[contains(@id, 'remove_topescomision_element')]"
    etiqueta_moneda = "//div[contains(@id, 'moneda_label_element')]"
    etiqueta_tope = "//div[contains(@id, 'tope_label_element')]"
    etiqueta_porcentajetope = "//div[text()= 'Porcentaje' and contains(@id, 'porcentaje_label_element')]"
    ayuda_moneda = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_tope = "//input[@type = 'text' and contains(@id, 'tope_element')]"
    campo_porcentajetope = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-numericbox/input"
    btn_Guarda_topes = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_ctaarticulo = "//button[contains(@id, 'comisionesxctaarticulo_tabitem')]"
    btn_Nuevo_ctaarticulo = "//div[contains(@id, 'add_comisionesxctaarticulo_element')]"
    btn_Elimina_ctaarticulo = "//div[contains(@id, 'remove_comisionesxctaarticulo_element')]"
    etiqueta_cuenta = "//div[contains(@id, 'cuenta_label_element')]"
    etiqueta_articulo = "//div[contains(@id, 'articulo_label_element')]"
    etiqueta_porcentajectaart = "//div[text()= 'Porcentaje' and contains(@id, 'porcentaje_label_element')]"
    ayuda_cuenta = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_articulo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    campo_porcentajectaart = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-numericbox/input"
    btn_Guarda_ctaarticulo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_cuentas = "//button[contains(@id, 'comisionesxcuenta_tabitem')]"
    btn_Nuevo_cuentas = "//div[contains(@id, 'add_comisionesxcuenta_element')]"
    btn_Elimina_cuentas = "//div[contains(@id, 'remove_comisionesxcuenta_element')]"
    etiqueta_cuentas = "//div[contains(@id, 'cuenta_label_element')]"
    etiqueta_porcentajecuentas = "//div[text()= 'Porcentaje' and contains(@id, 'porcentaje_label_element')]"
    ayuda_cuentas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_porcentajecuentas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-numericbox/input"
    btn_Guarda_cuentas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_articulos = "//button[contains(@id, 'comisionesxarticulo_tabitem')]"
    btn_Nuevo_articulos = "//div[contains(@id, 'add_comisionesxarticulo_element')]"
    btn_Elimina_articulos = "//div[contains(@id, 'remove_comisionesxarticulo_element')]"
    etiqueta_articulos = "//div[contains(@id, 'articulo_label_element')]"
    etiqueta_porcentajearticulos = "//div[text()= 'Porcentaje' and contains(@id, 'porcentaje_label_element')]"
    ayuda_articulos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_porcentajearticulos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-numericbox/input"
    btn_Guarda_articulos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_tipodoc = "//button[contains(@id, 'tiposdocumento_tabitem')]"
    btn_Nuevo_tipodoc = "//div[contains(@id, 'add_tiposdocumento_element')]"
    btn_Elimina_tipodoc = "//div[contains(@id, 'remove_tiposdocumento_element')]"
    etiqueta_tipodoc = "//div[contains(@id, 'tipodocumento_label_element')]"
    etiqueta_origen = "//div[contains(@id, 'origen_label_element')]"
    etiqueta_signo = "//div[contains(@id, 'signo_label_element')]"
    etiqueta_cancelado = "//div[contains(@id, 'cancelado_label_element')]"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_origen = "//div[contains(@id, 'origen_select')]"
    campo_signo = "//div[contains(@id, 'signo_select')]"
    campo_cancelado = "//input[@type = 'checkbox' and contains(@id, 'cancelado_checkbox')]"
    btn_Guarda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    selecciona = "//span[text()='Modifica C']"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_cerrar_ayuda = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    btn_cerrar_busqueda = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[1]/div/span[4]"
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