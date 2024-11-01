from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm2
# Vue pour gérer le formulaire
def controleform1(request):
    if request.method == 'POST':
        f = request.POST['firstname']  # Récupère le prénom
        l = request.POST['lastname']   # Récupère le nom
        e = request.POST['email']      # Récupère l'email
        m = request.POST['message']    # Récupère le message

        # Création de l'objet Contact avec les données du formulaire
        Contact.objects.create(firstname=f, lastname=l, email=e, message=m)

        return HttpResponse('<h2>Data has been submitted</h2>')

    # Si la méthode n'est pas POST, affiche le formulaire
    return render(request, 'myform1.html')

def controleform2(request):
    if request.method == 'POST':
        form = ContactForm2(request.POST)  # Capture the submitted data
        if form.is_valid():  # Validate the form
            # Extract cleaned data
            f = request.POST['firstname']  # Récupère le prénom
            l = request.POST['lastname']   # Récupère le nom
            e = request.POST['email']      # Récupère l'email
            m = request.POST['message']    # Récupère le message

            # Save data to the database
            Contact.objects.create(firstname=f, lastname=l, email=e, message=m)

            return HttpResponse('<h2> Data has been submitted </h2>')

    else:
        form = ContactForm2()  # Display an empty form for GET requests

    return render(request, "myform2.html", {"mycontactform2": form})