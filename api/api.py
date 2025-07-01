from ninja import NinjaAPI

from api.home_router import router as home_router

api = NinjaAPI()

api.add_router("/home/", home_router)
