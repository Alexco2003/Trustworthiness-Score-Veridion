def urlChecker(url):
    if url.startswith('https://'):
        return 1
    return 0

def main():
    print(urlChecker('http://www.google.com'))
    print(urlChecker('https://www.google.com'))
