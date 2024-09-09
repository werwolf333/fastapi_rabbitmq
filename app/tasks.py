def generate_tasks_cpu(num_tasks=100):
    return [
        {
            "name": f"task{i + 1}",
            "datasets": {
                "value": f"raw value {i + 1}",
            }
        }
        for i in range(num_tasks)
    ]


tasks_cpu = generate_tasks_cpu()
