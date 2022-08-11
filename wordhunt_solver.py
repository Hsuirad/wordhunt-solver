import csv
import os

#intializations
files = os.listdir('dictionary')
dictionary_mod = {
	"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]
} # dict is separated by letter, much faster this way
all_words = [] #list for the final solutions
consonants = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"] #consonants in english
vowels = ['a','e','o','i','u'] #this line is too complex to explain

#all illegal word pairs (hopefully) in english, i got this off quora
illegal_word_pairs = ["bx", "cj", "cv", "cx", "dx", "fq", "fx", "gq", "gx", "hx", "jc", "jf", "jg", "jq", "js", "jv", "jw", "jx", "jz", "kq", "kx", "mx", "px", "pz", "qb", "qc", "qd", "qf", "qg", "qh", "qj", "qk", "ql", "qm", "qn", "qp", "qs", "qt", "qv", "qw", "qx", "qy", "qz", "sx", "vb", "vf", "vh", "vj", "vm", "vp", "vq", "vt", "vw", "vx", "wx", "xj", "xx", "zj", "zq", "zx"]

#this just splits the one dictionary csv file i have into the dictionary i set up above, the dictionary i have is all english words with size 3-8 characters
with open('dictionary/dictionary.csv', newline = '') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		dictionary_mod[row[0][0].lower()].append(str(row[0]).strip())

def main():
	global all_words #need to declare global access apparently

	#input collection and sanitization
	raw = input("Input the grid as a string of letters: ").lower().strip()
	grid = []
	for i in range(0,4):
		grid.append(list(raw.lower()[i*4:i*4+4]))

	#this will be used later, its a 4x4 grid that tracks what spots have been "read" since you cant backtrack in wordhunt
	visited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]

	#i wonder what this is for
	all_words = []

	#this goes through each x,y and starts the grep_words function at each point
	for i in range(0,4):
		for j in range(0,4):
			grep_words(grid,i,j,visited);

	#sorts list from least to greatest and reverses it to output longest to shortest words
	all_words = sorted(all_words, key=len)[::-1]

	#outputting faster
	[print("\t** " + word) if len(word)>4 else None for word in all_words]

#this function checks if the word has 4 or more consonants or vowels in a row and disqualifies it as a word because thats not too common
#also checks if it starts with more than 3 consonants and if it does makes sure it has an s at the beginning because otherwise also not that common
def check_validity(word):
	value_word = "".join(["1" if i.lower() in consonants else "0" for i in word]) #turns word into 01010101, 1 meaning the lettter is a consonant and 0 meaning vowel
	if "1111" in value_word or "0000" in value_word:
		return False
	elif "111" == value_word[:3]:
		if word[0] != "s":
			return False
	return True

#this is the recursive function thtat grabs all possible word combinations on the grid
def grep_words(grid,y,x,visit,full_word="",l=0):
	global all_words #ive seen this before

	#if the word is longer than 8 characters or if it isnt "valid" then exit out
	if l > 8 or check_validity(full_word) == False:
		return
	for pair in illegal_word_pairs: #if it contains an illegal word pair also exit out
		if pair in full_word:
			return

	#sets the visited location to true
	visit[y][x] = True

	#adds the current letter to the word
	full_word += grid[y][x]

	#if its a word, add it to all_words and keep going
	if full_word not in all_words and len(full_word) >= 3 and full_word.lower() in dictionary_mod[full_word[0].lower()]:
		all_words.append(full_word)

	#checks all 8 neighbors and if theyre a valid grid location it begins traversing to that location
	for i in range(-1,2):
		for j in range(-1,2):
			if y+i >= 0 and y+i < 4 and x+j >= 0 and x+j < 4:
				if not visit[y+i][x+j]:
					grep_words(grid,y+i,x+j,visit,full_word,l+1);

	#gotta reset the visited boolean otherwise no other words can go there
	visit[y][x]=False

#might as well have this here
if __name__ == "__main__":
	main();
