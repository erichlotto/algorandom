import random
from algosdk.algod import AlgodClient
from time import sleep

algodAddress = "http://localhost:8080"
algodToken = "xxxxxxxxxx"


def generate(min, max):
    algodclient = AlgodClient(algodToken, algodAddress)

    try:
        # Get last round
        lastround = algodclient.status().get("lastRound")
        currentround = lastround

        # Wait for a new round
        while(lastround == currentround):
            sleep(1)
            currentround = algodclient.status().get("lastRound")

        # Get the hash of the new block
        hash = algodclient.block_info(currentround).get("hash")

    except Exception as e:
        # Print the error and exit
        print("Algod error: %s" % e)
        exit()

    # Apply the new block hash as the seed for the random object
    random.seed(hash)

    # Returns a random number between min and max
    print(hash, random.randint(min, max))


while(True):
    generate(0, 10)
