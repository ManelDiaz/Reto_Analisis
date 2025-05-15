import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Eliminar los CSV existentes si existen
csv_files = ['estudiantes.csv', 'asignaturas.csv', 'notas.csv']
for file in csv_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Deleted existing {file}")

fake = Faker('es_ES')

def should_introduce_error(error_probability=0.05):
    """Return True with the specified probability."""
    return random.random() < error_probability

# Generación de estudiantes
num_estudiantes = 1000
estudiantes = []
for i in range(1, num_estudiantes + 1):
    estudiante = {
        'id_estudiante': i,
        'nombre': fake.first_name() if not should_introduce_error() else None,
        'apellido': fake.last_name() if not should_introduce_error() else None,
        'edad': random.randint(18, 40) if not should_introduce_error() else 
               random.choice([None, random.randint(-5, 10), random.randint(80, 120)]),
        'sexo': random.choice(['M', 'F']) if not should_introduce_error() else 
               random.choice([None, 'X', '1', '']),
        'ciudad': fake.city() if not should_introduce_error() else None,
        'fecha_registro': fake.date_between(start_date='-3y', end_date='today') if not should_introduce_error() else 
                         random.choice([None, fake.date_between(start_date='-30y', end_date='-20y')])
    }
    estudiantes.append(estudiante)

df_estudiantes = pd.DataFrame(estudiantes)
df_estudiantes.fillna('null', inplace=True)
df_estudiantes.to_csv('estudiantes.csv', index=False)

# Generación de asignaturas con Faker
num_asignaturas = 30
departamentos = ['Ciencias', 'Humanidades', 'Ingeniería', 'Ciencias Sociales', 'Idiomas']
asignaturas = []
for i in range(1, num_asignaturas + 1):
    asignatura = {
        'id_asignatura': i,
        'nombre_asignatura': fake.job() if not should_introduce_error() else None,
        'departamento': random.choice(departamentos) if not should_introduce_error() else None,
        'creditos': random.randint(3, 6) if not should_introduce_error() else random.choice([None, -1, 0, 100])
    }
    asignaturas.append(asignatura)
df_asignaturas = pd.DataFrame(asignaturas)
df_asignaturas.fillna('null', inplace=True)
df_asignaturas.to_csv('asignaturas.csv', index=False)

# Generación de notas
notas = []
convocatorias = ['Ordinaria', 'Extraordinaria']

for estudiante in df_estudiantes['id_estudiante']:
    asignaturas_sample = random.sample(df_asignaturas['id_asignatura'].tolist(), k=3)
    for asignatura in asignaturas_sample:
        nota_record = {
            'id_estudiante': estudiante if not should_introduce_error() else random.choice([None, -100, 9999]),
            'id_asignatura': asignatura if not should_introduce_error() else random.choice([None, -5, 999]),
            'nota': round(random.uniform(0, 10), 1) if not should_introduce_error() else random.choice([None, -100, 9999]),
            'convocatoria': random.choice(convocatorias) if not should_introduce_error() else 
                           random.choice([None, '', 'Desconocida', 123]),
            'fecha_examen': fake.date_between(start_date='-2y', end_date='today') if not should_introduce_error() else
                           random.choice([None, fake.date_between(start_date='-30y', end_date='-20y')])
        }
        notas.append(nota_record)
df_notas = pd.DataFrame(notas)
df_notas['nota'] = df_notas['nota'].apply(lambda x: round(max(0, min(10, x)), 1) if pd.notna(x) and isinstance(x, (int, float)) else x)
df_notas.to_csv('notas.csv', index=False)