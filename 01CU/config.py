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

    Icodigo = "CódigoTest"
    Icodigousuario = "CódigoTest"
    Idescripcion = "Prueba automatizada para la descripción de cuentas contables"
    Mcodigousuario = "CambioTest"
    Mdescripcion = "Prueba automatizada para la modificacio de cuentas contables"
    Iobservacion1 = "Prueba automatizada para la observación de cuentas contables"
    Iobservacion2 = "Prueba automatizada para la observación de cuentas contables"
    Iobservacion3 = "Prueba automatizada para la observación de cuentas contables"
    Mobservacion1 = "Prueba automatizada para la modificacio de cuentas contables"
    Mobservacion2 = "Prueba automatizada para la modificacio de cuentas contables"
    Mobservacion3 = "Prueba automatizada para la modificacio de cuentas contables"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Cuentas Contables']"
    Iopcionbuscador = "Cuentas Contables"

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

    etiqueta_codigo = "//div[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigo_usuario = "//div[contains(@id, 'codigousuario_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_tipomoneda = "//div[contains(@id, 'tipomoneda_label_element')]"
    etiqueta_perdidas = "//div[contains(@id, 'cuentapedidaportipocambio_label_element')]"
    etiqueta_ganancias = "//div[contains(@id, 'cuentagananciaportipocambio_label_element')]"
    etiqueta_clasificacion = "//div[contains(@id, 'clasificacion_label_element')]"
    etiqueta_ignorarajuste = "//label[contains(@id, 'ignorarajustextipocambio_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_tipomoneda = "//div[contains(@id, 'tipomoneda_select')]"
    ayuda_perdidas = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-lookup/span[1]"
    ayuda_ganancias = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-lookup/span[1]"
    ayuda_clasificacion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-lookup/span[1]"
    campo_ignorarajuste = "//input[@type = 'checkbox' and contains(@id, 'ignorarajustextipocambio_checkbox')]"

    btn_observaciones = "//button[contains(@id, 'Observaciones_tabitem')]"
    etiqueta_observacion1 = "//div[contains(@id, 'obs1_label_element')]"
    etiqueta_observacion2 = "//div[contains(@id, 'obs2_label_element')]"
    etiqueta_observacion3 = "//div[contains(@id, 'obs3_label_element')]"
    campo_observaciones1 = "//input[@type = 'text' and contains(@id, 'obs1_element')]"
    campo_observaciones2 = "//input[@type = 'text' and contains(@id, 'obs2_element')]"
    campo_observaciones3 = "//input[@type = 'text' and contains(@id, 'obs3_element')]"

    btn_gruposcc = "//button[contains(@id, 'GrupoCentroCosto_tabitem')]"
    btn_Nuevo_gruposcc = "//div[contains(@id, 'add_gruposcentrocosto_element')]"
    btn_Elimina_gruposcc = "//div[contains(@id, 'remove_gruposcentrocosto_element')]"
    etiqueta_gruposcc = "//div[contains(@id, 'gr_label_element')]"
    ayuda_gruposcc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
    btn_Guarda_gruposcc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_prorrateos = "//button[contains(@id, 'Prorrateos_tabitem')]"
    btn_Nuevo_prorrateos = "//div[contains(@id, 'add_prorrateos_element')]"
    btn_Elimina_prorrateos = "//div[contains(@id, 'remove_prorrateos_element')]"
    etiqueta_prorrateos = "//div[contains(@id, 'prorrateo_label_element')]"
    ayuda_prorrateos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    etiqueta_defecto = "//label[contains(@id, 'defecto_label')]"
    campo_defecto = "//input[@type = 'checkbox' and contains(@id, 'defecto_checkbox')]"
    btn_Guarda_prorrateos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

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
