from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from config import conditions
from config import Configuracion
from common.log import Log
from common.globalparam import img_path
import os
import time



class nuevoregistro:

    def nuevoregistro(self, conditions, Configuracion):
        """Abre la ventana para crear un nuevo registro"""
        self.wait = WebDriverWait(self.driver, 60)

        # Valida que la pantalla ejecutada para crear un nuevo registro sea correcta
        try:
            Crea = self.wait.until(conditions.visibility((By.XPATH, Configuracion.titulo_nuevo))).text
            self.assertEqual("VENDEDORES : PROPIEDADES", Crea, "La pantalla ejecutada es correcta")
            Log().info(" Se abrio la pantalla para el ingreso de un registro nuevo.")

        except Exception as e:
            Log().error(
                "La pantalla ejecutada no es correcta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida existencia de las etiquetas
        try:
            Codigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigo))).text
            self.assertEqual("Código", Codigo, "Campo visible")
            Log().info(" El campo 'Codigo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Codigo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigoalter))).text
            self.assertEqual("Código Alternativo", Codigoalter, "Campo visible")
            Log().info(" El campo 'Código Alternativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código Alternativo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Codigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_codigousuario))).text
            self.assertEqual("Código Usuario", Codigousuario, "Campo visible")
            Log().info(" El campo 'Código Usuario' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Código Usuario' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nomnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_nomnegocio))).text
            self.assertEqual("Nom Negocio", Nomnegocio, "Campo visible")
            Log().info(" El campo 'Nom Negocio' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Nom Negocio' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Docidentidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_docidentidad))).text
            self.assertEqual("Documento de Identidad", Docidentidad, "Campo visible")
            Log().info(" El campo 'Documento de Identidad' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Documento de Identidad' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Calle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_calle))).text
            self.assertEqual("Calle", Calle, "Campo visible")
            Log().info(" El campo 'Calle' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Calle' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Numpuerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_nropuerta))).text
            self.assertEqual("Nro. Puerta", Numpuerta, "Campo visible")
            Log().info(" El campo 'Nro. Puerta' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Nro. Puerta' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Esquinas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_esquinas))).text
            self.assertEqual("Esquinas", Esquinas, "Campo visible")
            Log().info(" El campo 'Esquinas' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Esquinas' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Telefonos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_telefonos))).text
            self.assertEqual("Teléfonos", Telefonos, "Campo visible")
            Log().info(" El campo 'Teléfonos' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Teléfonos' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Empresabase = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_empresabase))).text
            self.assertEqual("Empresa base", Empresabase, "Campo visible")
            Log().info(" El campo 'Empresa base' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Empresa base' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cuenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_cuenta))).text
            self.assertEqual("Cuenta", Cuenta, "Campo visible")
            Log().info(" El campo 'Cuenta base' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Cuenta' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Distribuidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_distribuidor))).text
            self.assertEqual("Distribuidor", Distribuidor, "Campo visible")
            Log().info(" El campo 'Distribuidor base' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Distribuidor' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Agencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_agencia))).text
            self.assertEqual("Agencia", Agencia, "Campo visible")
            Log().info(" El campo 'Agencia' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Agencia' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Oficina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_oficina))).text
            self.assertEqual("Oficina", Oficina, "Campo visible")
            Log().info(" El campo 'Oficina' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Oficina' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Deposito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_deposito))).text
            self.assertEqual("Depósito", Deposito, "Campo visible")
            Log().info(" El campo 'Depósito' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Depósito' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Modeloliquidacion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modeloliq))).text
            self.assertEqual("Modelo liquidación", Modeloliquidacion, "Campo visible")
            Log().info(" El campo 'Modelo liquidación' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Modelo liquidación' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Perfilmovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_perfilmovil))).text
            self.assertEqual("Perfil móvil", Perfilmovil, "Campo visible")
            Log().info(" El campo 'Perfil móvil' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Perfil móvil' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tipovendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipovendedor))).text
            self.assertEqual("Tipo de Vendedor", Tipovendedor, "Campo visible")
            Log().info(" El campo 'Tipo de Vendedor' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo de Vendedor' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # try:
        #     Usuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_usuario))).text
        #     self.assertEqual("Usuario", Usuario, "Campo visible")
        #     Log().info(" El campo 'Usuario' si se encuentra visible.")
        #
        # except Exception as e:
        #     Log().error(
        #         "El campo 'Usuario' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
        #     timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
        #     img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
        #     Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
        #     self.driver.get_screenshot_as_file(img_name)
        #     self.driver.close()
        #     self.driver.switch_to.window(self.driver.window_handles[0])
        #     self.driver.close()
        #     raise

        try:
            Plataformamovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_platmovil))).text
            self.assertEqual("Plataforma Móvil", Plataformamovil, "Campo visible")
            Log().info(" El campo 'Plataforma Móvil' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Plataforma Móvil' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Formulapedido = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_formulapedido))).text
            self.assertEqual("Fórmula pedido sugerido", Formulapedido, "Campo visible")
            Log().info(" El campo 'Fórmula pedido sugerido' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Fórmula pedido sugerido' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Habilitaencuestas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_habilitarencuestas))).text
            self.assertEqual("Habilitar Encuestas", Habilitaencuestas, "Campo visible")
            Log().info(" El campo 'Habilitar Encuestas' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Habilitar Encuestas' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False


        #Se realiza el ingreso de datos en los campos.

        try:
            Ccodigo = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigo)))
            Ccodigo.send_keys(Configuracion.Icodigo)
            Log().info(" Ingresa el codigo del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigoalter = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigoalter)))
            Ccodigoalter.send_keys(Configuracion.Icodigoalter)
            Log().info(" Ingresa el codigo alternativo del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo alternativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccodigousuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_codigousuario)))
            Ccodigousuario.send_keys(Configuracion.Icodigousuario)
            Log().info(" Ingresa el codigo usuario del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el codigo usuario, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnomnegocio = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nomnegocio)))
            Cnomnegocio.send_keys(Configuracion.Inomnegocio)
            Log().info(" Ingresa el Nom Negocio del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Nom Negocio, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdocidentidad = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_docidentidad)))
            Cdocidentidad.send_keys(Configuracion.Idocidentidad)
            Log().info(" Ingresa el Documento de Identidad del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Documento de Identidad, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ccalle = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_calle)))
            Ccalle.send_keys(Configuracion.Icalle)
            Log().info(" Ingresa la calle del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la calle, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cnropuerta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_nropuerta)))
            Cnropuerta.send_keys(Configuracion.Inropuerta)
            Log().info(" Ingresa el nro puerta del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el nro puerta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina1)))
            Cesquina1.send_keys(Configuracion.Iesquina1)
            Log().info(" Ingresa la Esquina 1 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la Esquina 1, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cesquina2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_esquina2)))
            Cesquina2.send_keys(Configuracion.Iesquina2)
            Log().info(" Ingresa la Esquina 2 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la Esquina 2, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono1 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono1)))
            Ctelefono1.send_keys(Configuracion.Itelefono1)
            Log().info(" Ingresa el Telefono 1 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 1, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctelefono2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_telefono2)))
            Ctelefono2.send_keys(Configuracion.Itelefono2)
            Log().info(" Ingresa el Telefono 2 del nuevo registro ")

        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar el Telefono 2, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cempresabase = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_empresabase)))
            Cempresabase.click()

            registro_empresabase = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='58']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_empresabase) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Empresa Base, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Ccuenta = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_cuenta)))
            Ccuenta.click()

            registro_cuenta = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='100% ZACATECANA']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_cuenta) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Cuenta, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdistribuidor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_distribuidor)))
            Cdistribuidor.click()
            
            registro_distribuidor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='500401']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_distribuidor) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Distribuidor, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Cagencia = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_agencia)))
            Cagencia.click()

            registro_agencia = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='Distribuidora Mabezihua (GUERRERO 76-522722-0001)']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_agencia) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Agencia, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Coficina = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_oficina)))
            Coficina.click()

            registro_oficina = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='76-522722D001']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_oficina) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Oficina, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdeposito = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_deposito)))
            Cdeposito.click()

            registro_deposito = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='4200']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_deposito) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Deposito, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloliq = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloliq)))
            Cmodeloliq.click()

            registro_modeloliq = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='1']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloliq) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Modelo Liquidación, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cperfilmovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_perfilmovil)))
            Cperfilmovil.click()

            registro_perfilmovil = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='3']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_perfilmovil) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Perfil Movil, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipovendedor = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipovendedor)))
            Ctipovendedor.click()

            registro_tipovendedor = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM01']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipovendedor) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Tipo Vendedor, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cusuario = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_usuario)))
            Cusuario.click()

            registro_usuario = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='mabvvv002']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_usuario) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Usuario, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cplatmovil = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_platmovil)))
            Cplatmovil.click()

            registro_platmovil = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='ANDROID']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_platmovil) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Plataforma Movil, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Moverpantalla = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_platmovil)))
            Moverpantalla.click()

            action = ActionChains(self.driver)
            action \
                .send_keys(Keys.SPACE) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se pudo mover la pantalla, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cformulapedido = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_formulapedido)))
            time.sleep(1)
            Cformulapedido = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_formulapedido)))
            Cformulapedido.click()

        except Exception as e:
            Log().error(
                "No se encontró el campo de Formula Pedido, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            registro_formulapedido = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='No Aplicar']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_formulapedido) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Formula Pedido, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chabilitarencuestas = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_habilitarencuestas)))
            Chabilitarencuestas.click()
            time.sleep(1)
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Habilitar Encuestas, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña Series

        try:
            Bseries = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_series)))
            Bseries.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")

        except Exception as e:
            Log().error(
                "No se dió click al botón Series, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevoserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_series)))
            Nuevoserie.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        #Valida Existencia etiquetas

        try:
            Serie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_serie))).text
            self.assertEqual("Serie", Serie, "Campo visible")
            Log().info(" El campo 'Serie base' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Serie' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Tipoimpresora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipoimpresora))).text
            self.assertEqual("Tipo Impresora", Tipoimpresora, "Campo visible")
            Log().info(" El campo 'Tipo Impresora' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo Impresora' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Puertoimpresora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_puertoimpresora))).text
            self.assertEqual("Puerto Impresora", Puertoimpresora, "Campo visible")
            Log().info(" El campo 'Puerto Impresora' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Puerto Impresora' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Impreslenguaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_impreslenguaje))).text
            self.assertEqual("Impresora + Lenguaje", Impreslenguaje, "Campo visible")
            Log().info(" El campo 'Impresora + Lenguaje' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Impresora + Lenguaje' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Clavecorr = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_clavecorr))).text
            self.assertEqual("Clave correlativo", Clavecorr, "Campo visible")
            Log().info(" El campo 'Clave correlativo' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Clave correlativo' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Desdenumero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_desdenumero))).text
            self.assertEqual("Desde número", Desdenumero, "Campo visible")
            Log().info(" El campo 'Desde número' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Desde número' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Hastanumero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_hastanumero))).text
            self.assertEqual("Hasta número", Hastanumero, "Campo visible")
            Log().info(" El campo 'Hasta número' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Hasta número' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Cserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_serie)))
            Cserie.click()

            registro_serie = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Mabezihua RUTA 01 (01)']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_serie) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Serie, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Ctipoimpresora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_tipoimpresora)))
            Ctipoimpresora.click()

            registro_tipoimpresora = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Serial']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_tipoimpresora) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Tipo Impresora, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cpuertoimpresora = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_puertoimpresora)))
            Cpuertoimpresora.click()

            registro_puertoimpresora = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='A']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_puertoimpresora) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Puerto Impresora, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            time.sleep(5)
            return False

        try:
            Cimpreslenguaje = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_impreslenguaje)))
            Cimpreslenguaje.click()

            registro_impreslenguaje = self.wait.until(conditions.visibility((By.XPATH, "//li[text()='Intermec Direct Protocol']")))

            action = ActionChains(self.driver)
            action \
                .click(registro_impreslenguaje) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Impresora Lenguaje, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cclavecorr = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_clavecorr)))
            Cclavecorr.send_keys(Configuracion.Iclavecorr)
            Log().info(" Ingresa la Clave Correlativo del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar la Clave Correlativo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cdesdenumero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_desdenumero)))
            Cdesdenumero.send_keys(Configuracion.Idesdenumero)
            Log().info(" Ingresa Desde Numero del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar Desde Numero, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Chastanumero = self.wait.until(conditions.visibility((By.XPATH, Configuracion.campo_hastanumero)))
            Chastanumero.send_keys(Configuracion.Ihastanumero)
            Log().info(" Ingresa Hasta Numero del nuevo registro ")
            
        except Exception as e:
            Log().error(
                "No se pudo encontrar el campo para ingresar Hasta Numero, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardarserie = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_serie)))
            Guardarserie.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio pestaña Documentos

        try:
            Bdocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_documentos)))
            Bdocumentos.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Documentos, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevodocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_documento)))
            Nuevodocumentos.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Validar Existencia Etiquetas
        try:
            Tipodocumento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodocumento))).text
            self.assertEqual("Tipo Documento", Tipodocumento, "Campo visible")
            Log().info(" El campo 'Tipo documento' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo documento' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Modeloimpresion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modeloimpresion))).text
            self.assertEqual("Modelo de Impresión", Modeloimpresion, "Campo visible")
            Log().info(" El campo 'Modelo de Impresión' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Modelo de Impresión' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingreso Valores

        try:
            Ctipodocumento = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocumento)))
            Ctipodocumento.click()

        except Exception as e:
            Log().error(
                "No se encontró el campo de tipo de documento, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
        
            registro_tipodocumento = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM10']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodocumento) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de tipo de documento, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloimpresion = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimpresion)))
            Cmodeloimpresion.click()
            
            registro_modeloimpresion = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 12899416']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloimpresion) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Modelo de Impresión, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardardocumentos = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_documento)))
            Guardardocumentos.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Cambio de pestaña documentos reparto

        try:
            Bdocreparto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_documentoreparto)))
            Bdocreparto.click()
            Log().info("Se hace el cambio de pestaña para continuar con el registro nuevo")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Documentos Reparto, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Nuevodocreparto = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Nuevo_documentoreparto)))
            Nuevodocreparto.click()
            Log().info(" Se presiona el boton 'Nuevo', para crear un nuevo registro.")

        except Exception as e:
            Log().error(
                "No se dió click al botón Nuevo, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Valida la existencia de las etiquetas

        try:
            Tipodocumento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_tipodocumento2))).text
            self.assertEqual("Tipo Documento 2", Tipodocumento2, "Campo visible")
            Log().info(" El campo 'Tipo Documento 2' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Tipo Documento 2' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Modeloimpresion2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.etiqueta_modeloimpresion2))).text
            self.assertEqual("Modelo de Impresión", Modeloimpresion2, "Campo visible")
            Log().info(" El campo 'Modelo de Impresión' si se encuentra visible.")

        except Exception as e:
            Log().error(
                "El campo 'Modelo de Impresión' no se muestra visible, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        # Ingresa Valores

        try:
            Ctipodocumento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_tipodocumento2)))
            Ctipodocumento2.click()

            registro_tipodocumento2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='PM93']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_tipodocumento2) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de tipo de documento, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Cmodeloimpresion2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.ayuda_modeloimpresion2)))
            Cmodeloimpresion2.click()

            registro_modeloimpresion2 = self.wait.until(conditions.visibility((By.XPATH, "//span[text()='_ 12899416']")))

            action = ActionChains(self.driver)
            action \
                .double_click(registro_modeloimpresion2) \
                .pause(0) \
                .release()
            action.perform()

        except Exception as e:
            Log().error(
                "No se encontró el registro deseado de Modelo de Impresión, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guardartipodocumento2 = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda_documentoreparto)))
            Guardartipodocumento2.click()
            Log().info(" Se presiona el boton 'Guardar', para guardar el registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False

        try:
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            time.sleep(1)
            Guarda = self.wait.until(conditions.visibility((By.XPATH, Configuracion.btn_Guarda)))
            Guarda.click()
            Log().info(" Se da clic en el boton Guardar; se debe crear un nuevo registro.")
            
        except Exception as e:
            Log().error(
                "No se dió click al botón Guardar, validar que la acción anterior haya finalizado,que el xpath sea el correcto o que la página no presente lentitud")
            timeStrmap = time.strftime('%Y%m%d_%H_%M_%S')
            img_name = os.path.join(img_path, "%s.png" % str(timeStrmap))
            Log().info(message=" Captura: %s  screen：%s" % (img_path, os.path.split(img_name)[1]))
            self.driver.get_screenshot_as_file(img_name)
            return False