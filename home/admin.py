from django.contrib import admin
# Register your models here.
from .models import Menuitem

@admin.register(Menuitem)
def MenuitemAdmin(models.AdminModel):
    list_display : ('name','description','price'),
    list_filter : ('is_available'),
    search_fileds : ('name','description'),