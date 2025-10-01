class Headquarter:
    def __init__(
        self,
        id,
        name,
        state,
        company_id
    ):
        self.id = id
        self.name = name
        self.state = state
        self.company_id = company_id

    def to_json(self):
        return self.__dict__
