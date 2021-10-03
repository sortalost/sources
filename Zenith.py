"""
Its a ready to run program ma'am.

Input: [NONE]

Output:

The raw array (both in a dict and a list)

Count of each letter, eg:
"a is 3 times"
"""

# Begin

# Imports (stdlibs, no external dependency)
import string, random, time # time is imported for the ping tests only, not required


# Base Code
def gen_str(all_l:list, ls:list):
	    for x in all_l:
	    	l = random.choice(all_l)
	    	ls.append(l.lower())
	    	if len(ls)==50:
	    		break
	    return ls
	

def count(elem:str, ls:list):
    count = 0
    for ele in ls:
            if (ele == elem):
            	count = count + 1
    return count


# The Driver Code
to_list = []
lx = gen_str(string.ascii_letters,to_list)
ly = gen_str(string.ascii_letters,to_list)
to_list=to_list[:100]

dc = dict((l,to_list.count(l)) for l in set(to_list))
lc = []

for x in dc:
	lc.append(f"{x} is {dc[x]} {'time only' if dc[x]==1 else 'times'}")

fs = str(lc).replace("[","").replace("]","").replace(",","\n").replace("'","")



# Main Output Code
if __name__=="__main__":
	t = time.monotonic()
	fc = f"""\
• Array length: {len(to_list)} in list || {len(dc)} in dict
• ARRAY:
▪︎ List:
{to_list[:100]}
			
▪︎Dict:
{dc}
	
• Counts:
{fs}
	
• Thanks!!
	"""
	
	print(f"{fc}\nCode Execution in {time.monotonic()-t} seconds")
