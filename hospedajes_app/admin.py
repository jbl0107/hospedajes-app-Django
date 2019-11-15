from django.contrib import admin
from .models import City, Property, RentalDate, Feature, ComfortXProperty, Comfort, Host

admin.site.register(City)
admin.site.register(Feature)
admin.site.register(Comfort)
admin.site.register(Host)


class RentalDate_inline(admin.TabularInline):
    model = RentalDate
    fk_name = 'property'
    # max_num = 30


class Comfort_inline(admin.TabularInline):
    model = ComfortXProperty
    fk_name = 'property'


class PropertyAdmin(admin.ModelAdmin):
    inlines = [Comfort_inline, RentalDate_inline,]


admin.site.register(Property, PropertyAdmin)