import main

def testmain():	
	assert main.weather('Boston')==1

def testmain2():	
	assert main.weather('LasVegas')==1

def testmain3():	
	assert main.weather('Miami')==1

def testmain4():	
	assert main.weather('')=="---- No Name Entered ----"