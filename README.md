# 程序功能
1. 每隔一端时间检查指定文件的变动情况
2. 调用系统命令rsync增量同步
3. 将输出保存到日志

# 用法
* 在终端执行如下命令
$ nohup python Autobak.py >> .autobak.log &
