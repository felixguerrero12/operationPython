# 'def' declares a function
# Declare function buildConnectionString
def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.

    Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

# __name__ will be compared to __main__
# Testing the module to confirm its actually __main__
if __name__ == "__main__":
# Create a dictionary with key-values pairs
    myParams = {
	### Key is first and the value is second ###
		"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    print buildConnectionString(myParams)
