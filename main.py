# def read_file_content
# [assignment] Add your code here
with open("story.txt", "r") as f:

    f_contents = f.read()
    print(f_contents)

# storytxt="Once upon a time a psychology professor walked around on a stage while teaching stress management principles to an auditorium filled with students. she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question. Instead, with a smile on her face, the professor asked, How heavy is this glass of water I am holding?"
#
# def read_file_content(storytxt):
#     # [assignment] Add your code here
#     f = open('storytxt')
#     return f

# print(storytxt)



    # return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
count = {}
with open("story.txt") as file:
    data = file.read().split()
    print(data)
    for word in data:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    print(count)
