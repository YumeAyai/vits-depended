import os
import re

if not os.path.exists('text'):
    os.mkdir('text')
#for /r %%a in (*.ogg) do ffmpeg -i "%%~fa" -ar 22050 "voicewav/%%~na.wav"


def read_files(path) :
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("ks"):
                file_name_list.append(file)
    return files

#正则表达式获取对照表
def find_script(path,file_name):
    with open(path + file_name,'r',encoding='utf-8') as f:
        content = f.read()
    script_list = []
    it = re.finditer( r'- 泠珞[\u4e00-\u9fa5]*[\s]*- (.*)\s*-(.*)\s*-(.*)\s*-(.*)\s*-(.*)\s*-(.*)\s*- (.*)\s*-(.*)\s*- ([1-9]\d*)\s*- MessageWindow', content, re.M|re.I) 
    for match in it: 
        add ='wav/'+match.group(9)+'.wav|' +match.group(7)+'|'+match.group(1)+'\n'
        script_list.append(add)
    
    return script_list
    
    


def save_script(file_name, script_list):
    f = open('./Text/{}.txt'. format(file_name), "a+", encoding="UTF-8")
    for script in script_list :
        f.write(script)
    f.close()


if __name__ == "__main__":
    path = "./scn/"
    file_name_list = read_files(path)
    # os.mkdir('./Text/')
    for file_name in file_name_list:
        script_list = find_script(path,file_name)
        save_script(file_name,script_list)
        print("save",file_name)
    print("over")

