import csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Establecimiento, Parroquia, Base
from configuracion import cadena_base_datos

# Crear conexión con la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Función para leer el archivo CSV y crear instancias de la entidad Establecimiento
def carga_establecimientos():
    with open('ejemplo02/data/Listado-Instituciones-Educativas-02.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for i, row in enumerate(reader, start=1):
            try:
                establecimiento_nombre = row['Nombre de la Institución Educativa']
                codigo_amie = row['Código AMIE']
                codigo_division_parroquia = row['Código División Política Administrativa Parroquia'].strip()  # Asegúrate de obtener el valor correcto y eliminar espacios adicionales
                zona_administrativa = row['Zona Administrativa']
                denominacion_distrito = row['Denominación del Distrito']
                codigo_distrito = row['Código de Distrito']
                codigo_circuito_educativo = row['Código de Circuito Educativo']
                sostenimiento = row['Sostenimiento']
                regimen_escolar = row['Régimen Escolar']
                jurisdiccion = row['Jurisdicción']
                tipo_educacion = row['Tipo de Educación']
                modalidad = row['Modalidad']
                jornada = row['Jornada']
                nivel = row['Nivel']
                etnia = row['Etnia']
                acceso = row['Acceso']
                numero_estudiantes = int(row['Número de estudiantes'])
                numero_docentes = int(row['Número de docentes'])
                estado = row['Estado']

                # Obtener el objeto Parroquia
                parroquia = session.query(Parroquia).filter(Parroquia.codigo_division_politica_administrativa_parroquia==codigo_division_parroquia).first()
                

                # Crear el objeto Establecimiento
                establecimiento = Establecimiento(
                    nombre=establecimiento_nombre,
                    codigo_amie=codigo_amie,
                    parroquia=parroquia,  # Asignar el objeto Parroquia
                    zona_administrativa=zona_administrativa,
                    denominacion_distrito=denominacion_distrito,
                    codigo_distrito=codigo_distrito,
                    codigo_circuito_educativo=codigo_circuito_educativo,
                    sostenimiento=sostenimiento,
                    regimen_escolar=regimen_escolar,
                    jurisdiccion=jurisdiccion,
                    tipo_educacion=tipo_educacion,
                    modalidad=modalidad,
                    jornada=jornada,
                    nivel=nivel,
                    etnia=etnia,
                    acceso=acceso,
                    numero_estudiantes=numero_estudiantes,
                    numero_docentes=numero_docentes,
                    estado=estado
                )

                session.add(establecimiento)
            except ValueError as e:
                print(f"ValueError en la fila {i}: {e}")
                # Se puede implementar lógica para manejar la falta de 'codigo_division_parroquia'
                # continue  # Se puede comentar para continuar a pesar de errores de 'codigo_division_parroquia'
            except Exception as e:
                print(f"Error inesperado en la fila {i}: {e}")
                continue

    session.commit()
    print("Datos cargados correctamente.")

if __name__ == "__main__":
    # Crear las tablas si no existen
    Base.metadata.create_all(engine)
    carga_establecimientos()
