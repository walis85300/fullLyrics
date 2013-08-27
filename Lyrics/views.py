from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

import json
import urllib

API_KEY = 'api_key=a669a55635e23810bc9bd76599f1310c'
FORMAT = 'format=json'
LAST_FM_API_URL = 'http://ws.audioscrobbler.com/2.0/?'

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def artista(request):

	# imagen = ''

	if request.GET.get('artist'):

		artist = request.GET.get('artist')

		URL = LAST_FM_API_URL + 'method=artist.getinfo&artist=' + artist + '&' + API_KEY + '&' + FORMAT

		try:

			reqAPI = urllib.urlopen(URL)
			artista = json.loads( reqAPI.read() )

			imagen = artista['artist']['image'][3]['#text']

			reqAPI.close()

		except:
			print 'nothing'

		return render_to_response('artista.html',{'artista':artista,'imagen':imagen},context_instance=RequestContext(request))








