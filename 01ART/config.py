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

    Icodigointerno = "FA0102021"
    Icodigousuario = "FA0102021"
    Icodigoalter = "Codigoalter1"
    Idescripcion = "Prueba automatizada"
    Idescripcioncolector = "Prueba automatizada"
    Iliquidarcomo = "FA0102021"
    Icodigobarras = "24002021"
    Idiasvalidez = "20"
    Iunidadesxpacking = "10"
    Idecimalespacking = "2"
    Iuhf1 = "0.100"
    Iuhf2 = "0.100"
    Iuhf3 = "20"
    Iuhf4 = "1"
    Mcodigoalter = "Cambioalter1"
    Mdescripcion = "Prueba Cambio Automatizada"
    Mdescripcioncolector = "Prueba Cambio"
    Mdiasvalidez = "25"
    Munidadesxpacking = "1"
    Mdecimalespacking = "0"
    Mcodigobarras = "21001031"

    Idescripcionlp = "24002021"
    Mdescripcionlp = "21001031"
    Iobservacionlp = "FA030082.03|FA050308.03"

    Iimpuesto = "%prunit/10"
    Mimpuesto = "%prunit"

    Ifiltro = "FA0102021"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Artículos']"
    Iopcionbuscador = "Artículos"

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

    etiqueta_codigointerno = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_codigo_usuario = "//div[contains(@id, 'codigousuario_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_descripcioncolector = "//div[contains(@id, 'descripcion2_label_element')]"
    etiqueta_liquidarcomo = "//div[contains(@id, 'liquidarcomo_label_element')]"
    etiqueta_familia = "//div[contains(@id, 'familia_label_element')]"
    etiqueta_lineanegocio = "//div[contains(@id, 'lineanegocio_label_element')]"
    etiqueta_codigobarras = "//div[contains(@id, 'codigobarra_label_element')]"
    etiqueta_packing = "//div[contains(@id, 'tipoempaque_label_element')]"
    etiqueta_unidadnegocio = "//div[contains(@id, 'unidadnegocio_label_element')]"
    etiqueta_unidadventa = "//div[contains(@id, 'tipounidad_label_element')]"
    etiqueta_diasvalidez = "//div[contains(@id, 'validez_label_element')]"
    etiqueta_unidadesxpacking = "//div[contains(@id, 'unidadesporpacking_label_element')]"
    etiqueta_decimalespacking = "//div[contains(@id, 'decimalespacking_label_element')]"
    etiqueta_unidadeshomofact1 = "//div[contains(@id, 'unidades_label_element')]"
    etiqueta_unidadeshomofact2 = "//div[contains(@id, 'unidadeshomogeneas2_label_element')]"
    etiqueta_unidadeshomofact3 = "//div[contains(@id, 'unidadeshomogeneas3_label_element')]"
    etiqueta_unidadeshomofact4 = "//div[contains(@id, 'unidadeshomogeneas4_label_element')]"
    etiqueta_activo = "//label[contains(@id, 'activo_label')]"
    etiqueta_facturaxpacking = "//label[contains(@id, 'facturarxpacking_label')]"
    etiqueta_controllotes = "//label[contains(@id, 'controlarlotes_label')]"
    etiqueta_controlstock = "//label[contains(@id, 'controlarstock_label')]"
    campo_codigointerno = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_descripcioncolector = "//input[@type = 'text' and contains(@id, 'descripcion2_element')]"
    campo_liquidarcomo = "//input[@type = 'text' and contains(@id, 'liquidarcomo_element')]"
    ayuda_familia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-lookup[1]/span[1]"
    ayuda_lineanegocio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-lookup[2]/span[1]"
    campo_codigobarras = "//input[@type = 'text' and contains(@id, 'codigobarra_element')]"
    ayuda_unidadnegocio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup/span[1]"
    ayuda_packing = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[1]/span[1]"
    ayuda_unidadventa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[2]/span[1]"
    campo_diasvalidez = "//input[@type = 'text' and contains(@id, 'validez_element')]"
    campo_unidadesxpacking = "//input[@type = 'text' and contains(@id, 'unidadesporpacking_element')]"
    campo_decimalespacking = "//input[@type = 'text' and contains(@id, 'decimalespacking_element')]"
    campo_unidadeshomofact1 = "//input[@type = 'text' and contains(@id, 'unidades_element')]"
    campo_unidadeshomofact2 = "//input[@type = 'text' and contains(@id, 'unidadeshomogeneas2_element')]"
    campo_unidadeshomofact3 = "//input[@type = 'text' and contains(@id, 'unidadeshomogeneas3_element')]"
    campo_unidadeshomofact4 = "//input[@type = 'text' and contains(@id, 'unidadeshomogeneas4_element')]"
    campo_activo = "//input[@type = 'checkbox' and contains(@id, 'activo_checkbox')]"
    campo_facturaxpacking = "//input[@type = 'checkbox' and contains(@id, 'facturarxpacking_checkbox')]"
    campo_controllotes = "//input[@type = 'checkbox' and contains(@id, 'controlarlotes_checkbox')]"
    campo_controlstock = "//input[@type = 'checkbox' and contains(@id, 'controlarstock_checkbox')]"

    btn_listaprecios = "//button[contains(@id, 'listaprecios_tabitem')]"
    etiqueta_descripcionlp = "//div[contains(@id, 'descripcionlp_label_element')]"
    etiqueta_observacionlp = "//div[contains(@id, 'obselp_label_element')]"
    campo_descripcionlp = "//input[@type = 'text' and contains(@id, 'descripcionlp_element')]"
    campo_observacionlp = "//input[@type = 'text' and contains(@id, 'obselp_element')]"

    btn_impuestos = "//button[contains(@id, 'impuestos_tabitem')]"
    etiqueta_formulapu = "//div[contains(@id, 'formulapreciounitario_label_element')]"
    campo_formulapu = "//input[@type = 'text' and contains(@id, 'formulapreciounitario_element')]"
    btn_Nuevo_impuesto = "//div[contains(@id, 'add_impuestos_element')]"
    btn_Elimina_impuesto = "//div[contains(@id, 'remove_impuestos_element')]"
    etiqueta_fechavigencia = "//div[text() = 'Fecha de Vigencia' and contains( @ id, 'fecha_label_element')]"
    etiqueta_impuesto = "//div[text() = 'Impuesto' and contains( @ id, 'impuesto_label_element')]"
    ayuda_fechavigencia = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-datebox/span"
    ayuda_impuesto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    btn_Guarda_impuesto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_varios = "//button[contains(@id, 'varios_tabitem')]"
    etiqueta_clasifart1 = "//div[contains(@id, 'clasificacionarticulo_label_element')]"
    etiqueta_sabor = "//div[contains(@id, 'sabor_label_element')]"
    etiqueta_tipoarticulo = "//div[contains(@id, 'tipoproducto_label_element')]"
    ayuda_clasifart1 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[1]/span/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_sabor = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[1]/span/ui-container/ui-row[5]/ui-lookup/span[1]"
    ayuda_tipoarticulo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[1]/span/ui-container/ui-row[6]/ui-lookup/span[1]"

    btn_customproperties = "//button[contains(@id, 'customproperties_tabitem')]"
    campo_aguascalientes = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[1]/div[1]/input"
    campo_bajacalifornia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[2]/div[1]/input"
    campo_bajacaliforniasur = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[3]/div[1]/input"
    campo_campeche = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[4]/div[1]/input"
    campo_coahuila = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[5]/div[1]/input"
    campo_colima = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[6]/div[1]/input"
    campo_chiapas = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[7]/div[1]/input"
    campo_chihuahua = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[8]/div[1]/input"
    campo_df = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[9]/div[1]/input"
    campo_durango = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[10]/div[1]/input"
    campo_guanajuato = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[11]/div[1]/input"
    campo_guerrero = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[12]/div[1]/input"
    campo_hidalgo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[13]/div[1]/input"
    campo_jalisco = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[14]/div[1]/input"
    campo_mexico = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[15]/div[1]/input"
    campo_michoacan = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[16]/div[1]/input"
    campo_morelos = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[17]/div[1]/input"
    campo_nayarit = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[18]/div[1]/input"
    campo_nuevoleon = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[19]/div[1]/input"
    campo_oaxaca = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[20]/div[1]/input"
    campo_puebla = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[21]/div[1]/input"
    campo_queretaro = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[22]/div[1]/input"
    campo_quintanaroo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[23]/div[1]/input"
    campo_sanluis = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[24]/div[1]/input"
    campo_sinaloa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[25]/div[1]/input"
    campo_sonora = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[26]/div[1]/input"
    campo_tabasco = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[27]/div[1]/input"
    campo_tamaulipas = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[28]/div[1]/input"
    campo_tlaxcala = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[29]/div[1]/input"
    campo_veracruz = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[30]/div[1]/input"
    campo_yucatan = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[31]/div[1]/input"
    campo_zacatecas = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row/span/ui-listview/div/div/div[2]/div/div[32]/div[1]/input"

    filtros = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[2]/div/div[2]/div"
    filtro_codigoarticulo = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[19]/div/div[2]"

    etiqueta_codarticulo = "//div[text()= 'Código de artículo' and contains(@id, 'label_element')]"
    campo_codarticulo = "//input[@type = 'text' and contains(@id, 'control_element')]"
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
