#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andrii Soldatenko'
SITENAME = u'Python Geek'
SITEDESCRIPTION = u'blog about interesting things'
#SITEURL = 'https://asoldatenko.com/'
# SITEDESCRIPTION = 'Andrii Soldatenko blog about Python'

ARTICLE_PATHS = ['blog']


PATH = 'content'

#ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
#ARTICLE_URL = '{date:%Y}/{slug}.html'
GITHUB_URL = 'http://github.com/andriisoldatenko/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True
# Blogroll
# LINKS = ((),)

# Social widget
SOCIAL = (('@a_soldatenko', 'http://twitter.com/a_soldatenko'),
                  ('andriisoldatenko', 'http://github.com/andriisoldatenko'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'pelicanyan'
GA_ACCOUNT = 'UA-12344321-1'
TWITTER_ACCOUNT = '@a_soldatenko'
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DEFAULT_LANG = 'en'
DATE_FORMATS = { 'en': '%B %d, %Y', }
STATIC_PATHS = ['static', 'images', 'favicon.ico']
TYPOGRIFY=True

PLUGIN_PATHS = ['plugins']

PLUGINS = [
    'slideshare',
    'pelican_youtube'
]
