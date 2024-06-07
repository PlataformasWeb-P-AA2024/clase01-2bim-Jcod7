from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import datetime

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados

class Club(Base):
    __tablename__ = 'club'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    deporte = Column(String(100))
    fundacion = Column(Integer, nullable=False)
    # Mapea la relación entre las clases
    # Club puede acceder a los jugadores asociados
    # por la llave foránea
    jugadores = relationship("Jugador", back_populates="club")

    
    def __repr__(self):
        return "Club: nombre=%s deporte=%s fundación=%d" % (
                          self.nombre, 
                          self.deporte, 
                          self.fundacion)
    
    def obtener_anios_vida(self):
        return datetime.datetime.now().year - self.fundacion

    
    def obtener_dorsales_jugadores(self):
        cadena = ""  # Inicializa una cadena vacía para almacenar los dorsales
        lista = []   # Lista opcional para almacenar los dorsales
        for jugador in self.jugadores:
            cadena = "%s%d\n" % (cadena, jugador.dorsal)  # Concatena el dorsal del jugador a la cadena
            #lista.append(jugador.dorsal)  # Opcional: agrega el dorsal del jugador a la lista
        return cadena  # Devuelve la cadena que contiene los dorsales
        #return lista  # Opcional: devuelve la lista de dorsales

    def obtener_suma_dorsales(self):
        # Suma los dorsales de todos los jugadores asociados al club
        suma = sum([jugador.dorsal for jugador in self.jugadores])
        return suma  # Devuelve la suma de los dorsales


class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String(100))
    # se agrega la columna club_id como ForeignKey
    # se hace referencia al id de la entidad club
    club_id = Column(Integer, ForeignKey('club.id'))
    # Mapea la relación entre las clases
    # Jugador tiene una relación con Club
    club  = relationship("Club", back_populates="jugadores")

    def __repr__(self):
        return "Jugador: %s - dorsal:%d - posición: %s" % (
                self.nombre, self.dorsal, self.posicion)

Base.metadata.create_all(engine)









