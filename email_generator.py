
import random

class EmailGenerator:
    def __init__(self, file_name, email_url):
        self.file_name = file_name
        self.email_url = email_url
    
    def generate_email(self):
        emails = []
        with open(self.file_name, 'r') as file:
            for line in file:
                name = line.strip().split()
                if len(name) >= 2:
                    first_name = name[0].lower()
                    last_name = name[1].lower()
                    email = last_name[0] + first_name + str(random.randint(0, 999)).zfill(3) + self.email_url
                    emails.append(email)
        
        return emails

#Sample Test
generator = EmailGenerator('Names.txt', '@outlook.com')
generated_emails = generator.generate_email()
for i, email in enumerate(generated_emails, start =1):
    print(i, " " +email)
     
