import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia,Base
from configuracion import cadena_base_datos

# Crear conexión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Función para leer el archivo CSV y crear instancias de la entidad Provincia
def carga_provincias():
    with open('ejemplo02/data/Listado-Instituciones-Educativas-02.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')  # Especificar el separador como '|'
        for i, row in enumerate(reader, start=1):
            try:
                provincia_nombre = row['Provincia']
                codigo_division_provincia = row['Código División Política Administrativa Provincia']
                
                # Verificar si la provincia ya existe en la base de datos
                provincia_existente = session.query(Provincia).filter_by(nombre=provincia_nombre).first()
                
                if provincia_existente:
                    print(f"La provincia '{provincia_nombre}' ya existe en la base de datos.")
                else:
                    provincia = Provincia(nombre=provincia_nombre, codigo_division_politica_administrativa_provincia=codigo_division_provincia)
                    session.add(provincia)
                    print(f"Provincia '{provincia_nombre}' agregada a la base de datos.")
            except ValueError as e:
                print(f"Error en la fila {i}: {e}")
                continue           

    session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Crear las tablas si no existen
    carga_provincias()
