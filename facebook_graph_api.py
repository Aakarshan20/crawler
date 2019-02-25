import requests
import json
from  bs4 import BeautifulSoup

token = 'EAAZA46vOX0JUBAGPPHjpbWsOPmcfJxdVsLlqC0yVtV4967ghiOLC6ZCy8LhjHhgKELGLZCs5cLjf6QzUVE5zT9ErL7ZCEJtCo5u5OTNorLKhfa37Y5Ot9TdsPd5zJc8xRvMHg6pIeWPbdaQlhBjmzFMQo4ZADOaXs9QHyv9wmSDeENwcGauRyMxLBZCrD2T40ZD'
res = requests.get('https://graph.facebook.com/v3.2/me?access_token=%s' %(token))
jsondata = json.loads(res.text)
print(jsondata['id'])





