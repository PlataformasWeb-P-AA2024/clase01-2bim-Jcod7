
# A cada provincia perdile el número de docentes

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


provincias = session.query(Provincia).all()

for p in provincias:
    print("Provincia: %s Número de docentes:%d"% (p.nombre,p.numero_docentes_provincia()))
    
print("-------------------------------------------------------------------------------\n")