class EmailValidator:
    def __init__(self, email):
        self.email = email if self.validate() else ""
    def validate(self):
        parts = self.email.split('@')
        return False if(len(parts) != 2 or len(parts[0]) == 0  or not parts[1].count('.')) else True
    def domain(self):
        parts = self.email.split('@')
        return parts[1] if(len(parts) == 2) else None
import csv, json
csvFilename = "email_list.csv"
with open(csvFilename, "w", newline="") as f:
    w = csv.writer(f)
    [
        EmailValidator(e).validate() and w.writerow([n, e]) 
        for n, e  in {
            "A":"delhiarpitpatel@gmail.com",
            "A2":"abcd",
            "A3":"@alaska.in",
            "A4":"aaaa@gmail.com",
            "A5":"ccccc@gmail.co.in"
        }.items()
    ]

with open(csvFilename, "r", newline="") as f:
    with open("email_list.json", "w", newline="") as fj:
        l = [ i for i in csv.reader(f) ]
        json.dump(l, fj)
