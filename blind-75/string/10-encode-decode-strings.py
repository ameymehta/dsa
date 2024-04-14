class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        result = []
        for string in strs:
            for c in string:
                result.append(str(ord(c)))
                result.append(";")
            result.append(" ")
        return "".join(result)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        result = []
        strs = s.split(" ")
        for string in strs:
            chars = []
            for c in string.split(";"):
                if c:
                    chars.append(chr(int(c)))
            result.append("".join(chars))
        result.pop()
        return result
