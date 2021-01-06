enable_utc = False
timezone = "Asia/Kolkata"

# broker_url = "amqp://admin:admin@localhost:5672//"
#
# result_backend = "redis://:admin@localhost:6379/1"

# beat_scheduler = 'redbeat.RedBeatScheduler'
beat_scheduler = "celery_pool_asyncio:PersistentScheduler"

beat_max_loop_interval = 5

redbeat_redis_url = "redis://:admin@localhost:6379/10"

redbeat_key_prefix = "redbeat"
redbeat_schedule_key = redbeat_key_prefix + ":schedule"
redbeat_statics_key = redbeat_key_prefix + ":statics"
redbeat_lock_key = redbeat_key_prefix + ":lock"
redbeat_lock_timeout = beat_max_loop_interval * 300


# beat_schedule = {
#     'add-every-10-seconds': {
#         'task': 'task.add_task',
#         'schedule': 2.0,
#         'args': (29,11)
#     },
#     'add-every-5-seconds': {
#         'task': 'task.test',
#         'schedule': 5.0,
#         'args': (16, 16)
#     },
# }
