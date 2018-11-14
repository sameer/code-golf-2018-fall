import urllib.request as u

x = 0
for l in u.urlopen('https://pastebin.com/raw/vkAg5jZm').readlines():
    l = l.rstrip().decode('utf-8')
    if len(l) == 0 or 'TN' in l:
        continue
    print(l)
