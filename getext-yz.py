#适用于yuzusoft,find方法实现的原型
import os
if not os.path.exists('text'):
    os.mkdir('text')
#for /r %%a in (*.ogg) do ffmpeg -i "%%~fa" -ar 22050 "voicewav/%%~na.wav"


def read_files(path) :
    file_name_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("tjs"):
                file_name_list.append(file)
    return file_name_list

#find方法爬取文本语音对应
def find_script(path,file_name,name):
    with open(path + file_name,'r',encoding='utf-8') as f:
        content = f.read()
    script_list = []
    Cp=Ve=0
    while Cp > -1 :
        Cp = content.find('''(const) [
          "%s",
          (const) [
            (const) [''' %name, Ve, -1)
        if Cp == -1 :
            break
        Cs = content.find('「', Cp, -1)
        Ce = content.find('」', Cs, -1)
        Vs = content.find('"voice" => "', Cp, -1)
        Ve = content.find('"', Vs+12, -1)
        Ves = content.find('|', Vs+12, Ve)
        if Ves == -1:
            add ='wav/'+content[Vs+12: Ve]+'.wav|' +content[Cs: Ce+1]+'\n'
        else :
            add ='wav/'+content[Vs+12: Ves]+'.wav|' +content[Cs: Ce+1]+'\n'
        script_list.append(add)
        #print(content[Vs+12: Ve],"v")
        #print(content[Cs: Ce+1],"c")
        #print(Cp)
        #print(add)
        
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



