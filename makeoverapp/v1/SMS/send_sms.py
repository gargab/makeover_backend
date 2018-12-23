import urllib2
import urllib

def send_sms(apikey, numbers, sender, message):
    data =  urllib.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib2.Request("https://api.txtlocal.com/send/?")
    f = urllib2.urlopen(request, data)
    fr = f.read()
    return(fr)
