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

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join("C:\chromedriver\chromedriver"))

    Icodigo = "CódigoTest"
    Idescripcion = "Prueba automatizada del campo descripción IE "
    Mdescripcion = "Prueba automatizada de la modificación del campo descripción IE "
    Iorden = "1"
    Morden = "2"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Instancias Encuestas']"
    Iopcionbuscador = "Instancias Encuestas"

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
    etiqueta_desdefecha = "//div[contains(@id, 'desdefecha_label_element')]"
    etiqueta_hastafecha = "//div[contains(@id, 'hastafecha_label_element')]"
    etiqueta_fechatope = "//div[contains(@id, 'fechatopemodificacion_label_element')]"
    etiqueta_grupoarticulos = "//div[contains(@id, 'grupopolitica_label_element')]"
    etiqueta_frecuencia = "//div[contains(@id, 'modofrecuencia_label_element')]"
    etiqueta_grupoentidades = "//div[contains(@id, 'grupoentidadesmp_label_element')]"
    etiqueta_obligatoria = "//label[contains(@id, 'obligatoria_label')]"
    etiqueta_noencuesta = "//label[contains(@id, 'nosolicitarmotivonoencuesta_label')]"
    etiqueta_agrupartipos = "//label[contains(@id, 'agrupartiposencuestaxmodelorespuestas_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    ayuda_desdefecha = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-datebox/span"
    ayuda_hastafecha = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-datebox/span"
    ayuda_fechatope = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-datebox/span"
    ayuda_grupoarticulos = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-lookup/span[1]"
    campo_frecuencia = "//div[contains(@id, 'modofrecuencia_select')]"
    ayuda_grupoentidades = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-lookup/span[1]"
    campo_obligatoria = "//input[@type = 'checkbox' and contains(@id, 'obligatoria_checkbox')]"
    campo_noencuesta = "//input[@type = 'checkbox' and contains(@id, 'nosolicitarmotivonoencuesta_checkbox')]"
    campo_agrupartipos = "//input[@type = 'checkbox' and contains(@id, 'agrupartiposencuestaxmodelorespuestas_checkbox')]"

    btn_tiposencuestas = "//button[contains(@id, 'tiposEncuentas_tabitem')]"
    btn_Nuevo_tipoencuesta = "//div[contains(@id, 'add_tiposencuesta_element')]"
    btn_Elimina_tipoencuesta = "//div[contains(@id, 'remove_tiposencuesta_element')]"
    etiqueta_tipoencuesta = "//div[contains(@id, 'tipoencuesta_label_element')]"
    etiqueta_orden = "//div[contains(@id, 'orden_label_element')]"
    ayuda_tipoencuesta = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_orden = "//input[@type = 'text' and contains(@id, 'orden_element')]"
    btn_Guarda_tipoencuestas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    selecciona = "//span[text()='Modifica C']"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_cerrar_ayuda = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[1]/div/span[4]"
    btn_cerrar_menu = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
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
