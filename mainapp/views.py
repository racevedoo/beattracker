from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")



from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from mainapp.models import Track
from mainapp.forms import UploadTrackForm

def upload_track(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadTrackForm(request.POST, request.FILES)
        if form.is_valid():
            track = Track(track_file = request.FILES['track_file'], length=0)#TODO: change length
            track.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('mainapp.views.upload_track'))
    else:
        form = UploadTrackForm() # A empty, unbound form

    # Load documents for the list page
    tracks = Track.objects.all()
    context = {'form' : form}
    if tracks:
    	context.update({'tracks' : tracks})
    # Render list page with the documents and the form
    return render_to_response(
        'mainapp/list.html',
        context,
        context_instance=RequestContext(request)
    )