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

    Icodigo = "PM55"
    Icodigoalter = "PMPru"
    Idescripcion = "Documento Prueba Automatizada"
    Idescripcionimp = "Documento Prueba"
    Iclavecorr = "PM55"
    Mcodigoalter = "Cambioalt1"
    Mdescripcion = "Documento Prueba Cambio Automatizada"
    Mdescripcionimp = "Documento Prueba Cambio"

    Itipodocumentogd = "PM03"
    Mtipodocumentogd = "PM04"

    Itipodocumentocan = "PM04"

    Idescripcionccd = "Venta Credito  %s %n"

    # IDS Y XPATH

    # Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    # Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Tipos de documento']"
    Iopcionbuscador = "Tipos de documento"

    # Agregar, modificar y eliminar el registro
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

    btn_titulocodigo = "//div[text()='Código']"
    etiqueta_codigo = "//div[contains(@id, 'codigo_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_grupo = "//div[contains(@id, 'grupodocumento_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_descripcionimp = "//div[contains(@id, 'descripcionimpresion_label_element')]"
    etiqueta_tipovalorizacion = "//div[contains(@id, 'tipovalorizacion_label_element')]"
    etiqueta_impuesto = "//div[contains(@id, 'impuesto_label_element')]"
    etiqueta_clavecorr = "//div[contains(@id, 'clavecorr_label_element')]"
    etiqueta_tipodocumento = "//div[contains(@id, 'tipo_label_element')]"
    etiqueta_modeloimp = "//div[contains(@id, 'modeloimpresion_label_element')]"
    etiqueta_modeloimpmovil = "//div[contains(@id, 'modeloimpresionmovil_label_element')]"
    etiqueta_emitircuando = "//div[contains(@id, 'emitircuando_label_element')]"
    etiqueta_guardarcomo = "//div[contains(@id, 'siemprependiente_label_element')]"
    etiqueta_visiblemenu = "//label[contains(@id, 'menuvisible_label')]"
    etiqueta_conarticulos = "//label[contains(@id, 'articulos_label')]"
    etiqueta_aceptaformaspago = "//label[contains(@id, 'formaspago_label')]"
    etiqueta_anularhh = "//label[contains(@id, 'anularenhh_label')]"
    etiqueta_cambiofechaemision = "//label[contains(@id, 'cambiarfechaemision_label')]"
    etiqueta_cambioformapago = "//label[contains(@id, 'permitircambiarformapago_label')]"
    etiqueta_coordenadasgps = "//label[contains(@id, 'registrarcoordenadasgps_label')]"
    etiqueta_calendariocerrado = "//label[contains(@id, 'validarcalendariocerrado_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    ayuda_grupo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_descripcionimp = "//input[@type = 'text' and contains(@id, 'descripcionimpresion_element')]"
    campo_tipovalorizacion = "//div[contains(@id, 'tipovalorizacion_select')]"
    ayuda_impuesto = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[5]/ui-lookup/span[1]"
    campo_clavecorr = "//input[@type = 'text' and contains(@id, 'clavecorr_element')]"
    campo_tipodocumento = "//div[contains(@id, 'tipo_select')]"
    ayuda_modeloimp = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[10]/ui-lookup/span[1]"
    ayuda_modeloimpmovil = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[11]/ui-lookup/span[1]"
    campo_emitircuando = "//div[contains(@id, 'emitircuando_select')]"
    campo_guardarcomo = "//div[contains(@id, 'siemprependiente_select')]"
    campo_visiblemenu = "//input[@type = 'checkbox' and contains(@id, 'menuvisible_checkbox')]"
    campo_conarticulos = "//input[@type = 'checkbox' and contains(@id, 'articulos_checkbox')]"
    campo_aceptarformaspago = "//input[@type = 'checkbox' and contains(@id, 'formaspago_checkbox')]"
    campo_anularhh = "//input[@type = 'checkbox' and contains(@id, 'anularenhh_checkbox')]"
    campo_cambiofechaemision = "//input[@type = 'checkbox' and contains(@id, 'cambiarfechaemision_checkbox')]"
    campo_cambioformapago = "//input[@type = 'checkbox' and contains(@id, 'permitircambiarformapago_checkbox')]"
    campo_coordenadasgps = "//input[@type = 'checkbox' and contains(@id, 'registrarcoordenadasgps_checkbox')]"
    campo_calendariocerrado = "//input[@type = 'checkbox' and contains(@id, 'validarcalendariocerrado_checkbox')]"

    btn_comportamiento = "//button[contains(@id, 'comportamiento_tabitem')]"
    etiqueta_modoafectacion = "//div[contains(@id, 'stock_label_element')]"
    etiqueta_rubro = "//div[contains(@id, 'rubstock_label_element')]"
    etiqueta_modogeneracionlotes = "//div[contains(@id, 'modolote_label_element')]"
    etiqueta_controlstockenlinea = "//label[contains(@id, 'stockenlinea_label')]"
    etiqueta_modostockenlinea = "//div[contains(@id, 'modocontrolstock_label_element')]"
    campo_modoafectacion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-container/ui-row[1]/ui-combobox/div"
    ayuda_rubro = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    campo_rubro = "//input[@type = 'number' and contains(@id, 'rubstock_element')]"
    campo_modogeneracionlotes = "//div[contains(@id, 'modolote_select')]"
    campo_controlstockenlinea = "//input[@type = 'checkbox' and contains(@id, 'stockenlinea_checkbox')]"
    campo_modostockenlinea = "//div[contains(@id, 'modocontrolstock_select')]"
    etiqueta_tiposrubropermitidos = "//div[contains(@id, '201_element')]"
    btn_Nuevo_tiposrubro = "//div[contains(@id, 'add_tiposrubrostock_element')]"
    btn_Elimina_tiposrubro = "//div[contains(@id, 'remove_tiposrubrostock_element')]"
    etiqueta_tiposrubro = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-label/div"
    ayuda_tiposrubro = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
    btn_Guarda_tiposrubro = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_ventas = "//button[contains(@id, 'pagina3_tabitem')]"
    etiqueta_modoafectacionventas = "//div[contains(@id, 'ventas_label_element')]"
    etiqueta_afectarimportes = "//label[contains(@id, 'afectarimportes_label')]"
    etiqueta_afectarunidades = "//label[contains(@id, 'afectarunidades_label')]"
    etiqueta_afectartopeventa = "//label[contains(@id, 'afectatopevta_label')]"
    etiqueta_calculodescrecar = "//div[contains(@id, 'modocalculodtorec_label_element')]"
    etiqueta_modoaplipoliticas = "//div[contains(@id, 'modoaplicacionpoliticasventa_label_element')]"
    campo_modoafectacionventas = "//div[contains(@id, 'ventas_select')]"
    campo_afectarimportes = "//input[@type = 'checkbox' and contains(@id, 'afectarimportes_checkbox')]"
    campo_afectarunidades = "//input[@type = 'checkbox' and contains(@id, 'afectarunidades_checkbox')]"
    campo_afectartopeventa = "//input[@type = 'checkbox' and contains(@id, 'afectatopevta_checkbox')]"
    campo_calculodescrecar = "//div[contains(@id, 'modocalculodtorec_select')]"
    campo_modoaplipoliticas = "//div[contains(@id, 'modoaplicacionpoliticasventa_select')]"

    btn_ccd = "//button[contains(@id, 'pagina4_tabitem')]"
    etiqueta_modoafectacionccd = "//div[contains(@id, 'cuentacorriente_label_element')]"
    etiqueta_descripcionccd = "//div[contains(@id, 'descripcioncc_label_element')]"
    etiqueta_verificalim = "//label[contains(@id, 'verificarcredito_label')]"
    campo_modoafectacionccd = "//div[contains(@id, 'cuentacorriente_select')]"
    campo_descripcionccd = "//input[@type = 'text' and contains(@id, 'descripcioncc_element')]"
    campo_verificalim = "//input[@type = 'checkbox' and contains(@id, 'verificarcredito_checkbox')]"
    campo_aux = "//div[contains(@id, 'aux_select')]"

    btn_liquidaciones = "//button[contains(@id, 'pagina6_tabitem')]"
    etiqueta_afectaliquidacion = "//label[contains(@id, 'afectaliquidaciondinero_label')]"
    etiqueta_modoafectacionliq = "//div[contains(@id, 'liquidaciondinero_label_element')]"
    etiqueta_visibleagregarnuevo = "//label[contains(@id, 'visibleenagregarnuevo_label')]"
    etiqueta_afectaentrega = "//label[text()= 'Afecta entrega' and contains(@id, 'entrega_label')]"
    campo_afectaliquidacion = "//input[@type = 'checkbox' and contains(@id, 'afectaliquidaciondinero_checkbox')]"
    campo_modoafectacionliq = "//div[contains(@id, 'liquidaciondinero_select')]"
    campo_visibleagregarnuevo = "//input[@type = 'checkbox' and contains(@id, 'visibleenagregarnuevo_checkbox')]"
    campo_afectaentrega = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[11]/span/ui-checkbox/div/input"

    btn_regvisita = "//button[contains(@id, 'pagina7_tabitem')]"
    etiqueta_genregistrovisita = "//label[contains(@id, 'generaregistrovisita_label')]"
    etiqueta_rubrovisita = "//div[contains(@id, 'rubrovisita_label_element')]"
    campo_genregistrovisita = "//input[@type = 'checkbox' and contains(@id, 'generaregistrovisita_checkbox')]"
    ayuda_rubroregvisita = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[8]/ui-container/ui-row[3]/span[2]/ui-lookup/span[1]"

    btn_cheques = "//button[contains(@id, 'pagina9_tabitem')]"
    etiqueta_tiposcheque = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[10]/ui-container/ui-row[2]/span[1]/ui-container/ui-row[1]/ui-label/div"
    btn_Nuevo_tipocheque = "//div[contains(@id, 'add_tiposcheque_element')]"
    btn_Elimina_tipocheque = "//div[contains(@id, 'remove_tiposcheque_element')]"
    etiqueta_tipocheque = "//div[text()= 'Tipo de Cheque' and contains(@id, 'codigo_label_element')]"
    ayuda_tipocheque = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
    etiqueta_aceptacheque = "//label[contains(@id, 'aceptacheques_label')]"
    etiqueta_calcularpagoefectivo = "//label[contains(@id, 'calcularefectivo_label')]"
    etiqueta_combinarmediospago = "//label[contains(@id, 'permitircombinarmediospago_label')]"
    etiqueta_aceptaefectivo = "//label[contains(@id, 'aceptaefectivo_label')]"
    etiqueta_destinocheque = "//div[contains(@id, 'destinocheque_label_element')]"
    campo_aceptacheque = "//input[@type = 'checkbox' and contains(@id, 'aceptacheques_checkbox')]"
    campo_calcularpagoefectivo = "//input[@type = 'checkbox' and contains(@id, 'calcularefectivo_checkbox')]"
    campo_combinarmediospago = "//input[@type = 'checkbox' and contains(@id, 'permitircombinarmediospago_checkbox')]"
    campo_aceptaefectivo = "//input[@type = 'checkbox' and contains(@id, 'aceptaefectivo_checkbox')]"
    ayuda_destinocheque = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[10]/ui-container/ui-row[2]/span[2]/ui-container/ui-row[8]/ui-lookup/span[1]"
    btn_Guarda_tipocheque = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_cancelaciones = "//button[contains(@id, 'pagina10_tabitem')]"
    etiqueta_tiposdocumentocan = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row/span/ui-container/ui-row/ui-tabstrip/div/div[11]/ui-container/ui-row[2]/span[1]/ui-container/ui-row[1]/ui-label/div"
    btn_Nuevo_doccancelacion = "//div[contains(@id, 'add_cancelaciones_element')]"
    btn_Elimina_doccancelacion = "//div[contains(@id, 'remove_cancelaciones_element')]"
    etiqueta_tipodocumentocan = "//div[text()= 'Tipo de Documento' and contains(@id, 'codigo_label_element')]"
    campo_tipodocumentocan = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/input"
    btn_Guarda_doccancelacion = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_repartohh = "//button[contains(@id, 'pagina21_tabitem')]"
    etiqueta_editableliq = "//label[contains(@id, 'editableenreparto_label')]"
    campo_editableliq = "//input[@type = 'checkbox' and contains(@id, 'editableenreparto_checkbox')]"

    btn_restricciones = "//button[contains(@id, 'restrinciones_tabitem')]"
    etiqueta_lineasnegociopermitida = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[5]/ui-container/ui-row/span[1]/ui-container/ui-row[1]/ui-label/div"
    btn_Nuevo_lineanegpermitida = "//div[contains(@id, 'add_lineasnegocio_element')]"
    btn_Elimina_lineanegpermitida = "//div[contains(@id, 'remove_lineasnegocio_element')]"
    etiqueta_codigolinea = "//div[contains(@id, 'clineanegocio_label_element')]"
    ayuda_codigolinea = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
    btn_Guarda_lineanegpermitida = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_generardesde = "//button[contains(@id, 'generardesdetd_tabitem')]"
    etiqueta_generarconbonif = "//label[contains(@id, 'generarconbonificacion_label')]"
    etiqueta_incluirbonif = "//label[contains(@id, 'incluirbonificaciones_label')]"
    etiqueta_mantenerpreciosydesc = "//label[contains(@id, 'mantenerpreciosydescuentos_label')]"
    etiqueta_asociargenerar = "//label[contains(@id, 'asociaralgenerardesde_label')]"
    etiqueta_cancelarccd = "//label[contains(@id, 'cancelarccdalgenerardesde_label')]"
    etiqueta_incluiritems = "//div[contains(@id, 'incluirItems_label_element')]"
    campo_generarconbonif = "//input[@type = 'checkbox' and contains(@id, 'generarconbonificacion_checkbox')]"
    campo_incluirbonif = "//input[@type = 'checkbox' and contains(@id, 'incluirbonificaciones_checkbox')]"
    campo_mantenerpreciosydesc = "//input[@type = 'checkbox' and contains(@id, 'mantenerpreciosydescuentos_checkbox')]"
    campo_asociargenerar = "//input[@type = 'checkbox' and contains(@id, 'asociaralgenerardesde_checkbox')]"
    campo_cancelarccd = "//input[@type = 'checkbox' and contains(@id, 'cancelarccdalgenerardesde_checkbox')]"
    btn_Nuevo_incluiritem = "//div[contains(@id, 'add_generardesdetd_element')]"
    btn_Elimina_incluiritem = "//div[contains(@id, 'remove_generardesdetd_element')]"
    etiqueta_tipodocitem = "//div[contains(@id, 'modelosdocumentos_label_element')]"
    campo_tipodocitem = "//input[@type = 'text' and contains(@id, 'modelosdocumentos_element')]"
    btn_Guarda_incluiritem = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
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
