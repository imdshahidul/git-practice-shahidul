from datetime import datetime
from utils import add, subtract


print("Name: Md Shahidul Islam")
print("Today's Date:", datetime.now().strftime("%Y-%m-%d"))


print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
