"""
As an amateur hitman, your job is to murder a list of people that you were paid to kill.
As like every serial killer, you decide to have a unique signature in your methods.
Given a list of people, you decide to murder your victims in the following pattern:

Every cycle, you kill/remove the person on the top of the list,
then spare the second person by moving them to the bottom of the list.
Then repeat this process until everyone on the list is dead.

You want to leave a surprise for the last person alive on your list,
can you find a way to return the name of the last person alive on a given list?

Example

For people = ["Michael","Janet","Kenny"], the output should be
hitman(people) = Janet.

-> Michael Janet Kenny (Cycle 0)
-> Janet Kenny (Cycle 1, and Michael gets killed)
-> Kenny Janet (Cycle 1, and Janet is moved to the end of the list)
-> Janet (Cycle 2, Kenny is killed and Janet is the last victim)

For ["Alex","Ken","Danny","Marley"], the output should be
hitman(people) = Marley.

-> Alex Ken Danny Marley (Cycle 0)
-> Ken Danny Marley (Cycle 1, and Alex gets murdered)
-> Danny Marley Ken (Cycle 1, and Ken gets moved to the back)
-> Marley Ken (Cycle 2, and Danny gets slaughtered)
-> Ken Marley (Cycle 2, and Marley gets moved to the end)
-> Marley (Cycle 3, Ken gets killed, and Marley is the last to live)

Hint: Wbfrcuhf (ROT13)
"""

# people: ["Michael", "Janet", "Kenny"]
# "Janet"
#
# people: ["Alex", "Ken", "Danny", "Marley"]
# "Marley"
#
# people: ["Dan", "Sarah"]
# "Sarah"
#
# people: ["Mark", "Jennifer", "James", "Ryan", "Logan"]
# "Jennifer"
#
# people: ["Abe", "Abby", "Malcolm", "Ian", "Deborah", "Olive", "Jake"]
# "Olive"
#
# people: ["Abe", "Abby", "Malcolm", "Ian", "Deborah",
#          "Olive", "Jake", "Tim", "Jennifer", "Jack", "Freddy"]
#
# people: ["SurelyThisWorks"]
# "SurelyThisWorks"


# 209 chars
# import math
#
# def hitman(people):
#    length = len(people)
#    log = int(1+math.log(length, 2))
#    return people[(3*length - int(math.pow(2, log)) - 1) % length]

# 84 chars
def hitman(p):
    import math as M
    l = len(p)
    return p[(3 * l - int(M.pow(2, int(1 + M.log(l, 2)))) - 1) % l]
