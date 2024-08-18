from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from app.core.config import settings


jobstores = {
    'default': SQLAlchemyJobStore(url=settings.JOBS_DB_URL)
}

scheduler = BackgroundScheduler(jobstores=jobstores)


def init_scheduler():
    scheduler.start()


def schedule_task(task_func, interval_seconds, task_id):
    from apscheduler.triggers.interval import IntervalTrigger
    scheduler.add_job(
        task_func,
        trigger=IntervalTrigger(seconds=interval_seconds),
        id=task_id,
        replace_existing=True
    )


def remove_task(task_id):
    scheduler.remove_job(task_id)
