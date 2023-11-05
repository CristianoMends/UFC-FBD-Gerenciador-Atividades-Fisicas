
class User:
    def __init__(self):
        pass

    def __init__(self, user_id, first_name, last_name, date_birth, weight, height):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.weight = weight
        self.height = height

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_name(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def get_user_id(self):
        return self.user_id

    def get_date_of_birth(self):
        return self.date_birth

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height
