# -*- coding: utf-8 -*-
import grequests
import json
import time
from PyQt4.QtCore import QThread, SIGNAL

class EDDNExport(QThread):
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        self.parent = parent
        self.counter = 0
        self.outcomeok = []
        self.outcomefail = []
    
    def execute(self, data, userID):
        self.data = data
        self.userID = userID
        self.start()
    
    def getEDDNResponse(self, response,  **kwargs):
        if response.text.strip() == "OK":
            self.outcomeok.append("OK")
        else:
            self.outcomefail.append("Fail")
        self.counter += 1
        self.emit(SIGNAL("update(int,int)"), self.counter, self.toprocess)
        if self.counter == self.toprocess:
            self.exportFinished()
            
    def exportFinished(self):
        self.result = "Success: "+unicode(len(self.outcomeok))+" Fail: "+unicode(len(self.outcomefail))
        self.emit(SIGNAL("finished(QString)"), self.result)
    
    def run(self):
        self.counter = 0
        parent = self.parent
        data = self.data
        userID = self.userID
        #print data
        self.outcomeok = []
        self.outcomefail = []
        self.toprocess = len(data)
        counter = 0
        
        req_list = []
        for line in data:
            req_list.append(json.dumps(self.createRequest(line, userID)))
            
        async_list = []

        for d in req_list:
            action_item = grequests.post("http://eddn-gateway.elite-markets.net:8080/upload/", data=d, hooks = {'response' : self.getEDDNResponse})
            async_list.append(action_item)

        # Do our list of things to do via async
        grequests.map(async_list)
        
        
    def createRequest(self, line, userID):
        request = {
                    "$schemaRef": "http://schemas.elite-markets.net/eddn/commodity/1",
                    "header": {
                        "uploaderID": userID,
                        "softwareName": "EliteOCR",
                        "softwareVersion": self.parent.appversion
                    },
                    "message": self.makeDict(line)
                   }
        return request
        
    def makeDict(self, line):
        new_dict = { "systemName": line[0],
                     "stationName": line[1],
                     "itemName": line[2],
                     "buyPrice": (int(line[4]) if line[4] else 0),
                     "stationStock": (int(line[7]) if line[7] else 0),
                     "sellPrice": (int(line[3]) if line[3] else 0),
                     "demand": (int(line[5]) if line[5] else 0),
                     "timestamp": line[9],
                    }
        if line[8] != "":
            new_dict["supplyLevel"] = line[8]
        if line[6] != "":
            new_dict["demandLevel"] = line[6]
        #print new_dict
        return new_dict