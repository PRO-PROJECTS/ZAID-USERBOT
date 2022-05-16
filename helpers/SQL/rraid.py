from helpers.SQL import dbb

gmuteh = dbb["RRAID"]


async def rs_gmuted(sender_id):
    kk = await rmuteh.find_one({"sender_id": sender_id})
    if not kk:
        return False
    else:
        return True


async def rmute(sender_id, reason="#GMuted"):
    await rmuteh.insert_one({"sender_id": sender_id, "reason": reason})


async def rngmute(sender_id):
    await rmuteh.delete_one({"sender_id": sender_id})
