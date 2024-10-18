from django.shortcuts import get_object_or_404, redirect, render
from meetings.forms import MeetingForm
from meetings.models import Meeting, Room


# Create your views here.
def meetings_list_view(request):
    meetings = Meeting.objects.all()
    return render(request, "meetings.html", {"meetings": meetings})

def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, "detail.html", {"meeting": meeting})

def delete(request, id):
    meeting = get_object_or_404(Meeting, id=id) # Get the meeting by
  
    if request.method == "POST":
        meeting.delete() # Delete the meeting
        return redirect('meetings_list_view') # Redirect to the
  
    return render(request, "delete.html", {'meeting': meeting})
def add(request):
    rooms = Room.objects.all()
    
    if request.method == "POST":
        form = MeetingForm(request.POST)
        
        if form.is_valid():  # Validate the form
            new_meeting = form.save(commit=False)  # Create a new Meeting instance
            new_meeting.room = Room.objects.get(id=request.POST['room'])  # Set the room
            new_meeting.save()  # Save the meeting
            
            return redirect('meetings_list_view')  # Redirect to the meetings list
    
    else:
        form = MeetingForm()  # Create a new form instance if GET request
    
    return render(request, 'add.html', {'form': form, 'rooms': rooms})
def update(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    rooms = Room.objects.all()  # Get all rooms for the form

    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)  # Bind the form with the current meeting instance
        
        if form.is_valid():  # Validate the form
            updated_meeting = form.save(commit=False)  # Get the updated Meeting instance
            updated_meeting.room = Room.objects.get(id=request.POST['room'])  # Set the room if needed
            updated_meeting.save()  # Save the updated meeting
            
            return redirect('meetings_list_view')  # Redirect to the meetings list
    else:
        form = MeetingForm(instance=meeting)  # Prepopulate the form with the current meeting data
    
    return render(request, 'update.html', {'form': form, 'rooms': rooms}) 