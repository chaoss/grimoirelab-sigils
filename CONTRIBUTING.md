# How to Contribute

Please follow these guidelines before sending your contribution.

## Recommended panel contents

You are free of create whatever panel you may want. Following recommendations are based on
our experience and aim at creating simple panels that don't overwhelm users at first glance:

* On each panel, it should be possible to filter mainly by project, and repository.
  For those that are related with several data sources, it might useful to filter by
  data source, or have a panel for each data source.
* No more than 5 widgets, to avoid overwhelming the user.
* A markdown widget below with some basic explanations about what we are looking at 
  (panel definition) and a link to documentation page (the one described at 
  [Adding or updating documentation section](#adding-or-updating-documentation)).

For instance, [GitHub Issues Efficiency panel](https://chaoss.github.io/grimoirelab-sigils/panels/github-issues-efficiency/)
was built following these recommendations.

## Directory structure

There are two important places in Sigils:
* `docs/` directory: it contains panels documentation.
* `<collection_name>/` directory: it contains JSON files corresponding to a collection named `<collection_name>`. The current standard Bitergia's collection is `panels/`.

We refer to these directories later for creating your Pull Request.

## Opening a new Pull Request

A new Pull Request could contain a panel and its corresponding documentation. A panel with outdated documentation will not be accepted. Once in your branch, follow below steps to export your panel(s) and create/update documentation if needed. 

### Working with branches

The usual workflow we encourage you to follow is:
* Fork repository.
* Create a new branch with a meaningful name. As you are going to create or modify a panel, use
the name of the panel together with some keywords about what that branch intends to achieve. For
instance, for a new git timing panel we would use a branch called `git-timing`. For a fix on
widgets related to organizations in an existing gerrit timing panel we would use something like
`gerrit-timing-fix-orgs`.

### Importing panels

If you don't have Kidash tool installed, please see [installing Kidash section](#installing-kidash).

As starting point, you will probably want to import some existing panels into your
Kibana environment. Choose the panel you want to work with, for instance from [json](json)
folder and import it to your Kibana/Kibiter using a line like the following:
```
(kidash-venv)$> kidash -e <elasticsearch_endpoint> --import <file_name>.json
```
And you should be able to load the panel from your Kibana/Kibiter instance. Notice you may need to import also some index pattern files to get the panel working. You can do it with the same line, just using index pattern file name as <file_name>.

For instance, to import Git panel to an empty environment:
```
(kidash-venv)$> kidash -e <elasticsearch_endpoint> --import git.json

(kidash-venv)$> kidash -e <elasticsearch_endpoint> --import git-index-pattern.json

```

### Exporting panel

* Panel should work in Kibana/Kibiter 6.1.0.
* Follow naming conventions explained in our [README.md](README.md)
* Export the panel using Kidash tool. If you don't have Kidash tool installed, please see [installing Kidash section](#installing-kidash).

In order to **export the panel you have been working on**, once Kidash is installed, you can use a line like the one below:
```
(kidash-venv)$> kidash --split-index-patterns -e <elasticsearch_endpoint> --dashboard <dashboard_name> --export <file_name>.json
```
Two important details:
* Index patterns are stored in separate files, this is why the option `--split-index-patterns` is needed.
* Only add your index pattern(s) to your PR in case you modified something related to that index pattern (fields format, scripted fields, new fields added) or if you are using a totally new index pattern.
* `<dashboard_name>` is the identifier of the panel in Kibiter, that is the string you see after last slash of the URL when the panel is loaded in your browser.E.g.:
```
https://xxxxx.biterg.io/app/kibana#/dashboard/Gerrit?_g=(refreshInterval...  

identifier --> Gerrit

https://xxxxx.biterg.io/app/kibana#/dashboard/2e968fe0-b1bb-11e8-8aac-ef7fd4d8cbad?_g=(refreshInterval:(display:....
identifier ---> 2e968fe0-b1bb-11e8-8aac-ef7fd4d8cbad
```

After the execution of kidash you should get at least two files, one per each index pattern used in the panel and one with the panel itself. You should put them under `<collection_name>/` directory. Please remind index patterns are required only if you modify them is some way (fields format, scripted fields, new fields added) or if they are new.

### Adding or updating documentation

**Sigils documentation is publicly available at https://chaoss.github.io/grimoirelab-sigils**

If you are adding a new panel or updating an existing one, you will be required to document it. Bug fixes usually don't need documentation updates. [Jekyll](https://jekyllrb.com/) is used on top of [GitHub Pages](https://pages.github.com/) to build the web page. For more information on how to configure a local Jekyll instance to work with GitHub Pages see [Jekyll and GitHub Pages section](#jekyll-and-github-pages).

Under `docs/` directory you'll find the following structure:
```
.
├── docs
│   ├── _layouts
│   ├── _panels
|   ├── assets
│   │   └── images
│   ├── _config.yml
│   └── index.html
│    
├── panels
├── CONTRIBUTING.md
├── LICENSE.md
└── README.md
```
As you can see, for each collection we have a directory in root folder and then another one in `docs/`. For instance, `panels` collection has a directory `panels/` in root folder (this is actually a link to `json` directory, that is the legacy directory for Bitergia's panel) and then a `_panels` in `docs/` (notice the `_` before the name, this is needed for Jekyll collections to work).

What you may need to modify is:
* `_config.yml` and `index.html`: if you added a new collection, you need to add a collection in `_config.yml` similar to `panels`. You also need to add a loop in `index.html` to iterate over all docs in the collection and add links to them, again it would be copying, pasting and slightly modifying what is already done for `panels`.
* `_panels/` or `_<collection_name>/`: here you need to put MarkDown files for your panels or updating those you modified. These files must contain a Jekyll Front Matter like the following in order to be correctly rendered (modify title and description if needed):
```
---
title: Community Structure
description: find who are your core, regular and casual contributors.
author: John Doe
created_at: 2018-12-05 (YYYY-MM-DD)
grimoirelab_version: 0.2.1
layout: panel
---
MD document should contain at least:
* What does it display (list of metrics)?
* Why was it built and what is it used for?
* Screenshot.
```

* `assets/images/`: the place to store screenshots, if needed.

For more details on how to build local links, please see the existing files. For instance, this would be a link to an image:
```
![Global View]({{ site.baseurl }}/assets/images/onion_filters_on_top_2.png)
###### Figure 1a. Panel filter on top and Data Source widget at the right
```
And this a link to another local MarkDown file:
```
[Data Status](data-status.md)
```

### Creating your Pull Request

Use GitHub interface to create a new Pull Request from your branch to our master repo.
  * If your panel needs something special, like creating a specific alias on ES, please use comments space
  in your Pull Request to give us instructions on how to proceed.
  
## Installing kidash

Kidash is Bitergia's tool for importing/exporting
panels. All panels in this repo follows Kidash JSON format, which is slightly different
from Kibana's format.

Kidash is part of [GrimoireELK](https://github.com/grimoirelab/GrimoireELK) toolchain
and can be installed as a pypi package: `grimoire-kidash` [![PyPI version](https://badge.fury.io/py/grimoire-kidash.svg)](https://badge.fury.io/py/grimoire-kidash)
We recommend you to install it in a **Python 3** Virtual Environment:
```
$> python3 -m venv kidash-venv
$> . kidash-venv/bin/activate
(kidash-venv)$> pip3 install kidash
(kidash-venv)$> kidash
usage: usage: kidash [options]
kidash: error: --export or --import or --list needed
```

## Jekyll and GitHub Pages

To install a local version of Jekyll and test your changes you can follow instructions on [GitHub help pages](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/). Following commands should be enough:

``` 
sudo gem install bundler

ruby --version
ruby 2.5.1p57 (2018-03-29 revision 63029) [x86_64-linux-gnu]
```

Then create `Gemfile` to make sure we're using same version as GH Pages and whitelisted plugins:
```
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
gem 'jekyll-relative-links'
```
Last gem is used to keep markdown relative links working properly without need of modifying them.

And execute:
```
bundle install
```

If you see the following error:
```
Traceback (most recent call last):
	2: from /usr/local/bin/bundle:23:in `<main>'
	1: from /usr/lib/ruby/2.5.0/rubygems.rb:308:in `activate_bin_path'
/usr/lib/ruby/2.5.0/rubygems.rb:289:in `find_spec_for_exe': can't find gem bundler (>= 0.a) with executable bundle (Gem::GemNotFoundException)
```

Then you need to update your ruby gems:
```
sudo gem update --system '2.7.9'
```

At this point you need `g++`. If it is not installed you'll get the following error:
```
...
current directory: /tmp/bundler20200113-21702-swo6greventmachine-1.2.7/gems/eventmachine-1.2.7/ext
make "DESTDIR="
compiling binder.cpp
make: g++: Command not found
Makefile:234: recipe for target 'binder.o' failed
make: *** [binder.o] Error 127

make failed, exit code 2
...
```

In that case, just install it. For instance, in Ubuntu:
```
sudo apt-get install g++

bundle install
```

If you had some dependency problems:
```
Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    current directory: /tmp/bundler20181212-15181-1is4dcfcommonmarker-0.17.13/gems/commonmarker-0.17.13/ext/commonmarker
/usr/bin/ruby2.5 -r ./siteconf20181212-15181-1rif9my.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h

extconf failed, exit code 1

Gem files will remain installed in /tmp/bundler20181212-15181-1is4dcfcommonmarker-0.17.13/gems/commonmarker-0.17.13 for inspection.
Results logged to /tmp/bundler20181212-15181-1is4dcfcommonmarker-0.17.13/extensions/x86_64-linux/2.5.0/commonmarker-0.17.13/gem_make.out

An error occurred while installing commonmarker (0.17.13), and Bundler cannot continue.
Make sure that `gem install commonmarker -v '0.17.13' --source 'https://rubygems.org/'` succeeds before bundling.

In Gemfile:
  github-pages was resolved to 193, which depends on
    jekyll-commonmark-ghpages was resolved to 0.1.5, which depends on
      jekyll-commonmark was resolved to 1.2.0, which depends on
        commonmarker
```

Then you need to install some things:
```
sudo apt-get install ruby`ruby -e 'puts RUBY_VERSION[/\d+\.\d+/]'`-dev

sudo gem install commonmarker -v '0.17.13' --source 'https://rubygems.org/'
```

And then it should work:
```
bundle install
```

Then we can start a local server to test our changes using following command from `docs` folder:
```
bundle exec jekyll serve --watch
```

As we want to build a project web site, URL looks like: `https://chaoss.github.io/grimoirelab-sigils/index.html`

The problem is `project name` is not added to local links, so they will point to `https://chaoss.github.io/` instead of pointing to `https://chaoss.github.io/grimoirelab-sigils/index.html`. To solve this, add `baseurl` to `_config.yml`:
```
baseurl: /grimoirelab-sigils
```

And then update all local links to use that variable. Some examples:
```
<a href="{{ site.baseurl }}{{panel.url}}">{{panel.name}}</a>

![Global View]({{ site.baseurl }}/assets/images/onion_filters_on_top_2.png)
```

To avoid using `project name` in URLs when testing **local changes**, we can overwrite it from command line when launching our local jekyll server:
```
bundle exec jekyll serve --baseurl '' --watch
```

More info on this at:
https://github.com/jekyll/jekyll/issues/332



