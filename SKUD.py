from boa.interop.Neo.Runtime import Log, Notify
from boa.interop.Neo.Storage import Get, Put, GetContext
from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.builtins import concat


def Main(operation, args):
    if operation == 'add':
        id = args[0]
        hash = args[1]
        AddHash(id, hash)

    elif operation == 'get':
        id = args[0]
        GetHash(id)

    return False


def AddHash(id, hash):
    msg = concat("RegisterHash: ", id)
    msg = concat(msg, hash)
    Notify(msg)

    context = GetContext()
    exists = Get(context, id)
    if exists:
        Notify("ID is already registered")
        return False

    Put(context, id, hash)
    return True


def GetHash(id):
    context = GetContext()
    hash = Get(context, id)
    if not hash:
        Notify("ID is not yet registered")
        return False

    return hash
