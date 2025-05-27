'''
5.1 En una consulta, obtener todos los cursos.
5.2 Realizar un ciclo repetitivo para obtener en cada iteración las 
	entregas por cada curso (con otra consulta), y presentar el promedio 
	de calificaciones de las entregas
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

cursos = session.query(Curso).all()

for e in cursos:
	entregas = []

	for t in cursos.tareas:
		entregas.extend(t.entregas) # Acumular entregas
    
    if entregas:
    	total = sum([float(entrega.calificacion) for entrega in entregas if entrega.calificacion is not None])
    	promedio = total / len(entregas)
    	print(f"Curso: {curso.titulo} - Promedio calificacion: {promedio.2f}")
    else:
    	print(f"Curso: {curso.titulo} - Sin entregas")