from registration.backends.simple.views import RegistrationView
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, get_user_model, login
from registration import signals


User = get_user_model()

class MyRegistrationView(RegistrationView):
    """
    Overrides django-registration RegistrationView class
    """
    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        new_user.is_staff = True
        new_user.save()
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/vocab'