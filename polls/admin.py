from django.contrib import admin

from .models import Product, Delivery, Category, Catalog, Charact, Property


class PropertyInline(admin.StackedInline):
    model = Property
    extra = 1

class CharactInline(admin.StackedInline):
    model = Charact
    inlines = [PropertyInline,]
    extra = 1

class CharactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['charact_title']}),
        (None,               {'fields': ['charact_text']}),
        (None,               {'fields': ['charact_product']}),
    ]
    inlines = [PropertyInline]

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [CharactInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Charact, CharactAdmin)
admin.site.register(Category)
admin.site.register(Catalog)
admin.site.register(Property)
admin.site.register(Delivery)


