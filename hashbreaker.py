#!/usr/bin/python3

import hashlib

# This function prints ethical use information and walks the user through the input process.
# The function returns a tuple containing the hash type, the file containing the hashes, and the wordlist file.
def print_info():
	print("Please use this program only for ethical purposes.")
	print("Never attempt to crack someone's hash without that person's permission.")
	print()
	print()
	print("Here are the hash types supported by this program: ")
	print("\t1) SHA-1")
	print("\t2) SHA-256")
	print("\t3) MD5")
	print()
	hash_type = input("Please enter the number corresponding to your hash type: ")
	hash_file = input("Please enter the path to the file containing the hash(es): ")
	wordlist = input("Please enter the path to the wordlist: ")
	print()
	print()
	return (hash_type, hash_file, wordlist)
	
# This function cracks a hash by comparing the hashes of lines in a wordlist against the given hash string.
def crack_hash(hash_string, wordlist, hash_type):
	if hash_type == "1":
		if len(hash_string) != 40:	# SHA1 hashes should have a length of 40.
			print(hash_string + " is not a valid SHA1 hash!")
			return
		for line in wordlist:
			if hashlib.sha1(line.strip().encode()).hexdigest() == hash_string:
				print("Solution for " + hash_string + ":\t\t\t" + line.strip())
				return
	elif hash_type == "2":
		if len(hash_string) != 64:	# SHA256 hashes should have a length of 64.
			print(hash_string + " is not a valid SHA256 hash!")
			return
		for line in wordlist:
			if hashlib.sha256(line.strip().encode()).hexdigest() == hash_string:
				print("Solution for " + hash_string + ":\t\t\t" + line.strip())
				return
	elif hash_type == "3":
		if len(hash_string) != 32:	# MD5 hashes should have a length of 32.
			print(hash_string + " is not a valid MD5 hash!")
			return
		for line in wordlist:
			if hashlib.md5(line.strip().encode()).hexdigest() == hash_string:
				print("Solution for " + hash_string + ":\t\t\t" + line.strip())
				return
		

def main():
	(hash_type, hash_file, wordlist) = print_info()		# Obtain the hash type, hash file path, and the wordlist path from the user.
	h = 0
	w = 0
	if not hash_type in ["1","2","3"]:	# Verify that the hash type is valid.
		print("Invalid hash type! Please enter a value between 1 and 3 with no spaces.")
		return 0 
	
	# Try to open the hash file. If this fails, exit the program.
	try:
		hfile = open(hash_file, "r", errors='replace')
		h = hfile.readlines()
	except:
		print("Unable to open hash file.")
		return 0
		
	# Try to open the wordlist file. If this fails, close the hash file and exit the program.
	try:
		wfile = open(wordlist, "r", errors='replace')
		w = wfile.readlines()
	except:
		print("Unable to open wordlist.")
		hfile.close()
		return 0
	
	# For each line in the hash file, attempt to crack it.
	for line in h:
		if line.strip() and not line.strip().isspace():	# Ignore empty strings and strings that only contain whitespace.
			crack_hash(line.strip(), w, hash_type)
	
	# Close files and exit the program.
	hfile.close()
	wfile.close()
	return 1
	
main()
