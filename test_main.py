import pytest
import main

def testmain():
	namelist=['Bosotn',"Los Angeles","San Francisco"]
	for item in namelist:
		main.loc=item
