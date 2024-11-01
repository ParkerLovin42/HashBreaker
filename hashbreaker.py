#!/usr/bin/python3
import hashlib

# NOTE TO SELF: Remember to add handling for multiple hashes.
#		Also, add improved handling for closing files during errors.

def print_info():
	print("Here are the hash types supported by this program: ")
	print("\t1) SHA-1")
	print("\t2) SHA-256")
	print("\t3) MD5")
	print()
	hash_type = input("Please enter the number corresponding to your hash type: ")
	hash_file = input("Please enter the path to the file containing the hash(es): ")
	wordlist = input("Please enter the path to the wordlist: ")
	return (hash_type, hash_file, wordlist)
	
def crack_hash(hash_string, wordlist, hash_type):
	if hash_type == "1":
		for line in wordlist:
			if hashlib.sha1(line.strip().encode()).hexdigest() == hash_string:
				print("Solution: " + line.strip())
				return
	elif hash_type == "2":
		for line in wordlist:
			if hashlib.sha256(line.strip().encode()).hexdigest() == hash_string:
				print("Solution: " + line.strip())
				return
	elif hash_type == "3":
		for line in wordlist:
			if hashlib.md5(line.strip().encode()).hexdigest() == hash_string:
				print("Solution: " + line.strip())
				return
		

def main():
	#(hash_type, hash_file, wordlist) = print_info()
	
	# TEMP
	hash_type = "1"
	hash_file = "/home/kali/Desktop/hash.txt"
	wordlist = "/home/kali/Desktop/Arsenal/wordlists/rockyou.txt"
	
	h = 0
	w = 0
	try:
		hfile = open(hash_file, "r", errors='replace')
		h = hfile.readlines()
	except:
		print("Unable to open hash file.")
		return 0
	try:
		wfile = open(wordlist, "r", errors='replace')
		w = wfile.readlines()
	except:
		print("Unable to open wordlist.")
		hfile.close()
		return 0
	
	for line in h:
		crack_hash(line.strip(), w, hash_type)

	hfile.close()
	wfile.close()
	print("Files closed successfully.")
main()
