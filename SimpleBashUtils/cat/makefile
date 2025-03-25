FILE = *.txt

GCC = gcc -Wall -Wextra -Werror -std=c11

all: build

build: s21_cat.o
	$(GCC) -o s21_cat s21_cat.o

s21_cat.o: 
	$(GCC) -c s21_cat.c

clean:
	rm -f s21_cat s21_cat.o

rebuild: clean build

clang:
	clang-format -i *.c
	clang-format -i *.h

test: rebuild
	bash -c 'diff <(./s21_cat $(FILE)) <(cat $(FILE))'
	bash -c 'diff <(./s21_cat -b $(FILE)) <(cat -b $(FILE))'
	bash -c 'diff <(./s21_cat -e $(FILE)) <(cat -e $(FILE))'
	bash -c 'diff <(./s21_cat -n $(FILE)) <(cat -n $(FILE))'
	bash -c 'diff <(./s21_cat -s $(FILE)) <(cat -s $(FILE))'
	bash -c 'diff <(./s21_cat -t $(FILE)) <(cat -t $(FILE))'
