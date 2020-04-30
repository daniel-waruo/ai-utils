class Node:
    """Class representing the Node A.D.T

    Attributes:
        parent(Node) : parent node
        state (object)): state of the current node
        action: action taken to transition from parent to current node
    """

    def __init__(self, parent, state, action):
        # parent of state
        self.parent = parent
        # current state
        self.state = state
        # action that led to the state
        self.action = action
