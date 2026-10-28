from urllib.parse import urlsplit



def normalize_url(url):
    result = urlsplit(url)
    
    return f"{result.netloc}{result.path}"

