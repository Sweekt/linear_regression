#pragma once
#include <iostream>
#include <vector>

class Data {
    private:
		std::vector<std::pair<int, int> >	_values;
    public:
        // Constructors & destructor
        Data();
        Data(const Data &copy);
        ~Data();

        // Overloaded operators
        Data &operator=(const Data &src);

        // Public methods
};
