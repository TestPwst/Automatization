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

    Icodigo = "100"
    Icodigoalter = "Codigoalt1"
    Idescripcion = "Prueba automatizada"
    Iviviendas = "200"
    Ihogares = "100"
    Ihombres = "50"
    Imujeres = "50"
    Iptotal = "100"
    Icodigoiso = "MX"
    Mcodigoalter = "Cambioalt1"
    Mdescripcion = "Prueba Modifica "
    Mviviendas = "300"
    Mhogares = "150"
    Mhombres = "75"
    Mmujeres = "75"
    Mptotal = "150"
    Mcodigoiso = "BR"

    Icodigodep = "101"
    Icodigoalterdep = "Codigoalt2"
    Idescripciondep = "Departamentos"
    Iviviendasdep = "200"
    Ihogaresdep = "100"
    Ihombresdep = "50"
    Imujeresdep = "50"
    Iptotaldep = "100"
    Mcodigoalterdep = "Cambioalt2"
    Mdescripciondep = "Modificación"
    Mviviendasdep = "300"
    Mhogaresdep = "150"
    Mhombresdep = "75"
    Mmujeresdep = "75"
    Mptotaldep = "150"

    Icodigoloc = "102"
    Icodigoalterloc = "Codigoalt3"
    Idescripcionloc = "automatizada"
    Iviviendasloc = "200"
    Ihogaresloc = "100"
    Ihombresloc = "50"
    Imujeresloc = "50"
    Iptotalloc = "100"
    Mcodigoalterloc = "Cambioalt3"
    Mdescripcionloc = "automatizada"
    Mviviendasloc = "300"
    Mhogaresloc = "150"
    Mhombresloc = "75"
    Mmujeresloc = "75"
    Mptotalloc = "150"

    Icodigobar = "103"
    Icodigoalterbar = "Codigoalt4"
    Idescripcionbar = "automatizada"
    Iviviendasbar = "200"
    Ihogaresbar = "100"
    Ihombresbar = "50"
    Imujeresbar = "50"
    Iptotalbar = "100"
    Mcodigoalterbar = "Cambioalt4"
    Mdescripcionbar = "Modificación"
    Mviviendasbar = "300"
    Mhogaresbar = "150"
    Mhombresbar = "75"
    Mmujeresbar = "75"
    Mptotalbar = "150"


    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Ubicaciones geográficas']"
    Iopcionbuscador = "Ubicaciones geográficas"

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
    etiqueta_alternativo = "//div[contains(@id, 'CodigoAlternativo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'Descripcion_label_element')]"
    etiqueta_viviendas = "//div[contains(@id, 'Viviendas_label_element')]"
    etiqueta_hogares = "//div[contains(@id, 'HogaresParticulares_label_element')]"
    etiqueta_poblacionhombres = "//div[contains(@id, 'Hombres_label_element')]"
    etiqueta_poblacionmujeres = "//div[contains(@id, 'Mujeres_label_element')]"
    etiqueta_poblaciontotal = "//div[contains(@id, 'PoblacionTotal_label_element')]"
    etiqueta_codigoiso = "//div[contains(@id, 'CodigoISO3166_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_alternativo = "//input[@type = 'text' and contains(@id, 'CodigoAlternativo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_viviendas = "//input[@type = 'text' and contains(@id, 'Viviendas_element')]"
    campo_hogares = "//input[@type = 'text' and contains(@id, 'HogaresParticulares_element')]"
    campo_poblacionhombres = "//input[@type = 'text' and contains(@id, 'Hombres_element')]"
    campo_poblacionmujeres = "//input[@type = 'text' and contains(@id, 'Mujeres_element')]"
    campo_poblaciontotal = "//input[@type = 'text' and contains(@id, 'PoblacionTotal_element')]"
    campo_codigoiso = "//input[@type = 'text' and contains(@id, 'CodigoISO3166_element')]"
    buscar_registro ="//div[text()='Código']"

    btn_departamentos = "//button[contains(@id, 'Departamentos_tabitem')]"
    btn_Nuevo_departamento = "//div[contains(@id, 'add_Departamentos_element')]"
    btn_Elimina_departamento = "//div[contains(@id, 'remove_Departamentos_element')]"
    etiqueta_codigodep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-label/div"
    etiqueta_alternativodep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-label/div"
    etiqueta_descripciondep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_impuestodep = "//div[contains(@id, 'impuesto_label_element')]"
    etiqueta_viviendasdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_hogaresdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_poblacionhombresdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_poblacionmujeresdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-label/div"
    etiqueta_poblaciontotaldep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/ui-label/div"
    campo_codigodep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-numericbox/input"
    campo_alternativodep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-textbox/input"
    campo_descripciondep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input"
    ayuda_impuestodep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-lookup/span[1]"
    campo_viviendasdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-numericbox/input"
    campo_hogaresdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-numericbox/input"
    campo_poblacionhombresdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-numericbox/input"
    campo_poblacionmujeresdep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-numericbox/input"
    campo_poblaciontotaldep = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/ui-numericbox/input"
    btn_Guarda_departamentos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_localidades = "//button[contains(@id, 'Localidades_tabitem')]"
    btn_Nuevo_localidades = "//div[contains(@id, 'add_Localidades_element')]"
    btn_Elimina_localidades = "//div[contains(@id, 'remove_Localidades_element')]"
    etiqueta_localidad = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-label/div"
    etiqueta_alternativoloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-label/div"
    etiqueta_descripcionloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_viviendasloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-label/div"
    etiqueta_hogaresloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_poblacionhombresloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_poblacionmujeresloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_poblaciontotalloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-label/div"
    campo_codigoloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-numericbox/input"
    campo_alternativoloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-textbox/input"
    campo_descripcionloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input"
    campo_viviendasloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-numericbox/input"
    campo_hogaresloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-numericbox/input"
    campo_poblacionhombresloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-numericbox/input"
    campo_poblacionmujeresloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-numericbox/input"
    campo_poblaciontotalloc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-numericbox/input"
    btn_Guarda_localidades = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_barrios = "//button[contains(@id, 'Barrios_tabitem')]"
    btn_Nuevo_barrios = "//div[contains(@id, 'add_Barrios_element')]"
    btn_Elimina_barrios = "//div[contains(@id, 'remove_Barrios_element')]"
    etiqueta_codigobar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-label/div"
    etiqueta_alternativobar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-label/div"
    etiqueta_descripcionbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_viviendasbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-label/div"
    etiqueta_hogaresbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_poblacionhombresbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_poblacionmujeresbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_poblaciontotalbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-label/div"
    campo_codigobar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-numericbox/input"
    campo_alternativobar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-textbox/input"
    campo_descripcionbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input"
    campo_viviendasbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/ui-numericbox/input"
    campo_hogaresbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/ui-numericbox/input"
    campo_poblacionhombresbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/ui-numericbox/input"
    campo_poblacionmujeresbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/ui-numericbox/input"
    campo_poblaciontotalbar = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/ui-numericbox/input"
    btn_Guarda_barrios = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_impuestoarticulo = "//button[contains(@id, 'impuestoArticulos_tabitem')]"
    btn_Nuevo_impuestoarticulo = "//div[contains(@id, 'add_impuestosxarticulo_element')]"
    btn_Elimina_impuestoarticulo = "//div[contains(@id, 'remove_impuestosxarticulo_element')]"
    etiqueta_articulo = "//div[contains(@id, 'articulo_label_element')]"
    etiqueta_impuestoart = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-label/div"
    ayuda_articulo = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_impuestoart = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    btn_Guarda_impuestoarticulo = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    selecciona = "//span[text()='Modifica C']"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"
    btn_cerrar_barrios = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[1]/div/span[4]"
    btn_cerrar_localidades = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[1]/div/span[4]"
    btn_cerrar_departamentos = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )