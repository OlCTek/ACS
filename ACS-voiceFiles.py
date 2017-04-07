from gtts import gTTS
import os

ftest = gTTS(text = 'Testing testing one two three.', lang = 'en')
ftest.save('test.mp3')

#Address----------------------------------------------------------------

fcall = gTTS(text = 'What can I do for you sir?', lang = 'en')
fcall.save('callFile.mp3')

fgreet = gTTS(text = 'Hello there.', lang = 'en')
fgreet.save('greetFile.mp3')

#-----------------------------------------------------------------------

#General----------------------------------------------------------------

fawait = gTTS(text = 'Awaiting user input.', lang='en')
fawait.save('awaitFile.mp3')

funknown = gTTS(text = 'I cant understand what you are saying. Learn to ununciate.', lang = 'en')
funknown.save('unknownFile.mp3')

fend = gTTS(text = 'Powering down systems. Goodnight Craig.', lang = 'en')
fend.save('endFile.mp3')

fopeningGen = gTTS(text = 'Opening. One moment sir.', lang = 'en')
fopeningGen.save('openingFile.mp3')

fwillDo = gTTS(text = 'Will do sir.', lang = 'en')
fwillDo.save('willdoFile.mp3')

#-----------------------------------------------------------------------

#Password---------------------------------------------------------------

fpassPrompt = gTTS(text = 'Enter activation password please.', lang = 'en')
fpassPrompt.save('pass?File.mp3')

fpassGrant = gTTS(text = 'Access granted. Artificial control systems initiating. Welcome Craig.', lang = 'en')
fpassGrant.save('pass1File.mp3')

fpassDeny = gTTS(text = 'Access denied.', lang = 'en')
fpassDeny.save('pass0File.mp3')

#fpassNum = how many attempts remaining

#-----------------------------------------------------------------------

#Open-------------------------------------------------------------------
	#App----------------------------------------------------------------

fopenApp = gTTS(text = 'Which application would you like to open?', lang = 'en')
fopenApp.save('openAFile.mp3')

fopeningApp = gTTS(text = 'Opening application. One moment sir.', lang = 'en')
fopeningApp.save('openingAFile.mp3')

	#File---------------------------------------------------------------
	
fopenFile = gTTS(text = 'Which file would you like to open?', lang = 'en')
fopenFile.save('openFFile.mp3')

fopeningFile = gTTS(text = 'Opening file. One moment sir.', lang = 'en')
fopeningFile.save('openingFFile.mp3')

	#Website------------------------------------------------------------
	
fopenSite = gTTS(text = 'Which site would you like to open?', lang = 'en')
fopenSite.save('openSFile.mp3')

fopeningSite = gTTS(text = 'Opening site. One moment sir.', lang = 'en')
fopeningSite.save('openingSFile.mp3')

	#Sample Audio-------------------------------------------------------

fsampleAudio = gTTS(text = 'What audio would you like to sample?', lang = 'en')
fsampleAudio.save('sampleAFile.mp3')

fsamplingAudio = gTTS(text = 'Playing audio. One moment sir.', lang = 'en')
fsamplingAudio.save('playingAFile.mp3')

#-----------------------------------------------------------------------

