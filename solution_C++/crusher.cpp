#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    set<string> words;
    set<string> :: iterator itr;

    for( itr = words.begin(); itr != words.end(); ++itr  ) {
        cout << *itr << endl;
    }
    cout << "blam" << endl;
    return 0;
}
