class Sentence:
    """Class that abstract prepositional sentences"""

    def evaluate(self, model):
        """Evaluates the logical sentence.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            model: Dictionary containing True/False values of symbols

        Raises:
            Exception: raised when the method is not implemented
        """
        raise Exception("nothing to evaluate")

    def formula(self):
        """Returns string formula representing logical sentence."""
        return ""

    def symbols(self):
        """Returns a set of all symbols in the logical sentence.

        Returns:
            set: An empty set
        """
        return set()

    @classmethod
    def validate(cls, sentence):
        """Checks if sentence is a valid sentence.

        The method is an instance of `Sentence`

        Args:
            sentence (Sentence) : an instance of a sentence

        Raises:
            TypeError: raised if sentence is not a valid instance of Sentence
        """
        if not isinstance(sentence, Sentence):
            raise TypeError("must be a logical sentence")

    @classmethod
    def parenthesize(cls, s: str) -> str:
        """Parenthesizes an expression if not already parenthesized.

        Args:
            s : This is the expression to be parenthesized

        Returns:
            str: parenthesized expression
        """

        def balanced(s):
            """Checks if a string has balanced parentheses."""
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0

        if not len(s) or s.isalpha() or (
                s[0] == "(" and s[-1] == ")" and balanced(s[1:-1])
        ):
            return s
        else:
            return f"({s})"
