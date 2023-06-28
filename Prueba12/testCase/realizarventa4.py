from importlib.machinery import SourceFileLoader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time
from cerrarsesion import cerrarsesion

class realizarventa4:

    def realizarventa4(self):
        """Realiza venta4"""
       
        """Ingresa Articulos"""
        self.wait = WebDriverWait(self.driver, 60)
        time.sleep(5)
# # Cierra mensaje de alerta
#         try:
#             alerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_buton_cerrarmensaje)))
#             alerta.click()
#             Log().info("Cierra mensaje de alerta")
#             time.sleep(1)


#         except Exception as e:
#             Log().error(
#                 "No se pudo cerrar el mensaje de alerta, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
#             timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
#             img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
#             Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
#             self.driver.get_screenshot_as_file(img_name)
#             return cerrarsesion.cerrarsesion()
#             raise
        
        # Ingresa primer articulo
        try:
            Articulo1 = self.wait.until(conditions.visibility((By.ID, Configuracion.id_articulos)))
            Articulo1.send_keys(Configuracion.articulo1)
            Log().info(" Escribe el primer articulo")
            time.sleep(2)


        except Exception as e:
            Log().error(
                "No se pudo escribir el codigo del articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        #Selecciona el articulo
        try:
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.DOWN) \
                .send_keys(Keys.ENTER) \
                .pause(1) \
                .release()
            action.perform()
            Log().info("Selecciona el articulo")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(3)



        except Exception as e:
            Log().error(
                "No se pudo seleccionar el articulo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        

        

        



       

        # Da click en proceed
        try:
            time.sleep(3)
            boton_proceed = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_proceed)))
            boton_proceed.click()
            Log().info(" Da click en el boton continuar")
            



        except Exception as e:
            Log().error(
                "No se pudo darle click al boton proceed, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        # Obtiene el total a pagar
        try:
            obtenertotal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.text_xpath_total))).text
            Log().info(" Obtiene el total a pagar")
            



        except Exception as e:
            Log().error(
                "No se pudo obtener el total a pagar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise


        # Da click en boton cash
        try:
            boton_cash = self.wait.until(conditions.clickable((By.XPATH, Configuracion.boton_xpath_ANG)))
            boton_cash.click()
            Log().info(" Da click en el boton cash")



        except Exception as e:
            Log().error(
                "No se pudo darle click al boton para digitar el efectivo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

         # Da click en boton caja
        try:
            boton_caja = self.wait.until(conditions.clickable((By.XPATH, Configuracion.boton_xpath_caja)))
            boton_caja.click()
            Log().info(" Da click en el boton para seleccionar la caja")



        except Exception as e:
            Log().error(
                "No se pudo darle click al boton para seleccionar la caja, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        #Selecciona la caja
        try:
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.DOWN) \
                .send_keys(Keys.ENTER) \
                .pause(1) \
                .release()
            action.perform()
            Log().info("Selecciona la caja")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)



        except Exception as e:
            Log().error(
                "No se pudo seleccionar la caja, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        # Escribe el total
        try:
            escribetotal = self.wait.until(conditions.visibility((By.XPATH, Configuracion.id_escribirtotal)))
            escribetotal.send_keys(obtenertotal)
            Log().info(" Escribe el total a pagar")



        except Exception as e:
            Log().error(
                "No se pudo escribir el total a pagar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        # Da clic en el boton para agregar el total
        try:
            agregatotal = self.wait.until(conditions.clickable((By.XPATH, Configuracion.boton_agregarmontoapagar)))
            agregatotal.click()
            Log().info(" Da click en el boton para agregar el total a pagar")
            
            


        except Exception as e:
            Log().error(
                "No se realizo la acccion para darle click al boton de agregar el monto a pagar, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        # Va hacia abajo
        try:
            MoverpantallaVenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_desplazarabajoVenta)))
            MoverpantallaVenta.click()
            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(1) \
                .release()
                
            action.perform()


        except Exception as e:
            Log().error(
                "No se pudo desplazar hacia abajo, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise

        # Da clic en el boton para finalizar la venta
        try:
            finalizaventa = self.wait.until(conditions.clickable((By.XPATH, Configuracion.boton_xpath_checkout)))
            finalizaventa.click()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Log().info(" Da click en el boton para finalizar la venta")



        except Exception as e:
            Log().error(
                "No se pudo finalizar la venta, revise si el monto total si fue cubierto o si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return cerrarsesion.cerrarsesion()
            raise
        # Cierra el ticket

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.xpath_desplazarabajo)))
            Moverpantalla.click()


            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(1) \
                .release()
            action.perform()
            cierraticket = self.wait.until(conditions.clickable((By.XPATH, Configuracion.boton_xpath_cerrarticket)))
            cierraticket.click()
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            Log().info(" Da click en el boton para cerrar el ticket")



        except Exception as e:
                Log().error(
                    "No se pudo cerrar la ventana del ticket, revise si el xpath sigue siendo el mismo, para mas detalles del error consulte el reporte")
                timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
                img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
                Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
                self.driver.get_screenshot_as_file(img_name)
                return cerrarsesion.cerrarsesion()
                raise










