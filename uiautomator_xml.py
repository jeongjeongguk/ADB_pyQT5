import subprocess as cmd
from xml.dom.minidom import parse

class parsing(object):
    def __init__(self):
        self.filepath = ""

    @staticmethod


    @classmethod
    def parseXML(cls, targetPath):
        dom = None
        dom = parse(targetPath)
        dom.toprettyxml(encoding="utf-8")
        # clickable = "true" 인것에 대해서, resource-id= 를 뽑기
        # os 4.1.2 에서는 clickable 요소가 resoucre-id가 항목이 없음
        clickable = {}
        clickable["resource-id"] = []
        clickable["Text"] = []
        clickable["bounds"] = []

        for node in dom.getElementsByTagName('node'):
            if node.getAttribute('clickable') == "true":
                clickable["bounds"].append([node.getAttribute('bounds')])
                if node.getAttribute('resource-id') != '':
                    clickable["resource-id"].append([node.getAttribute('resource-id')])
                else:
                    #clickable["Text"].append([node.getAttribute('text')]) #여기 추가되는 횟수만큼 아래 주석문에 의한 내용이 반복추가됨
                    #pass

                    for childnode in dom.getElementsByTagName('node'):
                        if childnode.getAttribute('text') != '':
                            clickable["Text"].append([childnode.getAttribute('text')])

        return clickable

if __name__ == "__main__":
    parsing.exportXML()
    import os, pprint
    directory = '%s/' % os.getcwd()
    pprint.pprint(parsing.parseXML(directory + ".\\test_me.xml"))
