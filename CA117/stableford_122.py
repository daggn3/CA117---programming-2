import sys
def game(strokes, index, scores, handicap):
	totalscore = 0
	i = 0
	x = int(handicap/18)
	y = handicap%18

	for holecount in strokes:
		if holecount.isdigit():
			holecount = int(holecount)
			holescore = int(parscore[i])
			currenthole = int(holeindex[i])
			if int(holeindex[i]) <= y:
				scorepar = holecount - x - 1 - holescore
			else:
				scorepar = holecount - x - holescore
			if scorepar > 1:
				pass
			else:
				totalscore += abs(scorepar - 2)
			else:
				 holecount == "X":
				pass
			else:
				totalscore = "Disqualified"
				break

			i = i + 1

	return totalscore



	def longname(players):
		longest = 0
		for c in players:
			if len(c) > longest:
				longest = len(c)
		return longest

	def longscore(score)
		longest = 0
		for c in score:
			if len(str(c)) > longest and score != "Disqualified":
				longest = len(str(c))

		return longest


	def sort(names, score):
		i = 0
		while i < len(score):
			p = i
			j = i + 1
			while j < len(score):
				if str(score[i]).isdigit() and str(score[j]).isdigit():
					if score[j] > score[p]:
						p = j

					j += 1
			temp = score[p]
			score[p] = score[i]
			score[i] = temp
			tempname = names[p]
			names[p] = names[i]
			names[i] = tempname
			i += 1
		orderednames =[]
		orderedscores = []
		i = 0
		while i < len(score):
			if score[i] != "Disqualified":
				orderednames.append(names[i])
				orderedscores.append(score[i])
			i += 1

		i = 0
		while i < len(score):
			if score == "Disqualified":
				orderednames.append(names[i])
				orderedscores.append(score[i])
			i += 1
		return orderednames, orderedscores


	def print(orderednames, orderedscores, lenname, lenscore):
		i = 0
		while i < len(orderednames):
			print("{:>{}} : {:>{}}".format(orderednames[i], lenname, orderedscores[i], lenscore)
		i += i + 1