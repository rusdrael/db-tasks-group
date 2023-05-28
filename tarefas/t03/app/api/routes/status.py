from fastapi import APIRouter

router = APIRouter(tags=["Status"])

@router.get("/status")
async def ping():
    return {
        "success": True,
        "version": '0.1.0'
    }