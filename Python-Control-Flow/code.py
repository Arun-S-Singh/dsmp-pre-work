# --------------
##File path for the file 
file_path 


#Code starts here

# Define read file function
def read_file(path):
    file = open(path , 'r')
    sentence = file.readline()
    file.close()

    return sentence

# Call function read_file()
sample_message = read_file(file_path)

# sample message
print(sample_message)


# --------------
#Code starts here

def fuse_msg(message_a, message_b):
    quotient = int(message_b)//int(message_a)
    return quotient


# Read file file_path_1
message_1 = read_file(file_path_1)

# Read file file_path_2
message_2 = read_file(file_path_2)

# Print message_1
print(message_1)

# Print message_2
print(message_2)

# Call fuse_msg()
secret_msg_1 = str(fuse_msg(message_1,message_2))

# Print secret_msg_1
print(secret_msg_1)



# --------------
#Code starts here

# Define function substitute_msg()
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = "Army General"
    elif message_c == 'Green':
        sub = "Data Scientist"
    elif message_c == 'Blue':
        sub = "Marine Biologist"

    return sub

# Read file file_path_3
message_3 = read_file(file_path_3)

# Print message_3
print(message_3)

# Call function substitute_msg
secret_msg_2 = substitute_msg(message_3)

# Print  secret_msg_2
print(secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

# Define function compare_msg()
def compare_msg(message_d,message_e):
    a_list = str.split(message_d,' ')
    b_list = str.split(message_e,' ')

    c_list = [i for i in a_list if i not in b_list]

    final_msg = " ".join(c_list)

    return final_msg

# Read file file_path_4
message_4 = read_file(file_path_4)

# Read file file_path_5
message_5 = read_file(file_path_5)

# Print message_4
print(message_4)

# Print message_5
print(message_5)

secret_msg_3 = compare_msg(message_4,message_5)

print(secret_msg_3)




# --------------
#Code starts here

# Define function extract_msg
def extract_msg(message_f):
    a_list = str.split(message_f , ' ')

    even_word = lambda x : len(x) % 2 == 0

    b_list = list(filter(even_word , a_list))

    final_msg = " ".join(b_list)

    return final_msg

# Read file file_path_6
message_6 = read_file(file_path_6)

# Print message_6
print(message_6)

# Call function extract_msg with message_6
secret_msg_4 = extract_msg(message_6)

# Print secret_msg_4
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

# Define function write_file()
def write_file(secret_msg , path):
    file = open(path,'a+')
    file.write(secret_msg)
    file.close()

    return

# Join message parts to create sentence
secret_msg = " ".join(message_parts)

# Call write_file() with secret_msg
write_file(secret_msg,final_path)

# Print secret message
print(secret_msg)


