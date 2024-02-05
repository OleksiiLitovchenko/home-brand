from django.contrib import admin
from .models import Portfolio, About, Services, Team,Partners,Reservation


# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(About)
admin.site.register(Services)
admin.site.register(Team)
admin.site.register(Partners)
admin.site.register(Reservation)