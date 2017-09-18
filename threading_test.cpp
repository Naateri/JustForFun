#include <iostream>
#include <thread>
#include <time.h>
#include <stdlib.h>


#define THREADS 8

using namespace std;
typedef void (*q)();

int aae = 145;


void lol(){
	unsigned int i;
	for(i = 0; i < 2000000000; i++)
		//cout << i << endl;
		;
}

void yaes(){
	char ae = char(aae);
	for(int i = 0; i < 2000000; i++){
		cout << "Mi enamoradita es Y" << ae << "s\n";
		;
	}
}

void bar(){
	float i = 0.0;
	while (i < 200000.00){
		i += 0.1;
	}
}

int main(int argc, char *argv[]) {
	q myList[3];
	double elapsedTime;
	myList[0] = lol;
	myList[1] = yaes;
	myList[2] = bar;
	thread threads[THREADS];
	clock_t begin = clock();
	for(int i = 0; i < THREADS; i++){
		threads[i] = thread(myList[i%2]);
		//threads[i].join();
	}
	for(int i = 0; i < THREADS; i++)
		threads[i].join();
	cout << "acabo!\n";
	clock_t end = clock();
	elapsedTime = double(end-begin)/CLOCKS_PER_SEC;
	cout << elapsedTime;
	return 0;
}

