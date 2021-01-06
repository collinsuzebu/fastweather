from celery import Celery
from . import celery_config
from fastweather.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


celery = Celery("fastweather", backend=CELERY_BROKER_URL, broker=CELERY_RESULT_BACKEND)
celery.conf.task_routes = {"celery.tasks.fetch_dat": "test-queue"}
celery.conf.update(task_track_started=True)
# celery.config_from_object(celery_config)


# celery_app = Celery(
#     "mycelery",
#     broker=f"amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@rabbitmq:5672",
#     backend="rpc://",
# )
#
# celery_app.conf.update(
#     {
#         "task_routes": {
#             "worker.worker.celery1": {"queue": "main-queue"},
#             "worker.worker.celery2": {"queue": "beat-queue"},
#         }
#     }
# )
