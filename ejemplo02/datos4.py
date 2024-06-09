
# A cada provincia preguntar la lista de parroquias


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Provincia, Base
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

provincias = session.query(Provincia).all()

for provincia in provincias:
    lista_parroquias = provincia.lista_parroquias()
    print("Provincia: %s, Lista de parroquias: %d" % (provincia.nombre, len(lista_parroquias)))
    #for parroquia in lista_parroquias:
    #   print(" : %s" % parroquia.nombre)
    
print("-------------------------------------------------------------------------------\n")

