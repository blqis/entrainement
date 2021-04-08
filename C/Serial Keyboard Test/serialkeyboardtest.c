#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include "serial.h"



int main(){
	
	serial_com sp;
	serial_open(&sp,"/dev/ttyACM0");


	return 0;
}






void serial_open(serial_com* sp,char *name){
	sp->fd = (int) open(name,O_RDWR);
	printf("On a la valeur %d", (*sp).fd);
}


void serial_close(serial_com* sp){
	close((*sp).fd);
}







