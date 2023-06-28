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

    Icodigo = "PRU20"
    Idescripcion = "Prueba Compañia"
    Mdescripcion = "Prueba Cambio Compañia"

    Inopermitirfact = "2"
    Icantdecimalespre = "2"
    Icantdecimalesdoc = "2"
    Icalendariocierre = "7"
    Idiferenciahoraria = "-180"

    Irangosdesde = "0"
    Irangoshasta = "1000"

    Inombreusuarios = "mobile"
    Icontrasena = "Pwst12345*"
    Icargatransfer = "C:\ temp\cdrem"

    Iclave = "PWST_ActualizarStockLiquidacionesActivas"
    Ivalor = "TRUE"

    Iclave2 = "PWST_AplicarDescuentosXGrupoPolitica"
    Ivalor2 = "TRUE"

    Iclave3 = "PWST_ColAdicExploradorDocumentos"
    Ivalor3 = "TRUE"

    # IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Opciones']"
    Iopcionbuscador = "Opciones"

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
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"

    btn_documentos = "//button[contains(@id, 'documentos_tabitem')]"
    etiqueta_empresaemision = "//div[contains(@id, 'empresaemisiondocumentos_label_element')]"
    etiqueta_serieemision = "//div[contains(@id, 'serieemisiondocumentos_label_element')]"
    etiqueta_monedabase = "//div[contains(@id, 'monedabase_label_element')]"
    etiqueta_vendedoremision = "//div[contains(@id, 'vendedoremisiondocumentos_label_element')]"
    etiqueta_depositoemision = "//div[contains(@id, 'depositoemisiondocumentos_label_element')]"
    etiqueta_modoemision = "//div[contains(@id, 'modoemisiondocumentos_label_element')]"
    etiqueta_modofechastock = "//div[contains(@id, 'modofechastock_label_element')]"
    etiqueta_modolimcredito = "//div[contains(@id, 'modolimitecredito_label_element')]"
    ayuda_empresaemision = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row[1]/span/ui-lookup[1]/span[1]"
    ayuda_serieemision = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row[1]/span/ui-lookup[2]/span[1]"
    ayuda_monedabase = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row[2]/span/ui-lookup[1]/span[1]"
    ayuda_vendedoremision = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row[2]/span/ui-lookup[2]/span[1]"
    ayuda_depositoemision = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[3]/ui-container/ui-row[2]/span/ui-lookup[3]/span[1]"
    campo_modoemision = "//div[contains(@id, 'modoemisiondocumentos_select')]"
    campo_modofechastock = "//div[contains(@id, 'modofechastock_select')]"
    campo_modolimcredito = "//div[contains(@id, 'modolimitecredito_select')]"

    btn_varios = "//button[contains(@id, 'varios_tabitem')]"
    etiqueta_lenguajexdefecto = "//div[contains(@id, 'idiomadefault_label_element')]"
    etiqueta_lenguajetraduccion = "//div[contains(@id, '27_element')]"
    etiqueta_cierrecalendario = "//div[contains(@id, 'modocierrecalendario_label_element')]"
    etiqueta_nopermitirfactura = "//div[contains(@id, 'diasfechafac_label_element')]"
    etiqueta_cantdecimalespre = "//div[contains(@id, 'decimales_label_element')]"
    etiqueta_cantdecimalesdoc = "//div[contains(@id, 'decimalesdoc_label_element')]"
    etiqueta_diferenciahoraria = "//div[contains(@id, 'diferenciahoraria_label_element')]"
    etiqueta_generarentrega = "//label[contains(@id, 'generarentregasdinerocheques_label')]"
    etiqueta_mantenerdocs = "//label[contains(@id, 'mantenerdocsenliq_label')]"
    etiqueta_permitircomp = "//label[contains(@id, 'permitirvaloresceroencombos_label')]"
    etiqueta_validarnur = "//label[contains(@id, 'controlarasignacionrutas_label')]"
    ayuda_lenguajexdefecto = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[4]/ui-container/ui-row[1]/span/ui-lookup[1]/span[1]"
    ayuda_lenguajetraduccion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[4]/ui-container/ui-row[1]/span/ui-lookup[2]/span[1]"
    campo_cierrecalendario = "//div[contains(@id, 'modocierrecalendario_select')]"
    campo_cierrecalendario2 = "//input[@type = 'text' and contains(@id, 'cerrardiaautomaticamente_element')]"
    campo_nopermitirfactura = "//input[@type = 'text' and contains(@id, 'diasfechafac_element')]"
    campo_cantdecimalespre = "//input[@type = 'text' and contains(@id, 'decimales_element')]"
    campo_cantdecimalesdoc = "//input[@type = 'text' and contains(@id, 'decimalesdoc_element')]"
    campo_diferenciahoraria = "//input[@type = 'text' and contains(@id, 'diferenciahoraria_element')]"
    campo_generarentrega = "//input[@type = 'checkbox' and contains(@id, 'generarentregasdinerocheques_checkbox')]"
    campo_mantenerdocs = "//input[@type = 'checkbox' and contains(@id, 'mantenerdocsenliq_checkbox')]"
    campo_permitircomp = "//input[@type = 'checkbox' and contains(@id, 'permitirvaloresceroencombos_checkbox')]"
    campo_validarnur = "//input[@type = 'checkbox' and contains(@id, 'controlarasignacionrutas_checkbox')]"

    btn_rangoscodigo = "//button[contains(@id, 'rangosCodigo_tabitem')]"
    etiqueta_desde = "//div[contains(@id, 'lblDesde_element')]"
    etiqueta_hasta = "//div[contains(@id, 'lblHasta_element')]"
    campo_desde = "//input[@type = 'text' and contains(@id, 'txtDesde_element')]"
    campo_hasta = "//input[@type = 'text' and contains(@id, 'txtHasta_element')]"
    btn_aceptar = "//button[text()='Aceptar']"

    btn_propiedadesxdefecto = "//button[contains(@id, 'propiedadesDefecto_tabitem')]"
    etiqueta_listaprecios = "//div[contains(@id, 'listaprecio_label_element')]"
    etiqueta_grupocliente = "//div[contains(@id, 'grupo_label_element')]"
    etiqueta_subgrupocliente = "//div[contains(@id, 'subgrupo_label_element')]"
    etiqueta_canal = "//div[contains(@id, 'canal_label_element')]"
    etiqueta_subcanal = "//div[contains(@id, 'subcanal_label_element')]"
    etiqueta_estado = "//div[contains(@id, 'pais_label_element')]"
    etiqueta_deptoprovi = "//div[contains(@id, 'departamento_label_element')]"
    etiqueta_localidad = "//div[contains(@id, 'localidad_label_element')]"
    etiqueta_barrio = "//div[contains(@id, 'barrio_label_element')]"
    etiqueta_zonageo = "//div[contains(@id, 'zona_label_element')]"
    etiqueta_zonareparto = "//div[contains(@id, 'zonareparto_label_element')]"
    etiqueta_zonaventa = "//div[contains(@id, 'zonaventa_label_element')]"
    etiqueta_distribuidor = "//div[contains(@id, 'distribuidor_label_element')]"
    etiqueta_agencia = "//div[contains(@id, 'agencia_label_element')]"
    etiqueta_oficina = "//div[contains(@id, 'oficina_label_element')]"
    etiqueta_perfilcuenta = "//div[contains(@id, 'perfil_label_element')]"
    etiqueta_empresa = "//div[contains(@id, 'empresacliente_label_element')]"
    etiqueta_tipocliente = "//div[contains(@id, 'tipocliente_label_element')]"
    etiqueta_tipoexclusividad = "//div[contains(@id, 'tipoexclusividad_label_element')]"
    etiqueta_primernivel = "//div[contains(@id, 'arqcli1_label_element')]"
    etiqueta_segundonivel = "//div[contains(@id, 'arqcli2_label_element')]"
    etiqueta_tercernivel = "//div[contains(@id, 'arqcli3_label_element')]"
    etiqueta_cuartonivel = "//div[contains(@id, 'arqcli4_label_element')]"
    ayuda_listaprecios = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[2]/span/ui-lookup[1]/span[1]"
    ayuda_grupocliente = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[3]/span/ui-lookup[1]/span[1]"
    ayuda_subgrupocliente = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[4]/span/ui-lookup[1]/span[1]"
    ayuda_canal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[5]/span/ui-lookup[1]/span[1]"
    ayuda_subcanal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[6]/span/ui-lookup[1]/span[1]"
    ayuda_estado = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[7]/span/ui-lookup[1]/span[1]"
    ayuda_deptoprovi = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[8]/span/ui-lookup[1]/span[1]"
    ayuda_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[9]/span/ui-lookup/span[1]"
    ayuda_barrio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[10]/span/ui-lookup[1]/span[1]"
    ayuda_zonageo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[11]/span/ui-lookup[1]/span[1]"
    ayuda_zonareparto = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[12]/span/ui-lookup[1]/span[1]"
    ayuda_zonaventa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[13]/span/ui-lookup[1]/span[1]"
    ayuda_distribuidor = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[2]/span/ui-lookup[2]/span[1]"
    ayuda_agencia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[3]/span/ui-lookup[2]/span[1]"
    ayuda_oficina = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[4]/span/ui-lookup[2]/span[1]"
    ayuda_perfilcuenta = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[5]/span/ui-lookup[2]/span[1]"
    ayuda_empresa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[6]/span/ui-lookup[2]/span[1]"
    ayuda_tipocliente = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[7]/span/ui-lookup[2]/span[1]"
    ayuda_tipoexclusividad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[8]/span/ui-lookup[2]/span[1]"
    ayuda_primernivel = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[11]/span/ui-lookup[2]/span[1]"
    ayuda_segundonivel = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[12]/span/ui-lookup[2]/span[1]"
    ayuda_tercernivel = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[13]/span/ui-lookup[2]/span[1]"
    ayuda_cuartonivel = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[7]/ui-container/ui-row[14]/span/ui-lookup/span[1]"

    btn_dispositivos = "//button[contains(@id, 'dispositivos_tabitem')]"
    etiqueta_nombreusuarios = "//div[contains(@id, 'clientmachineloginname_label_element')]"
    etiqueta_contrasena = "//div[contains(@id, 'clientmachinepassword_label_element')]"
    etiqueta_cargatransfer = "//div[contains(@id, 'pathcargadescargaremota_label_element')]"
    campo_nombreusuarios = "//input[@type = 'text' and contains(@id, 'clientmachineloginname_element')]"
    campo_contrasena = "//input[@type = 'password' and contains(@id, 'clientmachinepassword_element')]"
    campo_cargatransfer = "//input[@type = 'text' and contains(@id, 'pathcargadescargaremota_element')]"

    btn_opcpersonalizadas = "//button[contains(@id, 'opcPersonal_tabitem')]"
    btn_Nuevo_opcpersonalizadas = "//div[contains(@id, 'lstopcPersonal|add_element')]"
    btn_Elimina_opcpersonalizadas = "//div[contains(@id, 'lstopcPersonal|remove_element')]"
    etiqueta_clave = "//div[contains(@id, 'lblclave_element')]"
    etiqueta_valor = "//div[contains(@id, 'lblvalor_element')]"
    campo_clave = "//input[@type = 'text' and contains(@id, 'txtclave_element')]"
    campo_valor = "//input[@type = 'text' and contains(@id, 'txtvalor_element')]"
    btn_aceptaropc = "//button[text()='Aceptar']"

    btn_contabilidad = "//button[contains(@id, 'contabilidad_tabitem')]"
    etiqueta_agruparitems = "//label[contains(@id, 'agruparitemsasiento_label')]"
    campo_agruparitems = "//input[@type = 'checkbox' and contains(@id, 'agruparitemsasiento_checkbox')]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
