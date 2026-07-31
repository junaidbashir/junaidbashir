import json
from urllib.parse import quote as url_encode
# ==========================
# Load data
# ==========================

with open("cache/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

name = data["name"]
headline = data["headline"]
title = data["title"]
subtitle = data["subtitle"]
bio = "\n\n".join(
    [f"> {paragraph}" for paragraph in data["bio"]]
)
quote_text = data["quote"]
focus_title = data["focus_title"]

typing = data["typing"]

github_username = data["github"]
linkedin = data["linkedin"]
email = data["email"]

github_title = data["github_title"]

# ==========================
# Generate sections
# ==========================

focus = "\n".join(
    [f"- 🚀 {item}" for item in data["focus"]]
)

skills = ",".join(data["skills"])




typing_lines = ";".join(
    url_encode(line) for line in data["typing"]
)

typing_url = (
    "https://readme-typing-svg.demolab.com?"
    "font=Poppins"
    "&weight=700"
    "&size=26"
    "&duration=3200"
    "&pause=1200"
    "&center=true"
    "&vCenter=true"
    "&width=950"
    "&color=3A5F5B"
    f"&lines={typing_lines}"
)


# ==========================
# Banner
# ==========================

banner = """
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="./dark_mode.svg">

  <img
    src="./light_mode.svg"
    width="100%">
</picture>
"""

# ==========================
# README
# ==========================

readme = f"""
<div align="center">

{banner}

# {headline}

### ☁️ {title}

**{subtitle}**

<img src="{typing_url}" />

</div>

---

## 💫 Who I Am

{bio}


---

## {focus_title}

{focus}

---

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i={skills}&perline=7"/>

</div>

---

## {github_title}

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username={github_username}&show_icons=true&hide_border=true"/>

<img width="49%" src="https://streak-stats.demolab.com?user={github_username}&hide_border=true"/>

</div>

---

## ☁️ My Approach

> {quote_text}

---

<div align="center">

### 🤝 Connect With Me

[LinkedIn](https://linkedin.com/in/{linkedin}) •
[GitHub](https://github.com/{github_username}) •
[Email](mailto:{email})

</div>
"""

# Save README
# ==========================

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README generated successfully.")