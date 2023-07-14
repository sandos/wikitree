f = open("71l16e_114520pb19e6m91e7a1472_A.ged", "rb")

content = f.read()

newContent = bytearray()
controlChar = None

for index in range(len(content)):
    if (content[index] == 0xC3 or content[index] == 0xCC)and index < len(content)-10 and content[index+1] == 13:
        pass
        print(str(content[index-30:index]))
        print(content[index+1])
        print(content[index+2])
        newContent.append(32)
        newContent.append(32)
        newContent.append(32)
        controlChar = content[index]
    elif content[index] == 0xC3 and content[index+1] == 0xC3:
        pass
    elif content[index] == 0xC3 and index < len(content)-10 and content[index+1] == 10:
        pass
        print(str(content[index-10:index]))

    elif content[index] == 32 and index < len(content)-10 and content[index+1] > 127 and content[index+2] < 127 and content[index+2] > 13:
        #Replace second character by making it a valid utf-8 sequence by adding the control character
        newContent.append(32)
        if controlChar:
            newContent.append(controlChar)
        else:
            print("Missing ctrlchar")
            newContent.append(0xC3)
        pass
        #newContent.append(content[index+1])

    else:
        newContent.append(content[index])


newFile = open("out.ged", "wb")
newFile.write(newContent)