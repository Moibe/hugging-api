from gradio_client import Client

#Los dos inguales.
#client = Client("abidlabs/en2fr")
client = Client("https://abidlabs-en2fr.hf.space/--replicas/5x7vj/")

result = client.predict("Hello", api_name='/predict')

print(result)