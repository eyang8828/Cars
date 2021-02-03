# Cars

The leading high-end sports car showroom in Beverly Hills is looking to improve customer satisfaction. To that end, they asked you to write software to track their sales metrics, which include wait times and agent performance. Here are their requirements.

When a customer arrives, she is assigned an agent with the highest expertise for the car she is planning to buy. If multiple agents are available, the one with the highest rating must be picked. And if no agent is available, the customer will wait and gets assigned to the next agent that becomes available.

Generally, each agent takes a different amount of time with the customer, but he takes the same time with every customer whether or not he closes the deal. For every deal closed, an agent is rewarded $10,000 in commission. If he closes 10 or more deals in a week, he is further awarded a bonus of $100,000.

Your job is to create the logic to generate metrics for the customer wait times:
* Mean across all customers
* Median
* Standard deviation

In addition, you need to list out the agents with their performance:
* Deals closed
* Revenue generated for the showroom
* Earnings, split out into commission and bonus amounts

The showroom is providing you with test data for agents and customers for an integration test of your software. Conduct your test with 5 agents and 100 customers. In addition, they insist that you write unit tests so they can be confident your logic works.

Aspect                       | Points
---------------------------- | :----:
Operation (50)               | 40
Organization (100)           | 80
Application of concepts (100)| 100
Tests (50)                   | 40
TOTAL                        | 260
