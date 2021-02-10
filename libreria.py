#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pg

class Base:
    nombre=''
    host=''
    puerto=5432
    usuario=''
    pasword=''

    def __init__(self, nombre, host, puerto=5432, usuario='', password=''):
        self.nombre=nombre
        self.host=host
        self.puerto=puerto
        if usuario:
            self.usuario = usuario
        if password:
            self.password = password

    def conecta(self):
        #self.db = pg.DB()
        
        try:
            if self.usuario != '':
                self.db = pg.connect(dbname=self.nombre,  host=self.host, port=self.puerto, passwd=self.password, user=self.usuario)   
            else:
                self.db = pg.connect(self.nombre, self.host, self.puerto)
        except TypeError:
            return 'Error BD argumentos'
        except SyntaxError:
            return 'Error BD argumentos duplicados'
        except:
            return 'Error desconocido conectanco a' + self.nombre
        return 'Conectado'

    def borraTabla(self, tabla):
        sql = 'DROP TABLE ' + tabla + ';'
        try:
            res=self.db.query(sql)
        except:
            return 'Error borrando tabla'
        return 'Tabla borrada'

    def creaTabla(self, nombre, campos):
        sql='CREATE TABLE ' + nombre + ' ("'
        for x in campos:
            campo=x.split(':')[0]
            tipo=x.split(':')[1]
            sql += campo + '" ' + tipo + ', "'
        
        sql=sql[:len(sql)-3]
        sql += ");"
        try:
            res=self.db.query(sql)
            return 'Creada tabla ' + nombre
        except:
            if self.db.error[-15:-1] == 'already exists':
                self.borraTabla(nombre)
                res=self.db.query(sql)
            return 'Error creando tabla '+ nombre 
        
    def anadeRegistro(self, tabla, campos, valores):
        sql='INSERT INTO ' + tabla + ' ("'
        for a in campos:
            sql += a.split(":")[0] + '", "'
        
        sql=sql[:len(sql)-3] + ') VALUES ('
        n=0
        for a in valores:
            tipo = campos[n].split(':')[1]
            if tipo[0:7] == 'varchar':
                tipo='varchar'

            if a=='':
                a='Null'
                tipo='integer'
            sql += case(tipo) + a + case(tipo) + ', ' 
            n += 1
        sql = sql[:len(sql)-2] + ');'
        try:
            res = self.db.query(sql)
        except:
            print(sql)
            return 'Error añadiendo datos'
        
    def existeTabla(self, tabla):
        sql="SELECT table_name FROM information_schema.columns WHERE table_name='" + tabla + "'"
        res = self.db.query(sql)
        return res.ntuples()
        
def case(argumento):
    dicc = {
        'varchar' : "'",
        'char' : "'",
        'time' : "'",
        'timestamp' : "'",
        'date' : "'",
        'integer' : '',
        'double' : '',
        'float' : ''
    }
    return dicc.get(argumento, 'Null')
