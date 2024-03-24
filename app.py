import requests

url = 'https://wwwapi.kugou.com/play/songinfo?srcappid=2919&clientver=20000&clienttime=1711282649689&mid=192c55f7a80b5d730a02d045907da863&uuid=192c55f7a80b5d730a02d045907da863&dfid=2C7fDh4HYEtu1hGMQZ4VJA6U&appid=1014&platid=4&encode_album_audio_id=5p0wxwec&token=&userid=0&signature=02dee11553a7aa331df084f578ed8759'
headers = {
    'authority': 'wwwapi.kugou.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'origin': 'https://www.kugou.com',
    'referer': 'https://www.kugou.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

response = requests.get(url, headers=headers)
json_data = response.json()
print(json_data)

# 解析json
album_audio_id = json_data['data']['album_audio_id']
audio_name = json_data['data']['audio_name']
author_name = json_data['data']['author_name']
song_name = json_data['data']['song_name']
audio_url = json_data['data']['play_url']

print(f"专辑音频ID：{album_audio_id}")
print(f"音频名称：{audio_name}")
print(f"作者：{author_name}")
print(f"歌曲名称：{song_name}")
print(f"音频URL：{audio_url}")
