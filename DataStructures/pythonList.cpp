#include <iostream>
#include <stdexcept>
//#define MAXSIZE 500
using namespace std;

template <class LOL> class PythonList{
private:
	unsigned short end = 0;
	LOL *arrayXD;
	void resize(int);
public:
	PythonList();
	int size();
	void append(LOL);
	LOL at(int);
	void insert(LOL, int);
	void erase(int);
};

template <class LOL> void PythonList<LOL>::resize(int size){
	LOL *newarr = new LOL[size];
	for(int i = 0; i < end; i++){
		newarr[i] = arrayXD[i];
	}
	this->arrayXD = newarr;
	delete [] newarr;
}

template <class LOL> PythonList<LOL>::PythonList(){
	this->arrayXD = new LOL[0];
}

template <class LOL> int PythonList<LOL>::size(){ 
	return end;
}

template <class LOL> void PythonList<LOL>::append(LOL lel){
	end++;
	resize(end);
	arrayXD[end-1] = lel;
}

template <class LOL> LOL PythonList<LOL>::at(int pos){
	try{
		if (pos < 0 || pos > end){
			throw 69;
		}
	} catch (int e){
		cout << "Error, valor no aceptado. Error Nro. " << e << ". Contactarse con admin.\n";
	}
	return arrayXD[pos];
	
}

int main(int argc, char *argv[]) {
	PythonList<int> myList;
	cout << myList.size() << endl;
	myList.append(8);
	myList.append(10);
	cout << myList.at(1) << endl;
	cout << myList.size() << endl;
	return 0;
}

