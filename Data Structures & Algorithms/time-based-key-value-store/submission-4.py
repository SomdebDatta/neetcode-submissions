class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append([value, timestamp])
        else:
            self.hashmap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        values = self.hashmap[key]
        if timestamp < values[0][1]:
            return ""
        if timestamp > values[-1][1]:
            return values[-1][0]
        
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if timestamp < values[mid][1]:
                r = mid - 1
            elif timestamp > values[mid][1]:
                l = mid + 1
            else:
                return values[mid][0]

        if mid == 0:
            return values[mid][0]
        return values[mid - 1][0]