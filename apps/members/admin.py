from django.contrib import admin
from apps.members.models import Member
from apps.members.models import Participation


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'function', 'site','github', 'twitter','slideshare','lattes','started_nsi_date')
    list_filter = ('function','started_nsi_date',)
    inlines = [ParticipationInline]


admin.site.register(Member, MemberAdmin)
admin.site.register(Participation)
