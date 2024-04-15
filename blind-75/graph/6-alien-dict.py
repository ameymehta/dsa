from collections import defaultdict


class Solution(object):

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        successors = defaultdict(set)
        predecessors = defaultdict(set)
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    successors[c1].add(c2)
                    predecessors[c2].add(c1)
                    break
        all_chars = set("".join(words))
        root_chars = all_chars - set(predecessors)
        order = ""
        while root_chars:
            c1 = root_chars.pop()
            order += c1
            for c2 in successors[c1]:
                predecessors[c2].discard(c1)
                if not predecessors[c2]:
                    root_chars.add(c2)
        if set(order) == all_chars:
            return order
        else:
            return ""
