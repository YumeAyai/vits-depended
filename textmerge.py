#本脚本实现将所有txt列表合成到train.txt中用于训练
#使用前需将文件存入同级目录text中
import os
if not os.path.exists('text'):
    os.mkdir('text')
#for /r %%a in (*.ogg) do ffmpeg -i "%%~fa" -ar 22050 "voicewav/%%~na.wav"


def read_files(path) :
    file_name_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("txt"):
                file_name_list.append(file)
    return file_name_list


def find_script(path,file_name):
    with open(path + file_name,'r',encoding='utf-8') as f:
        content = f.read()
    script_list=[]
    script_list.append(content[0 : -1]+'\n')
    return script_list


def save_script(script_list):
    f = open('./{}.txt'. format('train'), "a+", encoding="UTF-8")
    for script in script_list :
        f.write(script)
    f.close()


if __name__ == "__main__":
    path = "./text/"
    file_name_list = read_files(path)
    for file_name in file_name_list:
        #print(path, file_name)
        script_list = find_script(path,file_name)
        save_script(script_list)
        print("save",file_name)
    print("over")



