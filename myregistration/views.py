from registration.backends.simple.views import RegistrationView
from django.contrib.auth.models import Permission


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
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/vocab'