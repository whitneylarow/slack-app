from django.shortcuts import render
from django.http import HttpResponse

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

