from fastapi import APIRouter

health_router = APIRouter(prefix="/health")

@health_router.get(
    "",
    summary="This will be visible at start",
    description="We can describe this API call",
    response_description="We can describe the response",
)
def health() -> dict:
    return {
        "status": "online",
        "engine": "on",
    }