---
title: python按指定大小完成文本切割 合并脚本
comments: true
type: categories
categories: python
tags:
  - 脚本
description: python按指定大小完成文本切割 合并脚本
password: hbjb
abbrlink: 44128
date: 2017-05-09 21:03:22
---




```python
#!/usr/bin/env python
# coding=utf-8
__author__ = 'BARRY'
import os



class SplitText():
    def __init__(self, filename, max_size):
        """初始化要分割的源文件名和分割文件大小"""
        self.filename = filename
        self.max_size = max_size

    def readFile(self,filename):
        with open(self.filename, 'r',encoding='utf-8') as in_file:
            for line in in_file:
                yield line

    def get_part_file_name(self, filename, part_num=1):
        """"获取分割后的文件名称：在源文件相同目录下建立输出文件夹split_out，然后将分割后的文件放到该路径下"""
        # temp_path = os.path.dirname(filename) # 获取文件的路径（不含文件名）
        temp_path, temp_out_name = os.path.split(filename)
        out_name, suffix = temp_out_name.split('.')
        out_path = temp_path + os.sep + "split_out"
        if not os.path.exists(out_path):  # 如果临时目录不存在则创建
            os.makedirs(out_path)
        part_file_name = out_path + os.sep + out_name + "["+str(part_num) +"]" "." + suffix
        return part_file_name
    def splitText(self):
        content = ""
        part_num=1
        split_size=0
        p = self.readFile(self.filename)
        try:
            while True:
                with open(self.get_part_file_name(self.filename, part_num), 'w',encoding='utf-8') as out_file:
                    while True:
                        content = next(p)
                        # n+=1
                        # print(n)
                        # print content
                        split_size += len(content)
                        # print(split_size)
                        if split_size < self.max_size:

                            out_file.write(content)
                        else:
                            part_num += 1
                            split_size = 0
                            break
                            # if n<=max_line:
                            #     out_file.write(content)
                            # else:
                            #     part_num+=1
                            #     n=0
                            #     break
        except StopIteration as e:
            print("文件处理完毕！")

class JoinFile():
    # 初始化需要合并文件的路径，合并的文件名 可选
    def __init__(self, srcDir):

        self.srcDir = srcDir


    def find_all_subFile(self):
        file_list = os.listdir(self.srcDir )
        # 找出所有可以合并的文件 根据‘。’前一位是‘]’查询
        a = (name for name in file_list if os.path.splitext(name)[0][-1] == ']')
        return a

    def filenames_all(self):
        file_list = []
        for file in self.find_all_subFile():
            # print (file)
            temp_name = file.split('[')[0]
            file_name = temp_name + os.path.splitext(file)[1]
            # print(file_name)
            if file_name not in file_list:
                file_list.append(file_name)
        return file_list

    def join_single_file(self,filename):

        # 找出所有子文件
        file_list = [name for name in self.find_all_subFile() if name.startswith(filename.split('.')[0])]
        file_list.sort()
        if not os.path.exists(self.srcDir+os.sep+ 'join_out' + os.sep):  # 如果临时目录不存在则创建
            os.makedirs(self.srcDir+os.sep+ 'join_out' + os.sep)
        for file in file_list:

            with open(self.srcDir+os.sep+ 'join_out' + os.sep+filename, 'a', encoding='utf-8') as f, open(self.srcDir  + os.sep + file,
                                                                  'r', encoding='utf-8') as read_in:
                for line in read_in:
                    f.write(line)

    def join_all_files(self):
        for file in self.filenames_all():
            self.join_single_file(file)

if __name__ == "__main__":

    # splitFile=r"C:\Users\w\PycharmProjects\Q1\function\characterTest.py"
    # splitSize=500
    # sf = SplitText(splitFile,splitSize)
    # sf.splitText()


    src=r"C:\Users\w\PycharmProjects\Q1\function\split_out"
    file="characterTest.py"
    sf = JoinFile(src)


    # sf.join_single_file(file)
    sf.join_all_files()
```


