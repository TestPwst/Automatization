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

    Icodigo = "1000"
    Icodigousuario = "Codigousuprueba"
    Icodigoalter = "Codigoalt1"
    Icodigogln = "Codigoglnprueba"
    Idescripcion = "Prueba automatizada del campo descripción depósitos"
    Icalle = "Calle 1 prueba automatizada"
    Inropuerta = "1000"
    Iesquina1 = "Esquina 1 prueba"
    Iesquina2 = "Esquina 2 prueba"
    Icapacidad = "1000000"
    Iobservacion1d = "Prueba auto del campo observación 1D"
    Iobservacion2d = "Prueba auto del campo observación 2D"
    Istockmin = "1000000"
    Istockdes = "1000000"
    Mcodigousuario = "Cambiousuprueba"
    Mcodigoalter = "Cambioalt1"
    Mcodigogln = "Cambioglnprueba"
    Mdescripcion = "Prueba automatizada de la Modificación descripción depósitos"
    Mcalle = "Calle 1 Modificación prueba automatizada"
    Mnropuerta = "1111"
    Mesquina1 = "Esquina 1 prueba Mod"
    Mesquina2 = "Esquina 2 prueba Mod"
    Mcapacidad = "1111111"
    Mobservacion1d = "Prueba modificación del campo observación 1D"
    Mobservacion2d = "Prueba modificación del campo observación 2D"
    Mstockmin = "1111111"
    Mstockdes = "1111111"


    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Depósitos']"
    Iopcionbuscador = "Depósitos"

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
    etiqueta_codigo_alter = "//div[contains(@id, 'codigoalternativo_label_element')]"
    etiqueta_codigo_gln = "//div[contains(@id, 'codigogln_label_element')]"
    etiqueta_descripcion = "//div[contains(@id, 'descripcion_label_element')]"
    etiqueta_calle = "//div[contains(@id, 'direccion_label_element')]"
    etiqueta_nropuerta = "//div[contains(@id, 'nropuerta_label_element')]"
    etiqueta_esquinas = "//div[contains(@id, 'esquina_label_element')]"
    etiqueta_capacidadm3 = "//div[contains(@id, 'capacidad_label_element')]"
    etiqueta_observacion1d = "//div[contains(@id, 'observacion1d_label_element')]"
    etiqueta_observacion2d = "//div[contains(@id, 'observacion2d_label_element')]"
    etiqueta_clasificacion = "//div[contains(@id, 'clasificacion_label_element')]"
    etiqueta_distribuidor = "//div[contains(@id, 'distribuidor_label_element')]"
    etiqueta_depositoprincipal = "//div[contains(@id, 'depositoprincipal_label_element')]"
    etiqueta_agencia = "//div[contains(@id, 'agencia_label_element')]"
    etiqueta_oficina = "//div[contains(@id, 'oficina_label_element')]"
    etiqueta_depositocentral = "//label[contains(@id, 'base_label')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_usuario = "//input[@type = 'text' and contains(@id, 'codigousuario_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoalternativo_element')]"
    campo_codigo_gln = "//input[@type = 'text' and contains(@id, 'codigogln_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"
    campo_calle = "//input[@type = 'text' and contains(@id, 'direccion_element')]"
    campo_nropuerta = "//input[@type = 'text' and contains(@id, 'nropuerta_element')]"
    campo_esquina1 = "//input[@type = 'text' and contains(@id, 'esquina_element')]"
    campo_esquina2 = "//input[@type = 'text' and contains(@id, 'esquina2_element')]"
    campo_capacidad = "//input[@type = 'text' and contains(@id, 'capacidad_element')]"
    campo_observacion1d = "//input[@type = 'text' and contains(@id, 'observacion1d_element')]"
    campo_observacion2d = "//input[@type = 'text' and contains(@id, 'observacion2d_element')]"
    ayuda_clasificacion = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span[2]/ui-lookup/span[1]"
    ayuda_distribuidor = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/span[2]/ui-lookup/span[1]"
    ayuda_depositoprincipal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[9]/span[4]/ui-lookup/span[1]"
    ayuda_agencia = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/span[4]/ui-lookup/span[1]"
    ayuda_oficina = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[10]/span[6]/ui-lookup/span[1]"
    campo_depositocentral = "//input[@type = 'checkbox' and contains(@id, 'base_checkbox')]"

    btn_stockmercaderia = "//button[contains(@id, 'StockdeMercaderia_tabitem')]"
    btn_Nuevo_stockmercaderia = "//div[contains(@id, 'add_stockmercaderia_element')]"
    btn_Elimina_stockmercaderia = "//div[contains(@id, 'remove_stockmercaderia_element')]"
    btn_Guarda_stockmercaderia = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    etiqueta_articulo = "//div[contains(@id, 'articulo_label_element')]"
    etiqueta_stockmin = "//div[contains(@id, 'stockminimo_label_element')]"
    etiqueta_stockdes = "//div[contains(@id, 'stockdeseado_label_element')]"
    ayuda_articulo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-container/ui-row[1]/ui-lookup/span[1]"
    campo_stockmin = "//input[@type = 'text' and contains(@id, 'stockminimo_element')]"
    campo_stockdes = "//input[@type = 'text' and contains(@id, 'stockdeseado_element')]"

    btn_CuentasCont = "//button[contains(@id, 'CtasCont_tabitem')]"
    btn_Nuevo_CuentasCont = "//div[contains(@id, 'add_CtasCont_element')]"
    btn_Elimina_CuentasCont = "//div[contains(@id, 'rem_CtasCont_element')]"
    btn_acepta_ctacont = "//button[text()='Aceptar']"
    etiqueta_tipodoc = "//div[text()='Tipo Documento']"
    etiqueta_cuentacont = "//div[text()='Cuenta Contable']"
    etiqueta_centrocosto = "//div[text()='Centro Costo']"
    ayuda_tipodoc = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_ctacont = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_centrocosto = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row[1]/ui-container/ui-row[3]/ui-lookup/span[1]"
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
