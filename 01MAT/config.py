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

    Icodigo = "2"
    Icodigousuario = "CódigoTest"
    Icodigoalter = "CódigoTest"
    Idescripcion = "Prueba Automatizada"
    Icalle = "Calle Prueba"
    Itelefono1 = "5534123456"
    Itelefono2 = "5567892314"
    Mcodigousuario = "CambioTest"
    Mcodigoalter = "CambioTest"
    Mdescripcion = "Prueba Cambio Automatizado"
    Mcalle = "Calle cambio automatizado"
    Mtelefono1 = "5534126789"
    Mtelefono2 = "5590781234"

    Icodigocom = "3"
    Icodigoaltercom = "CódigoTest"
    Idescripcioncom = "Prueba Automatizada"
    Icallecom = "Calle Prueba"
    Itelefono1com = "5534123456"
    Itelefono2com = "5567892314"
    Mcodigoaltercom = "CambioTest"
    Mdescripcioncom = "Prueba Cambio Automatizado"
    Mcallecom = "Calle cambio automatizado"
    Mtelefono1com = "5534126789"
    Mtelefono2com = "5590781234"

    Icodigoreg = "4"
    Icodigoalterreg = "Test1"
    Idescripcionreg = "Prueba Automatizada"
    Icallereg = "Calle Prueba"
    Itelefono1reg = "5534123456"
    Itelefono2reg = "5567892314"
    Mcodigoalterreg = "CambioTest"
    Mdescripcionreg = "Prueba Cambio Automatizado"
    Mcallereg = "Calle cambio automatizado"
    Mtelefono1reg = "5534126789"
    Mtelefono2reg = "5590781234"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Matrices']"
    Iopcionbuscador = "Matrices"

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
    etiqueta_codigousuario = "//div[contains(@id, 'codigousuario_label_element')]"
    etiqueta_codigoalter = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_calle = "//div[contains(@id, 'direccion_label_element')]"
    etiqueta_telefono1 = "//div[contains(@id, 'telefono1_label_element')]"
    etiqueta_telefono2 = "//div[contains(@id, 'telefono2_label_element')]"
    etiqueta_estado = "//div[contains(@id, 'pais_label_element')]"
    etiqueta_tipomatriz = "//div[contains(@id, 'tipomatriz_label_element')]"
    etiqueta_municipio = "//div[contains(@id, 'departamento_label_element')]"
    etiqueta_localidad = "//div[contains(@id, 'localidad_label_element')]"
    etiqueta_barrio = "//div[contains(@id, 'barrio_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigousuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    campo_codigoalter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_calle = "//input[@type = 'text' and contains(@id, 'direccion_element')]"
    campo_telefono1 = "//input[@type = 'text' and contains(@id, 'telefono1_element')]"
    campo_telefono2 = "//input[@type = 'text' and contains(@id, 'telefono2_element')]"
    ayuda_estado = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[1]/span[1]"
    ayuda_tipomatriz = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[2]/span[1]"
    ayuda_municipio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span[2]/ui-lookup/span[1]"
    ayuda_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span[2]/ui-lookup/span[1]"
    ayuda_barrio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span[2]/ui-lookup/span[1]"

    btn_companias = "//button[contains(@id, 'companias_tabitem')]"
    btn_Nuevo_compania = "//div[contains(@id, 'add_companias_element')]"
    btn_Elimina_compania = "//div[contains(@id, 'remove_companias_element')]"
    etiqueta_codigocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigoaltercom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcioncom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    etiqueta_callecom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[1]/ui-label/div"
    etiqueta_telefono1com = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-label/div"
    etiqueta_estadocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-label[1]/div"
    etiqueta_tipocompania = "//div[contains(@id, 'tipocompania_label_element')]"
    etiqueta_municipiocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span[1]/ui-label/div"
    etiqueta_localidadcom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span[1]/ui-label/div"
    etiqueta_barriocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span[1]/ui-label/div"
    campo_codigocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-numericbox/input"
    campo_codigoaltercom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox/input"
    campo_descripcioncom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
    campo_callecom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-textbox/input"
    campo_telefono1com = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-textbox[1]/input"
    campo_telefono2com = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-textbox[2]/input"
    ayuda_estadocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[1]/span[1]"
    ayuda_tipocompania = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[2]/span[1]"
    ayuda_municipiocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span[2]/ui-lookup/span[1]"
    ayuda_localidadcom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span[2]/ui-lookup/span[1]"
    ayuda_barriocom = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span[2]/ui-lookup/span[1]"
    btn_Guarda_companias = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_regional = "//button[contains(@id, 'Regionales_tabitem')]"
    btn_Nuevo_regional = "//div[contains(@id, 'add_regionales_element')]"
    btn_Elimina_regional = "//div[contains(@id, 'remove_regionales_element')]"
    etiqueta_codigoreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-label/div"
    etiqueta_codigoalterreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-label/div"
    etiqueta_descripcionreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_callereg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-label/div"
    etiqueta_telefono1reg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_telefono2reg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_estadoreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_tiporegional = "//div[contains(@id, 'tiporegional_label_element')]"
    etiqueta_municipioreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/ui-label/div"
    etiqueta_localidadreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/ui-label/div"
    etiqueta_barrioreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[11]/ui-label/div"
    campo_codigoreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-numericbox/input"
    campo_codigoalterreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-textbox/input"
    campo_descripcionreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input"
    campo_callereg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-textbox/input"
    campo_telefono1reg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-textbox/input"
    campo_telefono2reg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-textbox/input"
    ayuda_estadoreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-lookup/span[1]"
    ayuda_tiporegional = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-lookup/span[1]"
    ayuda_municipioreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/ui-lookup/span[1]"
    ayuda_localidadreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/ui-lookup/span[1]"
    ayuda_barrioreg = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[11]/ui-lookup/span[1]"
    btn_Guarda_regional = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
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