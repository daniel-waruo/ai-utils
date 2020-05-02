from .sentence import Sentence


class Symbol(Sentence):
    """ Class Representing a Prepositional Symbol

    Args:
        name : Name used to identify the prepositional symbol
    """

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        """ Class Representing a Prepositional Symbol

        Args:
            model
        Raises:
            Exception : if the symbol was not found in the model
        """
        try:
            return bool(model[self.name])
        except KeyError:
            raise Exception(f"variable {self.name} not in model")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}
