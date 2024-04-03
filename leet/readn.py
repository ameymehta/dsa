"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution(object):
    def __init__(self):
        self.chunk_index = 0
        self.chunk_size = 0
        self.chunk = [" "] * 4

    # This is a dummy method to avoid showing errors
    def read4(self, chunk):
        return 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_index = 0
        while buf_index < n:
            # if chunk_index is 0, no left over in chunk, get new chunk
            if self.chunk_index == 0:
                self.chunk_size = read4(self.chunk)

            # if reached end of the file, break loop
            if self.chunk_size == 0:
                break

            # copy chunk to buffer
            while buf_index < n and self.chunk_index < self.chunk_size:
                buf[buf_index] = self.chunk[self.chunk_index]
                buf_index += 1
                self.chunk_index += 1

            # if it was regular chunk of size 4, reset chunk_index to 0
            if self.chunk_index >= self.chunk_size:
                self.chunk_index = 0

        return buf_index
