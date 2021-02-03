"""
Car sales.
"""
from data.customers import customers
from dealer import agent
from data.agents import agents


class Run(object):
    """
    Run the sales.
    """

    def sales(self):
        """
        Simulate sales using test data and print out customer and agent reports showing
            (1) Summary statistics, with the mean, median, and SD of customer wait times.
            (2) Agent data showing agent ID, deals closed, total revenue generated,
                commission earned, and bonus awarded, in a tabular form.
        """
        all_customers = customers(100)
        all_agents = agents(5)
        list_of_agent = []
        for aget in all_agents:
            new_agent = agent.Agent(**aget)
            list_of_agent.append(new_agent)
        agent.Agent.init(*list_of_agent)
        date = 0
        wait_times = []
        for customer in all_customers:
            """
            check if it's a new day. If true, reset the appointment 
            """
            if customer.get("arrival_time").day > date:
                agent.Agent.new_day()
                date = customer.get("arrival_time").day
            """
            pass the customer the method "get", and return with the selected agent and waittime
            """
            best_agent, wait_time = agent.Agent.get(**customer)
            wait_times.append(wait_time)
        """
        get the wait_time status
        """
        best_agent.get_stats(*wait_times)

        for aagent in list_of_agent:
            agent.Agent.bonus(aagent.agent_id)
            print()
            print("Agent_id : ", aagent.agent_id)
            agent.Agent.get_sales(aagent.agent_id)


if __name__ == "__main__":
    Run().sales()
