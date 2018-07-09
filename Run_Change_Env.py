import fileinput

path_to_file = "D://automation-newforexqa//src//main//python//utils//config//Config.py"

url_client_area = "https://newforexqa.pandats.com/"
new_url_crm = "https://newforexstaging.ptscrm.com/"

collector = []

with open(path_to_file, "a") as f:
    for i, line in enumerate(fileinput.input(path_to_file)):
        if line.startswith("url_client_area"):
            tmp_list = line.split("\"")
            tmp_list[1] = new_url_crm
            new_line = "\"".join(tmp_list)
            collector.append(new_line)
        elif line.startswith("url_crm"):
            tmp_list = line.split("\"")
            tmp_list[1] = url_client_area
            new_line = "\"".join(tmp_list)
            collector.append(new_line)
        else:
            collector.append(line)

open(path_to_file, 'w').close()

with open(path_to_file, "a") as f:
    for i in collector:
        f.write(i)
