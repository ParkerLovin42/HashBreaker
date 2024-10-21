#!/usr/bin/python3
import hashlib

# NOTE TO SELF: Remember to add handling for multiple hashes.

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
			if hashlib.sha1(line) == hash_string:
				print("TEST1: " + line)
				print("TEST2: " + line)
				return("Solution: " + line)
	elif hash_type == "2":
		for line in wordlist:
			if hashlib.sha256(line) == hash_string:
				print("TEST1: " + line)
				print("TEST2: " + line)
				return("Solution: " + line)
	elif hash_type == "3":
		for line in wordlist:
			if hashlib.md5(line) == hash_string:
				print("TEST1: " + line)
				print("TEST2: " + line)
				return("Solution: " + line)
		

def main():
	(hash_type, hash_file, wordlist) = print_info()
	h = 0
	w = 0
	try:
		h = open(hash_file, "r").readlines()
	except:
		print("Unable to open hash file.")
		return 0
	try:
		w = open(wordlist, "r").readlines()
	except:
		print("Unable to open wordlist.")
		h.close()
		return 0
	
	for line in h:
		crack_hash(line.strip(), w, hash_type)

	h.close()
	w.close()	
main()
