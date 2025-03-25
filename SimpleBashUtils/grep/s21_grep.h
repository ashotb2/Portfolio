#ifndef S21_GREP_H
#define S21_GREP_H

#include <getopt.h>
#include <regex.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct arguments {
  int e, i, v, c, l, n, h, s, f, o;
} arguments;

arguments argument_parser(int argc, char **argv);

void search(FILE *fptr, int optind, char *argv[], int reg, int i, int argc);
void search_v(FILE *fptr, int optind, char *argv[], int reg, int i, int argc);
void search_c(FILE *fptr, int optind, char *argv[], int reg, int i, int argc);
void search_n(FILE *fptr, int optind, char *argv[], int reg, int i, int argc);
void search_l(FILE *fptr, int optind, char *argv[], int reg, int i);
void search_h(FILE *fptr, int optind, char *argv[], int reg);
void search_f(FILE *fptr, int optind, char *argv[], int reg, int i, int argc);
void search_o(FILE *fptr, int optind, char *argv[], int reg, int i, int argc);

#endif
