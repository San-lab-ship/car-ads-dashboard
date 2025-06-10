import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de Anuncios de Venta de Coches')

# Leer los datos del archivo CSV
# Asegúrate de que 'vehicles_us.csv' esté en la misma carpeta que 'app.py'
try:
    car_data = pd.read_csv('vehicles_us.csv')
    # Esta línea es para depuración. Verás la lista de columnas en tu app web.
    # Después de confirmar que funciona, puedes comentarla o borrarla.
    
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que esté en la misma carpeta que app.py.")
    st.stop() # Detiene la ejecución si el archivo no se encuentra

# Botón para construir el histograma
hist_button = st.button("Construir histograma")

if hist_button:
    # Escribir un mensaje
    st.write('Creando un histograma del kilometraje (mileage) de los vehículos')

    # Crear un histograma de la columna 'mileage'
    # NOTA: Asegúrate que el nombre de la columna 'mileage' coincida EXACTAMENTE con el de tu CSV
    fig_hist = px.histogram(car_data, x="mileage")
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para construir el gráfico de dispersión (scatter plot)
build_scatterplot = st.checkbox("Construir gráfico de dispersión")

if build_scatterplot:
    st.write('Creando un gráfico de dispersión de precios vs. kilometraje (mileage)')

    # Crear un gráfico de dispersión de 'mileage' vs 'price'
    # NOTA: Asegúrate que el nombre de la columna 'mileage' coincida EXACTAMENTE con el de tu CSV
    fig_scatter = px.scatter(car_data, x="mileage", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Puedes agregar más elementos de Streamlit aquí si el proyecto lo requiere,
# como selectbox, radio buttons, etc.
# Ejemplo de selectbox para seleccionar tipo de vehículo (descomentar para usar):
# if 'type' in car_data.columns: # Comprueba si la columna 'type' existe
#     selected_type = st.selectbox('Selecciona un tipo de vehículo:', car_data['type'].unique())
#     st.write(f'Has seleccionado: {selected_type}')


