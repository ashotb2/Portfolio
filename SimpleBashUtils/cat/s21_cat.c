#include "s21_cat.h"

#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

arguments argument_parser(int argc, char **argv) {
  arguments arg = {0};
  struct option long_options[] = {{"number", no_argument, NULL, 'n'},
                                  {"number-nonblank", no_argument, NULL, 'b'},
                                  {"squeeze-blank", no_argument, NULL, 's'},
                                  {0, 0, 0, 0}};
  int opt;
  opt = getopt_long(argc, argv, "bneETts", long_options, 0);
  switch (opt) {
    case 'b':
      arg.b = 1;
      break;
    case 'n':
      arg.n = 1;
      break;
    case 's':
      arg.s = 1;
      break;
    case 'e':
      arg.E = 1;
      arg.v = 1;
      break;
    case 'E':
      arg.E = 1;
      break;
    case 't':
      arg.T = 1;
      arg.v = 1;
      break;
    case 'T':
      arg.T = 1;
      break;
    default:
      readFile(argv, argc);
      exit(1);
      break;
  }
  return arg;
}

void option(arguments *arg, char text[], int *count) {
  size_t len = strlen(text);
  if (arg->n) {
    n(text, len, count);
  } else if (arg->s) {
    s(text, len);
  } else if (arg->b) {
    b(text, len, count);
  } else if (arg->E) {
    e(text, len);
  } else if (arg->T) {
    t(text, len);
  } else {
    printf("Invalid option\n");
  }
}

void b(char text[], size_t len, int *count) {
  for (size_t i = 0; i < len; i++) {
    if (*count == 1 || (text[i - 1] == '\n' && text[i] != '\n')) {
      if (text[i] != '\n') {
        printf("%6d", *count);
        printf("\t");
        (*count)++;
      }
    }
    printf("%c", text[i]);
  }
}

void n(char text[], size_t len, int *count) {
  for (size_t i = 0; i < len; i++) {
    if (*count == 1 || text[i - 1] == '\n') {
      printf("%6d", *count);
      printf("\t");
      (*count)++;
    }
    printf("%c", text[i]);
  }
}

void s(char text[], size_t len) {
  for (size_t i = 1; i < len; i++) {
    if (text[i] == '\n' && text[i + 1] == '\n') {
      memmove(&text[i], &text[i + 1], len - i);
    }
  }
  text[len] = '\0';
  printf("%s", text);
}

void e(char text[], size_t len) {
  for (size_t i = 0; i < len; i++) {
    if (text[i] == '\n') {
      printf("$\n");
    } else {
      printf("%c", text[i]);
    }
  }
}

void t(char text[], size_t len) {
  for (size_t i = 0; i < len; i++) {
    if (text[i] == '\t') {
      printf("^I");
    } else {
      printf("%c", text[i]);
    }
  }
}

void output(arguments *arg, char **argv, int argc, int *count) {
  FILE *fptr;

  for (int j = optind; j < argc; j++) {
    if ((fptr = fopen(argv[j], "r"))) {
      char text[10000];
      int ch;
      int i = 0;
      while ((ch = fgetc(fptr)) != EOF) {
        text[i++] = ch;
      }
      text[i] = '\0';
      option(arg, text, count);
      fclose(fptr);
    } else {
      perror("ERROR");
    }
  }
}

void readFile(char **argv, int argc) {
  FILE *fptr;
  for (int j = 1; j < argc; j++) {
    if ((fptr = fopen(argv[j], "r"))) {
      int ch;
      while ((ch = fgetc(fptr)) != EOF) {
        printf("%c", ch);
      }
      fclose(fptr);
    } else {
      perror("ERROR");
    }
  }
}

int main(int argc, char **argv) {
  int count[1];
  *count = 1;
  arguments arg = argument_parser(argc, argv);
  output(&arg, argv, argc, count);

  return 0;
}