def urlChecker(url):
    if url.startswith('http://'):
        return 0
    elif url.startswith('https://'):
        value = 1
        return value

def main():
    print(urlChecker('http://www.google.com'))
    print(urlChecker('https://www.google.com'))

if __name__ == '__main__':
    main()

# Change value to make sense
