from django.contrib import admin


@admin.register()
class UnitAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount_due', )
    search_fields = ('title', 'city')
    list_filter = ('is_deleted',)

