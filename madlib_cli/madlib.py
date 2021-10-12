import re
"""
Welcoming message
"""
def welcome_msg():
    print(
        """
        ********************************
        **** Welcome to Madlib Game ****
        ********************************
        *                              *
        *                              *
        *    Please fill the blanks    * 
        ********************************
        """
    )

welcome_msg()

def read_template(path):
    """
    read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
    """

    try:
     with open (path) as f:
        file_content = f.read().strip()
        print('\n',file_content,'\n')
        return file_content
    except:
        raise FileNotFoundError(f"({path}) was not found")

def parse_template(word):
    
    """
    parse function that takes in a template string and returns a string with language parts removed,and a separate list of those language parts.
    """
    word_types=list(re.findall(r'{(.*?)}',word))
    # print(word_types)
    text=re.sub('{.*?}','{}',word)
    # print(text)
    return text,word_types


def merge(text,word):
    """
    merge function that takes in a “bare” template and a list of user entered language parts, 
    and returns a string with the language parts inserted into the template.
    """
    merged_text=text.format(*word)
    with open('assets/result.txt','w') as result:
        result.write(merged_text)
        print(merged_text)
    return merged_text

if __name__== "__main__":

    file_to_read=read_template("assets/madlib.txt")
    text,words=parse_template(file_to_read)
    word_result=[]
    for i in words:
        user_input=input(f"Enter {i} >> ")
        word_result.append(user_input)
    madlib_result=merge(text,word_result)