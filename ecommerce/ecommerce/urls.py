from django.conf.urls import url, include
from django.contrib import admin
#
from apps.ecommerce_app.models import User, Product, Species
class UserAdmin(admin.ModelAdmin):
  pass
admin.site.register(User, UserAdmin)
class ProductAdmin(admin.ModelAdmin):
  pass
admin.site.register(Product, ProductAdmin)
class SpeciesAdmin(admin.ModelAdmin):
  pass
admin.site.register(Species, SpeciesAdmin)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.ecommerce_app.urls')),
]
