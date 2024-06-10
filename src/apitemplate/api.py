from ninja import Router

from apitemplate.schemas import HelloSchema, UserSchema, Error
router = Router()


@router.get("/hellov1")
def hellov1(request, name: str = "world"):
    return f"Hello {name}"


@router.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"


@router.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}


@router.get("/me", response={200: UserSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user