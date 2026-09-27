def block_websites(host_path, websites, redirect):
    with open(host_path, "r+") as host_file:
        content = host_file.read()

        for website in websites:
            if website not in content:
                host_file.write(
                    redirect + " " + website + "\n"
                )


def unblock_websites(host_path, websites):
    with open(host_path, "r+") as host_file:
        lines = host_file.readlines()

        host_file.seek(0)

        for line in lines:
            if not any(website in line for website in websites):
                host_file.write(line)

        host_file.truncate()
