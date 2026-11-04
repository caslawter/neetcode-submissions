class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        count = 1
        if len(self.stack) == 0 or price < self.stack[-1]:
            self.stack.append(price)
            return count
        elif price >= self.stack[-1]:
            for index in range(len(self.stack) - 1, -1, -1):
                if price >= self.stack[index]:
                    self.stack[index] = price
                    count += 1
                else:
                    break
            self.stack.append(price)
            return count
        
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)