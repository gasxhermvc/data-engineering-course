# %%
import requests
import json
import locale
# locale.setlocale(locale.LC_ALL, 'th_TH')

# %%
url = 'https://notify-api.line.me/api/notify'

# %%
token = 'X3esjhlASjGdwkNRRIkTsGLa-------------'

# %%
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

# %%
f = open('/python_scripts/logs/stats.json','r')
content = f.read()
f.close()

# %%
data = json.loads(content)

# %%
msg = 'พบตำแหน่งที่อยู่ภายในจังหวัดราชบุรีจำนวน ' +  locale.format("%d", data['stats_within'], grouping=True) + ' point(s)\nภายนอกจังหวัดจำนวน ' + locale.format("%d", data['stats_not_within'], grouping=True)  + ' point(s).'

# %%
r = requests.post(url, headers=headers, data = {'message':msg})
print (r.text)


