#include "s21_grep.h"

int main(int argc, char **argv) {
  argument_parser(argc, argv);

  return 0;
}

arguments argument_parser(int argc, char **argv) {
  int opt;
  opt = getopt_long(argc, argv, "eivclnhsfo", NULL, 0);
  FILE *fptr;
  int reg = REG_EXTENDED;
  switch (opt) {
    case 'e':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'i':
      reg = REG_ICASE;
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'v':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_v(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'c':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_c(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'l':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_l(fptr, optind, argv, reg, i);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'n':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_n(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'h':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_h(fptr, optind, argv, reg);
        } else
          printf("File Invalid\n");
      }
      break;
    case 's':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search(fptr, optind, argv, reg, i, argc);
        }
      }
      break;
    case 'f':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_f(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    case 'o':
      for (int i = optind + 1; i < argc; i++) {
        if ((fptr = fopen(argv[i], "r"))) {
          search_o(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      break;
    default:
      argc++;
      for (int i = 2; i < argc - 1; i++) {
        optind = 1;
        if ((fptr = fopen(argv[i], "r"))) {
          search(fptr, optind, argv, reg, i, argc);
        } else
          printf("File Invalid\n");
      }
      exit(1);
      break;
  }
  return (arguments){0};
}

void search(FILE *fptr, int optind, char *argv[], int reg, int i, int argc) {
  regex_t regex;
  int flag;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    while (fgets(text, sizeof(text), fptr)) {
      if (text[strlen(text) - 1] == '\n') text[strlen(text) - 1] = '\0';
      if (regexec(&regex, text, 0, NULL, 0) == 0) {
        if (argc > 4) {
          printf("%s:%s\n", argv[i], text);
        } else {
          printf("%s\n", text);
        }
      }
    }
  } else
    printf("Invalid regex\n");

  regfree(&regex);
}

void search_v(FILE *fptr, int optind, char *argv[], int reg, int i, int argc) {
  regex_t regex;
  int flag;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    while (fgets(text, sizeof(text), fptr)) {
      if (text[strlen(text) - 1] == '\n') text[strlen(text) - 1] = '\0';
      if (regexec(&regex, text, 0, NULL, 0) != 0) {
        if (argc > 4) {
          printf("%s:", argv[i]);
        }
        printf("%s\n", text);
      }
    }
  } else
    printf("Invalid regex\n");

  regfree(&regex);
}

void search_c(FILE *fptr, int optind, char *argv[], int reg, int i, int argc) {
  regex_t regex;
  int flag;
  int count = 0;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    while (fgets(text, sizeof(text), fptr)) {
      if (regexec(&regex, text, 0, NULL, 0) == 0) {
        count++;
      }
    }
    if (argc > 4) {
      printf("%s:", argv[i]);
    }
    printf("%d\n", count);
  } else
    printf("Invalid regex\n");

  regfree(&regex);
}

void search_n(FILE *fptr, int optind, char *argv[], int reg, int i, int argc) {
  regex_t regex;
  int flag;
  int count = 0;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    while (fgets(text, sizeof(text), fptr)) {
      count++;
      if (regexec(&regex, text, 0, NULL, 0) == 0) {
        if (argc > 4) {
          printf("%s:", argv[i]);
        }
        printf("%d:%s", count, text);
      }
    }
  } else
    printf("Invalid regex\n");

  regfree(&regex);
}

void search_l(FILE *fptr, int optind, char *argv[], int reg, int i) {
  regex_t regex;
  int flag;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    int count = 0;
    while (fgets(text, sizeof(text), fptr)) {
      if (regexec(&regex, text, 0, NULL, 0) == 0) {
        count = 1;
      }
    }
    if (count == 1) {
      printf("%s\n", argv[i]);
    }
  } else
    printf("Invalid regex\n");

  regfree(&regex);
}

void search_h(FILE *fptr, int optind, char *argv[], int reg) {
  regex_t regex;
  int flag;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    while (fgets(text, sizeof(text), fptr)) {
      if (regexec(&regex, text, 0, NULL, 0) == 0) {
        printf("%s", text);
      }
    }
  } else
    printf("Invalid regex\n");

  regfree(&regex);
}

void search_f(FILE *fptr, int optind, char *argv[], int reg, int i, int argc) {
  FILE *fptr2;
  regex_t regex;
  if ((fptr2 = fopen(argv[optind], "r"))) {
    char filter[1000];
    while (fgets(filter, sizeof(filter), fptr2))
      filter[strlen(filter) - 1] = '\0';
    int flag;
    flag = regcomp(&regex, filter, reg);
    if (!flag) {
      char text[1000];
      while (fgets(text, sizeof(text), fptr)) {
        if (regexec(&regex, text, 0, NULL, 0) == 0) {
          if (argc > 4) {
            printf("%s:", argv[i]);
          }
          printf("%s", text);
        }
      }
    } else
      printf("Invalid regex\n");

    regfree(&regex);
  } else
    printf("File Invalid\n");
}

void search_o(FILE *fptr, int optind, char *argv[], int reg, int i, int argc) {
  regex_t regex;
  int flag;
  flag = regcomp(&regex, argv[optind], reg);
  if (!flag) {
    char text[1000];
    regmatch_t match;
    while (fgets(text, sizeof(text), fptr)) {
      char *p = text;
      while (regexec(&regex, p, 1, &match, 0) == 0) {
        if (argc > 4) {
          printf("%s:", argv[i]);
        }
        printf("%.*s\n", (int)(match.rm_eo - match.rm_so), p + match.rm_so);
        p += match.rm_eo;
      }
    }
  } else {
    printf("Invalid regex\n");
  }
  regfree(&regex);
}