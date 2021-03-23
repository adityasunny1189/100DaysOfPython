with open("mail.txt") as mail_template:
	mail_content = mail_template.read()

with open("names.txt") as file:
	names_list = file.read()
	names = names_list.split()

for name in names:
	with open(f"Names/{name}.txt", mode = "w") as mail_file:
		mail_to_send = mail_content.replace("name", name)
		mail_file.write(mail_to_send)
