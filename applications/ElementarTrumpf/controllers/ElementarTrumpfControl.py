import random


# ---- example index page ----
def index():
	session.humanScore = 0
	session.aiScore = 0
	redirect(URL('kartenZiehen'))


def kartenZiehen():
	# übersetzungen
	T.force('de')

	result = False
	humanMonsterValue = {}
	aiMonsterValue = {}
	monsters = {}
	monsterName = []

	file = open('Monsters.txt', 'r')
	for line in file.read().splitlines():
		name, groesse, inititaive, staerke, image = line.split (', ')
		monsters[name] = [groesse, inititaive, staerke, image, name]
		monsterName.append(name)
	file.close()

# 	2 random Monster ziehen
	humanMonster = monsters[monsterName[random.randint(0, len(monsterName)-1)]]
	aiMonster = monsters[monsterName[random.randint(0, len(monsterName)-1)]]

#	Ergebnis
	choice =  request.vars['choice']
	if choice:

		humanMonsterValue[0] = humanMonster[3]
		humanMonsterValue[1] = humanMonster[4]
		humanMonsterValue[2] = T(choice)
		
		aiMonsterValue[0] = aiMonster[3]
		aiMonsterValue[1] = aiMonster[4]
		aiMonsterValue[2] = T(choice)
		
		if choice == 'groesse':
			result = humanMonster[0] > aiMonster[0]
			humanMonsterValue[3] = humanMonster[0]
			aiMonsterValue[3] = aiMonster[0]
		elif choice == 'initiative':
			result = humanMonster[1] > aiMonster[1]
			humanMonsterValue[3] = humanMonster[1]
			aiMonsterValue[3] = aiMonster[1]
		elif choice == 'staerke':
			result = humanMonster[2] > aiMonster[2]
			humanMonsterValue[3] = humanMonster[2]
			aiMonsterValue[3] = aiMonster[2]
		else:
			humanMonsterValue = {}
			aiMonsterValue = {}
			result =  "none"
			
		if result == True:
			session.humanScore = session.humanScore + 1
		elif result == False:
			session.aiScore = session.aiScore +1
	
	return dict(humanMonsterValue=humanMonsterValue, aiMonsterValue=aiMonsterValue)
