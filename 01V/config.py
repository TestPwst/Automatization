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

    Icodigo = "VHCL021094"
    Idescripcion = "Esto es una prueba automatizada para validar PWST 2.0 vehicu"
    Imarca = "Validacion campo marca HONDA 1"
    Inumplaca = "Prueba para validar placa ML22"
    Inummotor = "Prueba para validar motor 2134"
    Inumchasis = "Prueba para validar chasis 123"
    Icaptoneladas = "10000"
    Icapkglts = "10000"
    Icapcajas = "10000"
    Imetroscubicos = "10000"
    Imaxvoldoc = "10000"
    Iminvoldoc = "10000"
    Imaxpesodoc = "10000"
    Iminpesodoc = "10000"
    Inummaxvisitas = "10000"

    Mdescripcion = "Esto es una modificacion para validar PWST 2.0 ventana vehic"
    Mmarca = "Validacion campo marca FORD 12"
    Mnumplaca = "Prueba para validar placa HT2"
    Mnummotor = "Prueba para validar motor 2.01"
    Mnumchasis = "Prueba para validar chasis 444"
    Mcaptoneladas = "11111"
    Mcapkglts = "11111"
    Mcapcajas = "11111"
    Mmetroscubicos = "11111"
    Mmaxvoldoc = "11111"
    Mminvoldoc = "11111"
    Mmaxpesodoc = "11111"
    Mminpesodoc = "11111"
    Mnummaxvisitas = "11111"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Vehiculos']"
    Iopcionbuscador = "Vehiculos"

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
    etiqueta_marca = "//div[contains(@id, 'Marca_label_element')]"
    etiqueta_numeroplaca = "//div[contains(@id, 'numeroplaca_label_element')]"
    etiqueta_numeromotor = "//div[contains(@id, 'numeromotor_label_element')]"
    etiqueta_numerochasis = "//div[contains(@id, 'numerochasis_label_element')]"
    etiqueta_captoneladas = "//div[contains(@id, 'capacidadcargatoneladas_label_element')]"
    etiqueta_capkglts = "//div[contains(@id, 'capacidadcargakglts_label_element')]"
    etiqueta_capcajas = "//div[contains(@id, 'capacidadcargacajas_label_element')]"
    etiqueta_metroscubicos = "//div[contains(@id, 'volumencargametroscubicos_label_element')]"
    etiqueta_maxvoldoc = "//div[contains(@id, 'volmaxdoc_label_element')]"
    etiqueta_minvoldoc = "//div[contains(@id, 'volmindoc_label_element')]"
    etiqueta_maxpesodoc = "//div[contains(@id, 'pesomaxdoc_label_element')]"
    etiqueta_minpesodoc = "//div[contains(@id, 'pesomindoc_label_element')]"
    etiqueta_nummaxvisitas = "//div[contains(@id, 'maxvisitas_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_marca = "//input[@type = 'text' and contains(@id, 'Marca_element')]"
    campo_numeroplaca = "//input[@type = 'text' and contains(@id, 'numeroplaca_element')]"
    campo_numeromotor = "//input[@type = 'text' and contains(@id, 'numeromotor_element')]"
    campo_numerochasis = "//input[@type = 'text' and contains(@id, 'numerochasis_element')]"
    campo_captoneladas = "//input[@type = 'text' and contains(@id, 'capacidadcargatoneladas_element')]"
    campo_capkglts = "//input[@type = 'text' and contains(@id, 'capacidadcargakglts_element')]"
    campo_capcajas = "//input[@type = 'text' and contains(@id, 'capacidadcargacajas_element')]"
    campo_metroscubicos = "//input[@type = 'text' and contains(@id, 'volumencargametroscubicos_element')]"
    campo_maxvoldoc = "//input[@type = 'text' and contains(@id, 'volmaxdoc_element')]"
    campo_minvoldoc = "//input[@type = 'text' and contains(@id, 'volmindoc_element')]"
    campo_maxpesodoc = "//input[@type = 'text' and contains(@id, 'pesomaxdoc_element')]"
    campo_minpesodoc = "//input[@type = 'text' and contains(@id, 'pesomindoc_element')]"
    campo_nummaxvisitas = "//input[@type = 'text' and contains(@id, 'maxvisitas_element')]"

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