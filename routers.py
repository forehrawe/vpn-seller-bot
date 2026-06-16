from handlers.start import start_router
from handlers.config_panel import config_panel_router
from handlers.admin import admin_router

def setup_routers(dp):
    dp.include_router(start_router)
    dp.include_router(config_panel_router)
    dp.include_router(admin_router)