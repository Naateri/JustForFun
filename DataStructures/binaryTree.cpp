#include <iostream>
using namespace std;

class TreeNode{
public:
	long val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(){
		this->left = nullptr;
		this->right = nullptr;
	}
};

class BinaryTree{
private:
	TreeNode* begin;
public:
	BinaryTree();
	//~BinaryTree();
	bool isEmpty();
	void insert(long);
	void findRoute(long);
	void preorder(TreeNode*);
	void inorder(TreeNode*);
};

BinaryTree::BinaryTree(){
	this->begin->left = nullptr;
	this->begin->right = nullptr;
	this->begin->val = 0L;
}

bool BinaryTree::isEmpty(){
	if (!(this->begin->val))
		return true;
	else return false;
}

void BinaryTree::insert(long val){
	if (isEmpty())
		this->begin->val = val;
	else {
		///TreeNode *lol = new TreeNode;
		TreeNode *temp = begin;
		while(temp->right != nullptr && temp->left != nullptr){
			if (val > temp->val){
				temp = temp->right;
			} else {
				temp = temp->left;
			}
		}
		TreeNode *newValue = new TreeNode;
		newValue->val = val;
		if (val > temp->val) temp->right = newValue;
		else temp->left = newValue;
	}
}

void BinaryTree::findRoute(long val){
	if (isEmpty()){
		cout << "El arbol esta vacio\n";
	} else {
		TreeNode *temp = begin;
		cout << "H" << temp->val << endl;
		while(temp->right != nullptr || temp->left != nullptr){
			if (val > temp->val){
				temp = temp->right;
				cout << "R";
			} else {
				temp = temp->left;
				cout << "L";
			}
			cout << temp->val << endl;
		}
		//cout << temp->val << endl;
	}

}

void BinaryTree::preorder(TreeNode* lel = nullptr){
	if (isEmpty()){
		cout << "El arbol esta vacio\n";
	} else {
		TreeNode *temp;
		if (lel == nullptr) lel = begin;
		temp = lel;
		cout << lel->val << endl;
		if (temp->left != nullptr){
			preorder(temp->left);
		}
		if (temp->right != nullptr){
			preorder(temp->right);
		}
	}
}

void BinaryTree::inorder(TreeNode* lel = nullptr){
	if (isEmpty()){
		cout << "El arbol esta vacio\n";
	} else {
		TreeNode *temp;
		if (lel == nullptr) lel = begin;
		temp = lel;
		cout << lel->val << endl;
		
	}
}

int main(int argc, char *argv[]) {
	BinaryTree Hola;
	Hola.insert(6);
	Hola.insert(8);
	Hola.insert(3);
	Hola.insert(7);
	Hola.insert(9);
	Hola.insert(4);
	Hola.insert(2);
	Hola.insert(15);
	//Hola.insert(13);
	//Hola.findRoute(15);
	Hola.preorder();
	return 0;
}

