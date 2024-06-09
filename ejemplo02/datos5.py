
# A cada parroquia preguntarle los tipos jornada de los establecimientos


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Parroquia, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


parroquias = session.query(Parroquia).all()

for p in parroquias:
    print("Parroquia: %s Tipos de jornada: %s" % (p.nombre, ', '.join(p.tipos_jornada_establecimiento())))
print("-------------------------------------------------------------------------------\n")