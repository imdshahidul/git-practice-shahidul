from datetime import datetime
from utils import add, subtract
from utils import multiply, subtract


print("Name: Md Shahidul Islam")
print("Today's Date:", datetime.now().strftime("%Y-%m-%d"))


print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))

print("Multiplication:", multiply(5, 3))

from utils import divide

print("Division:", divide(5, 0))
