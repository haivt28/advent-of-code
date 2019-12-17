from day09 import intcode_computer
import copy


def update_alignment_parameters(output):
    global output_view, upper_line, idx, idy, sum_ap, dust

    dust = output
    output_view += chr(output)
    if chr(output) == '#':
        current_line.append(idx)
        if idx > 1 and idx in current_line and idx-1 in current_line and idx-2 in current_line and idx-1 in upper_line:
            sum_ap += (idx - 1) * idy
    if chr(output) == '\n':
        upper_line = copy.copy(current_line)
        current_line.clear()
        idx = -1
        idy += 1
    idx += 1


ins = list(map(int, open('input/day17.txt').read().split(',')))

# PART 1
output_view = ''
upper_line = []
current_line = []
idx = 0
idy = 0
sum_ap = 0  # Sum of the alignment parameters

intcode_computer(ins, None, update_alignment_parameters)

print('OUTPUT VIEW:\n' + output_view)
print('Sum of the alignment parameters:', sum_ap)

# PART 2
# I solved this part by hand, todo is automatic find the pattern
ins[0] = 2

output_view = ''
upper_line = []
current_line = []
idx = 0
idy = 0
sum_ap = 0  # Sum of the alignment parameters

main_routine = 'A,B,A,B,C,C,B,C,B,A\n'
func_A = 'R,12,L,8,R,12\n'
func_B = 'R,8,R,6,R,6,R,8\n'
func_C = 'R,8,L,8,R,8,R,4,R,4\n'
input = main_routine + func_A + func_B + func_C + 'n\n'
input = [ord(c) for c in input]
dust = 0

intcode_computer(ins, input, update_alignment_parameters)

# print('OUTPUT VIEW:\n' + output_view)
print('Collected dust:', dust)
