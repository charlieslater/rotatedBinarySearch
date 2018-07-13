"""
Goal
- look for name in sorted table
Idea: 
- Cut amount to be searched in half with each lookup
- Pick midpoint of table
- If name is below midpoint, search the lower half of the table.
- If name is above midpoint, search the upper half of the table.
"""
def binlookup(name, tab):
    low, high = 0, len(tab) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if name < tab[mid]:
           high = mid - 1
        elif name > tab[mid]:
           low = mid + 1
        else:
           return mid;
    return -1

def lookup(name, tab):
    low, high = 0, len(tab) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if name == tab[mid]:
            return mid  # found it!
        if tab[0] > tab[mid]:
            #rotated part
            high = mid - 1
        else:
            #not rotated part
            if name < tab[mid] and name >= tab[0]:
                return binlookup(name, tab[:mid])
        if tab[mid] > tab[-1]:
            #rotated part
            low = mid + 1
        else:
            #not rotated part
            if name > tab[mid] and name <= tab[-1]:
                ans = binlookup(name, tab[mid:])
                if ans > -1:
                    return ans + mid
                else:
                    return -1
    return -1

table = ['Aaliyah', 'Abigail', 'Addison', 'Adeline', 'Alexa',
'Alice', 'Allison', 'Amelia', 'Anna', 'Aria', 'Ariana', 'Arianna',
'Aubree', 'Aubrey', 'Audrey', 'Aurora', 'Autumn', 'Ava', 'Avery',
'Bella', 'Brielle', 'Brooklyn', 'Camila', 'Caroline', 'Charlotte',
'Chloe', 'Claire', 'Clara', 'Cora', 'Delilah', 'Eleanor', 'Elena',
'Eliana', 'Elizabeth', 'Ella', 'Ellie', 'Emilia', 'Emily', 'Emma',
'Eva', 'Evelyn', 'Everly', 'Gabriella', 'Genesis', 'Gianna', 'Grace',
'Hailey', 'Hannah', 'Harper', 'Hazel', 'Isabella', 'Isabelle',
'Isla', 'Josephine', 'Julia', 'Katherine', 'Kaylee', 'Kennedy',
'Kinsley', 'Layla', 'Leah', 'Lillian', 'Lily', 'Lucy', 'Luna',
'Lydia', 'Mackenzie', 'Madeline', 'Madelyn', 'Madison', 'Maya',
'Melanie', 'Mia', 'Mila', 'Naomi', 'Natalie', 'Nevaeh', 'Nora',
'Nova', 'Olivia', 'Paisley', 'Penelope', 'Peyton', 'Piper', 'Quinn',
'Reagan', 'Riley', 'Ruby', 'Rylee', 'Sadie', 'Samantha', 'Sarah',
'Savannah', 'Scarlett', 'Serenity', 'Skylar', 'Sofia', 'Sophia',
'Sophie', 'Stella', 'Valentina', 'Victoria', 'Violet', 'Vivian',
'Willow', 'Zoe', 'Zoey']

ans = binlookup('Abigail',table)
print("expect: 1, got:",ans)
print("expect: Abigail, got:",table[ans])
ans = binlookup('Ruby',table)
print("expect: 87, got:",ans)
print("expect: Ruby, got:",table[ans])

from random import randint
i = randint(1,len(table)-2)
rotatedTable = table[i+1:] + table[:i]
print("rotatedTable=",rotatedTable)
ans = lookup('Abigail',rotatedTable)
print("rotated expect: Abigail, got:",rotatedTable[ans])
ans = binlookup('Ruby',table)
print("expect: Ruby, got:",table[ans])
