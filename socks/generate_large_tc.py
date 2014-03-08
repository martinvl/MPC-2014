import random


# TC1 (many equal words)
name_tc_1_in = "socks.large.1.in"
name_tc_1_out = "socks.large.1.out"
n = 10000
file_tc_1_in = open(name_tc_1_in, 'w+')
file_tc_1_in.write(str(n) + '\n')
for i in range(n):
    file_tc_1_in.write('a\n')
file_tc_1_out = open(name_tc_1_out, 'w+')
file_tc_1_out.write('Sock-sess\n')




# TC2 (many random words, but all of them different)
def get_random_word(m):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_word = ''
    for j in range(m):
        l = random.choice(letters)
        random_word += l
    return random_word

name_tc_2_in = "socks.large.2.in"
name_tc_2_out = "socks.large.2.out"
n = 10000
m = 10
file_tc_2_in = open(name_tc_2_in, 'w+')
file_tc_2_in.write(str(n) + '\n')
covered_words = []
for i in range(n):
    random_word = get_random_word(m)
    while (random_word in covered_words):
        random_word = get_random_word(m)
    covered_words.append(random_word)
    file_tc_2_in.write(random_word + '\n')
file_tc_2_out = open(name_tc_2_out, 'w+')
covered_words.sort()
for i in covered_words:
    file_tc_2_out.write(i + '\n')


# TC3 (many random , but all of them different)
name_tc_3_in = "socks.large.3.in"
name_tc_3_out = "socks.large.3.out"
chosen_words = []
output_words = []
letters = 'abcdefghijklmnopqrstuvwxyz'
for l in letters:
    random_number = random.randint(0, 10)
    for i in range(random_number):
        chosen_words.append(l)
    if random_number == 1:
        output_words.append(l)

file_tc_3_in = open(name_tc_3_in, 'w+')
file_tc_3_in.write(str(len(chosen_words)) + '\n')
for i in chosen_words:
    file_tc_3_in.write(i + '\n')


file_tc_3_out = open(name_tc_3_out, 'w+')
output_words.sort()
for i in output_words:
    file_tc_3_out.write(i + '\n')

print "Done creating large test cases."
