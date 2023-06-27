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
    Icodigoconta = "10000"
    Idescripcion = "Esta es una prueba automatizada para validar la descripción de Eventos contables en la versión 2.0"
    Iorigenimporte = "Esto es una prueba automatizada para validar el campo Origen Importe en la versión nueva de PowerStreet 2.0"
    Iorigendescrip = "Esto es una prueba automatizada para validar el campo Origen Descripción en la versión nueva de PowerStreet 2.0"
    Mcodigoconta = "11111"
    Mdescripcion = "Prueba automatizada para la modificacio de cuentas contables"
    Morigenimporte = "Esto es una prueba automatizada para validar la modificación Importe en la versión nueva de PowerStreet 2.0"
    Morigendescrip = "Esto es una prueba automatizada para validar la modificación Descripción en la versión nueva de PowerStreet 2.0"

    Iorden = "100"
    Inomnegocio = "Prueba automatizada para el campo nombre del nego"
    Iorigenvalor = "Prueba automatizada para  validar el campo origen valor en la nueva versión de PWST 20"
    Ilargo = "100"
    Idecimales = "100"
    Morden = "100"
    Mnomnegocio = "Prueba automatizada para la modificación del camp"
    Morigenvalor = "Prueba automatizada para validar el campo modificación en la nueva versión de PWST 2.0"
    Mlargo = "100"
    Mdecimales = "100"

    Iordenitem = "10"
    Idescripitem = "Esto es prueba automatizada para validar el campo descripción en items en la nueva versión PWST 2.00"
    Iorigenimportei = "Esta es una realización de una prueba automatizada para hacer una validación del campo origen importe en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Iorigencuencon = "Esta es una realización de una prueba automatizada para hacer una validación del campo origen importe en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Iorigencencost1 = "Prueba Centro Costo  1"
    Iorigencencost2 = "Prueba Centro Costo  2"
    Iorigencencost3 = "Prueba Centro Costo  3"
    Iorigencotizacion = "Esta es una realización de una prueba automatizada para hacer una validación del campo origen cotización en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Iorigendescripi = "Esta es una realización de una prueba automatizada para hacer una validación del campo origen descripción en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Mordenitem = "10"
    Mdescripitem = "Esto es prueba automatizada para validar el campo modificacio en items en la nueva versión PWST 2.00"
    Morigenimportei = "Esta es una realización de una prueba automatizada para hacer una modificación del campo origen importe en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Morigencuencon = "Esta es una realización de una prueba automatizada para hacer una modificación del campo origen importe en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Morigencencost1 = "Modificaci Centro Costo 1"
    Morigencencost2 = "Modificaci Centro Costo 2"
    Morigencencost3 = "Modificaci Centro Costo 3"
    Morigencotizacion = "Esta es una realización de una prueba automatizada para hacer una modificación del campo origen cotización en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0"
    Morigendescripi = "Esta es una realización de una prueba automatizada para hacer una modificación del campo origen descripción en la pestaña items de la pantalla eventos contables realizada en la nueva versión de PowerStreet 2.0 "

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Eventos Contables']"
    Iopcionbuscador = "Eventos Contables"

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
    etiqueta_codigocontabilizador = "//div[contains(@id, 'codigocontabilizador_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_origenimporte = "//div[contains(@id, 'origenimporte_label_element')]"
    etiqueta_origendescripcion = "//div[contains(@id, 'origendescripcion_label_element')]"
    etiqueta_generarasiento = "//label[contains(@id, 'asientounico_label')]"
    etiqueta_forzarcierre = "//label[contains(@id, 'forzarcierre_label')]"
    etiqueta_cuentacierre = "//div[contains(@id, 'cuentacontablecierreforzado_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigocontabilizador = "//input[@type = 'text' and contains(@id, 'codigocontabilizador_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_origenimporte = "//input[@type = 'text' and contains(@id, 'origenimporte_element')]"
    campo_origendescripcion = "//input[@type = 'text' and contains(@id, 'origendescripcion_element')]"
    campo_generarasiento = "//input[@type = 'checkbox' and contains(@id, 'asientounico_checkbox')]"
    campo_forzarcierre = "//input[@type = 'checkbox' and contains(@id, 'forzarcierre_checkbox')]"
    ayuda_cuentacierre = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[8]/span[2]/ui-lookup/span[1]"


    btn_parametros = "//button[contains(@id, 'parametroscontabilizacion_tabitem')]"
    btn_Nuevo_parametros = "//div[contains(@id, 'add_parametroscontabilizacion_element')]"
    btn_Elimina_parametros = "//div[contains(@id, 'remove_parametroscontabilizacion_element')]"
    etiqueta_orden = "//div[contains(@id, 'orden_label_element')]"
    etiqueta_nomnegocio = "//div[contains(@id, 'nombre_label_element')]"
    etiqueta_origenvalor = "//div[contains(@id, 'origenvalor_label_element')]"
    etiqueta_largo = "//div[contains(@id, 'largo_label_element')]"
    etiqueta_decimales = "//div[contains(@id, 'decimales_label_element')]"
    campo_orden = "//input[@type = 'text' and contains(@id, 'orden_element')]"
    campo_nomnegocio = "//input[@type = 'text' and contains(@id, 'nombre_element')]"
    campo_origenvalor = "//input[@type = 'text' and contains(@id, 'origenvalor_element')]"
    campo_largo = "//input[@type = 'text' and contains(@id, 'largo_element')]"
    campo_decimales = "//input[@type = 'text' and contains(@id, 'decimales_element')]"
    btn_Guarda_parametros = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"


    btn_items = "//button[contains(@id, 'itemsevento_tabitem')]"
    btn_Nuevo_item = "//div[contains(@id, 'add_itemsevento_element')]"
    btn_Elimina_item = "//div[contains(@id, 'remove_itemsevento_element')]"
    etiqueta_ordeni = "//div[contains(@id, 'orden_label_element')]"
    etiqueta_descripcioni = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    etiqueta_origenimportei = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[1]/ui-label/div"
    etiqueta_origenctacont = "//div[contains(@id, 'origenctacontable_label_element')]"
    etiqueta_origenctrocosto = "//div[contains(@id, 'origencentrocosto_label_element')]"
    etiqueta_origencotizacion = "//div[contains(@id, 'origencotizacion_label_element')]"
    etiqueta_origendescripcioni = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span[1]/ui-label/div"
    etiqueta_modo = "//div[contains(@id, 'debehaber_label_element')]"
    campo_ordeni = "//input[@type = 'text' and contains(@id, 'orden_element')]"
    campo_descripcioni = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
    campo_origenimportei = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-textbox/input"
    campo_origenctacont = "//input[@type = 'text' and contains(@id, 'origenctacontable_element')]"
    campo_origenctrocosto1 = "//input[@type = 'text' and contains(@id, 'origencentrocosto_element')]"
    campo_origenctrocosto2 = "//input[@type = 'text' and contains(@id, 'origencentrocosto2_element')]"
    campo_origenctrocosto3 = "//input[@type = 'text' and contains(@id, 'origencentrocosto3_element')]"
    campo_origencotizacion = "//input[@type = 'text' and contains(@id, 'origencotizacion_element')]"
    campo_origendescripcioni = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[7]/span[2]/ui-textbox/input"
    campo_modo = "//div[contains(@id, 'debehaber_select')]"
    btn_Guarda_items = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
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
