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

    __CHROME_DRIVER_PATH = modify_name_for_windows(os.path.join("C:\chromedriver\chromedriver"))

# Recursos para iniciar sesion
    URL = "https://test-pos-pbi.pwstasp.com.uy/#/"
    usuario = "xi2posw12"
    contrasena = "Pwst12345*"

    id_usuario = "/html/body/div[3]/div[2]/form/input[1]"
    id_contrasena = "/html/body/div[3]/div[2]/form/input[2]"
    btn_ingresar = "/html/body/div[3]/div[2]/form/button"

    #Recursos para cerrar sesion
    id_seleccionarelperfil = "fondo"
    xpath_logout = "/html/body/nav/div/div[2]/ul/li[7]/ul/li[2]/a"
    xpath_confirmar = "/html/body/div[8]/div/div/div/div[3]/button[1]"


    # Recursos para seleccionar cliente
    id_cliente = "cliente_predefinido"
    nombre_cliente = "Aa"


    #Recursos para ingresar articulos
    id_articulos = "producto_buscador"
    articulo1 = "BM-006"
    articulo2 = "BM-007"
    articulo3 = "BM-008"
    articulo4 = "BM-009"
    articulo5 = "BM-0010"

    # Realizar la venta
    xpath_buton_cerrarmensaje = "/html/body/div[10]/button"
    xpath_proceed = "/html/body/div[3]/div/div[2]/div[2]/div[4]/div/div[1]/button"
    text_xpath_total = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[4]/div/div/div[2]/div/div[2]/div/div/div[5]/h2/div[2]"
    boton_xpath_ANG = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[4]/div/div/div[2]/div/div[3]/div[2]/div[1]/button"
    boton_xpath_caja = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[2]/div/div/div/span/button"
    id_escribirtotal = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[2]/div/div/div/div[3]/input"
    boton_agregarmontoapagar = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[2]/div/div/div/button[2]"
    xpath_desplazarabajoVenta = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[4]/div/div/div[1]/div/div[2]/h4/b"
    boton_xpath_checkout = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[4]/div/div/div[2]/div/div[3]/div[3]/div[1]/button"
    xpath_desplazarabajo = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[5]/div/div/div[1]/h1"
    boton_xpath_cerrarticket = "/html/body/div[3]/div/div[2]/div[2]/div[8]/div[5]/div/div/div[2]/button[4]"


    @classmethod
    def create_chrome_driver(cls, options=None):
        if not options:
            return webdriver.Chrome(cls.__CHROME_DRIVER_PATH)
        else:
            return webdriver.Chrome(
                executable_path=cls.__CHROME_DRIVER_PATH,
                options=options
            )
