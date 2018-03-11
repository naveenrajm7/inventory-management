from django.contrib import admin
from .models import MasterIn, WhouseIn, IssueIn, ItemIn, ConsumIn
# Register your models here.

admin.site.register(WhouseIn)
admin.site.register(MasterIn)
admin.site.register(IssueIn)
admin.site.register(ItemIn)
admin.site.register(ConsumIn)
