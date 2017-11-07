'''
Created on Oct 10, 2017

@author: Daniel
'''

class ReportGenerator(object):

    def createReport(self,testPlanName,result):
        global sectionList        
        sectionList ={}
        fileName = testPlanName+'_Report.html'
        report = open(fileName,'w+')
        report.write("<!DOCTYPE html><html><head><title>")
        report.write(testPlanName+"</title></head><h2 style=text-align:center>"+testPlanName+"</h2>")
        report.write("<hr><body><table cellpadding=5, cellspacing=5, class='param'><tr><th class='numi'>Page</th><th class='numi'>Test Case</th><th class='numi'>Result</th></tr>")
        for key in result.keys():
            sectionName = result[key][0]
            if sectionName in sectionList.keys():
                testCaseList = []
                testCaseList = sectionList[sectionName]
                testCaseList.insert(len(testCaseList),key)
                sectionList[sectionName] = testCaseList
            else:
                sectionList[sectionName] = []
                testCaseList = []
                testCaseList.insert(len(testCaseList),key)
                sectionList[sectionName] = testCaseList
        for key,value in sectionList.items():
            report.write("<tr><td class='numi' bordercolor='blue' rowspan='"+str(len(value)+1)+"'>"+key+"</strong></td></tr>")
            print(key+" section")
            for testCase in value:
                print(testCase+" testCase")
                report.write("<tr><td>"+testCase+"</td>")
                report.write("<td>"+str(result[testCase][1])+"</td></tr>")
        report.write("</table>")
        report.write("<hr></body></html>")
        report.close()
