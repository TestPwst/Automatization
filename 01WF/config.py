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

    Icodigo = "CODIGOWF12"
    Idescripcion = "Esta es una prueba para la automatización del campo descripción de los Work Flows"
    Mdescripcion = "Esta es una prueba para la MODIFICACIÓN del campo descripción de los Work Flows"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Work Flows']"
    Iopcionbuscador = "Work Flows"

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
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    btn_tipodoc = "//button[contains(@id, 'detalleworkflowperfilmovil_tabitem')]"
    btn_Nuevo_tipodoc = "//div[contains(@id, 'add_detalleworkflowperfilmovil_element')]"
    btn_Elimina_tipodoc = "//div[contains(@id, 'remove_detalleworkflowperfilmovil_element')]"
    btn_Guarda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    etiqueta_orden = "//div[contains(@id, 'Orden_label_element')]"
    etiqueta_tipodoc = "//div[contains(@id, 'tipodoc_label_element')]"
    etiqueta_modobloqueo = "//div[contains(@id, 'modobloqueo_label_element')]"
    etiqueta_obligatorio = "//div[contains(@id, 'obligatorio_label_element')]"
    campo_orden = "//input[@type = 'text' and contains(@id, 'Orden_element')"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    campo_modobloqueo = "//div[contains(@id, 'modobloqueo_select')]"
    campo_obligatorio = "//input[@type = 'checkbox' and contains(@id, 'obligatorio_checkbox')]"
    selecciona = "//span[text()='Modifica C']"
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