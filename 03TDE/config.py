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

    Icodigo = "PM00001"
    Icodigoalter = "Codigoalter1"
    Idescripcion = "Es una Prueba Automatizada?"
    Mcodigoalter = "Cambioalter1"
    Mdescripcion = "Es Prueba Cambio Automatizado?"

    Icodigores = "RE01"
    Iorden = "1"
    Idescripcionres = "SI"
    Icodigores2 = "RE02"
    Iorden2 = "2"
    Idescripcionres2 = "NO"
    Icodigores3 = "RE03"
    Iorden3 = "3"
    Idescripcionres3 = "TALVEZ"

    Mdescripcionres = "SI ES"
    Mdescripcionres2 = "NO ES"
    Mdescripcionres3 = "PUEDE SER"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Tipos Encuestas']"
    Iopcionbuscador = "Tipos Encuestas"

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

    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_codigoalter = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_tipo = "//div[contains(@id, 'tipo_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigoalter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_tipo = "//div[contains(@id, 'tipo_select')]"

    btn_respuestas = "//button[contains(@id, 'Respuestas_tabitem')]"
    btn_Nuevo_respuesta = "//div[contains(@id, 'add_respuestas_element')]"
    btn_Elimina_respuesta = "//div[contains(@id, 'remove_respuestas_element')]"
    etiqueta_codigores = "//div[contains(@id, 'id_label_element')]"
    etiqueta_orden = "//div[contains(@id, 'orden_label_element')]"
    etiqueta_descripcionres = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_finencuesta = "//label[contains(@id, 'finalizaencuesta_label')]"
    campo_codigores = "//input[@type = 'text' and contains(@id, 'id_element')]"
    campo_orden = "//input[@type = 'text' and contains(@id, 'orden_element')]"
    campo_descripcionres = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input"
    campo_finencuesta = "//input[@type = 'checkbox' and contains(@id, 'finalizaencuesta_checkbox')]"
    btn_Guarda_respuesta = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
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
