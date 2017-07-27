#include <iostream>
using namespace std;

struct Node{
	int val;
	Node* next;
};

class LinkedList{
private:
	Node* head;
public:
	LinkedList();
	bool isEmpty();
	void insert(int);
	void erase(int);
	void print();
};

LinkedList::LinkedList(){
	this->head = nullptr;
}

bool LinkedList::isEmpty(){
	if (this->head == nullptr) return true;
	else return false;
}

void LinkedList::insert(int value){
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
	try{
		if (isEmpty()){
			throw 469;
		}
	} catch (int e){
		cout << "Error, la lista esta vacía. Error Nro. " << e << ". Contactarse con admin.\n";
	}
	Node *temp = head;
	if (pos == 0){
		head = head->next;
		delete temp;
	} else {
		Node *prev;
		prev = temp;
		temp = temp->next;
		while(pos > 1){
			try{
				if (temp->next == nullptr){
					throw 420;
				}
			} catch (int e){
				cout << "Error, valor no aceptado. Error Nro. " << e << ". Contactarse con admin.\n";
			}
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
	
int main(int argc, char *argv[]) {
	LinkedList A;
	A.insert(1);
	A.insert(2);
	A.insert(3);
	A.insert(8);
	A.insert(9);
	A.print();
	cout << endl;
	A.erase(0);
	A.print();
	cout << endl;
	A.erase(1);
	A.print(); //2 8 9
	cout << endl;
	A.insert(3);
	A.erase(3);
	A.print(); //2 3 8
	//A.erase(3); //error for the sake of an error showing
	A.erase(0);
	A.erase(0);
	A.erase(0);
	A.erase(2); //another error for the sake of the other error showing
	return 0;
}

