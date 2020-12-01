from multiprocessing import Pool, Manager
import os

def copyFile(name, oldDirName, newDirName, queue):
	# openfile
	fr = open(oldDirName + "/" + name, "r")
	fw = open(newDirName + "/" + name, "w")
	contents = fr.read()
#	print(contents)
	fw.write(contents)

	fr.close()
	fw.close()

	queue.put(name)

def main():
	#0 get old folder's name and path
	oldDirName = input("Please tell me the folder's name: ")
	#print(oldDirName)
	newDirName = oldDirName + "-copy"
	
	#1 create new dir
	os.mkdir(newDirName)
	#2 get file list from old dir
	fileNames = os.listdir(oldDirName)
	# print(fileNames)
	#3 copy files from old dir to new dir
	# use multiprocessing to process large amounts of files
	pool = Pool(5)
	queue = Manager().Queue()

	for name in fileNames:
		pool.apply_async(copyFile, args=(name, oldDirName, newDirName, queue))
#	pool.close()
#	pool.join()
	num = 0
	numAll = len(fileNames)
	while True:
		queue.get()
		num += 1
		print("\r proceeing... %.2f%%"%(num/numAll*100))
		if num == numAll:
			break

if __name__ == "__main__":
	main()
