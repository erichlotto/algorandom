# algorandom
True random number generator (TRNG) using Algorand's blockchain latest block hash as seed

### Usage:
```python
import algorandom

RAND_MIN = 0
RAND_MAX = 3

while(True):
  print(algorandom.randint(RAND_MIN, RAND_MAX))
  ```
