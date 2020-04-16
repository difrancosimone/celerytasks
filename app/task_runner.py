from tasks import add
from tasks import simpleecho


result = add.delay(4, 6)
print(result.get())
print(result.status)
result = simpleecho.delay('TEST')
print(result.status)
print(result.get(timeout=10))
print(result.status)
