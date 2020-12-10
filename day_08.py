from copy import copy
from copy import deepcopy


class Instruction:
    def __init__(self, code, value):
        self.code = code
        self.value = value
        self.has_executed = False


def value_before_loop(instruction_set, rewrite_code=False):
    instructions: list[Instruction] = []
    for instruction in instruction_set:
        code, val = instruction.split()
        val = int(val)
        instructions.append(Instruction(code, val))

    solution_found = False
    prev_jmp_ip = 0
    inst_copy = deepcopy(instructions)
    while not solution_found:
        solution_found = not rewrite_code
        ip = 0
        accumulator = 0
        inst: Instruction = inst_copy[ip]
        while not inst.has_executed:
            inst.has_executed = True
            if inst.code == 'acc':
                accumulator += inst.value
                ip += 1
            elif inst.code == 'nop':
                ip += 1
            elif inst.code == 'jmp':
                ip += inst.value
            if ip < len(inst_copy):
                inst = inst_copy[ip]

        if rewrite_code:
            if ip < len(inst_copy):
                prev_jmp_ip, inst_copy = replace_jmp_with_nop(instructions, prev_jmp_ip)
            else:
                solution_found = True

    return accumulator


def replace_jmp_with_nop(instruction_set: list, from_ip: int) -> tuple[int, list[Instruction]]:
    """
    Replaces the first 'jmp' command after the 'from_ip'

    :param instruction_set: source instruction set
    :param from_ip: pointer to place where search begins
    :returns: tuple [new pointer, new instruction set]
    """
    new_instruction_set = []
    ip = 0
    new_from_ip = 0
    for inst in instruction_set:
        inst_copy: Instruction = copy(inst)
        if ip >= from_ip and new_from_ip == 0:
            if inst.code == 'jmp':
                inst_copy.code = 'nop'
                new_from_ip = ip + 1
        new_instruction_set.append(inst_copy)
        ip += 1

    return new_from_ip, new_instruction_set

