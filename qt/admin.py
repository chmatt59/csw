from django.contrib import admin
from models import *

class StatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(Status, StatusAdmin)


class ActionInline(admin.TabularInline):
    model = Action

class CostInline(admin.TabularInline):
    model = Cost


class NonconformityAdmin(admin.ModelAdmin):
    filter_horizontal = ['observers', ]
    inlines = [CostInline, ]
admin.site.register(Nonconformity, NonconformityAdmin)

class ProblemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Problem, ProblemAdmin)


class ActionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Action, ActionAdmin)

class ActorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Actor, ActorAdmin)

class CostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cost, CostAdmin)

class CostCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(CostCategory, CostCategoryAdmin)

class TargetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Target, TargetAdmin)




