import os
import base64
import requests as r

auth = ("marcinliebiediew", os.environ.get('GITHUB_PERSONAL_ACCESS_TOKEN'))
res = r.get(f"https://api.github.com/repos/marcinliebiediew/career/contents/roadmap.png",
            auth=auth)  # , headers={"Accept": "application/vnd.github.v3+json"})
content = base64.b64decode(res.json()['content'])
with open("/home/marcin/Pictures/wallpapers/diagram.png", 'wb') as f:
    f.write(content)
