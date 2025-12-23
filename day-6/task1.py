#Create an empty tuple
t1 = ()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros = ('Joona', 'Roni', 'Petrus')
systers = ('Mikaela', 'Anastasia', 'Ronja')
#Join brothers and sisters tuples and assign it to siblings
siblings = bros + systers
#How many siblings do you have?
siblings_count = len(siblings)
print(siblings)
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('Jouni')
family_members.append('Minna')
family_members = tuple(family_members)
print(family_members)
print(type(family_members))