class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []

        self.hashmap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            values = self.hashmap[key]
        else:
            return ""

            
        valid = ""
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left+right) // 2
        
            timestamp_mid = values[mid][0]

            if timestamp_mid <= timestamp:
                valid = values[mid][1]
                left = mid +1
            else:
                right = mid -1

        return valid


                
            



        
