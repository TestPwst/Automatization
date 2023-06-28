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

    Icodigo = "CODIGO-12"
    Icodigoalter = "CODIGO-ALT123456789"
    Idescripcion = "Esta es una prueba de automatizacion del campo descripcion 1"
    Iobservacion = "Estas observaciones son prueba de automatizacion de la ventana Tipos de Politica para la version 2.0"
    Mcodigoalter = "1234567-CODIGO-ALTE"
    Mdescripcion = "Esta es una prueba de MODIFICACION del campo descripcion 2.0"
    Mobservacion = "Estas observaciones son prueba de MODIFICACION de la ventana Tipos de Politica para la version 2.0"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Tipos de Política']"
    Iopcionbuscador = "Tipos de Política"

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

    btn_Nuevo_CuentasCont = "//*[contains(@id, 'add_CtasCont_element')]"
    btn_Elimina_CuentasCont = "//*[contains(@id, 'rem_CtasCont_element')]"
    btn_CuentasCont = "//*[contains(@id, 'cuentascontables_tabitem')]"
    btn_acepta_ctacont = "//button[text()='Aceptar']"
    etiqueta_codigo = "//*[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigo_alter = "//*[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'Descripcion_label_element')]"
    etiqueta_observaciones = "//*[contains(@id, 'observaciones_label_element')]"
    etiqueta_tipodoc = "//div[text()='Tipo Documento']"
    etiqueta_cuentacont = "//div[text()='Cuenta Contable']"
    etiqueta_centrocosto = "//div[text()='Centro Costo']"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_observaciones = "//input[@type = 'text' and contains(@id, 'observaciones_element')]"
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