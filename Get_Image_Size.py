from PIL import ImageFile
import requests

def get_image_size(url):
    response = requests.head(url)
    content_length = response.headers.get('content-length')
    if content_length:
        return int(content_length)
    chunk_size = 128
    image_data = requests.get(url, stream=True).iter_content(chunk_size=chunk_size)
    parser = ImageFile.Parser()
    for chunk in image_data:
        parser.feed(chunk)
        if parser.image:
            return len(chunk)
    return None

