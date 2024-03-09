
from django.contrib import admin

from apps.material import models


admin.site.register([
    models.Product,
    models.Material,
    models.Warehouse,
    models.RawMaterial
])
