'''
2.	Todos los departamentos que tengan notas de entregas menores 
	o iguales a 0.3 . En función de los departamentos, presentar el 
	nombre del departamento y el número de cursos que tiene cada 
	departamento
'''

from sqlalchemy import func

departamentos_con_bajas_notas = session.query(
    Departamento.nombre,
    func.count(Curso.id).label('cantidad_cursos')
).join(Departamento.cursos).\
    join(Curso.tareas).\
    join(Tarea.entregas).\
    filter(Entrega.calificacion <= 0.3).\
    group_by(Departamento.id).all()
