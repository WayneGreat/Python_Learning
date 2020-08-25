import setuptools
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", 'r') as f:  # 自动读取
    long_description = f.read()

setuptools.setup(
    name="wayneproject",  # 包名称
    version="1.0",  # 包版本
    author="qiwsir",  # 作者名称
    author_email="weihongye669@gmail.com",  # 作者邮箱
    description="This is my first project",  # 包详细描述
    long_description=long_description,  # 长描述，使用README,打包到pipy需要
    long_description_content_type="text/markdown",  # 描述格式类型
    url="",  # 项目官网
    py_modules=['langspeak'],  # 使用包时的名称
    package=setuptools.find_packages(),
    classifiers=[  # 程序的所属分类列表
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'  # python版本依赖
)
