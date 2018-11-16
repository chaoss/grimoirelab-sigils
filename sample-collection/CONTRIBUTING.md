# CONTRIBUTING

The requirement for panels collections is that they should be stored in a git
repository with the following structure:
```
.
├── docs
│   ├── assets
│   │   └── images
│   ├── panels
│   ├── _config.yml
│   ├── index.md
│   └── panel.md
├── panels
├── CONTRIBUTING.md
├── LICENSE.md
└── README.md
```

Beyond the obvious .md files:
* `panels` has the set of .json files for all the panels.
* `docs` folder has an structure to be rendered as static web with Jeckyll
(GitHub does it directly):
  * `_config.yml` is the config file for the Jekyll page, and it must indicate that there is a collection of items in `panels`. See [collections docs for Jekyll](https://jekyllrb.com/docs/step-by-step/09-collections/)
  * `index.md` is the default website the user will see in 
    bitergia.github.io/{panels-collection-name} (as we have 
    https://chaoss.github.io/grimoirelab, that is rendering the content in
    https://github.com/chaoss/grimoirelab/docs)
  * `panel.md` is the default template for a panel documention
  * `assets/images`has panels screenshots
  * `panels`has one .md file for each panel that document the metrics and
    charts in that panel

For example, some example files: 
* `_config.yml`
```lang=markdown
author: Bitergia
title: My Brand New Panels

collections:
  panels:
    output:true
```

* `index.md`:
```lang=html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{% if page.title %}{{ page.title }}{% else %}{{ site.description }}{% endif %}">
    <meta name="author" content="{{site.author}}">
    <title>{% if page.title %}{{ page.title }}{% else %}{{ site.title }}{% endif %}</title>
  </head>
  <body>
    <h1>{{site.title}} by {{site.author}}</h1>
    <ul>
      {% for panel in site.panels %}
      <li><a href="{{panel.url}}">{{panel.name}}</a></li>
      {% endfor %}
    </ul>
  </body>
</html>
```

* `panel.md`:
```lang=html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{% if page.title %}{{ page.title }}{% else %}{{ site.description }}{% endif %}">
    <meta name="author" content="{{site.author}}">
    <title>{% if page.title %}{{ page.title }}{% else %}{{ site.title }}{% endif %}</title>
  </head>
  <body>
    <a href="../index.html">Index</a>
    <h1>{{page.title}}</h1>
    {{ content }}
   </body>
</html>
```

One panel documentation, for example overview.md:

```lang=markdown
title: Overview panel
description: Panel showing basic activity and community overview in all the project data sources

---

This panel shows basic activity and community overview in all the project data sources

![Overview panel screenshot](../assets/images/overview.jpg)

The metrics shown in the panel are:
* Numeric metrics
* Evolution charts

etc, etc., etc...
```