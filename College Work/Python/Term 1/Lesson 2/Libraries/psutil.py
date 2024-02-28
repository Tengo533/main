import psutil

cpu_count = psutil.cpu_count()
cpu_usage = psutil.cpu_percent(interval=3)
bytes_sent = psutil.net_io_counters().bytes_sent
boot_time = psutil.boot_time()

print("\nCPU cores =", cpu_count,"\nCPU usage =", cpu_usage, "\nBytes sent =", bytes_sent, "\nBoot time =", boot_time)