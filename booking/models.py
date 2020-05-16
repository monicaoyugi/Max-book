from django.db import models
from authentication.models import User
from django.forms import ModelForm
# Create your models here.


class Movie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(
        max_length=200, verbose_name='Movie name', null=False, blank=False)
    rows = models.PositiveSmallIntegerField(
        default=100, verbose_name="Number of rows")
    columns = models.PositiveSmallIntegerField(
        default=100, verbose_name="Number of columns")


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'rows', 'columns']


TICKET_STATUS_CHOICES = (
    (1, 'AVAILABLE'),
    (2, 'BLOCKED'),
    (3, 'BOOKED')
)


class Tickets(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    col_num = models.PositiveSmallIntegerField(null=False, blank=False)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,)
    status = models.IntegerField(choices=TICKET_STATUS_CHOICES, default=1)
    session = models.CharField(blank=False, null=False, max_length=200)

    class Meta:
        unique_together = ('movie', 'row_num', 'col_num')


class TicketsForm(ModelForm):
    class Meta:
        model = Tickets
        fields = ['row_num', 'col_num', ]


class Seats(models.Model):
    seat_no = models.PositiveSmallIntegerField(
        blank=False, null=False, unique=True)
    row_no = models.PositiveSmallIntegerField(blank=False, null=False)
    seat_name = models.CharField(max_length=3, unique=True)
    booked_by = models.CharField(max_length=200, blank=True)
    ip = models.CharField(max_length=39, unique=True, blank=True)

    def __str__(self):
        return self.seat_name

    class Meta:
        verbose_name_plural = "Seats"
