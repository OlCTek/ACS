#Modules----------------------------------------------------------------

#Import modules and define/initiate if necessary
import speech_recognition as sr
ac = sr.Recognizer()
import webbrowser as wb
from easygui import *
from gtts import gTTS
import pygame
pygame.init()
import time
import math
import sys
import os

#Commands---------------------------------------------------------------

#Define key words for commands
name = ["ace"]
greet = ["hello", "hi", "hey"]
initiate = ["initiate"]
password = ["three four four seven"]
openApp = ["open"]
openFile = ["open", "file"] 
openSite = ["open", "site"]
playFile = ["play"]
endCom = ["power", "off"]

#Applications-----------------------------------------------------------

#Define key words for specific programs
chrome = ["google", "chrome", "not"]
firefox = ["fire", "fox", "anonymous"]

#Phrases----------------------------------------------------------------

#Establish variables for common phrases
calibrate = "Calibrating..."
awaiting = "Awaiting user input..."
userSaid = "User input: "
unknownIn = "Could not understand user."

#Address def------------------------------------------------------------
	
def called():
	#Computer response to being called by name
	pygame.mixer.music.load('callFile.mp3')
	pygame.mixer.music.play()
	time.sleep(3)
	
def greetResp():
	#Computer response to a common greeting
	pygame.mixer.music.load('greetFile.mp3')
	pygame.mixer.music.play()
	time.sleep(2)
	
#General def------------------------------------------------------------

def awaitUser():
	#Notify the user that the computer is awaiting input
	print(awaiting)
	pygame.mixer.music.load('awaitFile.mp3')
	pygame.mixer.music.play()
	time.sleep(2)
	
def unknown():
	#Notify the user the computer failed to recognize vocal input
	print(unknownIn)
	pygame.mixer.music.load('unknownFile.mp3')
	pygame.mixer.music.play()
	time.sleep(5)
	
def userInpuT(com):
	#General typing option for user input
	print("Awaiting user input...")
	com = enterbox("User input: ", title = "Artificial Control System")
	print("User input: " + com)

def END():
	#Notify user that the program is ending
	print("Program ending. Goodbye.")
	pygame.mixer.music.load('endFile.mp3')
	pygame.mixer.music.play()
	time.sleep(5)
	
#Password def-----------------------------------------------------------

def passPrompt():
	#Prompt user for vocal password
	print("Enter password.")
	pygame.mixer.music.load('pass?File.mp3')
	pygame.mixer.music.play()
	time.sleep(3)
	
def passCorrect():
	#Notify user that the password entered was correct
	print("Access granted. Welcome, Craig!")
	pygame.mixer.music.load('pass1File.mp3')
	pygame.mixer.music.play()
	time.sleep(6)
	
def passIncorrect():
	#Notify user that the passwored entered was incorrect
	print("Access denied.")
	pygame.mixer.music.load('pass0File.mp3')
	pygame.mixer.music.play()
	time.sleep(2)
	
#def passNum():
	#Notify user how many attempts are remaining

#Open def---------------------------------------------------------------
	#App----------------------------------------------------------------
	
def openAResp():
	#Prompt user for which application to open
	pygame.mixer.music.load('openAFile.mp3')
	pygame.mixer.music.play()
	time.sleep(2)

def openingApp():
	#Notify user that the selected application is being opened
	print("Opening application...")
	pygame.mixer.music.load('openingAFile.mp3')
	pygame.mixer.music.play()
	time.sleep(3)

	#File---------------------------------------------------------------

def openFResp():
	#Prompt user for which file to open
	pygame.mixer.music.load('openFFile.mp3')
	pygame.mixer.music.play()
	time.sleep(2)

def openingFile():
	#Notify user that the selected file is being opened
	print("Opening file...")
 	pygame.mixer.music.load('openingFFile.mp3')
	pygame.mixer.music.play()
	time.sleep(3)

	#Website---------------------------------------------------------------

def openSResp():
	#Prompt user for which site to open
	pygame.mixer.music.load('openSFile.mp3')
	pygame.mixer.music.play()
	time.sleep(2)
	
def openingSite():
	#Notify user that the selected site is being opened
	print("Opening site...")
	pygame.mixer.music.load('openingSFile.mp3')
	pygame.mixer.music.play()
	time.sleep(3)
	
	#Sample Audio-------------------------------------------------------
	
def playSample():
	#Prompt user for which audio file to sample
	pygame.mixer.music.load('sampleAFile.mp3')
	pygame.mixer.music.play()
	time.sleep(2)
	
def playingSample():
	#Notify user that the selected audio file is being sampled
	print("Playing audio...")
 	pygame.mixer.music.load('playingAFile.mp3')
	pygame.mixer.music.play()
	time.sleep(3)

#Main-------------------------------------------------------------------
	
def main():
	#Establish variables for general use
	a = 0
	i = 0
	
	with sr.Microphone() as source:
		#Set microphone as listening device and calibrate
		print(calibrate)
		ac.adjust_for_ambient_noise(source)
		audioIn = ac.listen(source)
		
	while a == 0:
		#Wait for user to initiate code
		await()
		try:
			#Listen for audio input
			com1 = ac.recognize_sphinx(audio)
			print(userSaid + com1)
		except sr.UnknownValueError:
			#Notify user that ACS could not understand audio input
			unknown()
		for word in initiate:
			#Prompt user for password to continue
			if word in com1:
				passPrompt()
				a += 1
			else:
				unknown()
				
	while a == 1:
		#Wait for user to input password
		await()
		try:
			#Listen for audio input
			com2 = ac.recognize_sphinx(audio)
			print(userSaid + com2)
		except sr.UnknownValueError:
			#Notify user that ACS could not understand audio input
			unknown()
		for code in password:
			#Check if password entered is correct
			for i < 3:
				#Give user three vocal attempts to enter password
				if code in com2:
					#Grant user access if password is correct
					passCorrect()
					a += 1
					i += 4
				else:
					#Deny user access if password in incorrect
					passIncorrect()
					i += 1
			for i == 3:
				#Give user typed input option if vocal attempts could not be understood
				userInpuT(com2)
				if code in com2:
					passCorrect()
					#Notify user that ACS is ready to receive user commands
					await()
					a += 1
					i += 1
				else:
					passIncorrect()
	
	while a == 2:
		#Wait for user to address ACS
		try:
			#Listen for audio input
			com3 = ac.recognize_sphinx(audio)
			print(userSaid + com3)
		except sr.UnknownValueError:
			#Notify user that ACS could not understand audio input
			unknown()
		for word in name:
			#Check if ACS was called by user
			if word in com3:
				#Respond to user 
				called()
				try:
					#Listen for audio input
					com4 = ac.recognize_sphinx(audio)
					print(userSaid + com4)
				except sr.UnknownValueError:
					#Notify user that ACS could not understand audio input
					unknown()
				for word in greet:
					#Check if command contained a greeting
					if word in com4:
						#Greet user in return
						greetResp()
				for word in openApp:
					#Check if command called for an application to be opened
					if word in com4:
						#Specify which application to open
						openAResp()
						try:
							#Listen for audio input
							com5 = ac.recognize_sphinx(audio)
							print(userSaid + com5)
						except sr.UnknownValueError:
							#Notify user that ACS could not understand audio input
							unknown()
						for word in chrome:
							#Check if application desired was Google Chrome
							if word in com5:
								#Open Google Chrome
								openingApp()
								url = 'www.google.com'
								wb.get('google-chrome %s').open_new_tab(url)
						for word in firefox:
							#Check if application desired was Firefox
							if word in com5:
								#Open Firefox
								openingApp()
								url = 'www.duckduckgo.com'
								wb.get('firefox %s').open_new_tab(url)
				for word in openFile():
					#Check if command called for a file to be opened
					if word in com4:
						#Specify which file to open
						openFResp()
						userInpuT(com5)
						#Open desired file
						openingFile()
						#open file
				for word in openSite():
					#Check if command called for a site to be opened
					if word in com4:
						#Specify which site to open
						openSResp()
						userInpuT(com5)
						#Open desired site
						openingSite()
						url = com5
						wb.get('google-chrome %s').open_new_tab(url)
				for word in playFile():
					#Check if command called for an audio file to be sampled
					if word in com4:
						#Specify which audio file to play
						playSample()
						userInpuT(com5)
						#Play audio
						playingSample()
						#play sample
				for word in endCom():
					#Check if command called to terminate the code
					if word in com4:
						#Terminate code
						END()
						a += 1
main()
						
						
						
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	