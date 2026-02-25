status = 404
match status:
    case 200: print("Success")
    case 404: print("Not Found")
    case _: print("Something went wrong")
