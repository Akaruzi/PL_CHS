from subprocess import run
import os, shutil, shlex, time
from sys import exit

def process_exec_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    result = []
    current_entry = ""
    
    for line in lines:
        if line.startswith("◆"):
            # 在处理下一个标识符行前，将当前条目加入结果集
            if "◆ru◆" in line and current_entry:
                current_entry += " " + line.split("◆ru◆")[1].strip()
            else:
                if current_entry:
                    result.append(current_entry.strip())
                current_entry = line.strip()

        elif line.startswith("◇en◇"):
            # 跳过 `◇jp◇` 的行
            continue

    # 将最后一个条目加入结果
    if current_entry:
        result.append(current_entry.strip())

    # 写入结果到输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        for entry in result:
            file.write(entry + "\n\n")

# 使用函数
process_exec_file("cn_pl_msg.txt", "./exec.msg.txt")

def malietool():
    try:
        shutil.move('exec.msg.txt',  r'malie_tool\complier\data\system\exec.msg.txt')
        os.chdir(r'malie_tool\complier')
        run(r".\Malie_Script_Tool.exe")

    except:
       print("exec.dat not found?")
    
    os.chdir(r"..\..")

    shutil.move(r"malie_tool\complier\.data\system\exec.dat", r"patch/data/system/exec.dat")

def compile():
    # packer_args = r"malie_tool/dat_packer/dat_pack.py patch ./patch"
    # packer_args = r"malie_tool/dat_packer/dat_pack.py patch ./patch"
    # run([r"./venv/python.exe"] + shlex.split(packer_args))
    run([r"python", r"./malie_tool/dat_packer/dat_pack.py"])
    shutil.move('new.dat', 'data9.dat')

malietool()
compile()
# shutil.copy('data9.dat', 'E:\PL')
