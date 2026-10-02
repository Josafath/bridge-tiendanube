import requests
import os

class TiendaNubeAPI:
    BASE_URL = "https://api.tiendanube.com/v1"

    def __init__(self, store_id=None, access_token=None):
        self.store_id = store_id or os.getenv("TIENDANUBE_STORE_ID")
        self.access_token = access_token or os.getenv("TIENDANUBE_ACCESS_TOKEN")
        self.headers = {
            "Authentication": f"bearer {self.access_token}",
            "User-Agent": "CompanyDashboardApp (admin@company.com)"
        }

    def get_orders(self, page=1, limit=50):
        url = f"{self.BASE_URL}/{self.store_id}/orders?page={page}&per_page={limit}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_product_stock(self, product_id, variant_id, stock_quantity):
        url = f"{self.BASE_URL}/{self.store_id}/products/{product_id}/variants/{variant_id}"
        payload = {"stock": stock_quantity}
        response = requests.put(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()