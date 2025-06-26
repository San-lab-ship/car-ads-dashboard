# Análisis de Anuncios de Venta de Coches

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
![image](https://github.com/user-attachments/assets/8be38f7b-b54f-4b48-8f28-4b004dd94a02)

## Tecnologías Utilizadas

✔️ Python 3.10  
✔️ Pandas  
✔️ NumPy  
✔️ Scikit-learn  
✔️ Plotly  
✔️ Folium  
✔️ Jupyter Notebook / Google Colab  
✔️ Joblib  
✔️ Draw.io (para esquemas y diagramas)

## Conclusión del Proyecto

Este proyecto ha logrado un análisis exploratorio inicial y visualizaciones claras de un conjunto de datos sobre anuncios de vehículos usados. Se aplicaron técnicas efectivas de limpieza de datos y se utilizaron gráficos para comprender la estructura y las relaciones del dataset. Estos primeros hallazgos ofrecen una base sólida para trabajos posteriores que podrían incluir predicción de precios, segmentación de mercado o estudios regionales sobre comportamiento de ventas.

## Estructura del proyecto

```python
- `app.py`: El código principal de la aplicación Streamlit.
- `vehicles_us.csv`: El conjunto de datos de anuncios de coches.
- `requirements.txt`: Lista de dependencias del proyecto.
- `notebooks/EDA.ipynb`: Jupyter Notebook con el análisis exploratorio de datos.
- `.gitignore`: Archivo para especificar archivos y directorios a ignorar por Git.
- `README.md`: Este archivo, con la descripción del proyecto.
