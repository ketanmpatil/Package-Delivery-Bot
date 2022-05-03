# from Digit_Recognizer import OCR


# list_directions = list(OCR('Image.png'))


reccur=True
while reccur:
    try:
        Id= str(input('Input ID:'))
        Destination,code,Unique_id = Id.split('_') # ex: B_0101_9999
        reccur=False
    except:
        pass

list_directions=list(code)

direction = {'0':'Left <--','1':'Straight |','2':'Right -->'}
print('\n')
print('Directions are as follow:')
for i in list_directions:
    try:
        print(direction[i])
    except:
        print('Unknown Direction')

print(f'\nDestination: {Destination}\n')
print(f"Unique ID: {Unique_id}")