
# A cada parroaquia preguntar el número de establecimientos


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Parroquia, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()


parroquias = session.query(Parroquia).all()

for p in parroquias:
    print("Parroquia: %s Número de establecimiento:%d"% (p.nombre,p.numero_establecimientos_parroquia()))
    
print("-------------------------------------------------------------------------------\n")