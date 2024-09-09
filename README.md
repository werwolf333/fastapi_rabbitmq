# FastAPI + RabbitMQ Project
## Описание

Этот проект демонстрирует использование FastAPI с RabbitMQ. В проекте используется один контейнер с FastAPI и один с RabbitMQ. Это абстрактный пример обработки датасетов, который иллюстрирует, как можно организовать взаимодействие между компонентами приложения для асинхронной обработки данных. В основном демонстрируя работу RabbitMQ. Поэтому "спикер" и "подписчики" в одном контейнере.

Есть два подписчика cpu и два подписчика gpu. 
Всего шесть очередей. Одна общая очередь для всех CPU. Одна общая очередь для всех GPU. У каждого подписчика CPU и GPU есть своя очередь, которая берет только одну задачу из общей очереди, что позволяет балансировать нагрузку и уменьшить простой.


## Установка и настройка

Следуйте этим шагам, чтобы развернуть проект на своей машине.

### 1. Клонирование репозитория

Начните с клонирования репозитория на локальную машину:

```bash
git clone https://github.com/yourusername/fastapi_rabbitmq.git
```
Перейдите в директорию проекта:

```bash
cd fastapi_rabbitmq
```

### 2. Запуск проекта

После клонирования репозитория выполните команду для сборки и запуска контейнеров:


```bash
docker-compose up --build
```

Это поднимет следующие сервисы:

- **FastAPI** на порту 8000 для добавления задач в очередь.
- **RabbitMQ** с веб-интерфейсом на порту 15672 (логин/пароль: guest/guest).

### 3. Открытие интерфейсов

- FastAPI доступен по адресу: http://localhost:8000/docs
- RabbitMQ Management доступен по адресу: http://localhost:15672

### 4. Пример использования

Перейдите в веб интерфейс RabbitMQ http://localhost:15672/#/queues и http://localhost:8000/docs. Запустите run_speaker и увидите как в очереди all_cpu_tasks появиться 100 задач. После запуска run_all_subscribers вы увидите что каждые 5 секунд по две задачи решаються перемешаясь all_gpu_tasks, и те в свою очередь тоже решаються по 2 раз в 5 секунд. При запуске stop_subscribers обработка остановиться.