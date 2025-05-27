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

# Otengo todos los cursos
cursos = session.query(Curso).all()

# Luego de eso recorro cada objeto con un for, y dentro de este for voy
# a realizar las entregas por curso y presentar su promedio de calificacion
# Hay que recordar que Cursos tiene una lista de entregas en este caso, 
# entonces a esa lista la debo recorrer con otro for y en este caso
# me ayudo de un array para acumularlas en un solo lado y poder trabajar
# una vez reocrrido ese segundo for, debo comprobar si entregas esta lleno
# o no, asi sin preocupaciones, puedo sacar el promedio.
# El promedio lo saco sumando la calificacion por cada entrega (me ayudo
# de un ciclo for) En caso de que haya un valor None o nulo, pues no se suma
# se lo descarta. Finalmente a ese acumulador llamado total lo utilizamos 
# para sacar el promedio
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
