def http_status(status):
    match status:
       case 200:
           return "ok"
       case 404:
           return "Not found"
       case 500:
          return "Internal server error"
       case _:
            return "Unkown status"#usage print(https_status(200))

print(http_status(200))
print(http_status(404))
print(http_status(500))

        
        