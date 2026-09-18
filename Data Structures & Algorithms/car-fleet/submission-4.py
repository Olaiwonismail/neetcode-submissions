class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = len(position)
        m = {}
        for n in range(ans):
            m[position[n]] = speed[n] 
        cars = sorted(position)
        closest_car = ans-1
        next_car = ans - 2
        while next_car > -1 :
            t1 = (target - cars[closest_car])/m[cars[closest_car]] 
            t2 = (target - cars[next_car])/m[cars[next_car]]

            if t2 < t1:
                ans-=1
                next_car -=1
            elif t2 ==t1:
                ans-=1
                next_car -=1
                closest_car-=1
            else:
                closest_car = next_car
                next_car -=1
                
        return ans

            

