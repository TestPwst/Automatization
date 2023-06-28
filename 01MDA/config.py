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
    Icodigoalter = "CódigoTest"
    Idescripcion = "Prueba Automatizada"
    Mcodigoalter = "CambioTest"
    Mdescripcion = "Prueba Cambio AutomatizadoM"
    Indicesalario = "30"
    IncrementoIPC = "50"
    Variaciondolar = "20"
    VIPCInicial = "5"
    VIPCFinal = "5"
    VIMSInicial = "5"
    VIMSFinal = "5"
    TCInicial = "5"
    TCFinal = "5"
    Porcentaje = "7"
    MIndicesalario = "40"
    MIncrementoIPC = "50"
    MVariaciondolar = "10"
    MVIPCInicial = "7"
    MVIPCFinal = "7"
    MVIMSInicial = "7"
    MVIMSFinal = "7"
    MTCInicial = "7"
    MTCFinal = "7"
    MPorcentaje = "10"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Modelos de ajustes']"
    Iopcionbuscador = "Modelos de ajustes"

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

    #pantalla general

    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    campo_codigoalter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    etiqueta_codigoalter = "//div[contains(@id, 'codigoak_label_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    campo_indicesalario = "//input[@type = 'text' and contains(@id, 'indicemediosalario_element')]"
    etiqueta_indicesalario = "//div[contains(@id, 'indicemediosalario_label_element')]"
    campo_incrementoipc = "//input[@type = 'text' and contains(@id, 'ipc_element')]"
    etiqueta_incrementoipc = "//div[contains(@id, 'ipc_label_element')]"
    campo_variaciondolar = "//input[@type = 'text' and contains(@id, 'valordolar_element')]"
    etiqueta_variaciondolar = "//div[contains(@id, 'valordolar_label_element')]"

    #pestaña ajustes

    btn_ajustes = "//button[contains(@id, 'ajustes_tabitem')]"
    ayuda_fecha = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-datebox/span"
    fecha_hoy = "/html/body/div[7]/div[3]/div/button"
    ayuda_fecha2 = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-datebox/span"
    fecha_hoy2 = "/html/body/div[8]/div[3]/div/button"
    ayuda_fecha3 = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-datebox/span"
    fecha_hoy3 = "/html/body/div[9]/div[3]/div/button"
    btn_Guarda_ajustes = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_nuevo_ajustes = "//div[contains(@id, 'add_ajustes_element')]"
    btn_eliminarajustes = "//div[contains(@id, 'remove_ajustes_element')]"
    campo_VIPCInicialajuste = "//input[@type = 'text' and contains(@id, 'vipcinicial_element')]"
    etiqueta_VIPCInicialajuste = "//div[contains(@id, 'vipcinicial_label_element')]"
    campo_VIPCFinalajuste = "//input[@type = 'text' and contains(@id, 'vipcfinal_element')]"
    etiqueta_VIPCFinalajuste = "//div[contains(@id, 'vipcfinal_label_element')]"
    campo_VIMSInicialajuste = "//input[@type = 'text' and contains(@id, 'vimsinicial_element')]"
    etiqueta_VIMSInicialajuste = "//div[contains(@id, 'vimsinicial_label_element')]"
    campo_VIMSFinalajuste = "//input[@type = 'text' and contains(@id, 'vimsfinal_element')]"
    etiqueta_VIMSFinalajuste = "//div[contains(@id, 'vimsfinal_label_element')]"
    campo_TCInicialajuste = "//input[@type = 'text' and contains(@id, 'tcinicial_element')]"
    etiqueta_TCInicialajuste = "//div[contains(@id, 'tcinicial_label_element')]"
    campo_TCFinalajuste = "//input[@type = 'text' and contains(@id, 'tcfinal_element')]"
    etiqueta_TCFinalajuste = "//div[contains(@id, 'tcfinal_label_element')]"
    campo_Porcentajeajuste = "//input[@type = 'text' and contains(@id, 'porcentaje_element')]"
    etiqueta_Porcentajeajuste = "//div[contains(@id, 'porcentaje_label_element')]"
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