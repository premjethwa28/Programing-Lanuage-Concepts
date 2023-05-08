// Name: Prem Atul Jethwa
// Stud ID: 1001861810
// Language: C version 14.0.0
// OS : Mac OS (Omega compatible)

#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>

int gds(char p[]) // Function get the list of directories
{
    int size = 0; // initialize size variable to 0
    char df[2000];

    struct dirent *dp;
    struct stat file;
    DIR *directory = opendir(p);

    while ((dp = readdir(directory)) != NULL) //  Get the path name of the file
    {
        if (strcmp(dp->d_name, ".") == 0 || strcmp(dp->d_name, "..") == 0)
        {
            continue;
        }
        strcpy(df, p);
        strcat(df, "/");
        strcat(df, dp->d_name);
        stat(df, &file);

        if (S_ISREG(file.st_mode)) // Recursion to go through all the directories
        {
            FILE *fpoint = fopen(df, "r");
            fseek(fpoint, 0L, SEEK_END);
            int res = ftell(fpoint);
            size += res;
            fclose(fpoint);
        }
        else
        {
            size += gds(df); // add the file size to the bytes variable
        }
    }
    return size; // return the final size of the directory
}

int main() // Main function
{
    int totalditorySize = gds(".");  // Path of the folder of which size is to be determine
    printf("%d\n", totalditorySize); // print the size in integer

    return 0;
}