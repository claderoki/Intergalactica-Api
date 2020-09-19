from enum import Enum
import argparse
import os

class Mode(Enum):
    production = 1
    development = 2






parser = argparse.ArgumentParser(description="Choose the mode.")
parser.add_argument("--mode", default="development", choices=[x.name for x in list(Mode)])
args = parser.parse_args()
mode = Mode[args.mode]

production = mode == Mode.production


path = __file__.replace("/src/config.py", "")
app = None



if not production:
    try:
        with open(path + "/env") as f:
            for line in f.read().splitlines():
                key, value = line.split("=")
                os.environ[key] = value
    except FileNotFoundError:
        with open(path + "/env", "w") as f:
            lines = []
            for var in ("mysql_user", "mysql_password", "mysql_port", "mysql_host", "discord_token", "owm_key"):
                lines.append(f"{var}=")
            f.write("\n".join(lines))
        raise Exception("Please fill in the 'env' file.")
