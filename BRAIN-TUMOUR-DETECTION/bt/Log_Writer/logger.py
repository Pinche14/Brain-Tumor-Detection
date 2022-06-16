from datetime import datetime

class App_Logger:

    def __init__(self):
        pass

    def log(self,log_message):
        self.now=datetime.now()
        self.date=self.now.date()
        self.current_time=self.now.strftime("%H:%M:%S")
        self.log_file=open('Centralised_Logs/logs.txt','a+')
        self.log_file.write(f"DATE : {self.date} --- TIME : {self.current_time} \t\t {log_message} \n")
