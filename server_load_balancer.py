servers = {
    "Server_A": 65,
    "Server_B": 92,
    "Server_C": 48
}

for server, load in servers.items():
    print(server, "Load:", load, "%")

    if load > 80:
        print("Traffic Redistribution Needed")

print("Monitoring Complete")
