from django.shortcuts import render
from .forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    """

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={},
    )
def reservas(request):
    """
    Función vista para el formulario de contacto. El formulario toma los datos para el envío de mail.
    """
        
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            email_from=settings.EMAIL_HOST_USER
            recipient=['sdp_seba@hotmail.com']
            # msg= f'{data.subject}, {data.mensaje}, {data.email} '
            msg="El usuario:"+request.POST['name'] + "(Teléfono:" + request.POST['tel'] + ")" +  "Dice: " + request.POST['msg'] + "Quiere reservar desde " + request.POST['check_in'] + "hasta" + request.POST['check_out']
            send_mail("Reserva: Web", msg, email_from, recipient)
            return render(request, 'gracias.html', {})
    else:
        form=BookingForm()

    return render(
        request,
        'cab.html',
        context={"form":form},
    )