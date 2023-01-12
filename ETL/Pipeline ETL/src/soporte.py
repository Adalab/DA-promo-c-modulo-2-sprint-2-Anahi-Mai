
import pandas as pd
import requests
from datetime import datetime, timedelta
import numpy as pd
import ast
from IPython.core.interactiveshell import InteractiveShell 
InteractiveShell.ast_node_interactivity = "all" 
import mysql.connector



class Subida_datos:

    def __init__(self, nombre_bbdd, contraseña):
        # nuestra clase va a recibir dos parámetros.
        self.nombre_bbdd = nombre_bbdd
        self.contraseña = contraseña


    def crear_bbdd(self):

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=self.contraseña)
      
        print("Conexión realizada con éxito")
    
        mycursor = mydb.cursor()

        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.nombre_bbdd};")
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)



    def crear_insertar_tabla(self,query):
    
   
        cnx = mysql.connector.connect(user='root', password=f"{self.contraseña}",
                                     host='127.0.0.1', database=f"{self.nombre_bbdd}")
   
        mycursor = cnx.cursor()
        
    
        try: 
            mycursor.execute(query)
            cnx.commit() 
            print('La query ha sido ejecutada con exito')
            
   
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)



