from tiendanube.services import TiendaNubeAPI
from company_data.models import InternalProduct

def sync_stock_to_tiendanube():
    api = TiendaNubeAPI()
    products_to_sync = InternalProduct.objects.filter(needs_sync=True)

    for product in products_to_sync:
        try:
            api.update_product_stock(
                product_id=product.tiendanube_product_id,
                variant_id=product.tiendanube_variant_id,
                stock_quantity=product.current_stock
            )
            product.needs_sync = False
            product.save()
        except Exception as e:
            # Log error in sync logs
            print(f"Failed to sync {product.sku}: {str(e)}")