from flask import session
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from configuracion import cadena_base_datos

# Crear el motor de la base de datos
engine = create_engine(cadena_base_datos)
Base = declarative_base()

# Definición de modelos
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo_division_politica_administrativa_provincia = Column(String(10), nullable=False, index=True) 
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: id=%d, nombre='%s', codigo_division_politica_administrativa_provincia='%s'" % (
            self.id, self.nombre, self.codigo_division_politica_administrativa_provincia
        )
    
    def numero_docentes_provincia(self):
        total_docentes_provincia = 0
        for canton in self.cantones:
            total_docentes_canton = 0
            for parroquia in canton.parroquias:  
                total_docentes_parroquia = 0
                for establecimiento in parroquia.establecimientos:
                    total_docentes_parroquia += establecimiento.numero_docentes
                total_docentes_canton += total_docentes_parroquia
            total_docentes_provincia += total_docentes_canton 
        return total_docentes_provincia
    
    def lista_parroquias(self):
        parroquias_list = []
        for canton in self.cantones:
            parroquias_list.extend(canton.parroquias)
        return parroquias_list
     
    
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo_division_politica_administrativa_canton = Column(String(10), nullable=False, index=True)
    codigo_provincia = Column(String(10), ForeignKey('provincia.codigo_division_politica_administrativa_provincia'))
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    def __repr__(self):
        return "Canton: id=%d, nombre=%s, codigo=%s, provincia=%s" % (
            self.id, 
            self.nombre, 
            self.codigo_division_politica_administrativa_canton, 
            self.codigo_provincia
        )
  # A cada cantón pedirle el número de estudiantes
    def numero_estudiantes_canton(self):
        total_estudiantes_canton = 0
        for parroquia in self.parroquias:
            total_estudiantes_parroquia = 0
            for establecimiento in parroquia.establecimientos:
                total_estudiantes_parroquia += establecimiento.numero_estudiantes
            total_estudiantes_canton += total_estudiantes_parroquia
        return total_estudiantes_canton

class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo_division_politica_administrativa_parroquia = Column(String(10), nullable=False, index=True)
    codigo_canton = Column(String(10), ForeignKey('canton.codigo_division_politica_administrativa_canton'))
    canton = relationship("Canton", back_populates="parroquias")
    establecimientos = relationship("Establecimiento", back_populates="parroquia")

    def __repr__(self):
        return "Parroquia: id=%d, nombre=%s, codigo=%s, canton=%s" % (
            self.id, 
            self.nombre, 
            self.codigo_division_politica_administrativa_parroquia, 
            self.codigo_canton
        )
    def numero_establecimientos_parroquia(self):
        numero = 0
        for establecimiento in self.establecimientos:
            numero += 1
        return numero
    
    def lista_parroquias(self):
        parroquias_list = []
        for canton in self.cantones:
            parroquias_list.extend(canton.parroquias)
        return parroquias_list
    
    def tipos_jornada_establecimiento(self):
        jornadas_list = []
        for j in self.establecimientos:
            jornadas_list.append(j.jornada)
        return list(set(jornadas_list))

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(Integer, primary_key=True)
    codigo_amie = Column(String(10), nullable=False)
    nombre = Column(String(100), nullable=False)
    codigo_parroquia = Column(String(10), ForeignKey('parroquia.codigo_division_politica_administrativa_parroquia'))
    zona_administrativa = Column(String(100))
    denominacion_distrito = Column(String(100))
    codigo_distrito = Column(String(10))
    codigo_circuito_educativo = Column(String(100))
    sostenimiento = Column(String(100))
    regimen_escolar = Column(String(100))
    jurisdiccion = Column(String(100))
    tipo_educacion = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    nivel = Column(String(100))
    etnia = Column(String(100))
    acceso = Column(String(100))
    numero_estudiantes = Column(Integer)
    numero_docentes = Column(Integer)
    estado = Column(String(100))
    parroquia = relationship("Parroquia", back_populates="establecimientos")

    def __repr__(self):
        return "Establecimiento: id=%d, nombre=%s, codigo_amie=%s, codigo_parroquia=%s, zona_administrativa=%s, denominacion_distrito=%s, codigo_distrito=%s, codigo_circuito_educativo=%s, sostenimiento=%s, regimen_escolar=%s, jurisdiccion=%s, tipo_educacion=%s, modalidad=%s, jornada=%s, nivel=%s, etnia=%s, acceso=%s, numero_estudiantes=%d, numero_docentes=%d, estado=%s" % (
            self.id,
            self.nombre,
            self.codigo_amie,
            self.codigo_parroquia,
            self.zona_administrativa,
            self.denominacion_distrito,
            self.codigo_distrito,
            self.codigo_circuito_educativo,
            self.sostenimiento,
            self.regimen_escolar,
            self.jurisdiccion,
            self.tipo_educacion,
            self.modalidad,
            self.jornada,
            self.nivel,
            self.etnia,
            self.acceso,
            self.numero_estudiantes,
            self.numero_docentes,
            self.estado
        )

# Eliminar todas las tablas existentes (comentar/descomentar según sea necesario)

# Base.metadata.drop_all(engine)

# Crear todas las tablas

Base.metadata.create_all(engine)

# Mensaje de confirmación de creación de tablas
print("Creando tablas...")
Base.metadata.create_all(engine)
print("Tablas creadas:")
for table in Base.metadata.tables.keys():
    print(f" - {table}")
