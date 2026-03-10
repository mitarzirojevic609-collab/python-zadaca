import psutil

memory_ifno = psutil.virtual_memory()

ram = psutil.virtual_memory()
total_ram_gb = ram.total/(1024**3)
print(f"total RAM: {total_ram_gb:.2f}GB")

cpu_usage = psutil.cpu_percent(interval=None)
coress_pf = psutil.cpu_count(logical=False)
coress_lc = psutil.cpu_count(logical=True)
current_process = psutil.Process()
number_of_threads = current_process.num_threads()

print(f"Cpu usage: {cpu_usage:}%")
print(f"Number of physical: {coress_pf}")
print(f"Number of logical: {coress_lc}")
print(f"Number of threads: {number_of_threads}")