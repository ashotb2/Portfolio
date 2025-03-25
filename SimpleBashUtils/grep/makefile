FILE_ALL = *.txt

GCC = gcc -Wall -Wextra -Werror -std=c11

all: build

build: s21_grep.o
	$(GCC) -o s21_grep s21_grep.o

s21_grep.o: 
	$(GCC) -c s21_grep.c

clean:
	rm -f s21_grep s21_grep.o

rebuild: clean build

clang:
	clang-format -i *.c
	clang-format -i *.h

test: rebuild

	bash -c 'diff <(./s21_grep 'is' $(FILE_ALL)) <(grep 'is' $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -e is $(FILE_ALL)) <(grep -e is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -i is $(FILE_ALL)) <(grep -i is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -v is $(FILE_ALL)) <(grep -v is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -l is $(FILE_ALL)) <(grep -l is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -n is $(FILE_ALL)) <(grep -n is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -h is $(FILE_ALL)) <(grep -h is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -s is $(FILE_ALL)) <(grep -s is $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -f word.txt $(FILE_ALL)) <(grep -f word.txt $(FILE_ALL))'
	bash -c 'diff <(./s21_grep -o is $(FILE_ALL)) <(grep -o is $(FILE_ALL))'