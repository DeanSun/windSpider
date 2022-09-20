# 安装、部署、打包的脚本
from setuptools import setup

install_requires = [
    # 此处将需要依赖的包配置在处
    'pymongo>=4.2.0',
    'selenium>=4.4.3',
    'beautifulsoup4>=4.11.1',
    'urllib3>=1.26.12'
]

setup(
    name='windSpider',
    version='0.0.1',
    packages=['spider'],
    install_requires=install_requires,
    include_package_data=True,
    python_requires='>=3.10'
)
