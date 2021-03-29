#项目描述

这是web的自动化，基于selenium+pytest框架

#环境准备
1.python 3.7
2.pytest 4.5.0

依赖包安装
> pip install –r requirements.txt

#运行用例
>pytest

#生成报告
生成allure报告
>pytest --alluredir ./allure_report


#pytest.ini配置
'''
#实时控制台输出日志
log_cli = 1
#链接
url = "http://49.235.92.12:8200/"
'''
