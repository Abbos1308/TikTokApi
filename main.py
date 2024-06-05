import random
from fastapi import FastAPI, HTTPException
import requests
from helper import random_ua, get_content
from fastapi.responses import FileResponse


app = FastAPI()

@app.get("/")
def hello():
    return {"say":"This is API for download tiktok video."}

@app.get("/tiktok/")
async def download_tiktok_video(url: str):
    
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '53',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'pll_language=en; PHPREFS=full',
        'Origin': 'https://tiktap.io',
        'Referer': 'https://tiktap.io/',
        'Sec-Ch-Ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': random_ua()
    }

    data = {
        'url': url,
    }

    headers["Content-Length"] = str(len(str(data)))

    res = requests.post("https://godownloader.com/api//tiktok-no-watermark-free", data=data, headers=headers)
    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail="Failed to fetch video data")
    response_json = res.json()
    if not res.text.startswith("{"):
        return {"status":False}
    if response_json["status"] != "success":
        raise HTTPException(status_code=400, detail="Failed to fetch video data")

    video_data = response_json["no_watermark"]
    if video_data:
        return video_data
    video_url = None

    if "nwm_video_url_HQ" in video_data.keys():
        video_url = video_data["nwm_video_url_HQ"]
    elif "nwm_video_url" in video_data.keys():
        video_url = video_data["nwm_video_url"]
    else:
        pass
        #raise HTTPException(status_code=400, detail="No suitable video URL found")

    #download_result = get_content(video_url, output_name)
    #if not download_result:
        #raise HTTPException(status_code=500, detail="Failed to download video")
    return {"video_url":video_url,"data":response_json}
    #return FileResponse(output_name)

