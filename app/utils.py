import re
from functools import wraps
from datetime import datetime, timezone

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        action_info = "System Operation"
        
        if len(args) > 1:
            first_arg = args[1]
            
            if hasattr(first_arg, "title") and not isinstance(first_arg, str):
                action_info = f"Book: '{first_arg.title}'"
            else:
                action_info = f"Target ISBN/Value: {str(first_arg)}"
                
        with open("../data/log.txt", "a", encoding="utf-8") as file:
            log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{log_time}] Called [{func.__name__}] with [{action_info}]\n")
            
        return func(*args, **kwargs)
    return wrapper

def validate_isbn(isbn):
    pattern = r"^\d{3}-\d{2}-\d{3}-\d{4}-\d$"
    return bool(re.match(pattern, isbn))

class LibraryDatabaseError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
        try:
            with open("../data/log.txt", "a", encoding="utf-8") as file:
                log_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{log_time}] LibraryDatabaseError occured! Skill issue!\n")
        except Exception:
            pass