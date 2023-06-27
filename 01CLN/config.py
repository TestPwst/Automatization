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

    Icodigo = "2021103"
    Icodigousuario = "818H002021"
    Icodigoalter = "818H002021"
    Icodigogln = "818H002021"
    Irazonsocial = "PRUEBA RAZON SOCIAL"
    Icalle = "Calle 1 prueba automatizada"
    Inropuerta = "20"
    Iesquina1 = "Esquina 1 prueba"
    Iesquina2 = "Esquina 2 prueba"
    Icodigopostal = "41310"
    Itelefono1 = "5508243022"
    Itelefono2 = "5521102034"
    Inomnegocio = "PRUEBA NOM NEGOCIO"
    Icolonia = "Prueba Colonia"
    Icoordenadasx = "16.84942"
    Icoordenadasy = "-99.90891"
    Mrazonsocial = "PRUEBA CAMBIO RAZON SOCIAL"
    Mcalle = "Calle 1 prueba cambio"
    Mnropuerta = "21"
    Mesquina1 = "Esquina 1 cambio"
    Mesquina2 = "Esquina 2 cambio"
    Mcodigopostal = "42300"
    Mtelefono1 = "5503220400"
    Mtelefono2 = "5510091109"
    Mnomnegocio = "PRUEBA CAMBIO NOM NEGOCIO"
    Mcolonia = "Prueba Cambio Colonia"
    Mcoordenadasx = "19.42847"
    Mcoordenadasy = "-99.12766"

    Itopedescuento = "100"

    Icodigoaltersuc = "818H002021"
    Icodigoglnsuc = "818H002021"
    Inomnegociosuc = "PRUEBA NOM NEGOCIO"
    Irazonsocialsuc = "PRUEBA RAZON SOCIAL"
    Icallesuc = "Calle 1 prueba automatizada"
    Icoloniasuc = "Prueba Colonia"
    Mnomnegociosuc = "PRUEBA CAMBIO NOM NEGOCIO"
    Mrazonsocialsuc = "PRUEBA CAMBIO RAZON SOCIAL"
    Mcallesuc = "Calle 1 prueba cambio"
    Mcoloniasuc = "Prueba Cambio Colonia"

    Ifiltro = "818H002021"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Cuentas']"
    Iopcionbuscador = "Cuentas"

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
    etiqueta_codigo_usuario = "//div[contains(@id, 'codigousuario_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_codigo_gln = "//div[contains(@id, 'codigogln_label_element')]"
    etiqueta_razonsocial = "//div[contains(@id, 'razonsocial_label_element')]"
    etiqueta_calle = "//div[contains(@id, 'direccion_label_element')]"
    etiqueta_nropuerta = "//div[contains(@id, 'nropuerta_label_element')]"
    etiqueta_esquinas = "//div[contains(@id, 'esquina_label_element')]"
    etiqueta_codigopostal = "//div[contains(@id, 'codpostal_label_element')]"
    etiqueta_telefonos = "//div[contains(@id, 'telefono1_label_element')]"
    etiqueta_nomnegocio = "//div[contains(@id, 'nombre_label_element')]"
    etiqueta_estado = "//div[contains(@id, 'pais_label_element')]"
    etiqueta_deptoprovi = "//div[contains(@id, 'departamento_label_element')]"
    etiqueta_perfilcuenta = "//div[contains(@id, 'perfil_label_element')]"
    etiqueta_empresa = "//div[contains(@id, 'empresa_label_element')]"
    etiqueta_perfilcredito = "//div[contains(@id, 'perfilcredito_label_element')]"
    etiqueta_aprobado = "//label[contains(@id, 'aprobado2_label')]"
    etiqueta_tipoidentificacion = "//div[contains(@id, 'tipoidentificacion_label_element')]"
    etiqueta_listaprecio = "//div[contains(@id, 'lista_label_element')]"
    etiqueta_localidad = "//div[contains(@id, 'localidad_label_element')]"
    etiqueta_barrio = "//div[contains(@id, 'barrio_label_element')]"
    etiqueta_colonia = "//div[contains(@id, 'colonia_label_element')]"
    etiqueta_coordenadasx = "//div[contains(@id, 'x_label_element')]"
    etiqueta_coordenadasy = "//div[contains(@id, 'y_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_codigo_gln = "//input[@type = 'text' and contains(@id, 'codigogln_element')]"
    campo_razonsocial = "//input[@type = 'text' and contains(@id, 'razonsocial_element')]"
    campo_calle = "//input[@type = 'text' and contains(@id, 'direccion_element')]"
    campo_nropuerta = "//input[@type = 'text' and contains(@id, 'nropuerta_element')]"
    campo_esquina1 = "//input[@type = 'text' and contains(@id, 'esquina_element')]"
    campo_esquina2 = "//input[@type = 'text' and contains(@id, 'esquina2_element')]"
    campo_codigopostal = "//input[@type = 'text' and contains(@id, 'codpostal_element')]"
    campo_telefono1 = "//input[@type = 'text' and contains(@id, 'telefono1_element')]"
    campo_telefono2 = "//input[@type = 'text' and contains(@id, 'telefono2_element')]"
    campo_nomnegocio = "//input[@type = 'text' and contains(@id, 'nombre_element')]"
    ayuda_estado = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[9]/ui-lookup[1]/span[1]"
    ayuda_deptoprovi = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[9]/ui-lookup[2]/span[1]"
    ayuda_perfilcuenta = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[10]/ui-lookup[1]/span[1]"
    ayuda_empresa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[10]/ui-lookup[2]/span[1]"
    ayuda_perfilcredito = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[11]/ui-lookup/span[1]"
    campo_aprobado = "//input[@type = 'checkbox' and contains(@id, 'aprobado2_checkbox')]"
    ayuda_tipoidentificacion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[4]/ui-lookup/span[1]"
    ayuda_listaprecio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[8]/ui-lookup/span[1]"
    ayuda_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[9]/ui-lookup[1]/span[1]"
    ayuda_barrio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[9]/ui-lookup[2]/span[1]"
    campo_colonia = "//input[@type = 'text' and contains(@id, 'colonia_element')]"
    campo_coordenadasx = "//input[@type = 'text' and contains(@id, 'x_element')]"
    campo_coordenadasy = "//input[@type = 'text' and contains(@id, 'y_element')]"

    btn_politicasventa = "//button[contains(@id, 'politicaVenta_tabitem')]"
    etiqueta_topedescuento = "//div[contains(@id, 'topedescuento_label_element')]"
    campo_topedescuento = "//input[@type = 'text' and contains(@id, 'topedescuento_element')]"

    btn_sucursales = "//button[contains(@id, 'sucursales_tabitem')]"
    btn_Nuevo_sucursal = "//div[contains(@id, 'add_sucursales_element')]"
    btn_Elimina_sucursal= "//div[contains(@id, 'remove_sucursales_element')]"
    etiqueta_nrosucursal = "//div[text() = 'Nro.' and contains( @ id, 'codigo_label_element')]"
    etiqueta_codigoaltersuc = "//div[text() = 'Código Alternativo' and contains( @ id, 'codigoalternativo_label_element')]"
    etiqueta_codigoglnsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[2]/ui-label[2]/div"
    etiqueta_nomnegociosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_razonsocialsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[4]/ui-label/div"
    etiqueta_callesuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_tipoidentificacionsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[12]/ui-label/div"
    etiqueta_listapreciosuc = "//div[contains(@id, 'listaprecio_label_element')]"
    etiqueta_estadosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_municipiosuc = "//div[text() = 'Municipio' and contains( @ id, 'departamento_label_element')]"
    etiqueta_localidadsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_barriosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_coloniasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_empresasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[9]/ui-label/div"
    campo_nrosucursal = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[1]/ui-numericbox/input"
    campo_codigoaltersuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[2]/ui-textbox[1]/input"
    campo_codigoglnsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[2]/ui-textbox[2]/input"
    campo_nomnegociosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[3]/ui-textbox/input"
    campo_razonsocialsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[4]/ui-textbox/input"
    campo_callesuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[6]/ui-textbox/input"
    ayuda_tipoidentificacionsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[12]/ui-lookup/span[1]"
    ayuda_listapreciosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_estadosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[3]/ui-lookup/span[1]"
    ayuda_municipiosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[4]/ui-lookup/span[1]"
    ayuda_localidadsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[5]/ui-lookup/span[1]"
    ayuda_barriosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[6]/ui-lookup/span[1]"
    campo_coloniasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[7]/ui-textbox/input"
    ayuda_empresasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[9]/ui-lookup/span[1]"
    btn_Guarda_sucursal = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_categorizacion = "//button[contains(@id, 'categorizacion_tabitem')]"
    btn_categorizacionsuc = "//button[contains(@id, 'frmcategorizacion_tabitem')]"

    filtros = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[2]/div/div[2]"
    filtro_codigocliente = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[20]/div/div[2]"

    etiqueta_codcliente = "//div[text()= 'Código de cliente' and contains(@id, 'label_element')]"
    campo_codcliente = "//input[@type = 'text' and contains(@id, 'control_element')]"
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
