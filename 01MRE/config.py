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

    #pestaña general

    Icodigo = "CódigoTest"
    Icodigoalter = "CódigoTest"
    Idescripcion = "Prueba Automatizada"
    Mcodigoalter = "CódigoTest"
    Mdescripcion = "Prueba Cambio AutomatizadoM"

    #pestaña respuestas
    Rcodigo = "CódigoTest"
    Rorden = "2"
    Rdescripcion = "Prueba Automatizada"
    Rpeso = "5"
    RMcodigo = "CódigoTest"
    RMorden = "1"
    RMdescripcion = "Prueba Cambio Automatizado"
    RMpeso = "7"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Modelos de respuesta']"
    Iopcionbuscador = "Modelos de respuesta"

    #Agregar, modificar y eliminar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@id, 'save_element')]"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_acepta_eliminar = "//button[text()='Aceptar']"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "//button[text()='Cerrar']"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigoalter = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigoalter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    etiqueta_codigousuario = "//div[contains(@id, 'codigousuario_label_element')]"
    selecciona = "//span[text()='Modifica C']"

    #cambio de pestaña respuestas

    btn_respuestas = "//button[contains(@id, 'Respuestas_tabitem')]"
    btn_Nuevo_respuestas = "//div[contains(@id, 'add_Respuestas_element')]"
    btn_Elimina_respuestas = "//div[contains(@id, 'remove_Respuestas_element')]"
    btn_guardarrespuestas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    # pestaña respuestas

    etiqueta_rcodigo = "//div[contains(@id, 'id_label_element')]"
    etiqueta_orden = "//div[contains(@id, 'orden_label_element')]"
    etiqueta_rdescripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_peso = "//div[contains(@id, 'peso_label_element')]"
    campo_rcodigo = "//input[@type = 'text' and contains(@id, 'id_element')]"
    campo_rorden = "//input[@type = 'text' and contains(@id, 'orden_element')]"
    campo_rdescripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_rpeso = "//input[@type = 'text' and contains(@id, 'peso_element')]"
    etiqueta_finalizarencuentas = "//div[contains(@id, 'finalizaencuesta_label')]"
    campo_checkfinalizarencuestas = "//input[@type = 'checkbox' and contains(@id, 'finalizaencuesta_checkbox')]"
    btn_guarda_respuestas  = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"
    btn_cerrar_menu = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )