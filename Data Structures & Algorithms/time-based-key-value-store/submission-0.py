class TimeMap:
    
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            arr = self.timemap.get(key)
            data = {"value": value, "timestamp": timestamp}
            arr.append(data)
            self.timemap[key] = arr
        else:
            data = {"value": value, "timestamp": timestamp}
            self.timemap[key] = [data]

    def get(self, key: str, timestamp: int) -> str:

        if self.timemap.get(key, None) == None:
            return ""

        data = self.timemap[key]
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2

            if data[mid]["timestamp"] == timestamp:
                return data[mid]["value"]
            elif timestamp > data[mid]["timestamp"]:
                left = mid + 1
            else:
                right = mid - 1


        if data[right]["timestamp"] > timestamp:
            return ""
        else:
            return data[right]["value"]
