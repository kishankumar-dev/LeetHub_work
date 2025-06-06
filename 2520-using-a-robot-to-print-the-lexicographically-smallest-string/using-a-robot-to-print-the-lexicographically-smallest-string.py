class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = defaultdict(list)
        for i, ch in enumerate(s):
            cnt[ch].append(i)
        p, stack, prev = [], [], -1
        for ch in ascii_lowercase:
            while stack and stack[-1] <= ch:
                p.append(stack.pop())
            for i in cnt[ch]:
                if i > prev:
                    p.append(ch)
                    stack.extend(s[prev+1:i])
                    prev = i
        p.extend(reversed(stack))
        return ''.join(p)