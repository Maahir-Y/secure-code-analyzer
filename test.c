#include <stdio.h>
#include <string.h>

int main(){

    char name[10]; // Declaring a 10 character name
    gets(name); // Reading the name using gets()    ** Warning: Dangerous Function ** 

    char dest[10]; // Declaring a 10 character destination variable
    strcpy(dest, name); // Copying the name into dest   ** Warning: Dangerous Function **

    printf("%s\n", dest); // Printing dest
    return 0;
}