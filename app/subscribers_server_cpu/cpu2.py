import time
import pika
import sys
import os
import json


# -------connection configuration variables-----------------
all_cpu_tasks = 'all_cpu_tasks'
cpu_tasks = 'cpu2_cpu_tasks'
host = 'rabbitmq'
name = "cpu2"
credentials = pika.PlainCredentials('guest', 'guest')


# ----processing a task to half-processed value-------------
def callback(ch, method, properties, body):
    task_ready = True
    task_dict_cpu = json.loads(body.decode())
    try:
        time.sleep(5)
        print(f"{name}: processed '{task_dict_cpu['name']}'")
    except Exception:
        print(f"error in {task_dict_cpu['name']}")
        task_ready = False
    ch.basic_ack(delivery_tag=method.delivery_tag)
    if task_ready:
        task_dict_gpu = {
            "name": task_dict_cpu['name'],
            "datasets": {
                "value": "half-processed value",
            }
        }
        all_cpu_tasks = 'all_gpu_tasks'
        ch.queue_declare(queue=all_cpu_tasks)
        ch.basic_publish(exchange='',
                         routing_key=all_cpu_tasks,
                         body=json.dumps(task_dict_gpu))
        print(f"{name}: Sent '{task_dict_gpu['name']}' to queue task_dict_gpu")


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
        host=host,
        credentials=credentials
        )
    )

    channel = connection.channel()
    channel.queue_declare(queue=all_cpu_tasks)
    channel.queue_declare(queue=cpu_tasks)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=all_cpu_tasks, on_message_callback=callback, auto_ack=False)
    channel.basic_consume(queue=cpu_tasks, on_message_callback=callback, auto_ack=False)
    print(f" [*] Waiting for messages in queue '{all_cpu_tasks}'.")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
