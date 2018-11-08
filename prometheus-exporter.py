from prometheus_client import start_http_server, Gauge
import os
import time
import psutil

def getCpuStats():
    return psutil.cpu_percent(interval=1)


def getFreeDiskSpacePercent(path):
    return psutil.disk_usage(path).percent

def getFreeDiskSpacePercentLambdaFactory(path):
    return lambda: getFreeDiskSpacePercent(path)

def getMemoryUsage():
    return psutil.virtual_memory().percent

dps = psutil.disk_partitions()

for partition in dps:
    g = Gauge('used_disk_space'+partition.mountpoint.replace('/', '_').replace('.', '_'), 'Used disk space in percent')
    g.set_function(getFreeDiskSpacePercentLambdaFactory(partition.mountpoint)) 


cpuUsage = Gauge('cpu_usage', 'Usage of the CPU in percent')
cpuUsage.set_function(getCpuStats)

memoryGauge = Gauge('memmory_usage', 'Usage of memory in percent')
memoryGauge.set_function(getMemoryUsage)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    
    while True:
        time.sleep(5)