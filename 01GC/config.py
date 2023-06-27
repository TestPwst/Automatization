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

    Icodigo = "1000"
    Icodigoalter = "Testing001"
    Idescripcion = "Esto es un prueba automatizada para validar la descripción de grupos de clientes en PWST 2.0"
    Mcodigoalter = "CambioTest"
    Mdescripcion = "Esto es un prueba automatizada para validar la modificación de grupos de cliente en PWST 2.0"

    Icodigosub = "100"
    Icodigoaltersub = "Testing002"
    Idescripcionsub = "Esto es un prueba automatizada para validar la descripción de subgrupos de clientes en PWST 2.0"
    Mcodigoaltersub = "CambioTest"
    Mdescripcionsub = "Esto es un prueba automatizada para validar la modificación de subgrupos de cliente en PWST 2.0"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Grupos']"
    Iopcionbuscador = "Grupos"

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
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"
    etiqueta_unidadnegocio = "//div[contains(@id, 'UnidadNegocio_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    ayuda_unidadnegocio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-lookup/span[1]"

    btn_subgrupos = "//button[contains(@id, 'SubGrupos_tabitem')]"
    btn_Nuevo_subgrupo = "//div[contains(@id, 'add_SubGrupos_element')]"
    btn_Elimina_subgrupo = "//div[contains(@id, 'remove_SubGrupos_element')]"
    etiqueta_codigosub = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_codigo_altersub = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcionsub = "//div[contains(@id, 'descripcion_label_element')]"
    campo_codigosub = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_altersub = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcionsub = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    btn_Guarda_subgrupos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_CuentasCont = "//button[contains(@id, 'ConfiguracionContable_tabitem')]"
    btn_Nuevo_CuentasCont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_Elimina_CuentasCont = "//div[contains(@id, 'rem_CtasCont_element')]"
    etiqueta_tipodoc = "//div[text()= 'Tipo Documento' and contains(@id, '3_element')]"
    etiqueta_cuentacont = "//div[text()= 'Cuenta Contable' and contains(@id, '6_element')]"
    etiqueta_centrocosto = "//div[text()= 'Centro Costo' and contains(@id, '9_element')]"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_ctacont = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-lookup/span[1]"
    btn_acepta_ctacont = "//button[text()='Aceptar']"
    selecciona = "//span[text()='Modifica C']"



    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
