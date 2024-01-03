from django.contrib import admin

# Register your models here.
from .models import Person,Team,Osoba,Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie','nazwisko','plec','idstanowiska']
    list_filter = ['stanowisko']

    @admin.display(description="id")
    def idstanowiska(self, obj):
        return f"{obj.stanowisko} ({obj.stanowisko.id})"

admin.site.register(Person)
admin.site.register(Team)
admin.site.register(Stanowisko)
admin.site.register(Osoba, OsobaAdmin)