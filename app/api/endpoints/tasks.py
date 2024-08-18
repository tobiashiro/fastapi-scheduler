from fastapi import APIRouter
from app.core.scheduler import schedule_task, remove_task
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


def example_task():
    print(f"Task executed at: {datetime.now()}")
    logger.info(f"Task executed at: {datetime.now()}")


@router.post("/start/")
def start_task():
    schedule_task(example_task, interval_seconds=10, task_id="example_task")
    return {"message": "Task scheduled to run every 10 seconds"}


@router.post("/stop/")
def stop_task():
    remove_task("example_task")
    return {"message": "Task stopped"}
