from pyteal import *
#This is a simple stateless smart contract that only allows withdrawals from a specific account.
#It also checks and verfies that CloseRemainder and AssetCloseTo transactions properties are not set, to prevent malicious transactions
def bank_for_account(receiver):
    #Only allows reciever to withdraw funds from this contract account
    is_payment = Txn.type_enum() == Int(1)
    #ensures the reciever address is correct
    is_correct_receiver = Txn.receiver() == Addr(receiver)
    #size of transaction cannot be greater than one
    is_one_transaction = Global.group_size() == Int(1)
    #algo balance of account is not closed so no accidental exit for funds
    is_not_close = Txn.close_remainder_to() == Global.zero_address()
    #asset balance of account is not closed so no accidental exit
    is_not_close_asset = Txn.asset_close_to() == Global.zero_address()
    #group all transaction fields
    return And(is_payment, is_correct_receiver, is_not_close, is_not_close_asset)
#please use the address that was generated from the CreatingAdress code from the other file and replace with the current address in the function below
program = bank_for_account("7OCMSFNBGM6TMZO2GJNMUXC42H7CKFIPNWVFYAUWSWRED4UCXVRVHFAIEE")
print(compileTeal(program, Mode.Application))