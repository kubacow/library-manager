import re
from functools import wraps
from datetime import datetime, timezone

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        target_info = "System Operation"
        
        if len(args) > 1:
            first_arg = args[1]
            
            from models import Book
            
            if isinstance(first_arg, Book):
                target_info = f"Book: '{first_arg.title}'"
            else:
                target_info = f"Target ISBN/Value: {str(first_arg)}"
                
        with open("log.txt", "a", encoding="utf-8") as file:
            log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{log_time}] Action: {func.__name__} -> {target_info}\n")
            
        return func(*args, **kwargs)
    return wrapper

class LibraryDatabaseError(Exception):
    pass

def validate_isbn(isbn):
    pattern = r"^\d{3}-\d{2}-\d{3}-\d{4}-\d$"
    return bool(re.match(pattern, isbn))