class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_number = {}

        for number in nums:
            if number not in frequent_number:
                frequent_number[number] = 1
            else:
                frequent_number[number] +=1
        
        sorted_count = sorted(frequent_number.items(), key=lambda x: x[1], reverse=True)
        return [x for x, y in sorted_count[:k]]