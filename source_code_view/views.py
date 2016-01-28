from django.shortcuts import render
from django.http import HttpResponse
from HTMLParser import HTMLParser

import urllib2
import httplib
import re


def index(request):
    return render(request, 'index.html')

class SourceCodeParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.counts = {}
        self.commentData = ''

    def handle_starttag(self, tag, attrs):
        if tag in self.counts:
            self.counts[tag] += 1
        else:
            self.counts[tag] = 1

    def handle_comment(self, data):
        self.commentData += data


def search(request):
    # If the form has been submitted...
    if request.method == 'GET':
        url = request.GET.get('url')
        try: 
            response = urllib2.urlopen(url)
            html = response.read()
            parser = SourceCodeParser()
            parser.feed(html)
            parser.feed(parser.commentData)
            result = {'url': url,
                      'html': html,
                      'counts': parser.counts}
            return render(request, 'index.html', result)
        except urllib2.HTTPError, e:
            return render(request, 'index.html', {'error': 'HTTP error',
                                                  'data': e,
                                                  'url': url})
        except urllib2.URLError, e:
            return render(request, 'index.html', {'error': 'URL error',
                                                  'data': e,
                                                  'url': url})
        except httplib.HTTPException, e:
            return render(request, 'index.html', {'error': 'HTTP exception error',
                                                  'data': e,
                                                  'url': url})
        except Exception:
            import traceback
            return render(request, 'index.html', {'error': 'general error',
                                                  'data': traceback.format_exc(),
                                                  'url': url})
    # Something besides a get method
    else:
        return render(request, 'index.html')

