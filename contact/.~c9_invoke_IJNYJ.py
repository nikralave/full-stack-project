from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages, auth
from .forms import ContactForm


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            template=get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
            
            subject = 'Thanks for getting in touch!'
                from_email = settings.EMAIL_HOST_USER
            from_email = settings.EMAIL_HOST_USER
            to_email = [contact_email]

            send_mail(subject,message,from_email,to_email,fail_silently=False)
          
            email = EmailMessage(
                "New contact form submission",
                content,
                "Happy Box" +'',
                ['admin@example .com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'We have recieved your email & will get back to you as soon as possible!')
            return redirect('home')

    return render(request, 'contact.html', {
        'form': form_class,
    })