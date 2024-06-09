import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Canton, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def carga_cantones():
    with open('ejemplo02/data/Listado-Instituciones-Educativas-02.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            canton_nombre = row['Cantón']
            codigo_division_canton = row['Código División Política Administrativa Cantón']
            codigo_division_provincia = row['Código División Política Administrativa Provincia']
            
            # Verificar si el cantón ya existe en la base de datos antes de insertarlo
            canton_existente = session.query(Canton).filter_by(nombre=canton_nombre, codigo_division_politica_administrativa_canton=codigo_division_canton).first()
            
            if not canton_existente:
                canton = Canton(nombre=canton_nombre, codigo_division_politica_administrativa_canton=codigo_division_canton, codigo_provincia=codigo_division_provincia)
                session.merge(canton)  # Utilizamos merge en lugar de add para evitar duplicados
            else:
                print(f"El cantón '{canton_nombre}' ya existe en la base de datos.")

    session.commit()
    print("Datos cargados correctamente.")

if __name__ == "__main__":
    carga_cantones()
