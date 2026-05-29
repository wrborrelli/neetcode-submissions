class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = {'step':[timestamp],'val':[value]}
        else:
            self.cache[key]['step'] = self.cache[key]['step'] + [timestamp]
            self.cache[key]['val'] = self.cache[key]['val'] + [value]
        print(self.cache)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        for i in range(len(self.cache[key]['step'])-1,-1,-1):
            if key in self.cache and self.cache[key]['step'][i] <= timestamp:
                return self.cache[key]['val'][i]
            else:
                pass
        return ""
