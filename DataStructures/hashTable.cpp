#include <iostream>
#include <string>
#define SIZE 50
using namespace std;

//including the linkedlist.cpp file 
//found in this same repo
//just that with strings instead of ints
//without the try and catch stuff 
//hash table starts at line 102

struct Node{
	string val;
	Node* next;
};

class LinkedList{
private:
	Node* head;
public:
	LinkedList();
	bool isEmpty();
	void insert(string);
	void erase(int);
	void print();
	Node* find(string);
	void modify(string, string);
	int get(string);
};

LinkedList::LinkedList(){
	this->head = nullptr;
}

bool LinkedList::isEmpty(){
	if (this->head == nullptr) return true;
	else return false;
}

void LinkedList::insert(string value){
	Node *newNode = new Node;
	newNode->val = value;
	if (isEmpty()){
		newNode->next = nullptr;
		this->head = newNode;
	} else {
		Node *temp = head;
		while(temp->next != nullptr && temp->next->val < value){
			temp = temp->next;
		}
		newNode->next = temp->next;
		temp->next = newNode;
	}
}

void LinkedList::erase(int pos){
	Node *temp = head;
	if (pos == 0){
		head = head->next;
	} else {
		Node *prev;
		prev = temp;
		temp = temp->next;
		while(pos > 1){
			temp = temp->next;
			prev = prev->next;
			pos--;
		}
		prev->next = temp->next;
	}
	delete temp;
}

void LinkedList::print(){
	Node* ptr = head;
	while(ptr != nullptr){
		cout << ptr->val << " ";
		ptr = ptr->next;
	}
}

Node* LinkedList::find(string value){
	Node* ptr = this->head;
	while(ptr != nullptr){
		if (value == ptr->val){ return ptr;}
		ptr = ptr->next;
	}
	return nullptr;
}

void LinkedList::modify(string val2Modify, string newVal){
	Node* ptr;
	ptr = find(val2Modify);
	if (ptr != nullptr){
		ptr->val = newVal;
	} else {
		insert(newVal);
	}
}

int LinkedList::get(string val){
	Node* ptr = head;
	int pos = -1;
	while(ptr != nullptr){
		pos++;
		ptr = ptr->next;
	}
	return pos;
}

//modulo function from https://github.com/Naateri/Algebra-Abstracta/blob/master/maths.cpp#L15

long modulo(long a, long n){ //a mod n
	long q, r;
	q = a/n;
	r = a - (q*n);
	if (r<0)
		r += n;
	return r;
}

//hashtable.h
class HashTable{
private:
	unsigned short hashFunction(string value);
	LinkedList *hashi;
public:
	HashTable();
	~HashTable();
	void insert(string);
	unsigned short getHash(string);
	int find(string);
	void modify(string, string);
	void erase(string);
};

//hashtable.cpp

unsigned short HashTable::hashFunction(string value){
	unsigned short sum = 0;
	for(unsigned int i = 0; i < value.size(); i++){
		sum += (int)(value[i]);
	}
	return modulo(sum, SIZE);
}

HashTable::HashTable(){
	LinkedList *wot = new LinkedList[SIZE-1];
	this->hashi = wot;
}

HashTable::~HashTable(){
	delete [] hashi;
}

void HashTable::insert(string value){
	unsigned short res = hashFunction(value);
	hashi[res].insert(value);
}

unsigned short HashTable::getHash(string val){
	//unsigned short res = hashFunction(val);
	//cout << "Supuestamente guardado en la posicion: " << res << endl;
	return hashFunction(val);
}

int HashTable::find(string val){
	unsigned short res = getHash(val);
	if (hashi[res].find(val) == nullptr){
		return -1;
	} else return res;
}

void HashTable::modify(string val2modify, string newval){
	unsigned short res = hashFunction(val2modify);
	Node* ptr;
	//LinkedList hola;
	//hola = hashi[res];
	ptr = hashi[res].find(val2modify); //puntero al nodo que vamos a modificar
	if (ptr != nullptr){
		hashi[res].erase(hashi[res].get(val2modify)); //borra el valor anterior
		this->insert(newval); //lo inserta en la tablita
	} else cout << "No se encontro ese valor\n";
}

void HashTable::erase(string value){
	unsigned short res = hashFunction(value);
	Node* ptr;
	ptr = hashi[res].find(value); //puntero al nodo que queremos borrar
	if (ptr != nullptr){
		hashi[res].erase(hashi[res].get(value));
	} else cout << "El valor no existe\n";
}



int main(int argc, char *argv[]) {
	HashTable Lel;
	Lel.insert("xd");
	Lel.insert("Hola");
	Lel.insert("Lol");
	Lel.insert("lel");
	Lel.insert("yc");
	cout << Lel.find("lel") << endl;
	cout << Lel.find("xd") << endl;
	cout << Lel.find("Lol") << endl;
	cout << Lel.find("yc") << endl;
	cout << Lel.find("lal") << endl;
	Lel.modify("lel", "lal");
	cout << Lel.find("lal") << endl;
	//cout << Lel.find("lel") << endl; //-1
	Lel.erase("lal");
	cout << Lel.find("lal") << endl; //-1
	return 0;
}

