

def print_longest_repetition_length(dna_seq: str) -> None:

    current_max_length = 0
    current_length = 0
    current_char = None

    for c in dna_seq:
        if current_char == None:
            current_char = c
            current_length = 1
            current_max_length = 1
            continue

        if c == current_char:
            current_length += 1
        else:
            current_char = c
            current_length = 1

        if current_length > current_max_length:
            current_max_length = current_length
    
    print(current_max_length)
        



if __name__ == "__main__":
    dna_seq = input()

    print_longest_repetition_length(dna_seq)