from pyteal import compileTeal, Mode
from contract import hello_world_contract

# Generate TEAL
teal_code = compileTeal(hello_world_contract(), mode=Mode.Application)

# Save TEAL to file
with open("helloworld.teal", "w") as f:
    f.write(teal_code)

print("TEAL code has been generated and saved to helloworld.teal")
