import subprocess
from fastapi import FastAPI

app = FastAPI()

scripts = [
    'subscribers_server_cpu/cpu1.py',
    'subscribers_server_cpu/cpu2.py',
    'subscribers_server_gpu/gpu1.py',
    'subscribers_server_gpu/gpu2.py'
]

processes = []

@app.get("/run_all_subscribers")
def run_all_subscribers():
    global processes
    try:
        for script in scripts:
            process = subprocess.Popen(['python3', script])
            processes.append(process)

        return {"message": "Все подписчики запущены!"}

    except Exception as e:
        return {"error": str(e)}

@app.get("/stop_subscribers")
def stop_subscribers():
    global processes
    try:
        for process in processes:
            process.terminate()
        processes.clear()

        return {"message": "Все подписчики остановлены!"}

    except Exception as e:
        return {"error": str(e)}

@app.get("/run_speaker")
def run_script():
    try:
        result = subprocess.run(['python', 'speaker.py'], capture_output=True, text=True)
        return {"output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"error": str(e)}
