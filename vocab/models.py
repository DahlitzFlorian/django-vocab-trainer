from django.db import models
from django.contrib.auth.models import User


class Learnset(models.Model):
    """
    Objects of this class represent learn-sets including a
    various number of vocabulary or definitions that a
    human can be trained on.
    """
    # name of the learn-set
    learnset_name = models.CharField(max_length=200)

    # related to a certain user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # creation date
    creation_date = models.DateTimeField('date created')

    # object's representation
    def __str__(self):
        return self.learnset_name


class Vocabulary(models.Model):
    """
    Objects of this class represent vocab-/definition-pairs
    related to a certain learn-set-object.
    """
    # related to certain learn-set
    learnset = models.ForeignKey(Learnset, on_delete=models.CASCADE)

    # attributes
    word = models.CharField(max_length=200)
    translation = models.CharField(max_length=200)
    forms = models.CharField(max_length=200, default="", blank=True)
    forms_enabled = models.BooleanField(default=False)

    # object's representation
    def __str__(self):
        return self.word
