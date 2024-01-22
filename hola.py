# from gradio_client import Client

# client = Client("https://moibe-video.hf.space/--replicas/4nh1z/")
# result = client.predict()
# print(result)

from gradio_client import Client

#client = Client("https://lightricks-longanimatediff.hf.space/--replicas/yhkq0/")
#client = Client("https://lightricks-longanimatediff.hf.space/--replicas/moi/yhkq0/api/predict")

# Establece el encabezado Authorization
#client.headers["Authorization"] = "Bearer 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"



client = Client("http://127.0.0.1:7860/")
result = client.predict(
		"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# filepath  in 'input1' Image component
		"https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4",	# Dict(video: filepath, subtitles: filepath | None)  in 'input2' Video component
		api_name="/predict"
)
print(result)

