from pyteal import *

"""Basic Bank"""

def bank_for_account(receiver):
    """Only allow receiver to withdraw funds from this contract account.
    
    Args:
        receiver (str): Base 32 Algorand address of the receiver.
    """
    is_payment = Txn.type_enum() == TxnType.Payment
    is_single_transaction = Global.group_size() == Int(1)
    is_correct_receiver = Txn.receiver() == Addr(receiver)
    no_close_out_addr = Txn.close_remainder_to() == Global.zero_address()
    no_rekey_addr = Txn.rekey_to() == Global.zero_address()
    acceptable_fee = Txn.fee() <= Int(1000)

    return And(
        is_payment,
        is_single_transaction,
        is_correct_receiver,
        no_close_out_addr,
        no_rekey_addr,
        acceptable_fee
    )

if __name__ == "__main__":
    #please use the address that was generated from the CreatingAdress code from the other file and replace with the current address in the function below
    program = bank_for_account("7OCMSFNBGM6TMZO2GJNMUXC42H7CKFIPNWVFYAUWSWRED4UCXVRVHFAIEE")
    print(compileTeal(program, Mode.Signature))