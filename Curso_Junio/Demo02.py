from urllib import request
import json
url = "https://api.appnexus.com/currency?code=CLP"
rptaHttp = request.urlopen(url)
if(rptaHttp.status==200):
    buffer = rptaHttp.read()
    objJson = json.loads(buffer)
    print("version: ", objJson["response"]["dbg_info"]["version"])