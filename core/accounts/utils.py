import threading

# A class for receive email_obj and run send mail operation
class EmailThreading(threading.Thread):
    def __init__(self, email_obj):
        threading.Thread.__init__(self)
        self.email_obj = email_obj

    def run(self):
        self.email_obj.send()