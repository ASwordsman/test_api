# test_api框架介绍
接口测试框架 --持续完善中 pytest + requests + jenkins + allure 添加pandas（数据分析部分）

本框架使用关键字自动化测试框架概念  需要一定的python基础  可适用于复杂业务逻辑api 也可适用于详细的大量的case


env 文件 ：负责切环境比如 测试环境 切到正式环境 由于我负责的是app项目 所以只需要换掉 请求头就可以

yaml_dict 文件: 负责管理环境变量

execl 文件 ：存放execl测试数据

本框架有俩部分 目前带添加  jenkins部分

目前编写自动化框架主要面临主要问题是：

1 请求参数的管理 2 返回数据的处理  3 实现出快速的编写自动化测试脚本

解决方案
  
  1 可使用conftest.py 和fixture 来进行请求参数的管理 和返回数据的处理
  
    缺点  
          后期case增多 可能会造成 conftest文件过大 conftest文件允许同一目录下有多个应该不是大问题
    
    解决方法  为更适用于实际的项目中使用 新增execl管理测试数据 以便管理大量的case 并使用 pytest进行数据驱动
更新记录并增加pytest数据驱动调试功能

      9月1号 
        在 reclient 类中添加requonse属性 解决了过于依赖conftest文件的 问题 使得编码更加简洁
      9月29号 
        新增log日志用于pytest的调试
      2020年1月27号
          新增execl数据驱动模块（基于pandas库）

    有改善建议请联系 微信 wanghaikang123 如有学习需求 也可联系  备注请填 测试学习 --地区 姓名选填

测试报告展示图
![image](https://github.com/ASwordsman/test_api/blob/master/jpg/result.png)
          
环境安装
       1.下载 pip install  pipenv
       2.运行 pipenv install

       安装allure
                 下载连接 https://github.com/allure-framework/allure2/releases/tag/2.13.1
                 教程 https://docs.qameta.io/allure/
