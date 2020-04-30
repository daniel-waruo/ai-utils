from unittest import TestCase

from ..frontier import StackFrontier, QueueFrontier
from ..node import Node


class StackFrontierTestCase(TestCase):
    def setUp(self):
        self.initial_state = Node(None, 'test-state', None)
        self.frontier = StackFrontier()
        self.frontier.push(self.initial_state)

    def test_pop_initial_state(self):
        # check if the initial state has been popped successfully
        self.assertEqual(self.frontier.pop(), self.initial_state, "Pop Initial State Failed")

    def test_pop_order(self):
        # add node to frontier
        new_node = Node(self.initial_state, "test-second-state", "test-action")
        self.frontier.push(new_node)
        # check if the popped node was the last one in the list
        last_node = self.frontier.frontier[-1]
        popped_node = self.frontier.pop()
        self.assertEqual(popped_node, last_node, "Stack Frontier Pop Order Failure")


class QueueFrontierTestCase(TestCase):
    def setUp(self):
        self.initial_state = Node(None, 'test-state', None)
        self.frontier = QueueFrontier()
        self.frontier.push(self.initial_state)

    def test_pop_initial_state(self):
        # check if the initial state has been popped successfully
        self.assertEqual(self.frontier.pop(), self.initial_state, "Pop Initial State Failed")

    def test_pop_order(self):
        # add node to frontier
        new_node = Node(self.initial_state, "test-second-state", "test-action")
        self.frontier.push(new_node)
        # check if the popped node was the last one in the list
        first_node = self.frontier.frontier[0]
        popped_node = self.frontier.pop()
        self.assertEqual(popped_node, first_node, "Queue Frontier Pop Order Failure")


class NodeTestCase(TestCase):

    def test_node_creation(self):
        node = Node(None, "test-state", "test-action")
        self.assertEqual(node.parent, None, "Node Failed to Set Parent")
        self.assertEqual(node.state, "test-state", "Node Failed to Set State")
        self.assertEqual(node.action, "test-action", "Node Failed to Set Action")
