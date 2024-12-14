
import requests

def get_youtube_links(search_query):
    api_key = "AIzaSyBnZCBkpJz0ZEcMR6P61z3Sx6AaLZBMWT8"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_query}&key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        print("API Response:", data)  
        
        if 'error' in data:
            print(f"API Error: {data['error']['message']}")
            return []
        
        video_links = []
        for item in data.get('items', []):
            if item['id']['kind'] == 'youtube#video':
                video_links.append(f"https://www.youtube.com/watch?v={item['id']['videoId']}")
        
        return video_links
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return []

links = get_youtube_links("skincare")
for link in links:
    print(link)
