from enum import Enum
import argparse
import os

path = __file__.replace("\\", "/").replace("/src/config.py", "")
app = None

try:
    with open(path + "/env") as f:
        for line in f.read().splitlines():
            key, value = line.split("=")
            os.environ[key] = value
except FileNotFoundError:
    with open(path + "/env", "w") as f:
        lines = []
        for var in ("mysql_db_name", "mysql_user", "mysql_password", "mysql_port", "mysql_host"):
            lines.append(f"{var}=")
        f.write("\n".join(lines))
    raise Exception("Please fill in the 'env' file.")
