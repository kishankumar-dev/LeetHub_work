class Solution(object):
    def averageWaitingTime(self, customers):
        totalWaitingTime = 0
        currentTime = 0

        for customer in customers:
            arrivalTime = customer[0]
            preparationTime = customer[1]

            if arrivalTime >= currentTime:
                totalWaitingTime += preparationTime
                currentTime = arrivalTime + preparationTime
            else:
                totalWaitingTime += (currentTime - arrivalTime) + preparationTime
                currentTime += preparationTime

        return totalWaitingTime / float(len(customers))