import os
import json

class JsonManager:
    
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.exists(self.file_path):
            pass
        else:
            with open(self.file_path,'w',encoding='utf-8') as file:
                json.dump({}, file, indent=4, ensure_ascii=False)

    def manage_json_file(self, default_data=None):
        """
        مدیریت فایل JSON برای ایجاد، خواندن و به‌روزرسانی.

        Args:
            file_path (str): مسیر فایل JSON.
            default_data (dict, optional): داده‌های پیش‌فرض برای ایجاد فایل. اگر None باشد، یک دیکشنری خالی ذخیره می‌شود.
        Returns:
            dict: داده‌های فایل JSON.
        """
        if not os.path.exists(self.file_path):
            # اگر فایل وجود نداشت، یک فایل جدید با داده‌های پیش‌فرض ایجاد کن
            with open(self.file_path, 'w') as file:
                json.dump(default_data or {}, file, indent=4)
            print(f"فایل {self.file_path} ساخته شد.")

        # خواندن داده‌های فایل JSON
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            print(f"داده‌های موجود در فایل: {data}")
        return data

    def read_json_file(self):
        """
        خواندن داده‌های فایل JSON.

        Args:
            file_path (str): مسیر فایل JSON.
        Returns:
            dict: داده‌های فایل JSON.
        """
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            print(f"داده‌های موجود در فایل: {data}")
        return data

    def update_json_file(self, updates):
        """
        به‌روزرسانی داده‌های فایل JSON.

        Args:
            file_path (str): مسیر فایل JSON.
            updates (dict): دیکشنری حاوی داده‌هایی که باید به‌روزرسانی شود.
        """
        # ابتدا فایل را بخوان
        data = self.manage_json_file(self.file_path)

        # داده‌ها را به‌روزرسانی کن
        data.update(updates)

        # داده‌های جدید را در فایل ذخیره کن
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"فایل {self.file_path} به‌روزرسانی شد.")

if __name__ == "__main__":
    # مسیر فایل JSON
    file_path = "config.json"
    mj = JsonManager(file_path)
    # داده‌های پیش‌فرض
    default_data = {"name": "Default", "version": 1.0}

    # مدیریت فایل (ساخت یا خواندن)
    data = mj.manage_json_file(default_data)

    # به‌روزرسانی فایل
    mj.update_json_file({"version": 1.0, 'something':'past'})

    # خواندن فایل بعد از به‌روزرسانی
    data = mj.manage_json_file()