import requests

def upload_videos(video_url: str) -> list[dict]:

    url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"

    querystring = {"url": video_url}

    headers = {
        "X-RapidAPI-Key": "267589e023mshce8afb84c99fa6dp12b608jsn0fbeacf17759",
        "X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return (response.json()['links']['Download High Quality'])



# url = "https://www.facebook.com/ThebeautyofNature68/videos/556be9bf/558413234780734/"
# print(upload_videos(url))