from django.contrib import admin
from apps.members.models import Member
from apps.members.models import Participation


class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1

class MemberAdmin(admin.ModelAdmin):
    inlines = [ParticipationInline]


admin.site.register(Member, MemberAdmin)
admin.site.register(Participation)
