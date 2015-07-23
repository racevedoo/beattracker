from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings

from mainapp.models import Track
from mainapp.forms import UploadTrackForm

import os

#returns list of floats
def readTimes(track_name):
    f = open(settings.TRACKER_ROOT + '/' + track_name + '.txt')
    content = f.read()
    content = content.split('\n')
    content = content[:-1]
    content = [float(i) for i in content]
    content = [1000 * i for i in content]
    content = [int(i) for i in content]
    return content

def index(request, track_id=0, level=0):
    # Handle file upload
    hasFile = False
    form = UploadTrackForm()
    track_name=''
    if request.method == 'POST':
        form = UploadTrackForm(request.POST, request.FILES)
        if form.is_valid():
            track_name = request.FILES['track_file'].name
            if Track.objects.filter(track_file=request.FILES['track_file'].name).exists():
                hasFile = True
            else:#save file
                track = Track(track_file = request.FILES['track_file'], length=0)
                track.save()
                command = "%s/aubiotrack %s/%s > %s/%s.txt" % (settings.TRACKER_ROOT, settings.MEDIA_ROOT, track_name, settings.TRACKER_ROOT, track_name)
                os.system(command)
                # Redirect to the track list after POST
                return HttpResponseRedirect(reverse('mainapp.views.index'))
    elif request.method == 'GET' and int(track_id) != 0:
        track_name = Track.objects.get(id=int(track_id)).track_file.name
    tracks = Track.objects.all()
    context = {'form' : form, 'hasFile' : hasFile}
    if tracks:
        context.update({'tracks' : tracks})
    if track_name != '':
        context.update({'timestamps' : readTimes(track_name), 'track_name' : track_name})
    if 0 != int(level):
        hard = int(level) == 3
        context.update({'level' : int(level)})
        if hard:
            context.update({'hard' : hard})
    #dsadsads
    return render_to_response(
        'mainapp/list.html',
        context,
        context_instance=RequestContext(request)
    )