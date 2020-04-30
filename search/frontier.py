from .node import Node


class BaseFrontier:
    """Base class for Frontier Data Structure

    class abstracts the addition , removal of nodes in the frontier

    Attributes:
        frontier (:obj:`list` of :obj:Node): list of nodes in the frontier
    """

    def __init__(self):
        self.frontier = []

    def push(self, node: Node):
        """ Handles addition of nodes to the frontier

        Args:
            node: Node to be added to the frontier.

        Returns: None
        """
        self.frontier.append(node)

    def pop(self):
        # handles popping of values from the frontier
        raise NotImplementedError("Implement remove method in child classes")

    def is_empty(self):
        """ Checks if the frontier is empty.

        Returns:
            True if frontier is empty,False if frontier is not empty
        """
        return len(self.frontier) == 0

    def contains_state(self, state: any):
        """ Checks if the frontier contains a specific state.

        Args:
            state: current state of a node.

        Returns:
            True if any of the nodes in the frontier have equal state,
            False if none of the nodes in the frontier have equal state
        """
        # check if any of the nodes in the frontier have the same
        return any(node.state == state for node in self.frontier)


class StackFrontier(BaseFrontier):
    """Frontier that is implemented using a Stack A.D.S

    It is based on the principle that a stack uses the LAST-IN-FIRST-OUT flow in
    determining what will be  popped out of the Frontier.
    Hence we pop the last element added to the list

    Attributes:
        frontier (:obj:`list` of :obj:Node): list of nodes in the frontier

    """

    def pop(self):
        """ Handles removal and returning of removed nodes from the frontier

        Note:
             This method returns the last element added to the list.
        Returns:
            Node which has been removed from the frontier
        """
        if self.is_empty():
            raise Exception("empty frontier")
        # get the last element in the frontier list
        node = self.frontier[-1]
        # return the frontier list without the removed node
        self.frontier = self.frontier[:-1]
        return node


class QueueFrontier(BaseFrontier):
    """Frontier that is implemented using a Queue A.D.S

    It is based on the principle that a stack used the FIRST-IN-FIRST-OUT flow in
    determining what will be  popped out of the Frontier.
    Thus we pop the first element added to the list

    Attributes:
        frontier (:obj:`list` of :obj:Node): list of nodes in the frontier

    """

    def pop(self):
        """Handles removal and returning of removed nodes from the frontier

        Note:
             This method returns the first element added to the list.

        Returns:
            Node which has been removed from the frontier
        """
        if self.is_empty():
            raise Exception("empty frontier")
        # get the first node in the frontier
        node = self.frontier[0]
        # set new frontier as old frontier without the first element
        self.frontier = self.frontier[1:]
        return node
