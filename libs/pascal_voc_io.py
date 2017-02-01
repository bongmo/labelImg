import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom
from lxml import etree
import json

class PascalVocWriter:
    def __init__(self, foldername, filename, imgSize, className, databaseSrc='Unknown', localImgPath=None):
        self.foldername = foldername
        self.filename = filename
        self.databaseSrc = databaseSrc
        self.imgSize = imgSize
        self.boxlist = []
        self.className = className
        self.localImgPath = localImgPath
        self.top = {}
        self.region_ids = {}
        self.top['id'] = self.filename
        self.top['regions'] = []

    def prettify(self, elem):
        """
            Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem,'utf8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

    def genJSON(self):
        """
            Return JSON root
        """
        # Check conditions
        if self.filename is None or \
                self.foldername is None or \
                self.imgSize is None:
                    return None

        return self.top

    def addBndBox(self, xmin, ymin, xmax, ymax, name):
        rid = str( int(self.top['id']) * 10 + len(self.boxlist) )
        bndbox = {u'x':xmin, u'y':ymin, u'width':xmax-xmin, u'height':ymax-ymin, u'region_id' : rid, u'image_id': self.top['id']}
        bndbox['phrase'] = name
        self.boxlist.append(bndbox);

    def appendObjects(self, top):
        self.top['regions'] = self.boxlist
            

    def createLabelObjects(self, top):
        object_item = SubElement(top, 'class')
        object_item.text = self.className

    def save(self, targetFile = None):
        root = self.genJSON()
        self.appendObjects(root)
        
        out_file = None
        if targetFile is None:
            with open(self.filename + '.json','w') as out_file:
                json.dump(self.top, out_file)
        else:
            with open(targetFile, 'w') as out_file:
                json.dump(self.top, out_file)

class PascalVocReader:

    def __init__(self, filepath):
        ## shapes type:
        ## [labbel, [(x1,y1), (x2,y2), (x3,y3), (x4,y4)], color, color]
        self.shapes=[]
        self.filepath = filepath
        self.parseXML()

    def getShapes(self):
        return self.shapes

    def addShape(self, label, rect):
        xmin = rect[0]
        ymin = rect[1]
        xmax = rect[2]
        ymax = rect[3]
        points = [(xmin,ymin), (xmin,ymin+ymax), (xmin+xmax, ymin+ymax), (xmin+xmax, ymin)]
        self.shapes.append((label, points, None, None))

    def parseXML(self):
        assert self.filepath.endswith('.json'), "Unsupport file format"
        data = ''
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        filename = data['id'] + '.jpg'
        for region in data['regions']:
            label = region['phrase']
            rect = []
            rect.append(region['x'])
            rect.append(region['y'])
            rect.append(region['width'])
            rect.append(region['height'])
            self.addShape(label, rect)

        return True


# tempParseReader = PascalVocReader('test.xml')
# print tempParseReader.getShapes()
"""
# Test
tmp = PascalVocWriter('temp','test', (10,20,3))
tmp.addBndBox(10,10,20,30,'chair')
tmp.addBndBox(1,1,600,600,'car')
tmp.save()
"""

