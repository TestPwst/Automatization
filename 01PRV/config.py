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
    Iidcorr = "20"
    Icodigoalter = "2021103"
    Icodigogln = "2021103"
    Iruc = "Prueba RUC 01"
    Irazonsocial = "PRUEBA RAZON SOCIAL"
    Inomnegocio = "PRUEBA NOM NEGOCIO"
    Icalle = "Calle 1 prueba automatizada"
    Iesquina1 = "Esquina 1 prueba"
    Iesquina2 = "Esquina 2 prueba"
    Inropuerta = "20"
    Itelefono1 = "5508243022"
    Itelefono2 = "5521102034"
    Icodigopostal = "41310"
    Icorreoelec = "prueba@gmail.com"
    Mrazonsocial = "PRUEBA CAMBIO RAZON SOCIAL"
    Mnomnegocio = "PRUEBA CAMBIO NOM NEGOCIO"
    Mcalle = "Calle 1 prueba cambio"
    Mesquina1 = "Esquina 1 cambio"
    Mesquina2 = "Esquina 2 cambio"
    Mnropuerta = "21"
    Mtelefono1 = "5503220400"
    Mtelefono2 = "5510091109"
    Mcodigopostal = "42300"
    Mcorreoelec = "pruebacambio@gmail.com"

    Itopedescuento = "100"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Proveedores']//descendant::small[text()='Tablas']"
    Iopcionbuscador = "Proveedores"

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
    etiqueta_idcorr = "//div[contains(@id, 'corrid_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_codigo_gln = "//div[contains(@id, 'codigogln_label_element')]"
    etiqueta_ruc = "//div[contains(@id, 'ruc_label_element')]"
    etiqueta_razonsocial = "//div[contains(@id, 'razonsocial_label_element')]"
    etiqueta_nomnegocio = "//div[contains(@id, 'nombre_label_element')]"
    etiqueta_calle = "//div[contains(@id, 'direccion_label_element')]"
    etiqueta_esquinas = "//div[contains(@id, 'esquina_label_element')]"
    etiqueta_nropuerta = "//div[contains(@id, 'nropuerta_label_element')]"
    etiqueta_telefonos = "//div[contains(@id, 'telefono1_label_element')]"
    etiqueta_codigopostal = "//div[contains(@id, 'codpostal_label_element')]"
    etiqueta_correoelectronico = "//div[contains(@id, 'correoelectronico_label_element')]"
    etiqueta_aceptacheque = "//label[contains(@id, 'aceptacheque_label')]"
    etiqueta_listaprecio = "//div[contains(@id, 'lista_label_element')]"
    etiqueta_estado = "//div[contains(@id, 'pais_label_element')]"
    etiqueta_deptoprovi = "//div[contains(@id, 'departamento_label_element')]"
    etiqueta_localidad = "//div[contains(@id, 'localidad_label_element')]"
    etiqueta_barrio = "//div[contains(@id, 'barrio_label_element')]"
    etiqueta_impuesto = "//div[contains(@id, 'impuesto_label_element')]"
    etiqueta_empresa = "//div[contains(@id, 'empresa_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_idcorr = "//input[@type = 'text' and contains(@id, 'corrid_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_codigo_gln = "//input[@type = 'text' and contains(@id, 'codigogln_element')]"
    campo_ruc = "//input[@type = 'text' and contains(@id, 'ruc_element')]"
    campo_razonsocial = "//input[@type = 'text' and contains(@id, 'razonsocial_element')]"
    campo_nomnegocio = "//input[@type = 'text' and contains(@id, 'nombre_element')]"
    campo_calle = "//input[@type = 'text' and contains(@id, 'direccion_element')]"
    campo_esquina1 = "//input[@type = 'text' and contains(@id, 'esquina_element')]"
    campo_esquina2 = "//input[@type = 'text' and contains(@id, 'esquina2_element')]"
    campo_nropuerta = "//input[@type = 'text' and contains(@id, 'nropuerta_element')]"
    campo_telefono1 = "//input[@type = 'text' and contains(@id, 'telefono1_element')]"
    campo_telefono2 = "//input[@type = 'text' and contains(@id, 'telefono2_element')]"
    campo_codigopostal = "//input[@type = 'text' and contains(@id, 'codpostal_element')]"
    campo_correoelectronico = "//input[@type = 'text' and contains(@id, 'correoelectronico_element')]"
    campo_aceptacheque = "//input[@type = 'checkbox' and contains(@id, 'aceptacheque_checkbox')]"
    ayuda_listaprecio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[2]/ui-lookup/span[1]"
    ayuda_estado = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[3]/ui-lookup/span[1]"
    ayuda_deptoprovi = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[4]/ui-lookup/span[1]"
    ayuda_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[5]/ui-lookup/span[1]"
    ayuda_barrio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[6]/ui-lookup/span[1]"
    ayuda_impuesto = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[7]/ui-lookup/span[1]"
    ayuda_empresa = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span/ui-container[2]/ui-row[8]/ui-lookup/span[1]"

    btn_politicasventa = "//button[contains(@id, 'politicas_tabitem')]"
    etiqueta_topedescuento = "//div[contains(@id, 'topedescuento_label_element')]"
    campo_topedescuento = "//input[@type = 'text' and contains(@id, 'topedescuento_element')]"

    btn_sucursales = "//button[contains(@id, 'sucursales_tabitem')]"
    btn_Nuevo_sucursal = "//div[contains(@id, 'add_sucursales_element')]"
    btn_Elimina_sucursal= "//div[contains(@id, 'remove_sucursales_element')]"
    etiqueta_nrosucursal = "//div[text() = 'Nro.' and contains( @ id, 'codigo_label_element')]"
    etiqueta_codigoaltersuc = "//div[text() = 'Código Alternativo' and contains( @ id, 'codigoalternativo_label_element')]"
    etiqueta_codigoglnsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_nomnegociosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[4]/ui-label/div"
    etiqueta_razonsocialsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_correoelecsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_callesuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_rif = "//div[text() = 'RIF' and contains( @ id, 'ruc_label_element')]"
    etiqueta_listapreciosuc = "//div[contains(@id, 'listaprecio_label_element')]"
    etiqueta_estadosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[3]/ui-label/div"
    etiqueta_municipiosuc = "//div[text() = 'Municipio' and contains( @ id, 'departamento_label_element')]"
    etiqueta_localidadsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[5]/ui-label/div"
    etiqueta_barriosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[6]/ui-label/div"
    etiqueta_coloniasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[7]/ui-label/div"
    etiqueta_impuestosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[8]/ui-label/div"
    etiqueta_empresasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[9]/ui-label/div"
    campo_nrosucursal = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[1]/ui-numericbox/input"
    campo_codigoaltersuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[2]/ui-textbox/input"
    campo_codigoglnsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[3]/ui-textbox/input"
    campo_nomnegociosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[4]/ui-textbox/input"
    campo_razonsocialsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[5]/ui-textbox/input"
    campo_correoelecsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[6]/ui-textbox/input"
    campo_callesuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[7]/ui-textbox/input"
    campo_rif = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[1]/ui-container/ui-row[11]/ui-textbox[1]/input"
    ayuda_listapreciosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_estadosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[3]/ui-lookup/span[1]"
    ayuda_municipiosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[4]/ui-lookup/span[1]"
    ayuda_localidadsuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[5]/ui-lookup/span[1]"
    ayuda_barriosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[6]/ui-lookup/span[1]"
    campo_coloniasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[7]/ui-textbox/input"
    ayuda_empresasuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[9]/ui-lookup/span[1]"
    ayuda_impuestosuc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/span[2]/ui-container/ui-row[8]/ui-lookup/span[1]"
    btn_Guarda_sucursal = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

    btn_cuentascontables = "//button[contains(@id, 'CtasCont_tabitem')]"
    btn_Nuevo_ctacont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_Elimina_ctacont = "//div[contains(@id, 'rem_CtasCont_element')]"
    etiqueta_tipodocumento = "//div[text() = 'Tipo Documento' and contains( @ id, '3_element')]"
    etiqueta_ctacontable = "//div[text() = 'Cuenta Contable' and contains( @ id, '6_element')]"
    etiqueta_centrocosto = "//div[text() = 'Centro Costo' and contains( @ id, '9_element')]"
    ayuda_tipodocumento = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_ctacontable = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-lookup/span[1]"
    btn_Guarda_ctascontables = "//button[text()='Aceptar']"

    btn_cerrarsucursal = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"

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
