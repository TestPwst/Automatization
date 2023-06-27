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

    Icodigo = "1"
    Icodigousuario = "Codigousuario01"
    Icodigoalter = "Codigoalt1"
    Idescripcion = "Prueba automatizada del campo descripción Distribuidores"
    Icalle = "Calle 1 prueba"
    Itelefono1 = "5530242334"
    Itelefono2 = "5523112203"
    Mcodigousuario = "Cambiousuario01"
    Mcodigoalter = "Cambioalt1"
    Mdescripcion = "Prueba automatizada de la Modificación del campo descripción Distribuidores"
    Mcalle = "Calle 1 prueba modificación"
    Mtelefono1 = "5510090302"
    Mtelefono2 = "5509102108"


    Icodigoage = "2"
    Icodigoalterage = "Codigoalt2"
    Idescripcionage = "Prueba automatizada del campo descripción Agencias"
    Icalleage = "Calle 2 prueba"
    Itelefono1age = "5530242334"
    Itelefono2age = "5523112203"
    Mcodigoalterage = "Cambioalt2"
    Mdescripcionage = "Prueba automatizada de la Modificación del campo descripción Agencias"
    Mcalleage = "Calle 2 prueba modificación"
    Mtelefono1age = "5510090302"
    Mtelefono2age = "5509102108"

    Icodigoofi = "3"
    Icodigoalterofi = "Codigoalt3"
    Idescripcionofi = "Prueba automatizada del campo descripción Oficina"
    Icalleofi = "Calle 3 prueba"
    Itelefono1ofi = "5530242334"
    Itelefono2ofi = "5523112203"
    Mcodigoalterofi = "Cambioalt3"
    Mdescripcionofi = "Prueba automatizada de la Modificación del campo descripción Oficina"
    Mcalleofi = "Calle 3 prueba modificación"
    Mtelefono1ofi = "5510090302"
    Mtelefono2ofi = "5509102108"




    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"

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
    etiqueta_codigo_usuario = "//div[contains(@id, 'codigousuario_label_element')]"
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_calle = "//div[contains(@id, 'direccion_label_element')]"
    etiqueta_telefonos = "//div[contains(@id, 'telefono1_label_element')]"
    etiqueta_estado = "//div[contains(@id, 'pais_label_element')]"
    etiqueta_municipio = "//div[contains(@id, 'departam_label_element')]"
    etiqueta_localidad = "//div[contains(@id, 'localida_label_element')]"
    etiqueta_barrio = "//div[contains(@id, 'barrio_label_element')]"
    etiqueta_matriz = "//div[contains(@id, 'matriz_label_element')]"
    etiqueta_compania = "//div[contains(@id, 'compania_label_element')]"
    etiqueta_regional = "//div[contains(@id, 'regional_label_element')]"
    etiqueta_unidadnegocio = "//div[contains(@id, 'unidadnegocio_label_element')]"
    etiqueta_tipodistribuidor = "//div[contains(@id, 'tipodistrib_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_calle = "//input[@type = 'text' and contains(@id, 'direccion_element')]"
    campo_telefono1 = "//input[@type = 'text' and contains(@id, 'telefono1_element')]"
    campo_telefono2 = "//input[@type = 'text' and contains(@id, 'telefono2_element')]"
    ayuda_estado = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[1]/span[1]"
    ayuda_municipio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-lookup[1]/span[1]"
    ayuda_localidad = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span/ui-lookup[1]/span[1]"
    ayuda_barrio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span/ui-lookup[1]/span[1]"
    ayuda_matriz = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[2]/span[1]"
    ayuda_compania = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-lookup[2]/span[1]"
    ayuda_regional = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span/ui-lookup[2]/span[1]"
    ayuda_unidadnegocio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span/ui-lookup[2]/span[1]"
    ayuda_tipodistribuidor = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/span[2]/ui-lookup/span[1]"


    btn_agencias = "//button[contains(@id, 'Agencias_tabitem')]"
    btn_Nuevo_agencias = "//div[contains(@id, 'add_Agencias_element')]"
    btn_Elimina_agencias = "//div[contains(@id, 'remove_Agencias_element')]"
    etiqueta_codigoage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigo_alterage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcionage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    etiqueta_calleage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[1]/ui-label/div"
    etiqueta_telefonosage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-label/div"
    etiqueta_estadoage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-label[1]/div"
    etiqueta_deptoprovi = "//div[contains(@id, 'departamento_label_element')]"
    etiqueta_localidadage = "//div[contains(@id, 'localidad_label_element')]"
    etiqueta_barrioage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span/ui-label[1]/div"
    etiqueta_matrizage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-label[2]/div"
    etiqueta_companiaage = "//html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-label[2]/div"
    etiqueta_regionalage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-label[2]/div"
    etiqueta_tipoagencia = "//div[contains(@id, 'tipoagencia_label_element')]"
    campo_codigoage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-numericbox/input"
    campo_codigo_alterage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox/input"
    campo_descripcionage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
    campo_calleage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-textbox/input"
    campo_telefono1age = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-textbox[1]/input"
    campo_telefono2age = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-textbox[2]/input"
    ayuda_estadoage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[1]/span[1]"
    ayuda_deptoprovi = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[1]/span[1]"
    ayuda_localidadage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-lookup[1]/span[1]"
    ayuda_barrioage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span/ui-lookup[1]/span[1]"
    ayuda_matrizage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[2]/span[1]"
    ayuda_companiaage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[2]/span[1]"
    ayuda_regionalage = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-lookup[2]/span[1]"
    ayuda_tipoagencia = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span/ui-lookup[2]/span[1]"
    btn_Guarda_agencias = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"


    btn_oficinas = "//button[contains(@id, 'Oficinas_tabitem')]"
    btn_Nuevo_oficina = "//div[contains(@id, 'add_Oficinas_element')]"
    btn_Elimina_oficina = "//div[contains(@id, 'remove_Oficinas_element')]"
    etiqueta_codigoofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigo_alterofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcionofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    etiqueta_calleofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[1]/ui-label/div"
    etiqueta_telefonosofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-label/div"
    etiqueta_estadoofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-label[1]/div"
    etiqueta_deptoproviofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-label[1]/div"
    etiqueta_localidadofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-label[1]/div"
    etiqueta_barrioofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span[1]/ui-label/div"
    etiqueta_matrizofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-label[2]/div"
    etiqueta_companiaofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-label[2]/div"
    etiqueta_regionalofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-label[2]/div"
    etiqueta_tipooficina = "//div[contains(@id, 'tipooficina_label_element')]"
    campo_codigoofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-numericbox/input"
    campo_codigo_alterofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox/input"
    campo_descripcionofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
    campo_calleofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-textbox/input"
    campo_telefono1ofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-textbox[1]/input"
    campo_telefono2ofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span/ui-textbox[2]/input"
    ayuda_estadoofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[1]/span[1]"
    ayuda_deptoprovioofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[1]/span[1]"
    ayuda_localidadofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-lookup[1]/span[1]"
    ayuda_barrioofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span[2]/ui-lookup/span[1]"
    ayuda_matrizofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[2]/span[1]"
    ayuda_companiaofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[6]/span/ui-lookup[2]/span[1]"
    ayuda_regionalofi = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span/ui-lookup[2]/span[1]"
    ayuda_tipooficina = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span[2]/ui-lookup/span[1]"
    btn_Guarda_oficina = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"


    btn_CuentasCont = "//button[contains(@id, 'CuentasContables_tabitem')]"
    btn_Nuevo_CuentasCont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_Elimina_CuentasCont = "//div[contains(@id, 'rem_CtasCont_element')]"
    etiqueta_tipodoc = "//div[text()='Tipo Documento']"
    etiqueta_cuentacont = "//div[text()='Cuenta Contable']"
    etiqueta_centrocosto = "//div[text()='Centro Costo']"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_ctacont = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-lookup/span[1]"
    btn_acepta_ctacont = "//button[text()='Aceptar']"
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
