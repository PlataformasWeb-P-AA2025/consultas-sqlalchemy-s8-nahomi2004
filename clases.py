from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


# se importa información del archivo configuracion
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Departamento(Base):
    __tablename__ = 'departamento'
    id       = Column(Integer, primary_key=True)
    nombre   = Column(String(100))
    cursos   = relationship('Curso', back_populates='departamento')

    def __repr__(self):
        return f"Departamento(id='{self.id}', nombre='{self.nombre}...')"

class Instructor(Base):
    __tablename__ = 'instructor'
    id       = Column(Integer, primary_key=True)
    nombre   = Column(String(200))
    cursos   = relationship('Curso', back_populates='instructor')

    def __repr__(self):
        return f"Instructor(id='{self.id}', nombre='{self.nombre}...')"

class Curso(Base):
    __tablename__ = 'curso'
    id              = Column(Integer, primary_key=True)
    titulo          = Column(String(200))
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    instructor_id   = Column(Integer, ForeignKey('instructor.id'))
    departamento    = relationship('Departamento', back_populates='cursos')
    instructor      = relationship('Instructor',  back_populates='cursos')
    inscripciones   = relationship('Inscripcion', back_populates='curso')
    tareas          = relationship('Tarea',       back_populates='curso')

class Estudiante(Base):
    __tablename__ = 'estudiante'
    id             = Column(Integer, primary_key=True)
    nombre         = Column(String(200))
    inscripciones  = relationship('Inscripcion', back_populates='estudiante')
    entregas       = relationship('Entrega',     back_populates='estudiante')

    def __repr__(self):
        return f"Estudiante(id='{self.id}', nombre='{self.nombre}')"



class Inscripcion(Base):
    __tablename__ = 'inscripcion'
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'), primary_key=True)
    curso_id      = Column(Integer, ForeignKey('curso.id'),      primary_key=True)
    fecha_inscripcion = Column(DateTime)
    estudiante    = relationship('Estudiante', back_populates='inscripciones')
    curso         = relationship('Curso',      back_populates='inscripciones')

class Tarea(Base):
    __tablename__ = 'tarea'
    id        = Column(Integer, primary_key=True)
    curso_id  = Column(Integer, ForeignKey('curso.id'))
    titulo    = Column(String(200))
    fecha_entrega = Column(DateTime)
    curso     = relationship('Curso',    back_populates='tareas')
    entregas  = relationship('Entrega',  back_populates='tarea')

    def __repr__(self):
        return f"Tarea(id='{self.id}', curso_id='{self.curso_id}', titulo='{self.titulo}', fecha_entrega='{self.fecha_entrega}')"

class Entrega(Base):
    __tablename__ = 'entrega'
    id          = Column(Integer, primary_key=True)
    tarea_id    = Column(Integer, ForeignKey('tarea.id'))
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'))
    fecha_envio = Column(DateTime)
    calificacion = Column(Numeric)
    tarea        = relationship('Tarea',     back_populates='entregas')
    estudiante   = relationship('Estudiante',back_populates='entregas')

    def __repr__(self):
        return f"Entrega(id='{self.id}', tarea_id='{self.tarea_id}', estudiante_id='{self.estudiante_id}', fecha_envio='{self.fecha_envio}', calificacion='{self.calificacion}, tarea='{self.tarea}', estudiante='{self.estudiante}')"

Base.metadata.create_all(engine)
