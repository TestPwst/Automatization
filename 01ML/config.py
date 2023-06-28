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

    Icodigo = "3"
    Idescripcion = "Prueba automatizada para la validación del campo descripción en modelos de liquidación en PWST 2.0"
    Icantidaddias = "10000"
    Icantidadmaxima = "10000"
    Mdescripcion = "Prueba automatizada para la modificacio del campo descripción en modelos de liquidación en PWST 2.0"
    Mcantidaddias = "11111"
    Mcantidadmaxima = "11111"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Modelos de liquidación']"
    Iopcionbuscador = "Modelos de liquidación"

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
    etiqueta_cantidaddias = "//div[contains(@id, 'diasfechageneracion_label_element')]"
    etiqueta_cantidadmaxima = "//div[contains(@id, 'cantidadxvendedor_label_element')]"
    etiqueta_listaprecio = "//div[contains(@id, 'listapreciovalorizacion_label_element')]"
    etiqueta_codigomodelo = "//div[contains(@id, 'codigomodelocobranza_label_element')]"
    etiqueta_mostraradver = "//label[contains(@id, 'mostraradvertencias_label')]"
    etiqueta_cierreliqcargadefinitiva = "//label[contains(@id, 'cierreencarga_label')]"
    etiqueta_quitardocsliqcerrada = "//label[contains(@id, 'quitardocumentos_label')]"
    etiqueta_inhibiroperaciones = "//label[contains(@id, 'inhibiroperacionenliqcerrada_label')]"
    etiqueta_cierreliqvacias = "//label[contains(@id, 'permitircerrarliqvacia_label')]"
    etiqueta_inhibircarga = "//label[contains(@id, 'inhibircargasihayliqactivas_label')]"
    etiqueta_solicitarfechacierre = "//label[contains(@id, 'solicitarfechacierre_label')]"
    etiqueta_ignorarerrores = "//label[contains(@id, 'ignorarerrorescheques_label')]"
    etiqueta_desdefecha = "//div[contains(@id, 'vigenciapreciosdesde_label_element')]"
    etiqueta_hastafecha = "//div[contains(@id, 'vigenciaprecioshasta_label_element')]"
    etiqueta_fechavigencia = "//div[contains(@id, 'fechaprecioscarga_label_element')]"
    etiqueta_cargaprecios = "//div[contains(@id, 'cargardatoscantdiasantes_label_element')]"
    etiqueta_hasta = "//div[contains(@id, 'cargardatoscantidaddias_label_element')]"

    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_cantidaddias = "//input[@type = 'text' and contains(@id, 'diasfechageneracion_element')]"
    campo_cantidadmaxima = "//input[@type = 'text' and contains(@id, 'cantidadxvendedor_element')]"
    ayuda_listaprecio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span[2]/ui-lookup/span[1]"
    ayuda_codigomodelo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span[2]/ui-lookup/span[1]"
    campo_mostraradver = "//input[@type = 'checkbox' and contains(@id, 'mostraradvertencias_checkbox')]"
    campo_cierreliqcargadefinitiva = "//input[@type = 'checkbox' and contains(@id, 'cierreencarga_checkbox')]"
    campo_quitardocsliqcerrada = "//input[@type = 'checkbox' and contains(@id, 'quitardocumentos_checkbox')]"
    campo_inhibiroperaciones = "//input[@type = 'checkbox' and contains(@id, 'inhibiroperacionenliqcerrada_checkbox')]"
    campo_cierreliqvacias = "//input[@type = 'checkbox' and contains(@id, 'permitircerrarliqvacia_checkbox')]"
    campo_inhibircarga = "//input[@type = 'checkbox' and contains(@id, 'inhibircargasihayliqactivas_checkbox')]"
    campo_solicitarfechacierre = "//input[@type = 'checkbox' and contains(@id, 'solicitarfechacierre_checkbox')]"
    campo_ignorarerrores = "//input[@type = 'checkbox' and contains(@id, 'ignorarerrorescheques_checkbox')]"
    ayuda_fechadesde = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[2]/ui-datebox/span"
    ayuda_fechahasta = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[3]/ui-datebox/span"
    ayuda_fechavigencia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-container[2]/ui-row[4]/ui-datebox/span"
    campo_cargaprecios = "//div[contains(@id, 'cargardatoscantdiasantes_select')]"
    campo_hasta = "//div[contains(@id, 'cargardatoscantidaddias_select')]"
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