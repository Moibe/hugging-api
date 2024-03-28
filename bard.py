from gradio_client import Client

# Crear un cliente para la API
client = Client("https://moibe-video.hf.space/", hf_token="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")

# Especificar las rutas a los archivos de imagen y video
image_path = "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"
video_path = "https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4"

# Preparar los datos para la predicción
data = {
    "input1": image_path,  # Enviar la ruta de la imagen al componente 'input1'
    "input2": {"video": video_path},  # Enviar la ruta del video al componente 'input2'
}

# Ejecutar la predicción
result = client.predict(data, api_name="/predict")

# Imprimir el resultado
print(result)