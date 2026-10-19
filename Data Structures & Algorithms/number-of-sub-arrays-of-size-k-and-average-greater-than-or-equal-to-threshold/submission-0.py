class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        window_sum = 0
        output = 0

        for right in range(len(arr)):
            window_sum += arr[right]

            if right - left + 1 == k:
                average = window_sum / k
                if average >= threshold:
                    output += 1

                window_sum -= arr[left]
                left += 1

        return output