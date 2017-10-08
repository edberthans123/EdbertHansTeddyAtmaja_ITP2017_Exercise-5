def log(original_function, logfilename="log.txt"):
	def new_function(*args, **kwargs):
		with open(logfilename, "w") as logfile:
	logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))
		return original_function(*args, **kwargs)
	return new_function

@log(new_function,original_function,'log.txt')
def my_function:
    print(my_function)
