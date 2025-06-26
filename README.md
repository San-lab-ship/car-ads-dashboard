# Tablero Coches: Un Dashboard Interactivo con Streamlit, Desplegado en Render

Este proyecto es una aplicación web interactiva desarrollada con Streamlit para el análisis exploratorio de datos de anuncios de anuncios de venta de coches. Permite a los usuarios visualizar distribuciones y relaciones entre diferentes características de los vehículos a través de histogramas y gráficos de dispersión.

## Descripción del Problema

Este proyecto aborda un análisis exploratorio de un conjunto de datos de anuncios de venta de coches usados en Estados Unidos. Aunque el dataset ofrece múltiples dimensiones para el análisis, el enfoque de este trabajo no se centra en modelado predictivo ni inferencias estadísticas, sino en entender la calidad y distribución de los datos, identificar patrones relevantes y sentar las bases para futuras investigaciones más profundas.

## Arquitectura del Proyecto
![image](https://github.com/user-attachments/assets/4bfd4bac-0e45-4998-b8c3-83512f07da45)

## Metodología

1. **Carga y limpieza de datos**  
   - Identificación y tratamiento de valores nulos en variables críticas (`model_year`, `odometer`, `cylinders`)
   - Imputación por mediana para `model_year`
   - Eliminación de filas incompletas que afectan la fiabilidad del análisis

2. **Análisis univariado y bivariado**  
   - Visualización de la distribución de precios
   - Exploración de la relación entre precio y kilometraje (`odometer`)

3. **Visualización interactiva**  
   - Histogramas y gráficos de dispersión utilizando herramientas avanzadas

## Parámetros

- Relleno de valores faltantes con la mediana (`model_year`)
- Eliminación de datos incompletos en variables claves para las visualizaciones
- Filtrado de outliers visualmente identificados en `price` y `odometer`

## Visualizaciones

- **Tablero Coches**
[https://tablero-coches-streamlit.onrender.com/](https://tablero-coches-streamlit.onrender.com/)

- **Distribución de Precios**  
![image](https://github.com/user-attachments/assets/17de7644-d5f9-4936-a920-c2a976f4e99b)

- **Relación Precio vs Kilometraje**  
![image](https://github.com/user-attachments/assets/dd519114-7040-4b60-a30e-fa138298e6ab)


## Tecnologías Utilizadas

✔️ Python 3.10
✔️ Pandas
✔️ NumPy
✔️ Scikit-learn
✔️ Plotly
✔️ Seaborn
✔️ Matplotlib
✔️ Folium
✔️ Jupyter Notebook / Google Colab
✔️ Joblib
✔️ Streamlit
✔️ io
✔️ google.colab.files
✔️ Draw.io
✔️ Render

## Conclusión del Proyecto

El conjunto de datos original contenía 51,525 registros y 13 atributos, pero presentaba importantes desafíos de completitud: 3,619 valores nulos en model_year, 5,260 en cylinders, 7,892 en odometer, y cerca del 50 % de los registros sin información en is_4wd. Durante la etapa de preparación de datos, se imputó la mediana para model_year y se eliminaron las filas con valores nulos en campos críticos como price, odometer, cylinders y condition, lo que resultó en un conjunto limpio de 39,185 registros, equivalente a una reducción del ~23.9 %.

El análisis estadístico posterior mostró que la variable price presenta una fuerte asimetría positiva, con una media cercana a los $12,132, una mediana de $9,000 y un valor máximo extremo de $375,000. Por su parte, el odometer exhibe una media de aproximadamente 115,553 millas, una mediana de 113,000 y un rango que se extiende hasta las 990,000 millas, lo cual refleja una considerable heterogeneidad en el uso de los vehículos.

Estas observaciones estadísticas respaldan las visualizaciones desarrolladas, permitiendo una interpretación sólida sobre la distribución de precios y su relación con el kilometraje, aportando así una base confiable para futuras investigaciones sobre el comportamiento del mercado de vehículos usados en EE. UU.

## Estructura del proyecto

```python
.
├── app.py               # Código principal de la aplicación Streamlit
├── vehicles_us.csv      # Conjunto de datos de anuncios de coches
├── requirements.txt     # Lista de dependencias del proyecto
├── .gitignore           # Archivos y carpetas ignoradas por Git
├── README.md            # Documentación del proyecto
└── notebooks
    └── EDA.ipynb        # Análisis exploratorio de datos en Jupyter Notebook
