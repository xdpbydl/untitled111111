import os


def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    # print(list)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new

    if r".log" in lists[-1]:    # 如果存在日志文件
        print(file_new + "111" * 8)
        # return file_new
        return "11"
    elif os.path.isdir(file_new):  # 判断是否为文件夹
        if len(os.listdir(file_new)) == 0:  # 如果为空文件夹，返回空
            print(file_new + "222" * 8)
            return ""
        else:   # 排除文件夹，如果子目录是文件夹继续调用
            print(file_new + "333" * 8)
            new_report(file_new)
    else:  # 存在非日志（*.log）最新文件，返回空
        print(file_new + "444" * 8)
        return ""


if __name__ == "__main__":
    test_report = r"D:\Program Files\IS-RPA2020\Logs"  # 目录地址


    print( new_report(test_report))