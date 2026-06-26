from fastapi import APIRouter
from Backend.services.policy_service import get_policy

router = APIRouter()


@router.get("/policy")
def fetch_policy():

    return {
        "policy": get_policy()
    }