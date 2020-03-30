# ipsum_file = open('files/ipsum.txt')

# for paragraph in ipsum_file:
#   print(paragraph.strip())

# ipsum_file.seek(2)
# lines = ipsum_file.readlines(10)
# print(lines)

# ipsum_file.close()


def sequence_filter(line):
  return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
  lines = dna_file.readlines()
  print(list(filter(sequence_filter, lines)))

# file will be closed itself