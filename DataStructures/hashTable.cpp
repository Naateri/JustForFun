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
	string find(string);
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
		delete temp;
	} else {
		Node *prev;
		prev = temp;
		temp = temp->next;
		while(pos > 1){
			temp = temp->next;
			prev = prev->next;
			pos--;
		}
		//Node *toBeErased = temp;
		prev->next = temp->next;
		delete temp;
	}
}

void LinkedList::print(){
	Node* ptr = head;
	while(ptr != nullptr){
		cout << ptr->val << " ";
		ptr = ptr->next;
	}
}

string LinkedList::find(string value){
	Node* ptr = head;
	while(ptr != nullptr){
		if (value == ptr->val) return ptr->val;
		ptr = ptr->next;
	}
	return "No se ha encontrado ese valor\n";
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
};

//hashtable.cpp

unsigned short HashTable::hashFunction(string value){
	unsigned short sum = 0;
	for(int i = 0; i < value.size(); i++){
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


int main(int argc, char *argv[]) {
	HashTable Lel;
	Lel.insert("xd");
	return 0;
}

