import sys
import platform
import hashlib
import io
import memcache
import json
from copy import deepcopy
from fontTools.ttLib import TTFont

ProRootDir = 'G:\\EveryDayCode\\JustPython\\StartItFromPython\\' \
                if platform.system() == 'Windows' else '/Users/wangjiawei/justpython/'
sys.path.append(ProRootDir + "utils")
import CreateFile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


def get_base_fonts():
    pathname = CreateFile.createFile('msyh.ttf', 'DataHub/cv')
    baseFonts = TTFont(pathname)
    base_uni_list = baseFonts.getGlyphOrder()[1:]
    return [baseFonts, base_uni_list]


def create_new_obj(baseGlyph):
    try:
        newobjstr = str(baseGlyph.coordinates.array.tolist()) + \
            str(baseGlyph.coordinates._a.tolist()) + \
            str(baseGlyph.endPtsOfContours) + \
            str(baseGlyph.flags.tolist()) + str(baseGlyph.xMax) + str(baseGlyph.xMin) + str(baseGlyph.yMax) + str(baseGlyph.yMin)
    except:
        newobjstr = ''
    return newobjstr


def main():
    baseRet = get_base_fonts()
    baseFonts = baseRet[0]
    base_uni_list = baseRet[1]
    result = {}
    for i in base_uni_list:
        baseGlyph = baseFonts['glyf'][i]
        newobjstr = create_new_obj(baseGlyph)
        if newobjstr == '':
            continue
        hashstr = hashlib.md5(newobjstr.encode("utf-8")).hexdigest()
        try:
            unistr = '\\u' + i[3:7].lower()
            realstr = unistr.encode('utf-8').decode('unicode_escape')
            result[hashstr] = realstr
        except:
            result[hashstr] = i.lower()

    mc = memcache.Client(['127.0.0.1:11211'], debug=1)
    # ret = mc.get('basefonts')
    # if ret is None:
    # mc.delete('basefonts')
    try:
        res = json.dumps(result)
        print(sys.getsizeof(res))
        r = mc.set('basefonts', res)
        print("return:", r)
    except:
        print('somethingwrong')

    # print(result)


if __name__ == '__main__':
    main()