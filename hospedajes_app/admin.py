from django.contrib import admin
from .models import Profile, TipoAula, Property, RentalDate, Caracteristica, CapacidadXProperty, Capacidad, Host

admin.site.register(TipoAula)
admin.site.register(Caracteristica)
admin.site.register(Capacidad)
admin.site.register(Host)
admin.site.register(Profile)



class RentalDate_inline(admin.TabularInline):
    model = RentalDate
    fk_name = 'property'
    # max_num = 30


class Capacidad_inline(admin.TabularInline):
    model = CapacidadXProperty
    fk_name = 'property'


class PropertyAdmin(admin.ModelAdmin):
    inlines = [Capacidad_inline, RentalDate_inline,]


admin.site.register(Property, PropertyAdmin)