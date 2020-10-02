#importing pyteal sdk
from pyteal import  *

#deleting from smart contract using localdel
program = App.localDel(Int(0), Bytes("MyKey"))
#compiling pyteal to teal language and printing out the compiles teal code
print(compileTeal(program, Mode.Application))

#comment out the above print command and uncomment the following opcodes below to compile and create a new teal file compiled from the pyteal code above
# with open('Pyteal5.teal', 'w') as f:
#     compiled = compileTeal(create, Mode.Application)
#     f.write(compiled)