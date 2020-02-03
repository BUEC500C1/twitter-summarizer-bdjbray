import pytest
import main

def testmain():	
	locs=['Boston','Los Angeles','New York']
	for items in locs:
	   assert main.test(items)==1
