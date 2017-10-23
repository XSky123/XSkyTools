#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
----------------------------------------
    Filename   : Web.py
    Description: Deal with web requests and some parsing.
    Author     : XSky123
    Created at : 2017/10/21 13:45
----------------------------------------
"""
import re
import urlparse
import requests
from bs4 import BeautifulSoup as bs
_USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
               "Chrome/61.0.3163.100 Safari/537.36")


def get(url, origin=False):
    """ Send GET requests and return encoded html."""
    headers = {'User-Agent': _USER_AGENT}
    r = requests.get(url, headers=headers)
    r.encoding = _get_coding(r)
    if origin:
        return r.content

    else:
        return r.text


def get_json(url):
    """ Send GET requests and return JSON."""
    headers = {'User-Agent': _USER_AGENT}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None


def get_soup(url):
    """ Send GET requests and directly parsed by BeautifulSoup"""
    html = get(url, origin=True)
    soup = bs(html, "html.parser")
    return soup


def _get_coding(response):
    """ Get text coding from response object. """
    regex = re.search("charset=(.*?)[\"]", response.content)
    if regex:
        coding = regex.group(1)

    else:
        coding = "utf-8"

    return coding


def format_url(url):
    """ format url, add scheme(default http) and delete end-hash if has."""
    if not re.match("^(.*?:\/\/|\/\/)", url):  # check scheme
        url = "http://%s" % url

    if url.endswith('/'):
        url = url[:-1]

    return url


def main():
    pass


if __name__ == '__main__':
    main()
