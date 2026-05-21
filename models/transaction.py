class Transaction:
    def __init__(self, sort,value, description):
        self.sort=sort
        self.value=value
        self.description=description

    def to_dict(self):
        return{
            'sort':self.sort,
            'value':self.value,
            'description':self.description
        }