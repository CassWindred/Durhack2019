with open('apikey.txt') as f:
    api_key = f.readline()
    f.close
gmaps.configure(api_key)

