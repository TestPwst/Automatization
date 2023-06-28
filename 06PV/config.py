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

    Icodigo = "840011"
    Icodigoalter = "840011"
    Idescripcion = "Prueba automatizada del campo descripción PV"
    Ifechahasta = "29-07-2030"
    Mcodigoalter = "CambioTest"
    Mdescripcion = "Prueba automatizada de la Modificación campo descripción PV"
    Mfechahasta = "29-07-2033"

    Igrupopolitica = "ZI01"
    Mgrupopolitica = "ZI06"
    Iporcentajedesc = "20"
    Mporcentajedesc = "25"

    Itopedescuento1 = "100"
    Itopedescuento2 = "100"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Políticas de venta']"
    Iopcionbuscador = "Políticas de venta"

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
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_fechadesde = "//div[contains(@id, 'desdefecha_label_element')]"
    etiqueta_fechahasta = "//div[contains(@id, 'hastafecha_label_element')]"
    etiqueta_moneda = "//div[contains(@id, 'moneda_label_element')]"
    etiqueta_modo = "//div[contains(@id, 'modo_label_element')]"
    etiqueta_aplicableen = "//div[contains(@id, 'aplicableen_label_element')]"
    etiqueta_activa = "//div[contains(@id, 'activa_label_element')]"
    etiqueta_apliglobal = "//div[contains(@id, 'aplicaglobal_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    ayuda_fechadesde = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-container/ui-row[4]/ui-datebox/span"
    campo_fechahasta = "//input[@type = 'text' and contains(@id, 'hastafecha_element')]"
    ayuda_moneda = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span/ui-container[1]/ui-row[9]/ui-lookup/span[1]"
    campo_modo = "//div[contains(@id, 'modo_select')]"
    campo_aplicableen = "//div[contains(@id, 'aplicableen_select')]"
    campo_activa = "//input[@type = 'checkbox' and contains(@id, 'activa_checkbox')]"
    campo_apliglobal = "//input[@type = 'checkbox' and contains(@id, 'aplicaglobal_checkbox')]"

    btn_porarticulo = "//button[contains(@id, 'porarticulo_tabitem')]"
    btn_Nuevo_porarticulo = "//div[contains(@id, 'add_descuentosxarticulo_element')]"
    btn_Elimina_porarticulo = "//div[contains(@id, 'remove_descuentosxarticulo_element')]"
    etiqueta_grupopolitica = "//div[contains(@id, 'grupopolitica_label_element')]"
    etiqueta_porcentajedesc = "//div[contains(@id, 'porcentajedescuento_label_element')]"
    etiqueta_topedescuento1 = "//div[contains(@id, 'topedescuento1_label_element')]"
    etiqueta_topedescuento2 = "//div[contains(@id, 'topedescuento2_label_element')]"
    campo_grupopolitica = "//input[@type = 'text' and contains(@id, 'grupopolitica_element')]"
    campo_porcentajedesc = "//input[@type = 'text' and contains(@id, 'porcentajedescuento_element')]"
    campo_topedescuento1 = "//input[@type = 'text' and contains(@id, 'topedescuento1_element')]"
    campo_topedescuento2 = "//input[@type = 'text' and contains(@id, 'topedescuento2_element')]"
    btn_Guarda_porarticulo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    selecciona = "//span[text()='Modifica C']"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )