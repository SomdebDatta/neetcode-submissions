class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        nextIdle = customers[0][0]
        waitTime = 0

        for customer in customers:
            nextIdle = max(nextIdle, customer[0])
            nextIdle += customer[1]
            waitTime += nextIdle - customer[0]
        
        return waitTime / len(customers)
            