class Customer:
    def __init__(
        self,
        id,
        nit,
        name,
        telephone,
        representative,
        representative_role,
        email,
        complementary_direction,
        state,
        image,
        municipios_id
        ):
        self.id = id
        self.nit = nit
        self.name = name
        self.telephone = telephone
        self.representative = representative
        self.representative_role = representative_role
        self.email = email
        self.complementary_direction = complementary_direction
        self.state = state
        self.image = image
        self.municipios_id = municipios_id

    def to_json(self):
        return self.__dict__
    
