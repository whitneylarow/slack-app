from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import urllib2
import httplib
import re

def index(request):
    return render(request, 'index.html')


def search(request):
    # If the form has been submitted...
    if request.method == 'GET':
        url = request.GET.get('url')
        try: 
            response = urllib2.urlopen(url)
            html = response.read()
            tags = re.findall('<([^/!<>\s]+)[^<>]*>', html)
            counts = {}
            for tag in tags:
                if tag in counts:
                    counts[tag] += 1
                else:
                    counts[tag] = 1
            result = {'url': url,
                      'html': html,
                      'tags': tags,
                      'counts': counts}
            return render(request, 'index.html', result)
        except urllib2.HTTPError, e:
            return render(request, 'index.html', {'error': 'HTTP error',
                                                  'data': e,
                                                  'url': url})
            # checksLogger.error('HTTPError = ' + str(e.code))
        except urllib2.URLError, e:
            # checksLogger.error('URLError = ' + str(e.reason))
            return render(request, 'index.html', {'error': 'URL error',
                                                  'data': e,
                                                  'url': url})
        except httplib.HTTPException, e:
            # checksLogger.error('HTTPException')
            return render(request, 'index.html', {'error': 'HTTP exception error',
                                                  'data': e,
                                                  'url': url})
        except Exception:
            import traceback
            # checksLogger.error('generic exception: ' + traceback.format_exc())
            return render(request, 'index.html', {'error': 'general error',
                                                  'data': traceback.format_exc(),
                                                  'url': url})
    # Something besides a get method
    else:
        return render(request, 'index.html')

