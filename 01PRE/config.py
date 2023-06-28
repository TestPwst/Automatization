import os
import platform
from selenium import webdriver
from selenium.webdriver.support import expected_conditions

def modify_name_for_windows(in_path):
    if platform.system().lower().startswith("win"):
        return in_path + ".exe"
    return in_path

#expected_conditions
class conditions:
    visibility = expected_conditions.visibility_of_element_located
    clickable = expected_conditions.element_to_be_clickable

class Configuracion:

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join("C:\chromedriver\chromedriver"))

    Iprecio = "500"
    Idesdeserie = "1"
    Ihastaserie = "1000"
    Mprecio = "650.50"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    btn_sandwich = "//*[@id='toggleMenuBar']"
    titulo_pantalla = "/html/body/div[3]/div[2]/ui-container/ui-window/div[1]/span[2]"
    texto_buscador = "//div[text()='Precios']"
    Iopcionbuscador = "Precios"

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

    etiqueta_lista = "//div[contains(@id, 'lista_label_element')]"
    etiqueta_articulo = "//div[contains(@id, 'articulo_label_element')]"
    etiqueta_fecha = "//div[contains(@id, 'fecha_label_element')]"
    etiqueta_precio = "//div[contains(@id, 'precio_label_element')]"
    etiqueta_desdeserie = "//div[contains(@id, 'desdenroserie_label_element')]"
    etiqueta_hastaserie = "//div[contains(@id, 'hastanroserie_label_element')]"
    ayuda_lista = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_articulo = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    ayuda_fecha = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/ui-datebox/span"
    campo_precio = "//input[@type = 'text' and contains(@id, 'precio_element')]"
    campo_desdeserie = "//input[@type = 'text' and contains(@id, 'desdenroserie_element')]"
    campo_hastaserie = "//input[@type = 'text' and contains(@id, 'hastanroserie_element')]"
    filtros = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[4]/div/div[2]"
    filtro_articulo = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[5]/div/div[2]"
    filtro_listaprecio = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-treeview/div/div/div[2]/div/div[10]/div/div[2]"
    input_descripcion_articulo = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-container/ui-row[2]/ui-container/ui-row[1]/ui-textbox/input"
    input_filtro_lista = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-container/ui-row[2]/ui-container/ui-row[2]/ui-numericbox/input"

    etiqueta_articulofiltro = "//div[text()= 'Articulo' and contains(@id, 'label_element')]"
    etiqueta_listapreciofiltro = "//div[text()= 'Lista de precios' and contains(@id, 'label_element')]"
    ayuda_articulofiltro = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-container/ui-row[2]/ui-container/ui-row[1]/ui-lookup/span[1]"
    ayuda_listapreciofiltro = "/html/body/div[3]/div[2]/ui-container/ui-window/div[10]/div[2]/ui-container/ui-row[2]/ui-container/ui-row[2]/ui-container/ui-row[2]/ui-lookup/span[1]"

    selecciona = "//span[text()='Modifica C']"
    btn_cerrar_modal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[1]/div/span[4]"

    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )