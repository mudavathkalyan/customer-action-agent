from fastapi import FastAPI

from app.api.tickets import router as ticket_router


app = FastAPI(
    title="Customer Action Agent",
    version="1.0.0",
)

app.include_router(ticket_router)