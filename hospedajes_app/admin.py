from django.contrib import admin
from .models import City, Property, RentalDate

admin.site.register(City)


class RentalDate_inline(admin.TabularInline):
    model = RentalDate
    fk_name = 'fk_property'
    # max_num = 30


class PropertyAdmin(admin.ModelAdmin):
    inlines = [RentalDate_inline, ]


admin.site.register(Property, PropertyAdmin)