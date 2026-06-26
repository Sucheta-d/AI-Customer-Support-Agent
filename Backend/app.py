from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend.routes.customer import router as customer_router
from Backend.routes.order import router as order_router
from Backend.routes.policy import router as policy_router
from Backend.routes.refund import router as refund_router

app = FastAPI(
    title="AI Customer Support Agent"
)

# ---------------------------------------------------
# CORS Configuration
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Routes
# ---------------------------------------------------

app.include_router(customer_router)
app.include_router(order_router)
app.include_router(policy_router)
app.include_router(
    refund_router,
    tags=["Refund"]
)


@app.get("/")
def home():
    return {
        "message": "AI Customer Support Agent Running"
    }