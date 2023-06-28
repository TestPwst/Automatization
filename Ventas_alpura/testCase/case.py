import time
import unittest
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import Log
from iniciar import iniciar
from descargar import descargar
from venta import venta
from inicio_visita import inicio_visita
from fin_visita import fin_visita
from importlib.machinery import SourceFileLoader

capabilities = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "a04ub",
    "automationName": "UiAutomator2",
    "appPackage": "uy.com.assist.eaf",
    "appActivity": ".MainActivity",
    "autoGrantPermissions": "true",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true",
    "connectHardwareKeyboard": "false"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)


class Test(unittest.TestCase):
    
    #driver = Configuracion.__DRIVER
    @classmethod
    def test(self):
        Log().info("Se carga el driver")

    def test_000(self):
        return iniciar.iniciar(driver)

    def test_001(self):
        for x in range(8):
            venta.venta(driver)
            time.sleep(10)
            
    #def test_002(self):
        #return fin_visita.fin_visita(driver)

    #def test_003(self):
        #return descargar.descargar(driver)


if __name__ == '__main__':
    unittest.main()