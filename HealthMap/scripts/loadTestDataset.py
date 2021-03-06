from xml.dom import minidom
from HealthMap.models import Region, Dataset, Datarow, Category, Range
import random

def run():
# colors:
    DARK_GREEN="#006600"
    GREEN="#009900"
    LIGHT_GREEN="#33FF66"
    LIGHT_YELLOW="#FFFF66"
    YELLOW="#FFFF00"
    ORANGE="#FFFC00"
    LIGHT_RED="#FFF900"
    RED="#FFF000"
    DARK_RED="#CC0000"
    DARK="#333333"

    print "Loading test Datasets"

    # clean up if necessary
    cat = Category.objects.filter(name__startswith='Test')
    if cat:
        cat.delete()
    # create the test Category
    cat = Category(name="Test")
    cat.save()
    print "Created Category"

    # clean up if necessary
    dat = Dataset.objects.filter(name__startswith='Test')
    if dat:
        dat.delete()
    
    # create 3 test Datasets
    dat1 = Dataset(category=cat, name="Test1", description="1st Test Dataset", legend="Empty")
    dat1.save()
    dat2 = Dataset(category=cat, name="Test2", description="2nd Test Dataset", legend="Empty")
    dat2.save()
    dat3 = Dataset(category=cat, name="Test3", description="3rd Test Dataset", legend="Empty")
    dat3.save()
    print "Created Test Datasets"

    # clean up if necessary
    ran = Range.objects.filter(name__startswith='Test')
    if ran:
        ran.delete()
    # create the test Ranges
    ran = Range(dataset=dat1, name="Test Low Range", low=0, high=9, color=GREEN)
    ran.save()
    ran = Range(dataset=dat1, name="Test Mid Range", low=10, high=19, color=YELLOW)
    ran.save()
    ran = Range(dataset=dat1, name="Test High Range", low=20, high=29, color=RED)
    ran.save()
    ran = Range(dataset=dat2, name="Test Low Range", low=0, high=9, color=GREEN)
    ran.save()
    ran = Range(dataset=dat2, name="Test Mid Range", low=10, high=19, color=YELLOW)
    ran.save()
    ran = Range(dataset=dat2, name="Test High Range", low=20, high=29, color=RED)
    ran.save()
    ran = Range(dataset=dat3, name="Test Low Range", low=0, high=9, color=GREEN)
    ran.save()
    ran = Range(dataset=dat3, name="Test Mid Range", low=10, high=19, color=YELLOW)
    ran.save()
    ran = Range(dataset=dat3, name="Test High Range", low=20, high=29, color=RED)
    ran.save()
    print "Created Ranges"

    # use states.xml to iterate through States
    xmldoc = minidom.parse('HealthMap/scripts/states.xml')
    cNodes = xmldoc.childNodes
    sList = cNodes[0].getElementsByTagName("state")     # top level in DOM is States

    # populate datasets
    for state in sList: # iterate through each State
        # create the State record in Datarow table with one zero value
#        print ("%s (%s)" % (state.getAttribute('name'), state.getAttribute('abbrev')))
        reg = Region.objects.filter(state=state.getAttribute('abbrev'))
        if len(reg)==1:
            row = Datarow(dataset=dat1, region=reg[0], value=random.randrange(0,29))
            row.save()
            row = Datarow(dataset=dat2, region=reg[0], value=random.randrange(0,29))
            row.save()
            row = Datarow(dataset=dat3, region=reg[0], value=random.randrange(0,29))
            row.save()
            
    print ("... %s values" % len(sList))

