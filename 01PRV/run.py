import os
import time
from unittest import defaultTestLoader
from common.HTMLReport import HTMLTestRunner
from common.globalparam import report_path, case_path
import mysql.connector

discover = defaultTestLoader.discover(start_dir=case_path, pattern='Proveedores.py', top_level_dir=None)
timeStrmap = time.strftime('%d_%m_%Y_%H_%M_%S')
if not os.path.exists(report_path + '/' + str(time.strftime("%Y"))):
    os.makedirs(report_path + '/' + str(time.strftime("%Y")))

if not os.path.exists(report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b"))):
    os.makedirs(report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")))

if not os.path.exists(
        report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")) + '/' + str(time.strftime("%d"))):
    os.makedirs(
        report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")) + '/' + str(time.strftime("%d")))

file_name = report_path + '/' + str(time.strftime("%Y")) + '/' + str(time.strftime("%b")) + '/' + str(
    time.strftime("%d")) + '/' + "{}-{}.htmlexecute".format("Reporte de pruebas", str(timeStrmap))
fp = open(file_name, 'wb')
new_path = file_name[0:-13] + ".html"

if __name__ == "__main__":
    runner = HTMLTestRunner(stream=fp, title=u'Reporte de pruebas', description='Detalles')
    runner.run(discover)
    fp.close()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="automatizacion"
    )
    if (mydb):
        print("Conexión exitosa")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT count(*) FROM guardar WHERE color='verde' AND  ventana='01PRV'")
    myresult = mycursor.fetchall()
    value = myresult[-1][-1]
    "print(value)"
    if (value != 0):
        sql = "UPDATE guardar SET link = %s WHERE color=%s AND  ventana=%s"
        val = (new_path, "verde", "01PRV")
        mycursor.execute(sql, val)
        mydb.commit()
    else:
        sql = "INSERT INTO guardar (link, color, ventana) VALUES (%s, %s, %s)"
        val = (new_path, "verde", "01PRV")
        mycursor.execute(sql, val)
        mydb.commit()
    os.rename(file_name, new_path)
