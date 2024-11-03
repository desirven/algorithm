class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        gas, cost = gas*2, cost*2
        gas_tank = 0
        start_station = 0
        for i in range(length*2):
            gas_tank += gas[i] - cost[i]
            if gas_tank < 0:
                start_station = i+1
                gas_tank = 0
            elif i+1-start_station == length:
                return start_station
        return -1