'''
1.	Obtener las entregas de todos los estudiantes que pertenecen al 
	departamento de Arte. En función de la entrega, presentar, nombre 
	del tarea, nombre del estudiante, calificación, nombre de instructor 
	y nombre del departamento
'''

# Tengo que pasar por entregas, estudiante, curso, departamento 
# Obtener un reporte de reacciones en función del número de 
# veces que fueron usadas

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from clases import Entrega, Estudiante, Curso, Departamento, Inscripcion

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

# Hice join hasta llegar a Departamento y de ahi filter
# Creo que esta mal, snif
# Voy desde Entrega Tarea Curso y Departamente y luego de Entrega Estudiante e Incripciones,
# esto es para asegurar que el estudiante realmente este inscrito
entregas_artes = session.query(Entrega).join(Estudiante.tarea).join(Tarea.curso).\
				join(Curso.departamento).join(Entrega.estudiante).\
				join(Estudiante.inscripciones).\
				filter(Departamento.nombre == 'Arte').all()

for e in entregas_artes:
	print(e)
	print("")
