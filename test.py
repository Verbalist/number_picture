import subprocess
proc = subprocess.Popen(['ls'])
print(id(proc), proc.pid, proc)

