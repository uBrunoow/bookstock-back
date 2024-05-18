from django.contrib.gis import admin
from apps.management.models import (
    User,
    Stock,
    Book,
    BookTransaction,
)

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "is_superuser"]
    search_fields = ["name"]
    readonly_fields = ["updated_at", "created_at"]


admin.site.register(User, UserAdmin)

class StockAdmin(admin.ModelAdmin): 
    list_display = [
        "id",
        "user",
        "library_name",
        "location",
        "creation_date",
        "capacity",
    ]
    search_fields = ["library_name"]
    readonly_fields = ["creation_date", "updated_at", "created_at"]

admin.site.register(Stock, StockAdmin)

class BookAdmin(admin.ModelAdmin): 
    list_display = [
        "id",
        "stock",
        "title",
        "author",
        "rental_price",
        "sale_price",
    ]
    search_fields = ["title"]
    readonly_fields = ["updated_at", "created_at"]
  
admin.site.register(Book, BookAdmin)

class BookTransactionAdmin(admin.ModelAdmin): 
    list_display = [
        "id",
        "book",
        "user",
        "stock",
        "transaction_type",
        "transaction_date",
        "transaction_value",
    ]
    search_fields = ["book"]
    readonly_fields = ["transaction_date", "updated_at", "created_at"]

admin.site.register(BookTransaction, BookTransactionAdmin)
