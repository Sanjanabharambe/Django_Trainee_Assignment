import time
from myapp.models import MyModel

start = time.time()
MyModel.objects.create(name="Sanjana")
end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")
