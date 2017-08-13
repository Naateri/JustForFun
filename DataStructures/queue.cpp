#include <iostream>
#include <string>

using namespace std;

//dynamic queue

struct Persona{
	int age;
	string name;
};

ostream& operator<<(ostream& out, const Persona& person){
	out << "Nombre: " << person.name << endl;
	out << "Edad: " << person.age << endl;
	return out;
}

struct PersonaNode{
	Persona val; 
	PersonaNode* prev;
};

class Queue{
private:
	PersonaNode* top;
	unsigned int size;
public:
	Queue();
	bool isEmpty();
	void push(Persona);
	Persona pop();
	unsigned int getSize();
};


Queue::Queue(){
	this->top = nullptr;
	this->size = 0;
}

bool Queue::isEmpty(){
	if (this->top == nullptr) return true;
	else return false;
}

void Queue::push(Persona A){
	PersonaNode *newperson = new PersonaNode;
	newperson->val = A;
	newperson->prev = nullptr;
	if (isEmpty()){
		top = newperson;
	} else { //no fixed size
		PersonaNode* temp = top;
		while(temp->prev != nullptr){
			temp = temp->prev;
		}
		temp->prev = newperson;
	}
	this->size++;
}

Persona Queue::pop(){
	Persona ret;
	PersonaNode* toDel = top;
	ret	= top->val;
	top = top->prev;
	delete toDel;
	this->size--;
	return ret;
}

unsigned int Queue::getSize(){ return this->size;}

////////////////////////////////////////////////////////////////////////////////

void agregarPersona(Queue* lol){
	Persona A;
	cout << "Ingrese el nombre:\n";
	cin.ignore();
	getline(cin, A.name);
	cout << "Ingrese la edad:\n"; 
	cin >> A.age;
	lol->push(A);
	cout << "Hay " << lol->getSize() << " personas.\n";
}

void darTurno(Queue* lol){
	if (!lol->isEmpty()){
		cout << "Es el turno de:\n";
		cout << lol->pop();
		cout << "Hay " << lol->getSize() << " personas.\n";
	} else {
		cout << "No hay personas adentro.\n";
	}
}

int main(int argc, char *argv[]) {
	Queue *example = new Queue;
	while (true){
		int opc;
		cout << "0 para salir, 1 para meter a alguien, 2 para sacar a alguien de la cola\n";
		cin >> opc;
		if (opc == 0) break;
		switch(opc){
			case 1:
				agregarPersona(example);
				break;
			case 2:
				darTurno(example);
				break;
			default:
				cout << "Vuelva a ingresar un numero\n";
				break;
		}
	}
	delete example;
	return 0;
}

