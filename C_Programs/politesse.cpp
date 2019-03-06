// A simple C++ program by Dante Falzone.

#include <iostream>
int main(void) {
	using namespace std; // Yes, using the lazy approach, because why the fuck not

	string name;
	string how_doing;

	cout << "Hello, world! My name is politesse.cpp and I'm a program written in C++.";
	cout << endl;
	cout << "What's your name?" << endl;
	getline(cin, name); // Use `getline` to ensure inclusion of spaces.
	// the next line concatenates the input to a sentence
	cout << "It's nice to meet you, " << name << "." << endl;
	cout << "How are you doing today? (Type 'good' or 'bad' and press ENTER.)" << endl;
	cin >> how_doing;
	if (how_doing == "good") {
		cout << "That's good to hear. I'm also doing well." << endl;
	}
	else if (how_doing == "bad") {
		cout << "I'm sorry to hear that. I hope your day goes better." << endl;
	}
	else {
		cout << "Sorry, I didn't understand that." << endl;
	}

	return 0;
}
