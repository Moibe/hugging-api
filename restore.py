from gradio_client import Client

#Los dos inguales.
#client = Client("abidlabs/en2fr")
client = Client("https://modelscope-old-photo-restoration.hf.space/--replicas/qemf3/")

result = client.predict("https://as2.ftcdn.net/v2/jpg/00/34/98/63/1000_F_34986397_49voRCjOO8kZrKqNo8O5OqrJV1I4wRjr.jpg", api_name='/predict')

print(result)