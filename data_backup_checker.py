from datetime import date

last_backup = date(2026, 7, 1)
today = date.today()
days_old = (today - last_backup).days

print("Days since backup:", days_old)

if days_old > 7:
    print("Backup required")
else:
    print("Backup is up to date")

print("Backup status checked")
