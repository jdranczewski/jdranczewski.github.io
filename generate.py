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
{links}
</div>

"""

link_template = '<a href="{link}" target="_blank">{link_text}</a>'

projects = [
    {
        "title": "Magic2",
        "img": "img/Magic2.jpg",
        "desc": "A Python-based GUI application for interpolating and analysing interferometry data. Created during an internship with the Plasma Physics group at Imperial College London.",
        "links": ["https://github.com/jdranczewski/Magic2"],
        "link_texts": ["GitHub"]
    },
    {
        "title": "WikiTranslator",
        "img": "img/wiki.jpg",
        "desc": "A translation engine for words and phrases that uses Wikipedia's linked network of articles to find correct translations for complicated and scientific terms.",
        "links": ["https://github.com/jdranczewski/WikiTranslator", "https://wikitranslator.github.io"],
        "link_texts": ["GitHub", "Visit"]
    },
    {
        "title": "CSSlides",
        "img": "img/CSSlides.jpg",
        "desc": "Winner in the Best Educational Hack category of IC Hack 2020. A slideshow editor focusing on giving you complete freedom in designing delightful transitions",
        "links": ["https://github.com/jdranczewski/ic-hack-2020", "https://csslides.netlify.app"],
        "link_texts": ["GitHub", "Try it"]
    },
    {
        "title": "Dimension Surfer",
        "img": "img/DimSurf.jpg",
        "desc": "A Python game that showcases the mathematical concept of higher dimensions through a simple platform mechanic with a twist. Used Blender to generate level data.",
        "links": ["https://github.com/jdranczewski/Dimension-Surfer-Project"],
        "link_texts": ["GitHub"]
    },
    {
        "title": "YouDecideWhoIAm",
        "img": "img/YDWIA.jpg",
        "desc": "An ID badge based on the Raspberry Pi Zero. In this project it randomly displayed audience submissions, but I've also used this hardware platform for other Pi experiments.",
        "links": ["https://github.com/jdranczewski/YouDecideWhoIAm"],
        "link_texts": ["GitHub"]
    },
    {
        "title": "DMX Controller",
        "img": "img/dmx.jpg",
        "desc": "Based on a PIC18 microprocessor with all of the code written in Assembly, this collaborative project outputs DMX (a data format for stage lighting).",
        "links": ["https://github.com/jdranczewski/DMXControllerProject"],
        "link_texts": ["GitHub"]
    },
    {
        "title": "SimpleWebStats",
        "img": "img/stats.jpg",
        "desc": "A very simple, GDPR-compliant web analytics app that gathers the bare minimum of information while respecting the users' privacy.",
        "links": ["https://github.com/jdranczewski/SimpleWebStats"],
        "link_texts": ["GitHub"]
    },
    {
        "title": "WYD Dictionary",
        "img": "img/WYD.jpg",
        "desc": "I've created the front end for a dictionary project for the World Youth Days in 2016. It interfaced with a SQLite database to provide browsing, searching, and submitting capabilities.",
        "links": ["https://github.com/jdranczewski/WikiTranslator", "http://dranczewski.j.pl/wyd-dict/"],
        "link_texts": ["GitHub", "Visit"]
    },
]

# To add: SimpleWebStats

projects_text = ""

for project in projects:
    project["links"] = " ".join([link_template.format(link=project["links"][i],
                                                      link_text=project["link_texts"][i])
                                 for i in range(len(project["links"]))])
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
