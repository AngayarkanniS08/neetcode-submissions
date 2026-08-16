class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for strings in strs:
            string_length = len(strings)
            encoded_string += str(string_length) + "#" + strings

        return encoded_string

    def decode(self, s: str) -> List[str]:

        string_array = []
        i = 0

        while i < len(s):

            length = ""

            # Read all digits until #
            while s[i].isdigit():
                length += s[i]
                i += 1

            jump_amount = int(length)

            # Skip #
            i += 1

            # Read exactly jump_amount characters
            collected_letter = s[i:i + jump_amount]

            string_array.append(collected_letter)

            # Move to the next encoded length
            i += jump_amount

        return string_array