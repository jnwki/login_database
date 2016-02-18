class DBReader:

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
        self.account = self.get_user(name, password)
        self.user_data = None
        self.status_report = ''
    def read_file(self):
        with open("login_db") as infile:
            return [line.split(',') for line in infile.readlines()]

    def get_user(self, name, password):
        return [line for line in self.read_file() if line[0] == name and line[1] == password]

    def __repr__(self):
        return str(self.account)

    def write_to_file(self, new_user=None):

        with open("login_db", "a") as outfile:
            outfile.write(new_user)
