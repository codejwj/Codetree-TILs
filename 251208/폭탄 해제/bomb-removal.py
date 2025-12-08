class Clear:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

unlock_code, wire_color, seconds = tuple(input().split())
seconds = int(seconds)

c = Clear(unlock_code, wire_color, seconds)

print(f"code : {c.unlock_code}")
print(f"color : {c.wire_color}")
print(f"second : {c.seconds}")