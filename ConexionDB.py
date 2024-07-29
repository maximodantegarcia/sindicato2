import sqlite3

class ConexionDB:
    def __init__(self):
        self.conn = sqlite3.connect('sindicato.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sindicato (
            LEGAJO TEXT PRIMARY KEY,
            APELLIDO_Y_NOMBRE TEXT,
            DIRECCION TEXT,
            LOCALIDAD TEXT,
            CP TEXT,
            FECHA_INGRESO TEXT,
            ANTIGUEDAD TEXT,
            FECHA_DE_NACIMIENTO TEXT,
            EDAD TEXT,
            DNI TEXT,
            NRO TEXT,
            CAT TEXT,
            OFICINA TEXT,
            NOMBRE_OFICINA TEXT,
            SECRETARIA TEXT,
            SINDICATO TEXT,
            SEPELIO TEXT,
            MUTUAL TEXT,
            SOLO_4 TEXT,
            COSEGURO TEXT,
            SEGURO TEXT,
            PUESTO TEXT,
            SEXO TEXT,
            ESTUDIO TEXT,
            NRO_DE_AFILIADO TEXT,
            FECHA_DE_AFILIACION TEXT,
            CAMPO_EXTRA TEXT,
            FECHA_EXTRA TEXT
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def buscar_legajo(self, legajo):
        query = "SELECT * FROM sindicato WHERE LEGAJO = ?"
        self.cursor.execute(query, (legajo,))
        resultados = self.cursor.fetchall()
        return resultados

    def actualizar_legajo(self, valores):
        query = """
        UPDATE sindicato
        SET 
            APELLIDO_Y_NOMBRE = ?, DIRECCION = ?, LOCALIDAD = ?, CP = ?, 
            FECHA_INGRESO = ?, ANTIGUEDAD = ?, FECHA_DE_NACIMIENTO = ?, EDAD = ?, 
            DNI = ?, NRO = ?, CAT = ?, OFICINA = ?, NOMBRE_OFICINA = ?, SECRETARIA = ?, 
            SINDICATO = ?, SEPELIO = ?, MUTUAL = ?, SOLO_4 = ?, COSEGURO = ?, 
            SEGURO = ?, PUESTO = ?, SEXO = ?, ESTUDIO = ?, NRO_DE_AFILIADO = ?, 
            FECHA_DE_AFILIACION = ?, CAMPO_EXTRA = ?, FECHA_EXTRA = ?
        WHERE LEGAJO = ?
        """
        valores_actualizados = (
            valores['APELLIDO_Y_NOMBRE'], valores['DIRECCION'], valores['LOCALIDAD'], valores['CP'], 
            valores['FECHA_INGRESO'], valores['ANTIGUEDAD'], valores['FECHA_DE_NACIMIENTO'], valores['EDAD'], 
            valores['DNI'], valores['NRO'], valores['CAT'], valores['OFICINA'], valores['NOMBRE_OFICINA'], valores['SECRETARIA'], 
            valores['SINDICATO'], valores['SEPELIO'], valores['MUTUAL'], valores['SOLO_4'], valores['COSEGURO'], 
            valores['SEGURO'], valores['PUESTO'], valores['SEXO'], valores['ESTUDIO'], valores['NRO_DE_AFILIADO'], 
            valores['FECHA_DE_AFILIACION'], valores['CAMPO_EXTRA'], valores['FECHA_EXTRA'], valores['LEGAJO']
        )
        self.cursor.execute(query, valores_actualizados)
        self.conn.commit()

    def obtener_bajas(self):
        query = "SELECT * FROM sindicato WHERE FECHA_EXTRA IS NOT NULL AND SINDICATO IS NOT NULL"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        return resultados

    def cerrar(self):
        self.conn.close()
