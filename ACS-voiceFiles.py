from gtts import gTTS
import os

ftest = gTTS(text = 'Testing testing one two three.', lang = 'en')
ftest.save('test.mp3')

#Address----------------------------------------------------------------

fcall = gTTS(text = 'What can I do for you sir?', lang = 'en')
fcall.save('callFile.mp3')

fgreet1 = gTTS(text = 'Hello there.', lang = 'en')
fgreet1.save('greet1File.mp3')

fgreet2 = gTTS(text = 'Hey there.', lang = 'en')
fgreet2.save('greet2File.mp3')

fgreet3 = gTTS(text = 'Hi there.', lang = 'en')
fgreet3.save('greet3File.mpl3')

fgreet4 = gTTS(text = 'Hello', lang = 'en')
fgreet4.save('greet4File.mp3')

fgreet5 = gTTS(text = 'Hey', lang = 'en')
fgreet5.save('greet5File.mp3')

fgreet6 = gTTS(text = 'Hi', lang = 'en')
fgreet6.save('greet6File.mp3')

#-----------------------------------------------------------------------

#General----------------------------------------------------------------

fawait = gTTS(text = 'Awaiting user input.', lang='en')
fawait.save('awaitFile.mp3')

funknown = gTTS(text = 'I cant understand what you are saying. Learn to ununciate.', lang = 'en')
funknown1.save('unknownFile.mp3')

fend = gTTS(text = 'Powering down systems. Goodnight Craig.', lang = 'en')
fend.save('endFile.mp3')

fopeningGen = gTTS(text = 'Opening. One moment sir.', lang = 'en')
fopeningGen.save('openingFile.mp3')

fplayingGen = gTTS(text = 'Playing. One moment sir.', lang = 'en')
fplayingGen.save('playingFile.mp3')

fwillDo = gTTS(text = 'Will do sir.', lang = 'en')
fwillDo.save('willdoFile.mp3')

#-----------------------------------------------------------------------

#Password---------------------------------------------------------------

fpassPrompt = gTTS(text = 'Enter activation password please.', lang = 'en')
fpassPrompt.save('pass?File.mp3')

fpassGrant1 = gTTS(text = 'Access granted. Artificial control systems initiating. Welcome Craig.', lang = 'en')
fpassGrant1.save('pass11File.mp3')

fpassGrant2 = gTTS(text = 'There we go. Access granted. Initiating artificial control systems.', lang = 'en')
fpassGrant2.save('pass12File.mp3')

fpassDeny1 = gTTS(text = 'Access denied.', lang = 'en')
fpassDeny1.save('pass01File.mp3')

fpassDeny2 = gTTS(text = 'Access still denied. How about trying a different password genius?', lang = 'en')
fpassDeny2.save('pass02File.mp3')

fpassDeny3 = gTTS(text = 'Either you dont know the password or you cant ununciate. Lets try typing shall we?', lang = 'en')
fpassDeny3.save('pass03File.mp3')

fpassDeny4 = gTTS(text = 'Well now you cant blame your inability to speak. Access denied.', lang = 'en')
fpassDeny4.save('pass04File.mp3')

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

