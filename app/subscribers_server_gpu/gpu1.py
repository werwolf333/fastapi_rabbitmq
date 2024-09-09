import time
import pika
import sys
import os
import json


# -------connection configuration variables-----------------
all_gpu_tasks = 'all_gpu_tasks'
gpu_tasks = 'gpu1_gpu_tasks'
host = 'rabbitmq'
name = "gpu1"
credentials = pika.PlainCredentials('guest', 'guest')


# --------processing a task to processed value----------------
def callback(ch, method, properties, body):
    task_dict_gpu = json.loads(body.decode())
    try:
        time.sleep(5)
        print(f"processed '{task_dict_gpu['name']}'")
    except Exception:
        print(f"error in {task_dict_gpu['name']}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
        host=host,
        credentials=credentials
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=all_gpu_tasks)
    channel.queue_declare(queue=gpu_tasks)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=all_gpu_tasks, on_message_callback=callback, auto_ack=False)
    channel.basic_consume(queue=gpu_tasks, on_message_callback=callback, auto_ack=False)
    print(f" [*] Waiting for messages in queue '{all_gpu_tasks}'.")
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
