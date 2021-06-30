#!/usr/bin/python

def decrypt(address, already_decrypted):
    # walk over string bytes until termination
    while True:
        # read a single byte from database
        encrypted_byte = bv.read(address, 1)

        # return if null byte or already decrypted
        if encrypted_byte == b'\x00' or address in already_decrypted:
            return

        # decrypt byte
        decrypted_byte = chr(int(encrypted_byte[0]) ^ 0x22)

        # write decrypted byte to database
        bv.write(address, decrypted_byte)

        # add to set of decrypted addresses
        already_decrypted.add(address)

        # increment address
        address += 1


# get function instance of target function
target_function = bv.get_function_at(0x10778)
# set of already decrypted bytes
already_decrypted = set()

# 1: walk over all callers
for caller_function in set(target_function.callers):

    # 2: walk over high-level IL instructions
    for instruction in caller_function.hlil.instructions:

        # 3: if IL instruction is a call
        #    and call goes to target function
        if (instruction.operation == HighLevelILOperation.HLIL_CALL and
            instruction.dest.constant == target_function.start):

            # 4: fetch pointer to encrypted strings
            p1 = instruction.params[0]
            p2 = instruction.params[1]

            # 5: decrypt strings
            decrypt(p1.value.value, already_decrypted)
            decrypt(p2.value.value, already_decrypted)
