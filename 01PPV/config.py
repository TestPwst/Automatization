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

    Icodigo = "CodigoTest"
    Idescripcion = "Prueba Automatizada"
    Iobservaciones = "Prueba Automatizada"
    Mdescripcion = "Prueba Cambio Automatizado"
    Mobservaciones = "Prueba Cambio Automatizado"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Programación de Políticas de Venta']"
    Iopcionbuscador = "Programación de Políticas de Venta"

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
    etiqueta_ejecutarcuando = "//div[contains(@id, 'ejecutarcuando_label_element')]"
    etiqueta_asignara = "//div[contains(@id, 'asignar_label_element')]"
    etiqueta_aplicarfiltros = "//div[contains(@id, 'filtrarpor_label_element')]"
    etiqueta_politicaventa = "//div[contains(@id, 'politicaventa_label_element')]"
    etiqueta_observaciones = "//div[contains(@id, 'observaciones_label_element')]"
    etiqueta_ejecutargenerar = "//label[contains(@id, 'execgenerar_label')]"
    etiqueta_ejecutareliminar = "//label[contains(@id, 'execeliminar_label')]"
    etiqueta_activa = "//label[contains(@id, 'activo_label')]"

    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_ejecutarcuando = "//div[contains(@id, 'ejecutarcuando_select')]"
    campo_asignara = "//div[contains(@id, 'asignar_select')]"
    campo_aplicarfiltros = "//div[contains(@id, 'filtrarpor_select')]"
    ayuda_politicaventa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span[2]/ui-lookup/span[1]"
    campo_observaciones = "//input[@type = 'text' and contains(@id, 'observaciones_element')]"
    campo_ejecutargenerar = "//input[@type = 'checkbox' and contains(@id, 'execgenerar_checkbox')]"
    campo_ejecutareliminar = "//input[@type = 'checkbox' and contains(@id, 'execeliminar_checkbox')]"
    campo_activa = "//input[@type = 'checkbox' and contains(@id, 'activo_checkbox')]"
    selecciona = "//span[text()='Modifica C']"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_cerrar_ayuda = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
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