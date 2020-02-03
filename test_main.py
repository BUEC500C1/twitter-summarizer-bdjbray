import pytest
import main

def testmain():	
	assert main.test('Boston')==1

def testmain1():	
	assert main.test('Los Angeles')==1

def testmain2():	
	assert main.test('New York')==1