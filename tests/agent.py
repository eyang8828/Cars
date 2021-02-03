"""
Unit tests for agent module.
"""
import unittest
from datetime import datetime, timedelta
from data import agents, customers
from dealer import agent


class TestAgent(unittest.TestCase):
    """
    Tests for agent.
    """

    def setUp(self):
        self.agents = agents.agents(5)
        self.customers = customers.customers(100)
        self.agents_list = []
        for aget in self.agents:
            new_agent = agent.Agent(**aget)
            self.agents_list.append(new_agent)

    def test_get_agent(self):
        """
        check the return value is in correct type.
        """
        agent.Agent.init(*self.agents_list)
        for customer in self.customers:
            best_agent, wait_time = agent.Agent.get(**customer)
        self.assertIsInstance(best_agent, agent.Agent)
        self.assertIsInstance(wait_time, int)

    def test_bonus(self):
        """
        check whether bonus applied correctly.
        """
        the_agent_stuff = agents.agents(1)
        test_list = []
        for stuff in the_agent_stuff:
            the_agent = agent.Agent(**stuff)
            test_list.append(the_agent)
        agent.Agent.init(*test_list)
        for customer in self.customers:
            best_agent, wait_time = agent.Agent.get(**customer)
        self.assertTrue(agent.Agent.bonus(best_agent.agent_id))
    def test_bonus_day(self):
        """
        check if the bonus will apllied correctly if we start the date at the end of a month
        """
        customer_list = []
        days = [28, 28, 28, 1, 1, 1, 2, 2, 2, 3]
        for date in days:
            the_customer = {
                "arrival_time": datetime(2019, 2, date, 7, 30),
                "interest": 0,
                "sale_closed": True
            }
            customer_list.append(the_customer)
        for customer in customer_list:
            best_agent, wait_time = agent.Agent.get(**customer)
        self.assertTrue(agent.Agent.bonus(best_agent.agent_id))

if __name__ == "__main__":
    unittest.main()
