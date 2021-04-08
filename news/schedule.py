from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    "reset_upvotes": {
        "task": "reset_upvotes",
        "schedule": crontab(hour=10, minute=10),
    },
}
