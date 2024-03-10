from rest_framework import views
from rest_framework import response

from apps.material import models


class ProductMaterialsView(views.APIView):
    def get(self, request):

        data = request.data
        required_products = data.get("required_products", [])

        result = []

        for item in required_products:
            product_name = item.get("name")
            product_qty = item.get("quantity")
            product_materials = []

            materials = models.RawMaterial.objects.filter(
                product__name=product_name
            )

            for material in materials:
                warehouse = models.Warehouse.objects.filter(
                    material=material.material
                ).first()

                if warehouse:
                    available_qty = warehouse.remainder
                    required_qty = material.quantity * product_qty
                    qty_to_use = min(available_qty, required_qty)

                    product_materials.append({
                        "warehouse_id": warehouse.id,
                        "material_name": material.material.name,
                        "qty": qty_to_use,
                        "price": warehouse.price if qty_to_use > 0 else None
                    })

            result.append({
                "product_name": product_name,
                "product_qty": product_qty,
                "product_materials": product_materials
            })

        return response.Response({"result": result})
