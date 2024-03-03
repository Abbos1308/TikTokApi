
# Tiktok Video Downloader API

Download video from Tiktok by this API

## https://tiktokdownloaderapi.onrender.com/


```http
  GET /tiktok?url={tiktok_video_url}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `string` | **Required**. Your Video Link |

# Example for using this api for Python3
```python3
import requests
api_url = "https://tiktokdownloaderapi.onrender.com/tiktok"
link = ""  # TikTok video url 
params = {"url": link}
response = requests.get(api_url, params=params)
# If you want:
print(response.json())
```

# That's all!
## If you have any problem, please contact me:
https://t.me/ravshanov_dev
