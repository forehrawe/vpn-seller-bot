from handlers.start import start_router
from handlers.config_panel import config_panel_router
from handlers.admin.start_admin import admin_router
from handlers.admin.manage_products_admin import product_router_A
from handlers.admin.manage_orders_admin import order_router

def setup_routers(dp):
    dp.include_router(start_router)
    dp.include_router(config_panel_router)
    dp.include_router(admin_router)
    dp.include_router(product_router_A)
    dp.include_router(order_router)