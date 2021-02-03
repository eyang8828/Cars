"""
Agent object.
"""
import statistics
from datetime import timedelta
import data



class Agent(object):
    """
    Car sales agent.
    """
    @staticmethod
    def get_stats(*wait_time):
        """
        get the stats for the customer wait time
        """
        mean = statistics.mean(wait_time)
        median = statistics.median(wait_time)
        std = statistics.stdev(wait_time)
        temp = {"mean": mean, "median": median, "std": "{:.2f}".format(std)}
        print(temp)

    @staticmethod
    def agent_summary():
        pass

    @classmethod
    def init(cls, *agent_data):
        """
        store the agent data, time that they get their customer
        """
        cls._agents_data = agent_data
        cls._agents_time = {}
        cls._agents = {}
        cls._deals_closed = {}
        for agent in cls._agents_data:
            temp = {agent.agent_id: {"deal_closed": 0, "Revenue": 0, "Commission" :0, "Bonus": 0}}
            another = {agent.agent_id: {"date": []}}
            cls._agents.update(temp)
            cls._deals_closed.update(another)

    @classmethod
    def bonus(cls, agent_id):
        """
        Calculate bonus for the agents
        """
        count = len(cls._deals_closed[agent_id]["date"])
        if count >= 10:
            for index in range(count-10):
                day_range = cls._deals_closed[agent_id]["date"][index+10] - cls._deals_closed[agent_id]["date"][index]
                if day_range <= timedelta(days=7):
                    cls._agents[agent_id]["Bonus"] += 100000
                    return True
        else:
            return False

    @classmethod
    def get_sales(cls, agent_id):
        """
        output sales record
        """
        print(cls._agents[agent_id])

    @classmethod
    def new_day(cls):
        """
        reset the times for a new day.
        """
        cls._agents_time = {}

    @classmethod
    def get(cls, **customer):
        """
        Assign the best agent for the customer, creating an instance if necessary.
        Return the agent and wait time (0 if an agent is readily available).
            - customer: Info of customer.
        """
        def total_minute(hour, minute):
            return hour*60 + minute
        """
        initialize variable
        """
        interest = customer.get("interest")
        wait_time = 0
        high_expertise = 0
        arrival_time = [customer.get("arrival_time").day,
                        customer.get("arrival_time").hour,
                        customer.get("arrival_time").minute]
        arrived_time = total_minute(arrival_time[1], arrival_time[2])
        wait_times = {}
        availble_agent_list = []

        """
        separate the agent by availbilities, and also save all their wait times for future referance
        """
        for agent in cls._agents_data:
            if cls._agents_time.get(agent.agent_id):
                if cls._agents_time.get(agent.agent_id) > arrived_time:
                    pending = {agent.agent_id: (cls._agents_time.get(agent.agent_id)-arrived_time)}
                    wait_times.update(pending)
                    continue
            availble_agent_list.append(agent)

        """
        for agents that is available, compare their expertise in customer's interest
        """
        for agent in availble_agent_list:
            if agent.expertise[interest] >= high_expertise:
                high_expertise = agent.expertise[interest]

        agent_list = []
        for agent in availble_agent_list:
            if agent.expertise[interest] == high_expertise:
                agent_list.append(agent)

        """
        If there are multiple agent with same high expertise, we take the one with higher ratings.
        If there is no agent available, ValueError will occur, therefore, we take the agent with the
        least waittime and assigned it to the customer.
        """
        try:
            best_agent = max(agent_list, key=lambda x: x.rating)
        except ValueError:
            wait_time = min(wait_times.values())
            for key, value in wait_times.items():
                if value == wait_time:
                    assigned_id = key
            for agent in cls._agents_data:
                if agent.agent_id == assigned_id:
                    best_agent = agent

        temp = {best_agent.agent_id : arrived_time + best_agent.service_time*60}
        cls._agents_time.update(temp)

        """
        if the agent was able to close the deal, update cls._agents in order to calculate
        their performanceindex
        """
        if customer.get("sale_closed"):
            cls._agents[best_agent.agent_id]["deal_closed"] += 1
            cls._agents[best_agent.agent_id]["Revenue"] += data.CARS[interest].get("price")
            cls._agents[best_agent.agent_id]["Commission"] += 10000
            cls._deals_closed[best_agent.agent_id]["date"].append(customer.get("arrival_time"))
        return best_agent, wait_time



    def __init__(self, **agent):
        self.agent_id = agent.get("agent_id")
        self.expertise = agent.get("expertise")
        self.service_time = agent.get("service_time")
        self.rating = agent.get("rating")
