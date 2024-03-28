from gradio_client import Client
import time

# Los dos iguales.
# client = Client("abidlabs/en2fr")
client = Client("https://multimodalart-stable-video-diffusion.hf.space/--replicas/6qs8e/")

result = client.predict("https://as2.ftcdn.net/v2/jpg/00/34/98/63/1000_F_34986397_49voRCjOO8kZrKqNo8O5OqrJVI4wRjr.jpg", api_name='/video')

# Espera hasta que la solicitud se complete
time.sleep(300)

# Imprime el resultado
print(result)