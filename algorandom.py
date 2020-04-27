import json
from urllib.request import Request, urlopen
import random


# Public Rest API
END_POINT = "https://api.algoexplorer.io"


# Data fetcher
def _fetch_data(url):
  req = Request(url)
  req.add_header('User-Agent', 'curl/7.65.3')
  return json.load(urlopen(req))


# Generate a random integer in range based on latest block hash on Algorand blockchain
def randint(min, max):

  # get latest block number
  latest_block = _fetch_data('%s/v1/status' % END_POINT)["round"]
  
  # get latest block hash
  hash = _fetch_data('%s/v1/block/%s' % (END_POINT, latest_block))["hash"]
  
  # Apply the current block hash as the seed for the random object
  random.seed(hash)

  # Returns a random number between min and max
  return random.randint(min, max)


