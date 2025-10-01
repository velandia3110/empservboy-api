class Company:
    def __init__(
            self,
            id,
            nit,
            telephone,
            direction,
            business_name,
            email,
            image):
        self.id = id
        self.nit = nit
        self.telephone = telephone
        self.direction = direction
        self.business_name = business_name
        self.email = email
        self.image = image

    def to_json(self):
        return self.__dict__
