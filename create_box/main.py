"""This is the entry point of the program."""


def create_box(height, width, character):
    if height < 1 or width < 1:
        return "Invalid Input"
    box = (character * width +'\n') * height
    return box
    
    
def create_border_box(height, width, character):
    box_rows = []
    box_rows.append(character * width + '\n')
    for i in range(height - 2):
        box_rows.append(character + (width - 2) * ' ' + character + '\n')
    box_rows.append(character * width + '\n')
    return ''.join(box_rows)
    
    
    
if __name__ == '__main__':
    create_box(3, 4, '*')
    
if __name__ == '__main__':
     create_border_box(4, 5, '$')