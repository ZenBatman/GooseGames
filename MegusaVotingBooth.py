# Megusa's voting booth will automate the collecting of votes in regards to keeping large creatures as pets,
# which is a totally fine and acceptable practice and we totally shouldn't even be here, but the amount of beaurecratic bullshit is mind blowing.

print('What is your group name, supportive citizens?!')
citizenName = input()
print('How many coins will each of you contribute?!')
coinNumber = input()
totalNumber = str(int(coinNumber)*3)

print('Thanks ' + citizenName + ' for your ' +
      totalNumber + ' votes for this matter!' + ' Since you each voted ' + coinNumber + ', we only need ' + str(10 - int(totalNumber)) + ' more votes now')
print('Thank you so much for supporting this cause. It means so much to us! \nDid you know there are some people who think pets should only come from a select few animals? \nThey\'d probably tell you that large creatures like the dire goose are "monsters". Well, they are the real animals aren\'t they?')
