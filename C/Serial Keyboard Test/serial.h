#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>


typedef struct{
	char* nom;
	int fd;
}serial_com;


void serial_open(serial_com*,char*);
void serial_close(serial_com*);