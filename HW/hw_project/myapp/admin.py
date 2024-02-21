from django.contrib import admin
from .models import User, Product, Order, Status


@admin.action(description="Сбросить количество в ноль")
def reset_count(modeladmin, request, queryset):
    queryset.update(count=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'count', 'price']
    ordering = ['count', '-price']
    list_filter = ['regist_prod_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_count]

    """Отдельный продукт."""
    fields = ['name', 'description', 'price', 'regist_prod_date', 'count']
    readonly_fields = ['regist_prod_date']


admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Status)
