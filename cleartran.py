#语音预处理clear 不太好用需要改
import pyopenjtalk

def find_script(file):
    with open(file,'r',encoding='utf-8') as f:
        content = f.read()
    script_list = []

    line = Ce = 0
    while line > -1 :
        line = content.find('wav/',Ce,-1)
        Cs = content.find('「', line, -1)
        Ce = content.find('」', Cs, -1)
        hirakana =content[Cs+1: Ce]
        
        romaji = pyopenjtalk.g2p(hirakana)
        add = content[line:Cs] + romaji
        script_list.append(add)
    return script_list


def save_script(script_list):
    f = open('./txt.cleared', "a+", encoding="UTF-8")
    for script in script_list :
        f.write(script)
    f.close()


if __name__ == "__main__":
    file = './train.txt'
    script_list = find_script(file)
    save_script(script_list)
    print('over')