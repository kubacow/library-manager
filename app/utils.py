from functools import wraps
from datetime import datetime, timezone

def logger(func) :
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 1:
            book_obj = args[1]
            book_name = getattr(book_obj, "name", "Unknown Title")
        else:
            book_name = "Unknown Object"
        with open("log.txt", "a", encoding="utf-8") as file:
            log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            file.write(f'[{log_time}]: Executed {func.__name__} for book: "{book_name}"\n')
        return func(*args, **kwargs)
    return wrapper