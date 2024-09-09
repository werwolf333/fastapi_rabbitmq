import pika
import json
from tasks import tasks_cpu


credentials = pika.PlainCredentials('guest', 'guest')
host = "rabbitmq"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=host,
        credentials=credentials
    )
)

queues = [
    "all_cpu_tasks",
    "cpu1_cpu_tasks",
    "cpu2_cpu_tasks",
    "all_gpu_tasks",
    "gpu1_gpu_tasks",
    "gpu2_gpu_tasks"
]

channel = connection.channel()
for queue in queues:
    channel.queue_declare(queue=queue)


def publish_tasks(channel, queue_name, tasks):
    for task in tasks:
        channel.basic_publish(exchange="", routing_key=queue_name, body=json.dumps(task))
        print(f" [x] Sent {task['name']}")


publish_tasks(channel, "all_cpu_tasks", tasks_cpu)
connection.close()
