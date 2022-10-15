#本脚本适用于真恋寄语枫秋
import os
import re

if not os.path.exists('text'):
    os.mkdir('text')
#for /r %%a in (*.ogg) do ffmpeg -i "%%~fa" -ar 22050 "voicewav/%%~na.wav"


def read_files(path) :
    file_name_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("ks"):
                file_name_list.append(file)
    return file_name_list

#正则表达式获取对照表
def find_script(path,file_name,name):
    with open(path + file_name,'r',encoding='utf-16 LE') as f:
        content = f.read()
    script_list = []
    uni = name.encode('unicode-escape').decode()
    #print(uni)
    #                                                    ↓  这里替换名字
    it = re.finditer( r'\[voice file="(.*?)"\]\n\u3010%s\u3011\[r\]\u300e(.*?)\u300f\[p\]'%uni, content, re.M|re.I) 
    for match in it: 
        #print ("voice file : ", match.group(1))
        #print ("string ", match.group(2))
        add ='wav/'+match.group(1)+'.wav|' +match.group(2)+'\n'
        script_list.append(add)
    
    return script_list
    
    


def save_script(file_name, name, script_list):
    f = open('./Text/{}/{}.txt'. format(name, file_name + '-' + name), "a+", encoding="UTF-8")
    for script in script_list :
        f.write(script)
    f.close()


if __name__ == "__main__":
    #file_name = input('file name')
    name = input('name')
    path = "./scn/"
    file_name_list = read_files(path)
    os.mkdir('./Text/{}'. format(name))
    for file_name in file_name_list:
        #print(path, file_name)
        script_list = find_script(path,file_name,name)
        save_script(file_name,name,script_list)
        print("save",file_name)
    print("over")



