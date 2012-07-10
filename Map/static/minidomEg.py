from xml.dom import minidom

xmldoc = minidom.parse('states.xml')
cNodes = xmldoc.childNodes
sList = cNodes[0].getElementsByTagName("state")


for state in sList:
    print ("%s (%s)" % (state.getAttribute('name'), state.getAttribute('abbrev')))
    
    pList = state.getElementsByTagName("point")
    print ("1st polyline:%s" % pList[0].toxml())
    print len(pList)
    

