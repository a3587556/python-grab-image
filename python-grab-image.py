import urllib2
import urllib
import re
response = urllib2.urlopen('http://www.icosky.com/iconset/rounded-world-flags-icons/')
html = response.read()
regex = re.compile("<h3>.* \((.*) Icon")
output = regex.findall(html)
for i in range(0, len(output)):
    url = 'http://www.icosky.com/icon/48/Flag/Rounded%20World%20Flags/' + output[i] + '.png'
    print url
    path = 'new/' + output[i].replace(' Flag','') + '.png'
    urllib.urlretrieve(url, path)