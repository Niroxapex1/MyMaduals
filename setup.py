from setuptools import setup, find_packages

setup(
    name="BestMaduals",  # نام پکیج
    version="0.1.0",  # نسخه اولیه
    packages=find_packages(),  # تمام پوشه‌های دارای __init__.py را اضافه می‌کند
    install_requires=[  
        "requests",  # کتابخانه‌های مورد نیاز  
    ],
    author="نام تو",
    author_email="ایمیل تو",
    description="توضیح کوتاه درباره ماژول",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Niroxapex1/MyMaduals.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # حداقل نسخه پایتون مورد نیاز
)
