class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value,timestamp])
        #print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        res_list = self.timemap.get(key, [])
        l, r = 0, len(res_list) - 1
        result = ""
        while l <= r:
            midlle = (l + r) // 2
            if res_list[midlle][1] <= timestamp:
                result= res_list[midlle][0]
                l = midlle + 1
            else:
                r = midlle - 1

        return result




# Your TimeMap object will be instantiated and called as such:
key = "foo"
value = "bar"
timestamp = 1
obj = TimeMap()
obj.set(key,value,timestamp)
param_2 = obj.get(key,timestamp)
print(param_2)