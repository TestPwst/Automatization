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

    Icodigo = "20"
    Idescripcion = "Prueba - Todas las Rutas"
    Iintervalolectura = "5"
    Itipodocdefault = "PM03"
    Mtipodocdefault = "PM04"
    Mdescripcion = "Prueba Cambio - Una Ruta"

    Iarticulo1 = "FA01001"
    Iarticulo2 = "FA01002"
    Iarticulo3 = "FA01003"
    Iarticulo4 = "FA01004"
    Iarticulo5 = "FA01005"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Perfiles móviles']"
    Iopcionbuscador = "Perfiles móviles"

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

    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_cargarrutas = "//div[contains(@id, 'rutas_label_element')]"
    etiqueta_tipodocdefault = "//div[contains(@id, 'tipodocumentodefault_label_element')]"
    etiqueta_modocargaliq = "//div[contains(@id, 'modocargaliquidacion_label_element')]"
    etiqueta_mododescargahh = "//div[contains(@id, 'mododescargahh_label_element')]"
    etiqueta_modopdv = "//label[contains(@id, 'modopdv_label')]"
    etiqueta_regcoordenadasgps = "//label[contains(@id, 'registrarcoordenadasgps_label')]"
    etiqueta_finautovisita = "//div[contains(@id, 'pdvfinauto_label_element')]"
    etiqueta_intervalolectura = "//div[contains(@id, 'intervaloregistrogps_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_cargarrutas = "//div[contains(@id, 'rutas_select')]"
    campo_tipodocdefault1 = "//input[@type = 'text' and contains(@id, 'tipodocumentodefault_element')]"
    campo_tipodocdefault2 = "//div[contains(@id, 'modotipodocumentodefault_select')]"
    campo_modocargaliq = "//div[contains(@id, 'modocargaliquidacion_select')]"
    campo_mododescargahh = "//div[contains(@id, 'mododescargahh_select')]"
    campo_modopdv = "//input[@type = 'checkbox' and contains(@id, 'modopdv_checkbox')]"
    campo_regcoordenadasgps = "//input[@type = 'checkbox' and contains(@id, 'registrarcoordenadasgps_checkbox')]"
    campo_finautovisita = "//div[contains(@id, 'pdvfinauto_select')]"
    campo_intervalolectura = "//input[@type = 'text' and contains(@id, 'intervaloregistrogps_element')]"

    btn_varios = "//button[contains(@id, 'Varios_tabitem')]"
    etiqueta_cargaresumenctasu = "//label[contains(@id, 'cargarresumen_label')]"
    etiqueta_verificarlimcredito = "//label[contains(@id, 'verificarlimitecredito_label')]"
    etiqueta_verificaropcguardar = "//label[contains(@id, 'verificarguardarcomo_label')]"
    etiqueta_permitirpagos = "//label[contains(@id, 'pagosacuentaencancelac_label')]"
    etiqueta_discodedatos = "//div[contains(@id, 'discoinformacion_label_element')]"
    etiqueta_tipovendedor = "//div[contains(@id, 'tipovendedor_label_element')]"
    etiqueta_enviardocumentos = "//label[contains(@id, 'enviardocumentoinmediato_label')]"
    campo_cargaresumenctasu = "//input[@type = 'checkbox' and contains(@id, 'cargarresumen_checkbox')]"
    campo_verificarlimcredito = "//input[@type = 'checkbox' and contains(@id, 'verificarlimitecredito_checkbox')]"
    campo_verificaropcguardar = "//input[@type = 'checkbox' and contains(@id, 'verificarguardarcomo_checkbox')]"
    campo_permitirpagos = "//input[@type = 'checkbox' and contains(@id, 'pagosacuentaencancelac_checkbox')]"
    campo_discodedatos = "//div[contains(@id, 'discoinformacion_select')]"
    campo_tipovendedor = "//div[contains(@id, 'tipovendedor_select')]"
    campo_enviardocumentos = "//input[@type = 'checkbox' and contains(@id, 'enviardocumentoinmediato_checkbox')]"

    btn_permisos = "//button[contains(@id, 'Permisos_tabitem')]"
    btn_Nuevo_permiso = "//div[contains(@id, 'add_permisos_element')]"
    btn_Elimina_permiso = "//div[contains(@id, 'remove_permisos_element')]"
    etiqueta_permisos = "//div[contains(@id, 'permisoscombo_label_element')]"
    campo_permisos = "//div[contains(@id, 'permisoscombo_select')]"
    btn_Guarda_permiso = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_lineasnegocio = "//button[contains(@id, 'LineasNegocio_tabitem')]"
    btn_Nuevo_lineanegocio = "//div[contains(@id, 'add_LineasNegocio_element')]"
    btn_Elimina_lineanegocio = "//div[contains(@id, 'remove_LineasNegocio_element')]"
    etiqueta_lineanegocio = "//div[text()= 'Línea negocio' and contains(@id, 'codigo_label_element')]"
    ayuda_lineanegocio = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
    btn_Guarda_lineanegocio = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_impulsoventas = "//button[contains(@id, 'ImpulsoVentas_tabitem')]"
    btn_Nuevo_impulsoventa = "//div[contains(@id, 'add_articulosimpulso_element')]"
    btn_Elimina_impulsoventa = "//div[contains(@id, 'remove_articulosimpulso_element')]"
    etiqueta_articulo = "//div[contains(@id, 'articlookup_label_element')]"
    campo_articulo = "//input[@type = 'text' and contains(@id, 'articlookup_element')]"
    btn_Guarda_impulsoventas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_mantenclientes = "//button[contains(@id, 'MantenimientoClientes_tabitem')]"
    etiqueta_agregarclientes = "//label[contains(@id, 'permisocrearclientes_label')]"
    etiqueta_modificarclientes = "//label[contains(@id, 'permisomodificarclientes_label')]"
    etiqueta_rutareferencia = "//div[contains(@id, 'rutareferenciahh_label_element')]"
    campo_agregarclientes = "//input[@type = 'checkbox' and contains(@id, 'permisocrearclientes_checkbox')]"
    campo_modificarclientes = "//input[@type = 'checkbox' and contains(@id, 'permisomodificarclientes_checkbox')]"
    ayuda_rutareferencia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[2]/span/ui-lookup/span[1]"
    campo_clasif1 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[3]/div[1]/input"
    campo_clasif2 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[4]/div[1]/input"
    campo_clasif3 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[5]/div[1]/input"
    campo_colonia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[6]/div[1]/input"
    campo_codigopostal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[8]/div[1]/input"
    campo_direccion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[10]/div[1]/input"
    campo_entornopdv = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[11]/div[1]/input"
    campo_esquina1 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[12]/div[1]/input"
    campo_esquina2 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[13]/div[1]/input"
    campo_estadoexhibidor = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[14]/div[1]/input"
    campo_nombre = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[17]/div[1]/input"
    campo_telefono1 = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[20]/div[1]/input"
    campo_paisdepartamento = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[20]/div[1]/input"
    campo_razonsocial = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[21]/div[1]/input"
    campo_ruc = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[1]/div/div/div[2]/div/div[22]/div[1]/input"
    campo_paises = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[1]/div[1]/input"
    campo_departamento = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[2]/div[1]/input"
    campo_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[3]/div[1]/input"
    campo_tipoexc = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[13]/div[1]/input"
    campo_credcomp = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[14]/div[1]/input"
    campo_entpdv = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[15]/div[1]/input"
    campo_estexhib = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[4]/span/ui-listview[2]/div/div/div[2]/div/div[16]/div[1]/input"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
