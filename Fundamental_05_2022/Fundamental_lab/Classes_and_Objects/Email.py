class Email:
    def __init__(self,sender,receiver,content,is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:
    command = input()
    if command == 'Stop':
        break
    else:
        comm = command.split()
        send = comm[0]
        rec = comm[1]
        cont = comm[2]
        email = Email(send,rec,cont)
        emails.append(email)

send_index = [int(x) for x in input().split(', ')]
for y in send_index:
    emails[y].send()

for email in emails:
    print(email.get_info())

#print(emails)


