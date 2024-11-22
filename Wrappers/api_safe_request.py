from functools import wraps
import time,requests
def safe_api_request(delay=1,repet=3):
    """اجرای درخواست‌های API با مدیریت خطاها و تکرار در صورت نیاز"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(repet):  # تلاش برای ارسال درخواست تا سه بار
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    print(f"API Request Error: {e}")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator