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

    Icodigo = "2021"
    Idescripcion = "Prueba automatizada del campo descripción Empresas"
    Icodigoalter = "Codigoalt1"
    Icodigogln = "Codigogln1"
    Irazonsocial = "Razón Social Prueba"
    Icalle = "Calle prueba automatizada"
    Inropuerta = "21"
    Iesquina1 = "Esquina 1 prueba"
    Iesquina2 = "Esquina 2 prueba"
    Itelefono1 = "5530112223"
    Itelefono2 = "5510200309"
    Iruc = "Prueba RUC"
    Iobservaciones = "Prueba automatizada del campo observaciones"
    Mdescripcion = "Prueba de la Modificación del campo descripción Empresass"
    Mcodigoalter = "Cambioalt1"
    Mcodigogln = "Cambiogln1"
    Mrazonsocial = "Razón Social Prueba Modificación"
    Mcalle = "Calle prueba modificación"
    Mnropuerta = "10"
    Mesquina1 = "Esquina 1 cambio"
    Mesquina2 = "Esquina 2 cambio"
    Mtelefono1 = "5505240821"
    Mtelefono2 = "5502080933"
    Mruc = "Prueba Cambio RUC"
    Mobservaciones = "Prueba automatizada de la modificación del campo observaciones"

    Icodigoserie = "20"
    Idescripcionserie = "Prueba Automatizada Serie"
    Icodigoalterserie = "20"
    Mdescripcionserie = "Prueba Cambio Automatizado Serie"
    Mcodigoalterserie = "Cambioseri"

    Itipodocvias = "PM03"
    Iviasback = "1"
    Iviasmobile = "1"
    Idescripcionvias = "1.ORIGINAL"
    Mtipodocvias = "PM03"
    Mviasback = "0"
    Mviasmobile = "1"
    Mdescripcionvias = "1.Original;2.Copia"

    Ifechaauthfin = "31-12-2030"
    Inroresolfiscal = "21302024"
    Irangoinicio = "1"
    Irangofin = "1000"
    Mfechaauthfin = "31-12-2031"

    Ifechadesde = "01-01-2021"
    Ifechahasta = "31-12-2030"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Empresas']"
    Iopcionbuscador = "Empresas"

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
    etiqueta_descripcion = "//div[contains(@id, 'nombre_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_codigo_gln = "//div[contains(@id, 'codigogln_label_element')]"
    etiqueta_razonsocial = "//div[contains(@id, 'razon_label_element')]"
    etiqueta_calle = "//div[contains(@id, 'direccion_label_element')]"
    etiqueta_nropuerta = "//div[contains(@id, 'nropuerta_label_element')]"
    etiqueta_esquinas = "//div[contains(@id, 'esquina_label_element')]"
    etiqueta_telefonos = "//div[contains(@id, 'telefono1_label_element')]"
    etiqueta_ruc = "//div[contains(@id, 'ruc_label_element')]"
    etiqueta_estado = "//div[contains(@id, 'pais_label_element')]"
    etiqueta_deptoprovi = "//div[contains(@id, 'departamento_label_element')]"
    etiqueta_localidad = "//div[contains(@id, 'localidad_label_element')]"
    etiqueta_barrio = "//div[contains(@id, 'barrio_label_element')]"
    etiqueta_observaciones = "//div[contains(@id, 'observaciones_label_element')]"
    etiqueta_resolfiscales = "//label[contains(@id, 'resolucionfiscal_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'nombre_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_codigo_gln = "//input[@type = 'text' and contains(@id, 'codigogln_element')]"
    campo_razonsocial = "//input[@type = 'text' and contains(@id, 'razon_element')]"
    campo_calle = "//input[@type = 'text' and contains(@id, 'direccion_element')]"
    campo_nropuerta = "//input[@type = 'text' and contains(@id, 'nropuerta_element')]"
    campo_esquina1 = "//input[@type = 'text' and contains(@id, 'esquina_element')]"
    campo_esquina2 = "//input[@type = 'text' and contains(@id, 'esquina2_element')]"
    campo_telefono1 = "//input[@type = 'text' and contains(@id, 'telefono1_element')]"
    campo_telefono2 = "//input[@type = 'text' and contains(@id, 'telefono2_element')]"
    campo_ruc = "//input[@type = 'text' and contains(@id, 'ruc_element')]"
    ayuda_estado = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span[2]/ui-lookup/span[1]"
    ayuda_deptoprovi = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/span[2]/ui-lookup/span[1]"
    ayuda_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[11]/span[2]/ui-lookup/span[1]"
    ayuda_barrio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[12]/span[2]/ui-lookup/span[1]"
    campo_observaciones = "//input[@type = 'text' and contains(@id, 'observaciones_element')]"
    campo_resolfiscales = "//input[@type = 'checkbox' and contains(@id, 'resolucionfiscal_checkbox')]"

    btn_series = "//button[contains(@id, 'series_tabitem')]"
    btn_Nuevo_serie = "//div[contains(@id, 'add_series_element')]"
    btn_Elimina_serie = "//div[contains(@id, 'remove_series_element')]"
    etiqueta_codigoserie = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_descripcionserie = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_codigoalterserie = "//div[text()= 'Codigo alternativo' and contains(@id, 'codigoalternativo_label_element')]"
    campo_codigoserie = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcionserie = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_codigoalterserie = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-textbox/input"
    btn_Guarda_series = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_configvias = "//button[contains(@id, 'vias_tabitem')]"
    btn_Nuevo_via = "//div[contains(@id, 'add_vias_element')]"
    btn_Elimina_via = "//div[contains(@id, 'remove_vias_element')]"
    etiqueta_tipodocvias = "//div[contains(@id, 'tipodocumento_label_element')]"
    etiqueta_viasbackoffice = "//div[contains(@id, 'cantidadvias_label_element')]"
    etiqueta_viasmobile = "//div[contains(@id, 'cantidadviascolector_label_element')]"
    etiqueta_descripcionvias = "//div[contains(@id, 'descripcionvias_label_element')]"
    campo_tipodocvias = "//input[@type = 'text' and contains(@id, 'tipodocumento_element')]"
    campo_viasbackoffice = "//input[@type = 'text' and contains(@id, 'cantidadvias_element')]"
    campo_viasmobile = "//input[@type = 'text' and contains(@id, 'cantidadviascolector_element')]"
    campo_descripcionvias = "//input[@type = 'text' and contains(@id, 'descripcionvias_element')]"
    btn_Guarda_vias = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_calendario = "//button[contains(@id, 'Calelaborables_tabitem')]"
    etiqueta_lunes = "//div[contains(@id, 'lunes_label_element')]"
    etiqueta_martes = "//div[contains(@id, 'martes_label_element')]"
    etiqueta_miercoles = "//div[contains(@id, 'miercoles_label_element')]"
    etiqueta_jueves = "//div[contains(@id, 'jueves_label_element')]"
    etiqueta_viernes = "//div[contains(@id, 'viernes_label_element')]"
    etiqueta_sabado = "//div[contains(@id, 'sabado_label_element')]"
    etiqueta_domingo = "//div[contains(@id, 'domingo_label_element')]"
    campo_lunes = "//input[@type = 'checkbox' and contains(@id, 'lunes_checkbox')]"
    campo_martes = "//input[@type = 'checkbox' and contains(@id, 'martes_checkbox')]"
    campo_miercoles = "//input[@type = 'checkbox' and contains(@id, 'miercoles_checkbox')]"
    campo_jueves = "//input[@type = 'checkbox' and contains(@id, 'jueves_checkbox')]"
    campo_viernes = "//input[@type = 'checkbox' and contains(@id, 'viernes_checkbox')]"
    campo_sabado = "//input[@type = 'checkbox' and contains(@id, 'sabado_checkbox')]"
    campo_domingo = "//input[@type = 'checkbox' and contains(@id, 'domingo_checkbox')]"

    btn_resolfiscales = "//button[contains(@id, 'resoluciones_tabitem')]"
    btn_Nuevo_resolfiscales = "//div[contains(@id, 'add_resoluciones_element')]"
    btn_Elimina_resolfiscales = "//div[contains(@id, 'remove_resoluciones_element')]"
    etiqueta_fechaauth = "//div[contains(@id, 'fechaingreso_label_element')]"
    etiqueta_serie = "//div[contains(@id, 'serie_label_element')]"
    etiqueta_nroresolucion = "//div[text()= 'Nro. Resolución' and contains(@id, 'codigo_label_element')]"
    etiqueta_rangocorr = "//div[contains(@id, 'desdenumero_label_element')]"
    fechaauth_inicio = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span/ui-datebox[1]/span"
    campo_fechafinauth = "//input[@type = 'text' and contains(@id, 'fechavencimiento_element')]"
    ayuda_serie = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-lookup/span[1]"
    campo_nroresolucion = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span[2]/ui-textbox/input"
    campo_rangoinicio = "//input[@type = 'text' and contains(@id, 'desdenumero_element')]"
    campo_rangofin = "//input[@type = 'text' and contains(@id, 'hastanumero_element')]"
    btn_Guarda_resolfiscales = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_contabilidad = "//button[contains(@id, 'conta_tabitem')]"
    etiqueta_periodocontable = "//div[contains(@id, 'panelPeriodoContable_label_element')]"
    etiqueta_desde = "//div[contains(@id, 'fechaaperturaactual_label_element')]"
    etiqueta_hasta = "//div[contains(@id, 'fechacierreactual_label_element')]"
    campo_fechadesde = "//input[@type = 'text' and contains(@id, 'fechaaperturaactual_element')]"
    campo_fechahasta = "//input[@type = 'text' and contains(@id, 'fechacierreactual_element')]"
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
