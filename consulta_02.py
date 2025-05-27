'''
2.	Todos los departamentos que tengan notas de entregas menores 
	o iguales a 0.3 . En función de los departamentos, presentar el 
	nombre del departamento y el número de cursos que tiene cada 
	departamento
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

# Lo que obtengo es el nombre del departamento
# Y el numero de cursos que cada uno tiene
# trazo el camino con ayuda de join
# filtro aquellos Departamentos que tengas entregas con 
# notas mejores a 0.3
# finalmente agrupo los departamentos 
departamentos_con_bajas_notas = session.query(
                                    Departamento.nombre,
                                    Entrega.calificacion,
                                    func.count(Curso.id).label('cantidad_cursos')
                                ).\
                                join(Departamento.cursos).\
                                join(Curso.tareas).\
                                join(Tarea.entregas).\
                                filter(Entrega.calificacion <= 0.3).\
                                group_by(Departamento.id).all()

for e in departamentos_con_bajas_notas:
    print(e)
    print("")