import requests

def display(value):
    pass

def get_value(url):
    result = False

    #get the value from the url
    response = requests.get(url)

    if response.status_code == 200:
        #convert to number and constrain within a range
        try:
            print response.text
            value = response.text.strip()
            if value.endswith('%'):
                result = {'type': 'percent', 'value': int(value.replace('%', ''))}
            else:
                result = {'type': 'absolute', 'value': int(value)}
        except ValueError:
            pass

    return result


print get_value('https://docs.google.com/spreadsheets/d/1jeHhw-KfUHlbeHGjvPrGESu6Qd9bFNgzCucxldac6UY/pub?gid=0&single=true&output=csv')