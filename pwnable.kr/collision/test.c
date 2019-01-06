#include <stdio.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char *p){
	int* ip = (int*)p;
	int res=0;
	for(int i=0; i<5; i++){
		printf("ip[%d]=%d\n",i,ip[i]);
		res += ip[i];
	}
	printf("res : %d\n",res);
	return res;
}

int main(int argc,char*argv[]){
	if(hashcode == check_password(argv[1])){
		printf("GOODJOB\n");
		return 0;
	}else{
		printf("N0p..\n");
	}
	return 0;
}
