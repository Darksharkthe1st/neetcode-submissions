class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        spots = []
        for i in range(len(position)):
            # print(position, " : ", speed)
            spots.append((position[i], speed[i]))

        spots = sorted(spots, key=lambda x: x[0])
        # print(spots)
        # print(spots[-1][0])
        # print((target - spots[-1][0]))
        end_time = (target - spots[-1][0]) / spots[-1][1]
        groups = 1

        for i in range(len(spots) - 2, -1, -1):
            new_end_time = (target - spots[i][0]) / spots[i][1]
            if new_end_time <= end_time or (new_end_time - end_time) < 0.01:
                continue
            else:
                groups += 1
                end_time = new_end_time
        return groups