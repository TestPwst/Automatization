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

    Icodigo = "Test1"
    Icodigoalter = "CódigoTest"
    Idescripcion = "Prueba automatizada del campo descripción en arq de clientes"

    Icodigosegundo = "Test2"
    Icodigoaltersegundo = "CódigoTest"
    Idescripcionsegundo = "Prueba automatizada del campo descripción en el segundo nivel 2"

    Icodigotercero = "Test3"
    Icodigoaltertercero = "CódigoTest"
    Idescripciontercero = "Prueba automatizada del campo descripción en el terecer nivel 3"

    Icodigocuarto = "Test4"
    Icodigoaltercuarto = "CódigoTest"
    Idescripcioncuarto = "Prueba automatizada del campo descripción en el cuarto nivel 4"

    Mcodigoalter = "Cambiotest"
    Mdescripcion = "Prueba automatizada del campo modificación en arq de cliente"

    Mcodigoaltersegundo = "Cambiotest"
    Mdescripcionsegundo = "Prueba automatizada del campo modificacion en el segundo nivel 2 "

    Mcodigoaltertercero = "Cambiotest"
    Mdescripciontercero = "Prueba automatizada del campo modificacion en el terecer nivel 3"

    Mcodigoaltercuarto = "Cambiotest"
    Mdescripcioncuarto = "Prueba automatizada del campo modificacion en el cuarto nivel 4"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Arquitectura']"
    Iopcionbuscador = "Arquitectura"

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

    etiqueta_codigo = "//*[contains(@id, 'codigo_label_element')]"
    etiqueta_codigo_alter = "//*[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'Descripcion_label_element')]"
    etiqueta_unidadnegocio = "//*[contains(@id, 'UnidadNegocio_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_codigo_alter = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    ayuda_unidadnegocio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-lookup/span[1]"

    btn_segundonivel = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[1]/button[2]"
    btn_Nuevo_segundonivel = "//*[contains(@id, 'add_ArqCli02_element')]"
    btn_Elimina_segundonivel = "//*[contains(@id, 'remove_ArqCli02_element')]"
    etiqueta_codigo_segundonivel = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigo_alter_segundonivel = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcion_segundonivel = "//*[contains(@id, 'descripcion_label_element')]"
    campo_codigo_segundonivel = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[1]/input"
    campo_codigo_alter_segundonivel= "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[2]/input"
    campo_descripcion_segundonivel = "//input[@type = 'text' and contains(@id, 'descripcion_element')]"

    btn_tercernivel = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[1]/button[2]"
    btn_Nuevo_tercernivel = "//*[contains(@id, 'add_ArqCli03_element')]"
    btn_Elimina_tercernivel = "//*[contains(@id, 'remove_ArqCli03_element')]"
    etiqueta_codigo_tercernivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigo_alter_tercernivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcion_tercernivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    campo_codigo_tercernivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[1]/input"
    campo_codigo_alter_tercernivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[2]/input"
    campo_descripcion_tercernivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"

    btn_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[1]/button[2]"
    btn_Nuevo_cuartonivel = "//*[contains(@id, 'add_ArqCli04_element')]"
    btn_Elimina_cuartonivel = "//*[contains(@id, 'remove_ArqCli04_element')]"
    etiqueta_codigo_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigo_alter_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcion_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    campo_codigo_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[1]/input"
    campo_codigo_alter_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[2]/input[1]"
    campo_descripcion_cuartonivel = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"

    btn_Guarda_cuarto = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_Guarda_tercero = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_Guarda_segundo = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"

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
