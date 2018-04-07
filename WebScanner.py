from urllib.request import urlopen, Request
from joblib import Parallel, delayed
import re
import time

def parseClass(subUrl, cl):
	return urlopen(subUrl+'/'+cl[0:7]).read().decode('utf-8')

def findSub(f,match):
    classHtml = []
    try:
        subUrl = 'https://app.testudo.umd.edu/soc/'+match
        a = urlopen(subUrl)
       # cookie = a.info()['Set-Cookie']
        subHtml = a.read().decode('utf-8')
        #print(subHtml)		
        #print(sub[7:10])		
        classes = re.findall('[A-Z]{4}\d{3}\" class=\"course', subHtml)
        #print(classes)
        #Parallel(n_jobs=len(classes))(delayed(parseClass)('https://app.testudo.umd.edu/soc/201808/sections?courseIds=', cl) for cl in classes)
        for cl in classes:
            classHtml.append(urlopen(subUrl+'/'+cl[0:7]).read().decode('utf-8'))	
        print('done ', match)
        return classHtml
    except:
        print(match)
        return None
def getData():
    f = urlopen('https://app.testudo.umd.edu/soc/search?courseId=&sectionId=&termId=201808&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on')
    #print(f.read())
    html = f.read().decode('utf-8')
    #print(html)
    match = re.findall('\d{6}\/[A-Z]{4}', html)
    return Parallel(n_jobs=32,backend="threading")(delayed(findSub)(f,match[i]) for i in range(len(match)))
	
start = time.time()
#res = getData()
print(time.time()-start)
