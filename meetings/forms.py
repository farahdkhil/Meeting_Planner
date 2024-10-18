from datetime import date
from django.forms import DateInput, ModelForm, TextInput, TimeInput, ValidationError
from meetings.models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'start_time', 'duration', 'room']  # Specify fields explicitly
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),  # Match the field name with your model
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }
    
    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return d  # Return the validated date
