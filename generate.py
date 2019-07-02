import datetime

subs = {
    "year": datetime.datetime.now().year
}

template = """
<div class="project">
<h1>{title}</h1>
<div class="description">{desc}</div>
<a href="{link}" target="_blank">{link_text}</a>
</div>
"""

projects = [
    {
        "title": "Magic2",
        "desc": "A Python-based GUI application for interpolating and analysing interferometry data. Created during an internship with the Plasma Physics group at Imperial College London.",
        "link": "https://github.com/jdranczewski/Magic2",
        "link_text": "GitHub"
    },
    {
        "title": "Dimension Surfer",
        "desc": "A Python game that showcases the mathematical concept of higher dimensions through a simple platform mechanic with a twist. Used Blender to generate level data.",
        "link": "https://github.com/jdranczewski/Dimension-Surfer-Project",
        "link_text": "GitHub"
    },
    {
        "title": "WikiTranslator",
        "desc": "A translation engine for words and phrases that uses Wikipedia's linked network of articles to find correct translations for complicated and scientific terms. Work in progress!",
        "link": "https://github.com/jdranczewski/WikiTranslator",
        "link_text": "GitHub"
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