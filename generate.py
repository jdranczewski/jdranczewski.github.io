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

link_template = '<a href="{link}" target="_blank" class="main_link">{link_text}</a>'

projects = [
    {
        "title": "puzzlepiece",
        "img": "img/puzzlepiece.png",
        "desc": "A GUI-forward Python framework for automating experimental setups - generates GUI components and a standardised API to make setup automation less unwieldy.",
        "links": ["https://puzzlepiece.readthedocs.io/en/latest/"],
        "link_texts": ["Documentation"]
    },
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
        "title": "PhD Thesis",
        "img": "img/thesis.jpg",
        "desc": "\"On-chip III-V semiconductor network lasers for neuromorphic computing\" – my work on neuromorphic computing at IBM Research Europe – Zurich and Imperial College London.",
        "links": ["https://spiral.imperial.ac.uk/entities/publication/d655d291-fa7f-416f-a4e0-affe4e3634b8", "https://github.com/jdranczewski/phd-thesis-template/tree/main"],
        "link_texts": ["Read it", "Template"]
    },
    {
        "title": "Internet Roadtrip Scripts",
        "img": "img/roadtrip.png",
        "desc": "Many userscripts for <a href='https://neal.fun/internet-roadtrip/' target='_blank'>the Neal.fun game</a>, mostly focused on custom mapping and navigation tools, and Google Street View interactivity.",
        "links": ["https://github.com/jdranczewski/internet-roadtrip-scripts", "https://greasyfork.org/en/users/1473129-jdranczewski"],
        "link_texts": ["GitHub", "Install"]
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
        "title": "Bachusiki",
        "img": "img/bachusiki.png",
        "desc": "A website started in 2012 cataloguing little sculptures across my hometown. Recently upgraded to take advantage of modern PHP and mapping tech, while keeping the old-web charm.",
        "links": ["https://bachusiki.zgora.pl/"],
        "link_texts": ["Visit (in Polish)"]
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
