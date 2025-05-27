'''
    Obtener todas las tareas asignadas a los siguientes estudiantes 

    Jennifer Bolton 
    Elaine Perez
    Heather Henderson
    Charles Harris

    En función de cada tarea, presentar el número de entregas que tiene
'''

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from clases import Entrega, Estudiante, Curso, Departamento, Inscripcion, Tarea

import pandas as pd

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Lo que obtengo es el titulo de la tarea, junto al nombre del estudiante
# luego con func cuento cuantas tareas por estudiante hay
# trazo el camino desde tareas a estudiante y con in_
# filtro los nombres de los estudiantes
# finalmente agrupo por tarea y listo!!

tareas_estudiantes = session.query(
                                    Tarea.titulo,
                                    Estudiante.nombre,
                                    func.count(Entrega.id).label('entregas_hechas')
                                ).\
                                join(Tarea.entregas).\
                                join(Entrega.estudiante).\
                                filter(
                                		Estudiante.nombre.in_(
                                			["Jennifer Bolton", "Elaine Perez", "Heather Henderson", "Charles Harris"])
                            			).\
                                group_by(Tarea.id).all()

for e in tareas_estudiantes:
    print(e)
    print("")