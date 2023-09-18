from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.controllers import item_controller, user_controller

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(user_controller.router,
                   prefix="/users",
                   tags=["Users"])
app.include_router(item_controller.router,
                   prefix="/items",
                   tags=["Items"])


@app.get("/", tags=["Root"])
async def read_root() -> dict[str, str]:
    return {"message": "Example API"}
