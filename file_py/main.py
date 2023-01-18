#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def letter_format():
    with open("./Input/Letters/starting_letter.docx", "r") as file1:
        read_content = file1.read()
        return read_content
    
def generate_mail():
    letter = letter_format()
    with open("./Input/Names/invited_names.txt", "r") as file1:
        read_content = file1.readlines()
        for line in read_content:
            name = line.strip()
            with open(f"./Output/ReadyToSend/{name}_mail_file.docx", mode="w") as new_file:
                new_file.write(letter.replace("[name]", name))

        
generate_mail()


