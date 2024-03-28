#from gradio_client import Client
import gradio_client

#Los dos inguales.
client = gradio_client.Client("Moibe/sepia")
#client = Client("https://moibe-sepia.hf.space/--replicas/dr0s1/")

#imagenLista = gradio_client.file("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Microsoft_.NET_logo.svg/1024px-Microsoft_.NET_logo.svg.png")
imagenLista = gradio_client.file("sepia.webp")

result = client.predict(
    #"https://as2.ftcdn.net/v2/jpg/00/34/98/63/1000_F_34986397_49voRCjOO8kZrKqNo8O5OqrJV1I4wRjr.jpg", 
    imagenLista,
    api_name='/predict')

print(result)

