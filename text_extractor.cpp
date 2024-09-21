#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>


void read_bin_file(char *fileName);

int main(int argc, char *argv[]) {
    
    if (argc < 2) {
        printf("========WELCOME TO 999: Nine Hours, Nine Persons, Nine Doors TEXT EXTRACTOR========\n\n");
        printf("---How to use it?\n");
        printf("Usage: <program> <dir path|file1> [file2] ...\n");
        printf("You can provide either a directory containing text files or individual text files to extract.\n");
        return 1;
    } 



    if (argc > 2) {
        printf("Extracting text from %d files...", argc-1);
        for (int i = 1; i < argc; i++) {
            printf("[%d/%d]Extraindo %s.", i, argc-1, argv[i]);
            read_bin_file(argv[i]);
        }
        return 0;
    }
    struct dirent *entry;
    const char *dirPath = argv[1];
    DIR *dp = opendir(dirPath);
    if (dp == NULL) {
        printf("Extracting data from %s!",argv[1]);
        read_bin_file(argv[1]);
        return 0;
    }
    while ((entry = readdir(dp)) != NULL) {
        if (entry->d_name[0] != '.') {
            char fullPath[256];
            sprintf(fullPath, "%s/%s", dirPath, entry->d_name);
            read_bin_file(fullPath);
        }
    }

    closedir(dp);

    return 0;
}

void read_bin_file(char *fileName) {
    FILE *file = fopen(fileName, "rb");
    char outputFileName[256];
    sprintf(outputFileName,"%s_extracted.txt", fileName);
    FILE *outputFile = fopen(outputFileName,"w");

    if (!file || !outputFile) {
        perror("Não foi possível abrir o arquivo");
        return;
    }
    int count = 0;
    int prevChar2 = fgetc(file);
    int prevChar1 = fgetc(file);
    int ch;
    while ((ch = fgetc(file)) != EOF) {
        if (ch ==170 && prevChar1 == 170 && count > 1) {
            break;
        }
        if (ch == 0 && prevChar1 == 165 && prevChar2 == 129) {
            count++;
            if (count > 2) {
                fprintf(outputFile, "\n\n");
            }
        }
        if (count > 0 && ch != 129 && ch != 165 && ch != 0 && ch != 170) {
            fputc(ch, outputFile);
        }
        prevChar2 = prevChar1;
        prevChar1 = ch;
    }
    printf("O arquivo %s tem %d linhas\n", fileName, count);
    fclose(file);
    fclose(outputFile);
}