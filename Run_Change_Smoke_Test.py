import fileinput

path_to_file = "D:/automation-newforexqa/src/main/python/utils/config/Config.py"

test = "Smoke New Forex Staging"

collector = []

with open(path_to_file, "a") as f:
    for i, line in enumerate(fileinput.input(path_to_file)):
        if line.startswith("test"):
            tmp_list = line.split("\"")
            tmp_list[1] = test
            new_line = "\"".join(tmp_list)
            collector.append(new_line)
        else:
            collector.append(line)

open(path_to_file, 'w').close()

with open(path_to_file, "a") as f:
    for i in collector:
        f.write(i)
