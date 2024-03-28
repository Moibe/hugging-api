from gradio_client import Client

# Crear un cliente para la API
#client = Client("https://moibe-video.hf.space/")
client = Client("https://moibe-video.hf.space/", hf_token="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")
#client = Client("https://moibe-video.hf.space/--replicas/cfj4a/", hf_token="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")
#client = Client("https://moibe-video.hf.space/--replicas/cfj4a/")

#try: 
		
result = client.predict(
		'https://as2.ftcdn.net/v2/jpg/00/34/98/63/1000_F_34986397_49voRCjOO8kZrKqNo8O5OqrJV1I4wRjr.jpg',	# filepath  in 'input1' Image component
		'https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4',	# Dict(video: filepath, subtitles: filepath | None)  in 'input2' Video component
							api_name='/predict'
)
print(result)
#except Exception as e:
	# Si se produce un error, ejecuta este código
#    print("Ocurrió un error", e)


