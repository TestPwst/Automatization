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

    Iefectividad = "90"
    Mefectividad = "99"

    Iobjetivodistribucion = "10"
    Mobjetivodistribucion = "12"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Objetivos Diarios']"
    Iopcionbuscador = "Objetivos Diarios"

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

    etiqueta_vendedor = "//div[contains(@id, 'vendedor_label_element')]"
    etiqueta_fecha = "//div[contains(@id, 'fecha_label_element')]"
    etiqueta_efectividad = "//div[contains(@id, 'porcentajeefectividad_label_element')]"
    ayuda_vendedor = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_fecha = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-datebox/span"
    campo_efectividad = "//input[@type = 'text' and contains(@id, 'porcentajeefectividad_element')]"

    btn_grupos = "//button[contains(@id, 'grupos_tabitem')]"
    btn_Nuevo_grupo = "//div[contains(@id, 'add_gruposxobjetivo_element')]"
    btn_Elimina_grupo = "//div[contains(@id, 'remove_gruposxobjetivo_element')]"
    etiqueta_grupopolitica = "//div[contains(@id, 'grupopolitica_label_element')]"
    etiqueta_tipoobjetivo = "//div[contains(@id, 'tipoobjetivo_label_element')]"
    etiqueta_objetivodistribucion = "//div[contains(@id, 'valor_label_element')]"
    ayuda_grupopolitica = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_tipoobjetivo = "//div[contains(@id, 'tipoobjetivo_select')]"
    campo_objetivodistribucion = "//input[@type = 'text' and contains(@id, 'valor_element')]"
    btn_Guarda_grupos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    selecciona = "//span[text()='Modifica C']"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"
    btn_cerrar_ayuda_grupos = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[1]/div/span[4]" 
    btn_cerrar_modal_grupos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    btn_cerrar_ayuda = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    
    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )