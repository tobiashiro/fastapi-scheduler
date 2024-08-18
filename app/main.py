from fastapi import FastAPI
from app.core.scheduler import init_scheduler
from app.api.endpoints import tasks

app = FastAPI()

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

init_scheduler()


@app.on_event("shutdown")
def shutdown_event():
    from app.core.scheduler import scheduler
    scheduler.shutdown()
