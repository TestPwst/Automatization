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
   

    __CHROME_DRIVER_PATH = modify_name_for_windows(("C:\chromedriver\chromedriver"))

    Icodigo = "Test1"
    Icodigoalt = "CodigoTest"
    Idescripcion = "Prueba automatizada del campo descripción arqpro en PWST 2.0"
    Mcodigoalt = "CambioTest"
    Mdescripcion = "Prueba automatizada del campo modificacio arqpro en PWST 2.0"

    IcodigoM = "Test2"
    IcodigoaltM = "CodigoTest"
    IdescripcionM = "Prueba automatizada del campo descripción arqpro en PWST 2.0"
    McodigoaltM = "CambioTest"
    MdescripcionM = "Prueba automatizada del campo modificacio arqpro en PWST 2.0"

    IcodigoF = "Test3"
    IcodigoaltF = "CodigoTest"
    IdescripcionF = "Prueba automatizada del campo descripción arqpro en PWST 2.0"
    McodigoaltF = "CambioTest"
    MdescripcionF = "Prueba automatizada del campo modificacio arqpro en PWST 2.0"

    IcodigoG = "Test4"
    IcodigoaltG = "CodigoTest"
    IdescripcionG = "Prueba automatizada del campo descripción arqpro en PWST 2.0"
    McodigoaltG = "CambioTest"
    MdescripcionG = "Prueba automatizada del campo modificacio arqpro en PWST 2.0"

    #IDS Y XPATH

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Arquitectura de productos']"
    Iopcionbuscador = "Arquitectura de productos"

    #Agregar, modificar y eliminar el registro
    btn_Nuevo = "//*[contains(@id, 'new_element')]"
    btn_Guarda = "//*[contains(@name, 'save_element')]"
    btn_GuardaG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_GuardaF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_GuardaM= "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
    btn_Refresca = "//*[contains(@id, 'refresh_element')]"
    btn_error = "//div[contains(@id, 'tbPanelErrors_element')]"

    btn_Elimina = "//*[contains(@id, 'removecurrent_element')]"
    btn_EliminaG = "//div[contains(@id, 'remove_ArqProd04_element')]"
    btn_EliminaF = "//div[contains(@id, 'remove_ArqProd03_element')]"
    btn_EliminaM = "//div[contains(@id, 'remove_ArqProd02_element')]"
    btn_acepta_eliminar = "/html/body/div[3]/div[2]/ui-modal/div/div[3]/button[1]"
    btn_cerrar_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/div/span[4]"
    btn_cerrar = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[1]/div/span[4]"
    btn_cerrar_ventana = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"
    btn_marcas = "//*[contains(@id, 'ArqProd02_tabitem')]"
    btn_nuevomarcas = "//*[contains(@id, 'add_ArqProd02_element')]"
    btn_eliminamarcas = "//*[contains(@id, 'remove_ArqProd02_element')]"
    btn_fam = "//*[contains(@id, 'ArqProd03_tabitem')]"
    btn_nuevofam = "//*[contains(@id, 'add_ArqProd03_element')]"
    btn_eliminafam = "//*[contains(@id, 'remove_ArqProd03_element')]"
    btn_gen = "//*[contains(@id, 'ArqProd04_tabitem')]"
    btn_nuevogen = "//*[contains(@id, 'add_ArqProd04_element')]"
    btn_eliminagen = "//*[contains(@id, 'remove_ArqProd04_element')]"
    titulo_nuevo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/span[2]"
    etiqueta_codigo = "//*[contains(@id, 'Codigo_label_element')]"
    etiqueta_codigoalt = "//*[contains(@id, 'codigoak_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'Descripcion_label_element')]"
    etiqueta_codigoM = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigoaltM = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcionM = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    etiqueta_codigoF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigoaltF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcionF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    etiqueta_codigoG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[1]/div"
    etiqueta_codigoaltG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-label[2]/div"
    etiqueta_descripcionG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[1]/ui-label/div"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'Codigo_element')]"
    campo_codigoalt = "//input[@type = 'text' and contains(@id, 'codigoak_element')]"
    campo_descripcion = "//input[@type = 'text' and contains(@id, 'Descripcion_element')]"
    campo_codigoM = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[1]/input"
    campo_codigoaltM = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[2]/input"
    campo_descripcionM = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
    campo_codigoF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[1]/input"
    campo_codigoaltF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[2]/input"
    campo_descripcionF = "/html/body/div[3]/div[2]/ui-container/div[2]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
    campo_codigoG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[1]/input"
    campo_codigoaltG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/span/ui-textbox[2]/input"
    campo_descripcionG = "/html/body/div[3]/div[2]/ui-container/div[3]/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/span[2]/ui-textbox/input"
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
