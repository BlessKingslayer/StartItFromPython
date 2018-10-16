import base64
import sys
import time
from fontTools.ttLib import TTFont
sys.path.append("G:\\EveryDayCode\\JustPython\\StartItFromPython\\utils")
import CreateFile

font_face = '''
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
'''

def createTtfAndXml(fontsstr):
    try:
        b = base64.b64decode(fontsstr)
        curtime = time.strftime("%Y%m%d_%H%M%S")
        pathnameTtf = CreateFile.createFile('zt_' + curtime + '.ttf',
                                            'DataHub/cv')
        with open(pathnameTtf, 'wb') as f:
            f.write(b)

        font = TTFont(pathnameTtf)
        pathnameXml = CreateFile.createFile('zt_' + curtime + '.xml', 'DataHub/cv')
        font.saveXML(pathnameXml)
        return {'ttf': pathnameTtf, 'xml': pathnameXml}

    except Exception as ex:
        print('utils -> createTtfAndXml(fontsstr) has errors. \n', ex)
        return {'ttf': '', 'xml': ''}


# pathnameTtf = CreateFile.createFile('zt_base.ttf', 'DataHub/cv')
# font = TTFont(pathnameTtf)
# pathnameXml = CreateFile.createFile('zt_base.xml', 'DataHub/cv')
# font.saveXML(pathnameXml)