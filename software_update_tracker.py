devices = {
    "PC_01": True,
    "PC_02": False,
    "PC_03": True
}

for device, updated in devices.items():
    status = "Updated" if updated else "Update Required"
    print(device, "-", status)

print("Update audit completed")
