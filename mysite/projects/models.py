from django.db import models

# Create your models here.
# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
PLCIE = (
    ('K', 'Kobieta'),
    ('M', 'Mezczyzna'),
    ('I', 'Inne')
)

class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Stanowisko(models.Model):

    nazwa = models.CharField(max_length=60, null=True, blank=True)
    opis = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):

    imie = models.CharField(max_length=60, null=True, blank=True)
    nazwisko = models.CharField(max_length=60, null=True, blank=True)
    plec = models.CharField(max_length=1, choices=PLCIE)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateField(null=True, auto_now_add=True)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

