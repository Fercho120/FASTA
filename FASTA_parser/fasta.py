import re

    def read_fasta(fp):
#        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if self.name: yield (self.name, ''.join(self.seq))
                self.name, self.seq = line, []
            else:
                self.seq.append(line)
                if self.name: yield self.name, self.seq

    def is_fasta():
#        user_input = input('Please enter the route to your file or the sequence in FASTA format \n')
        filepaths = re.findall("(/[a-zA-Z\./]*[\s]?)", user_input)
#        sequence = []
        self.sequence.append(user_input)
        while True:
            if filepaths:
                break
            try:
                user_input = input()
                if user_input == '':
                    break
                self.sequence.append(user_input)
            except EOFError:
                print('error')
                continue
        if filepaths:
            for filepath in filepaths:
                with open(filepath, mode='r',) as fp:
                    for entry in read_fasta(fp):
                        print(entry, '\n')
        else:
            for entry in read_fasta(sequence):
                print(entry, '\n')

is_fasta()
