class SystemUser:
    user_id = 0
    SYSTEM_USERS = []

    def __init__(self, name: str, contact: str):
        SystemUser.user_id += 1
        self.user_id = SystemUser.user_id
        self.name = name
        self.contact = contact
        SystemUser.SYSTEM_USERS.append(self)




