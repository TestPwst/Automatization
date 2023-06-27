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


    URL = "https://client.assist.com.uy/"
    Iopcionbuscador = "Acuerdos Comerciales"
    Icodigo = "1"
    Icontrato = "Contrato01"
    Idescripcion = "Prueba automatización descripción de acuerdos comerciales"
    Mcontrato = "Cambio01"
    Mdescripcion = "Esta es una Prueba de automatización de modificación de descripción de acuerdos comerciales"

    #IDS Y XPATH

    #Variables para ingresar a PWST 2.0
    id_usuario = "//*[@id='txtLoginUserName']"
    id_contrasena = "/html/body/div/form/div[1]/div[1]/div/div[2]/table/tbody/tr[1]/td/input[3]"
    btn_ingresar = "//*[@id='login-content']/div[1]/div/div[2]/table/tbody/tr[2]/td/input[1]"
    btn_Enterprise = "/html/body/div[2]/div/fieldset[1]/a[1]"

    #Ingreso a la pantalla a automatizar
    buscador = "//div[@title = 'acceso rápido' ]"
    buscador2 = "//input[@class = 'search-box-text']"
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

    etiqueta_codigo = "//*[contains(@id, 'codigo_label_element')]"
    etiqueta_numcontrato = "//*[contains(@id, 'nrocontrato_label_element')]"
    etiqueta_fecha = "//*[contains(@id, 'fecha_label_element')]"
    etiqueta_fecha_fin = "//*[contains(@id, 'fechafinalizacion_label_element')]"
    etiqueta_cuenta = "//*[contains(@id, 'cuenta_label_element')]"
    etiqueta_autoriza = "//*[contains(@id, 'quienautoriza_label_element')]"
    etiqueta_estado = "//*[contains(@id, 'estado_label_element')]"
    etiqueta_sucursal = "//*[contains(@id, 'sucursal_label_element')]"
    etiqueta_descripcion = "//*[contains(@id, 'descripcion_label_element')]"
    campo_codigo = "//input[@type = 'text' and contains(@id, 'codigo_element')]"
    campo_numcontrato = "//input[@type = 'text' and contains(@id, 'nrocontrato_element')]"
    ayuda_fecha = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[3]/span[2]/ui-datebox/span"
    ayuda_fecha_fin = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[4]/span[2]/ui-datebox/span"
    ayuda_cuenta = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[1]/span[1]"
    ayuda_sucursal = "/html/body/div[3]/div[2]/ui-container/ui-window[2]/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row[5]/span/ui-lookup[2]/span[1]"
    campo_descripcion = "//textarea[contains(@id, 'descripcion_element')]"
    btn_politicas = "//*[contains(@id, 'politicasxacuerdos_tabitem')]"
    btn_Nuevo_politicas = "//*[contains(@id, 'add_politicasxacuerdos_element')]"
    btn_Elimina_politicas = "//*[contains(@id, 'remove_politicasxacuerdos_element')]"
    etiqueta_politicas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-label/div"
    ayuda_politicas = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[2]/ui-container/ui-row/ui-tabstrip/div/div[2]/ui-container/ui-row/ui-lookup/span[1]"
    btn_Guarda_politica = "/html/body/div[3]/div[2]/ui-container/div/ui-window/div[10]/div[1]/ui-toolbar/div/span[1]/ui-toolbarbutton/div"
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
