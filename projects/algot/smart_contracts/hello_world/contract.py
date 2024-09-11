from pyteal import *

# Define HelloWorld contract
def hello_world_contract():
    return Approve()

if __name__ == "__main__":
    # Compile to TEAL
    print(compileTeal(hello_world_contract(), mode=Mode.Application))
