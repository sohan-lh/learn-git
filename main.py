# This is the main script which invokes other script

if __name__ == '__main__':
	print 'On the master'

	print 'Learning push and pull of Git'

	simulate_remote_branch_advance()

def simulate_remote_branch_advance():
	print "Remote branch 'first' advanced'
