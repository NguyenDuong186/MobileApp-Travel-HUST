import pyperclip
while True:
	print ('Nhap text')
	text = ''
	inp = ''
	while True:
		inp = input()
		text = text + inp
		if inp == '--' or inp == 'STOP':
			break	
	pyperclip.copy(text.replace('\n',' ').replace('-',''))
	if inp == 'STOP':
		break