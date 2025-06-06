# Reto_Analisis

 Miembros del equipo:
 
  - Manel Diaz

  - Rubén Alsasua

  - Eneko Saez

 Enlace a github: https://github.com/ManelDiaz/Reto_Analisis

 ## Explicación de los pasos seguidos
1. **Generación de csv-s**: El archivo python generador.py genera tres conjuntos de datos (estudiantes, asignaturas y notas) con errores intencionales añadidos de forma controlada para simular escenarios reales de datos incompletos o mal formateados.
2. **EDA**: El notebook eda.ipynb realiza un análisis exploratorio de datos (EDA) mostrando estadísticas, distribuciones, valores faltantes y visualizaciones para los datasets de asignaturas, estudiantes y notas.
3. **Tratador**: El notebook tratador.ipynb se encarga del tratamiento de los datos. Se realican transformaciones, normalizaciones y otras operaciones para preparar la información de cara a la visualización.
4. **Visualizador**: Finalmente, en vistas.ipynb se generan las visualizaciones correspondientes. Este apartado muestra gráficamente los datos, facilitando la interpretación de la información obtenida en los pasos previos.

## Posibles vías de mejora
- Robustecer la limpieza y validación de datos para detectar y eliminar valores atípicos y errores.
- Automatizar la generación de reportes y visualizaciones interactivas para facilitar el análisis iterativo.
- Integrar tests unitarios y validación continua para asegurar la calidad en cada paso del proceso.

## Alternativas posibles
- Podríamos haber usado otras librerías de python, como:
  - Para análisis exploratorio de datos:
    - pandas-profiling
    - Sweetviz
    - D-Tale
  - Para visualización interactiva:
    - Plotly
    - Bokeh
    - Altair
  - Para manejo de grandes volúmenes:
    - Dask
    - Vaex
