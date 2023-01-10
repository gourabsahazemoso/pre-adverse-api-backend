from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    court_search_status = models.BooleanField(
        default=True)  # True = Clear and False = Consider
    email_id = models.EmailField(null=False, default='')
    location = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class AdverseEmail(models.Model):
    """
    This model stores all the adverse notification email that was
    sent to each candidate.
    """
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, null=False, default=0)
    recepient_email = models.EmailField()
    content = models.TextField()
    charges = models.JSONField(default=dict)


class CourtSearchReport(models.Model):
    """
    This model stores the various court search records related to candidates.
    """
    charges = models.CharField(max_length=20)
    # True = Clear and False = Consider
    status = models.BooleanField(default=True)
