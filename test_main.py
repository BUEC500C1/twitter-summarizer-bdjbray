import main

def testmain():	
	assert main.test('Boston')==1

def testmain2():	
	assert main.test('LasVegas')==1

def testmain3():	
	assert main.test('Miami')==1

def testmain4():	
	assert main.test('abc')==0