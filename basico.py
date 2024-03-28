#from gradio_client import Client
import gradio_client
import time

# Los dos iguales.
client = gradio_client.Client("Moibe/basico")
#client = Client("https://multimodalart-stable-video-diffusion.hf.space/--replicas/6qs8e/")

result = client.predict(
		"Moibe",	# str  in 'name' Textbox component
		api_name="/predict"
)

# Espera hasta que la solicitud se complete
#time.sleep(300)

# Imprime el resultado
print(result)