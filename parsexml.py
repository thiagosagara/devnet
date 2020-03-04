# Fill in this file with the code from parsing XML exercise
# import the ElementTree helper library and the regular expression engine, re
import xml.etree.ElementTree as ET
import re

#Use the parse function from ET (ElementTree) to parse the myfile.xml file. 
#Get the root element with the getroot function
xml = ET.parse("myfile.xml")
root = xml.getroot()


ns = re.match(r'{.*}', root.tag).group(0)
editconf = root.find(f"{ns}edit-config")
defop = editconf.find(f"{ns}default-operation")
testop = editconf.find(f"{ns}test-option")

#Lastly, print the value for the default operation and the test option, 
#which your parser gathered in the code above.

print("The default-operation contains: %s" % defop.text)
print("The test-option contains: %s" % testop.text)
