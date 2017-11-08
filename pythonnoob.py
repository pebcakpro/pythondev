#!/usr/bin/python
import json




myname = str(raw_input("enter your name: "))

mydict = dict( 
              FirstName = "foo",
              LastName = "bar"
              )

nextdict = {
            "FirstName": myname,
            "LastName" : "bar"
           }

print "mydict: ", type(mydict)
print "nextdict: ", type(nextdict)
print "JSON OUTPUT OF NEXTDICT: ", json.dumps(nextdict)
print "OUTPUT: ", type(json.dumps(nextdict))
