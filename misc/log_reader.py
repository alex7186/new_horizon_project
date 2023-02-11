log_path = "new_horizon/users_logfile.log"

with open(log_path, "r") as file:
    data = file.read()

for line in data.split("\n"):
    if "127.0.0.1" not in line:
        print(line)
