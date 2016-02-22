all: genUnitTestCommonFunc genUnitTestIntegerFunc genUnitTestMathFunc genUnitTestRelationalFunc genUnitTestOperator genMakefile

genUnitTestCommonFunc:
	-python genUnitTestCommonFunc.py

genUnitTestIntegerFunc:
	-python genUnitTestIntegerFunc.py

genUnitTestMathFunc:
	-python genUnitTestMathFunc.py

genUnitTestRelationalFunc:
	-python genUnitTestRelationalFunc.py

genUnitTestOperator:
	-python genUnitTestOperator.py

genMakefile:
	cp ../Makefile ../test/
	cp ../Makefile ../test/common
	cp ../Makefile ../test/integer
	cp ../Makefile ../test/math
	cp ../Makefile ../test/operator
	cp ../Makefile ../test/relational

clean:
	-rm -rf ../test
