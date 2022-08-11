import csv
import os

files = os.listdir('dictionary')
dictionary_mod = {
	"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]
}

with open('dictionary/dictionary.csv', newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		dictionary_mod[row[0][0].lower()].append(str(row[0]).strip())

#dictionary = PyDictionary()

all_words = []
consonants = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
vowels = ['a','e','o','i','u']
illegal_word_pairs = ["bx", "cj", "cv", "cx", "dx", "fq", "fx", "gq", "gx", "hx", "jc", "jf", "jg", "jq", "js", "jv", "jw", "jx", "jz", "kq", "kx", "mx", "px", "pz", "qb", "qc", "qd", "qf", "qg", "qh", "qj", "qk", "ql", "qm", "qn", "qp", "qs", "qt", "qv", "qw", "qx", "qy", "qz", "sx", "vb", "vf", "vh", "vj", "vm", "vp", "vq", "vt", "vw", "vx", "wx", "xj", "xx", "zj", "zq", "zx"]


def main():
	global all_words

	# raw = input("The string of words: ")
	raw = "MLGVRENAECTHAMTW".lower()
	grid = []

	for i in range(0,4):
		grid.append(list(raw.lower()[i*4:i*4+4]))

	visited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]

	all_words = []

	for i in range(0,4):
		for j in range(0,4):
			grep_words(grid,i,j,visited);

	all_words = sorted(all_words, key=len)[::-1]

	[print("\t**" + word) if len(word)>4 else None for word in all_words]

def check_validity(word):
	value_word = "".join(["1" if i.lower() in consonants else "0" for i in word])
	if "1111" in value_word or "0000" in value_word:
		return False
	elif "111" == value_word[:3]:
		if word[0] != "s":
			return False
	return True

def grep_words(grid,y,x,visit,full_word="",l=0):
	global all_words

	if l > 8 or check_validity(full_word) == False:
		return
	for pair in illegal_word_pairs:
		if pair in full_word:
			return

	visit[y][x] = True
	full_word += grid[y][x]
	if full_word not in all_words and len(full_word) >= 3 and full_word.lower() in dictionary_mod[full_word[0].lower()]:
		all_words.append(full_word)

	for i in range(-1,2):
		for j in range(-1,2):
			if y+i >= 0 and y+i < 4 and x+j >= 0 and x+j < 4:
				if not visit[y+i][x+j]:
					grep_words(grid,y+i,x+j,visit,full_word,l+1);
	visit[y][x]=False

if __name__ == "__main__":
	main();
