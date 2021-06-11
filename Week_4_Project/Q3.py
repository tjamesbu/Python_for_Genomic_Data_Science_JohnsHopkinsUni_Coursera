# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

lengths = [len(i) for i in sequences]

print(max(lengths), min(lengths))
