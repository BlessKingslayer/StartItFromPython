import platform
import sys
import json
import operator

ProRootDir = 'G:\\EveryDayCode\\JustPython\\StartItFromPython\\' \
                if platform.system() == 'Windows' else '/Users/wangjiawei/justpython/'
sys.path.append(ProRootDir + "utils")
import CreateFile
from fontTools.ttLib import TTFont

pathname = CreateFile.createFile('msyh.ttf', 'DataHub/cv')
baseFonts = TTFont(pathname)
base_uni_list = baseFonts.getGlyphOrder()[1:]

pathname2 = CreateFile.createFile('zt_20181017_171918.ttf', 'DataHub/cv')
doFonts = TTFont(pathname2)
do_uni_list = doFonts.getGlyphOrder()[1:]

# 简单比较两个字体
def cmp_font_glyph(a, b):
    # for x in dir(a):
    #     # print(eval('a.' + str(x)))
    #     print(str(x))
    try:
        if a.coordinates == b.coordinates and a.endPtsOfContours == b.endPtsOfContours \
            and a.flags == b.flags and a.xMax == b.xMax and a.xMin == b.xMin \
            and a.yMax == b.yMax and a.yMin == b.yMin:
            return True
    except:
        pass

    return False


def print_mapping_item():
    global baseFonts, base_uni_list, doFonts, do_uni_list
    for i in do_uni_list:
        doGlyph = doFonts['glyf'][i]
        for j in base_uni_list:
            baseGlyph = baseFonts['glyf'][j]
            if cmp_font_glyph(doGlyph, baseGlyph):
                try: 
                    unistr = '\\u' + j[3:7].lower()
                    realstr = unistr.encode('utf-8').decode('unicode_escape')
                    print(i.lower(), "---", j.lower(), "---", realstr)
                except:
                    print(i.lower(), "---", j.lower())
                break



print_mapping_item()

def write_to_json(base_uni_list):
    obj = {}
    for item in base_uni_list:
        try:
            unistr = '\\u' + item[3:7].lower()
            realstr = unistr.encode('utf-8').decode('unicode_escape')
            print(realstr)
            obj[item] = realstr
        except:
            print('except:', unistr)
            pass

    jsonpath = CreateFile.createFile('msyh.json', 'DataHub/cv')
    with open(jsonpath, 'w', encoding='utf-8') as file:
        file.write(json.dumps(obj, indent=4, ensure_ascii=False))
# write_to_json(base_uni_list)
