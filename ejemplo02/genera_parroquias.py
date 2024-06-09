import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Parroquia, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

def carga_parroquias():
    with open('ejemplo02/data/Listado-Instituciones-Educativas-02.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            parroquia_nombre = row['Parroquia']
            codigo_division_parroquia = row['Código División Política Administrativa Parroquia']
            codigo_division_canton = row['Código División Política Administrativa Cantón']
            
            # Verificar si el cantón ya existe en la base de datos antes de insertarlo
            parroquia_existente = session.query(Parroquia).filter_by(nombre=parroquia_nombre, codigo_division_politica_administrativa_parroquia=codigo_division_parroquia).first()
            
            if not parroquia_existente:
                parroquia = Parroquia(nombre=parroquia_nombre, codigo_division_politica_administrativa_parroquia=codigo_division_parroquia, codigo_canton=codigo_division_canton)
                session.merge(parroquia)  # Utilizamos merge en lugar de add para evitar duplicados
            else:
                print(f"La parroqui '{parroquia_nombre}' ya existe en la base de datos.")

    session.commit()
    print("Datos cargados correctamente.")

if __name__ == "__main__":
    carga_parroquias()
