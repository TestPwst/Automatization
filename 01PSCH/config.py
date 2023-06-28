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
    Iqueryvariables = "Prueba Automatizada"
    Inombresalida = "Prueba Automatizada"
    Ipassword = "Constrasena123"

    Mdescripcion = "Prueba Cambio Automatizado"
    Mqueryvariables = "Prueba Cambio Automatizado"
    Mnombresalida = "Prueba Cambio Automatizado"
    Mpassword = "Constrasena12345"

    # IDS Y XPATH

    # Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Programas']"
    Iopcionbuscador = "Programas"

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
    etiqueta_queryvariables = "//div[contains(@id, 'queryvariables_label_element')]"
    etiqueta_nombresalida = "//div[contains(@id, 'nombresalida_label_element')]"
    etiqueta_comprimir = "//label[contains(@id, 'comprimir_label')]"
    etiqueta_formato = "//div[contains(@id, 'formato_label_element')]"
    etiqueta_usuario = "//div[contains(@id, 'usuario_label_element')]"
    etiqueta_password = "//div[contains(@id, 'passwd_label_element')]"
    etiqueta_activa = "//label[contains(@id, 'activo_label')]"
    etiqueta_ejecutar = "//div[contains(@id, 'ejecutar_label_element')]"

    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_queryvariables = "//textarea[contains(@id, 'queryvariables_element')]"
    campo_nombresalida = "//textarea[contains(@id, 'nombresalida_element')]"
    campo_comprimir = "//input[@type = 'checkbox' and contains(@id, 'comprimir_checkbox')]"
    campo_formato = "//div[contains(@id, 'formato_select')]"
    ayuda_usuario = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span/ui-container/ui-row[7]/ui-lookup/span[1]"
    campo_password = "//input[@type = 'password' and contains(@id, 'passwd_element')]"
    campo_activa = "//input[@type = 'checkbox' and contains(@id, 'activo_checkbox')]"
    campo_ejecutar = "//div[contains(@id, 'ejecutar_select')]"

    selecciona = "//span[text()='Modifica C']"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"
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