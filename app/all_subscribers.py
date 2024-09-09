# import subprocess
# import sys
#
# scripts = ['subscribers_server_cpu/cpu1.py', 'subscribers_server_cpu/cpu2.py',
#            'subscribers_server_gpu/gpu1.py', 'subscribers_server_gpu/gpu2.py']
#
# processes = []
# try:
#     for script in scripts:
#         process = subprocess.Popen(['python3', script])
#         processes.append(process)
#
#     for process in processes:
#         process.wait()
#
# except KeyboardInterrupt:
#     print("Program abort! Stopping all processes...")
#     for process in processes:
#         process.terminate()
#     sys.exit(0)
