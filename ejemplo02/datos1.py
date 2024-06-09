
# A cada cantón pedirle el número de estudiantes

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Canton, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


cantones = session.query(Canton).all()

for c in cantones:
    print("Canton: %s Número de estudiantes:%d"% (c.nombre,c.numero_estudiantes_canton()))
    
print("-------------------------------------------------------------------------------\n")


