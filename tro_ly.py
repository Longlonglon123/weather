import speech_recognition

while True:
	robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm listening")
		audio = robot_ear.listen(mic)
	print("Robot:....")

	try:
		you = robot_ear.recognize_google(audio)
	except TypeError as e:
		print(e)
		you = ""

	print("you: " + you)

	if you == " ":
		robot_brain = "I can't here you"
	elif "hello" in you:
		robot_brain = "hello, I can help you"
	elif "today" in you:
		from datetime import date

		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		from datetime import datetime

		now = datetime.now()
		robot_brain = now.strftime("%H:%M:%S")
	elif "president" in you:
		robot_brain = "Donald Trump"
	elif "thank you" in you:
		robot_brain = "ohh nothing"
	elif "bye" in you:
		robot_brain = "goodbye"
		robot_mouth = pyttsx3.init()
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else: 
		robot_brain = "sorry I can't help you"
	print(robot_brain)

	import pyttsx3

	robot_mouth = pyttsx3.init()
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
