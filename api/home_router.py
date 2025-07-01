from ninja import Router

router = Router()


@router.get("/home")
def home(request):
    return {"message": "Welcome to the home page!"}
