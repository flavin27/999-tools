#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>


void readTranslatedFile(FILE *translatedFile, FILE *binFile);
int findStringInBinFile(FILE *binFile, const char *needle);

int main() {

    FILE *translatedFile = fopen("a01b.fsb_extracted.txt", "r");
    FILE *binFile = fopen("a01b.fsb", "rb+");
    if (translatedFile == NULL || binFile == NULL) {
        perror("Erro ao abrir arquivo");
        return 1;
    }

    //printf("Debugando: %04x\n", findStringInBinFile(binFile, "Junpei"));
    readTranslatedFile(translatedFile, binFile);

    fclose(translatedFile);
    fclose(binFile);

    return 0;
}

void readTranslatedFile(FILE *translatedFile, FILE *binFile) {
    char buffer[300];
    while (fgets(buffer, sizeof(buffer), translatedFile) != NULL) {
        buffer[strcspn(buffer, "\r\n")] = 0;
        if (buffer[0] == '\n') {
            continue;
        }
        int position = findStringInBinFile(binFile, buffer);
        if (position != -1) {
            printf("Found %s at position %04x\n", buffer ,position);
            return;
        }
    }
    return;
}

int findStringInBinFile(FILE *binFile, const char *needle) {
    size_t needleSize = strlen(needle);
    long position = 0;
    char buffer[300];

    while (fread(buffer, 1, sizeof(buffer), binFile) > 0) {
        for (unsigned int i = 0; i < sizeof(buffer); i++) {
            if (buffer[i] == needle[0]) {
                unsigned int j = 0;
                while (j < needleSize && buffer[i+j] == needle[j]) {
                    j++;
                }
                if (j == needleSize) {
                    return position + i;
                }
            }

        }
        position += sizeof(buffer);
    }
    return -1;

}