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

    Iorden = "1"
    Iusuario = "UsuarioPrueba"
    Icontrasena = "Contrasena123"
    Ihorainicio = "11:00"
    Morden = "2"
    Musuario = "UsuarioPruebaCambio"
    Mcontrasena = "Contrasena12345"
    Mhorainicio = "01:00"


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

    etiqueta_codigo = "//div[contains(@id, 'id_label_element')]"
    etiqueta_horainicio = "//div[contains(@id, 'horainicio_label_element')]"
    etiqueta_activa = "//label[contains(@id, 'activa_label')]"
    etiqueta_usadialup = "//label[contains(@id, 'usedialup_label')]"
    etiqueta_lunes = "//label[contains(@id, 'lunes_label')]"
    etiqueta_martes = "//label[contains(@id, 'martes_label')]"
    etiqueta_miercoles = "//label[contains(@id, 'miercoles_label')]"
    etiqueta_jueves = "//label[contains(@id, 'jueves_label')]"
    etiqueta_viernes = "//label[contains(@id, 'viernes_label')]"
    etiqueta_sabado = "//label[contains(@id, 'sabado_label')]"
    etiqueta_domingo = "//label[contains(@id, 'domingo_label')]"

    ayuda_horainicio = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-datebox/span"
    campo_horainicio = "//input[@type = 'text' and contains(@id, 'horainicio_element')]"
    campo_activa = "//input[@type = 'checkbox' and contains(@id, 'activa_checkbox')]"
    campo_usadialup = "//input[@type = 'checkbox' and contains(@id, 'usedialup_checkbox')]"
    campo_lunes = "//input[@type = 'checkbox' and contains(@id, 'lunes_checkbox')]"
    campo_martes = "//input[@type = 'checkbox' and contains(@id, 'martes_checkbox')]"
    campo_miercoles = "//input[@type = 'checkbox' and contains(@id, 'miercoles_checkbox')]"
    campo_jueves = "//input[@type = 'checkbox' and contains(@id, 'jueves_checkbox')]"
    campo_viernes = "//input[@type = 'checkbox' and contains(@id, 'viernes_checkbox')]"
    campo_sabado = "//input[@type = 'checkbox' and contains(@id, 'sabado_checkbox')]"
    campo_domingo = "//input[@type = 'checkbox' and contains(@id, 'domingo_checkbox')]"




    btn_items = "//button[contains(@id, 'Items_tabitem')]"
    btn_Nuevo_item = "//div[contains(@id, 'add_itemsprogramacionsync_element')]"
    btn_Elimina_item = "//div[contains(@id, 'remove_itemsprogramacionsync_element')]"
    etiqueta_orden = "//div[contains(@id, 'orden_label_element')]"
    etiqueta_sincronizacion = "//div[contains(@id, 'sincronizacion_label_element')]"
    etiqueta_usuario = "//div[contains(@id, 'usuario_label_element')]"
    etiqueta_contrasena = "//div[contains(@id, 'password_label_element')]"
    campo_orden = "//input[@type = 'text' and contains(@id, 'orden_element')]"
    ayuda_sincronizacion = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[2]/ui-lookup/span[1]"
    campo_usuario = "//input[@type = 'text' and contains(@id, 'usuario_element')]"
    campo_contrasena = "//input[@type = 'password' and contains(@name, 'password_element')]"
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
