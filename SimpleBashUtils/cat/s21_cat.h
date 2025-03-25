#ifndef S21_CAT_H
#define S21_CAT_H

#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void b(char text[], size_t len, int *count);
void n(char text[], size_t len, int *count);
void s(char text[], size_t len);
void e(char text[], size_t len);
void t(char text[], size_t len);
void readFile(char **argv, int argc);

typedef struct arguments {
  int b, n, s, E, T, v;
} arguments;

#endif