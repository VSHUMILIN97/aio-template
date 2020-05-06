import multiprocessing

bind = "{{cookiecutter.bind_address}}:{{cookiecutter.bind_port}}"
workers = 1  # multiprocessing.cpu_count() - 1
loglevel = "DEBUG"
worker_class = "aiohttp.GunicornWebWorker"  # DO NOT CHANGE AT ALL


# For workers parameter it is better to use multiprocessing.cpu_count() as
# stated in aiohttp documentation. But there are several cases, when it's
# impossible to use forking model to scale application correctly.
