import datetime

subs = {
    "year": datetime.datetime.now().year
}

template = """
<div class="project">
<img src="{img}" class="thumb">
<div class="blinds">
<div class="left"></div>
<div class="top"></div>
<div class="right"></div>
<img src="img/blank.png">
</div>
<h1>{title}</h1>
<div class="description">{desc}</div>
<a href="{link}" target="_blank">{link_text}</a>
</div>
"""

projects = [
    {
        "title": "Magic2",
        "img": "img/Magic2.jpg",
        "desc": "A Python-based GUI application for interpolating and analysing interferometry data. Created during an internship with the Plasma Physics group at Imperial College London.",
        "link": "https://github.com/jdranczewski/Magic2",
        "link_text": "GitHub"
    },
    {
        "title": "Dimension Surfer",
        "img": "img/DimSurf.jpg",
        "desc": "A Python game that showcases the mathematical concept of higher dimensions through a simple platform mechanic with a twist. Used Blender to generate level data.",
        "link": "https://github.com/jdranczewski/Dimension-Surfer-Project",
        "link_text": "GitHub"
    },
    {
        "title": "WikiTranslator",
        "img": "img/wiki.jpg",
        "desc": "A translation engine for words and phrases that uses Wikipedia's linked network of articles to find correct translations for complicated and scientific terms.",
        "link": "https://wikitranslator.github.io",
        "link_text": "Visit"
    }
]

projects_text = ""

for project in projects:
    projects_text += template.format(**project)

subs["projects"] = projects_text

# Open main.html
with open("index_template.html", "r") as f:
    original = f.read()

# Substitute style
converted = original.format(**subs)

# Save out.html
with open("index.html", "w") as f:
    original = f.write(converted)
