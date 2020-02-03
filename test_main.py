import pytest
import main

def testmain():	
	locs=["Boston","New York"]
	for items in locs:
	   assert main.test(items)==1
