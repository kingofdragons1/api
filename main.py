from googleapiclient.discovery import build

api_key = "AIzaSyA7nB1coFcBh9YmMfHGmNpiLtu1SIhCSws"
youtube = build("youtube", "v3", developerKey=api_key)

video_id = "dQw4w9WgXcQ"
request = youtube.videos().list(part="snippet,contentDetails", id=video_id)
response = request.execute()

live_broadcast_content = response["items"][0]["snippet"]["liveBroadcastContent"]
video_type = response["items"][0]["snippet"]["description"]

if live_broadcast_content == "live":
    print("Тип видео: Прямая трансляция (Live Streaming)")
elif "Shorts" in video_type:
    print("Тип видео: Shorts")
else:
    print("Тип видео: Стандартное видео")
